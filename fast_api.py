from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import re

app = FastAPI(title="Fashion Recommendation API")

# ── Load artifacts at startup ─────────────────────────
sim_matrix = pickle.load(open('artifacts/feature_engineering/model/sim_matrix.pkl', 'rb'))
df         = pickle.load(open('artifacts/feature_engineering/featured_data/featured_data.pkl', 'rb'))

# ── Request Schemas ───────────────────────────────────
class Engine1Request(BaseModel):
    product_name : str
    top_k        : int = 5


class Engine2Request(BaseModel):
    aesthetic : str
    top_k     : int = 5


# ── Health Check ──────────────────────────────────────
@app.get("/hello")
def health():
    return {
        "status": "ok",
        "products": len(df),
        "aesthetics": df['aesthetic'].unique().tolist()
    }


# ── Similar Product Recommendation ────────────────────
@app.post("/recommend/similar")
def recommend_similar(request: Engine1Request):
    try:
        matches = df[df['product_name_clean'] == request.product_name]

        if len(matches) == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Product '{request.product_name}' not found"
            )

        product_id = matches.index[0]
        aesthetic  = df.loc[product_id, 'aesthetic']

        scores = sim_matrix[product_id].copy()
        scores[product_id] = -1

        top_idx = scores.argsort()[::-1][:request.top_k]

        results = df.iloc[top_idx][[
            'product_name_clean',
            'price',
            'rating',
            'aesthetic',
            'score',
            'image_url',
            'product_link'
        ]].copy()

        
        results['product_name_clean'] = results['product_name_clean'].apply(
            lambda x: re.sub(r"<.*?>", "", str(x))
        )

        results['price'] = np.expm1(results['price']).round(0).astype(int)
        results['similarity'] = scores[top_idx]

        return {
            "input_product": request.product_name,
            "product_id": int(product_id),
            "aesthetic": aesthetic,
            "recommendations": results.to_dict(orient='records')
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── Aesthetic Recommendation ──────────────────────────
@app.post("/recommend/aesthetic")
def recommend_aesthetic(request: Engine2Request):

    try:
        unique_aesthetic = df['aesthetic'].unique().tolist()

        if request.aesthetic not in unique_aesthetic:
            raise HTTPException(
                status_code=404,
                detail=f"Aesthetic '{request.aesthetic}' not found"
            )

        filtered = df[df['aesthetic'] == request.aesthetic]

        top_products = filtered.sort_values(
            'score',
            ascending=False
        ).head(request.top_k)

        
        top_products['product_name_clean'] = top_products['product_name_clean'].apply(
            lambda x: re.sub(r"<.*?>", "", str(x))
        )

        top_products['price'] = np.expm1(top_products['price']).round(0).astype(int)

        return {
            "aesthetic": request.aesthetic,
            "total_in_category": len(filtered),
            "recommendations": top_products[[
                'product_name_clean',
                'price',
                'rating',
                'discount',
                'score',
                'image_url',
                'product_link'
            ]].to_dict(orient='records')
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── Product Names Endpoint ────────────────────────────
@app.get("/product_names")
def Product_names():

    names = df['product_name'].unique().tolist()

    return {
        'unique_product_names': names
    }

