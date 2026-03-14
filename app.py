import streamlit as st
import streamlit.components.v1 as components
import pickle
import pandas as pd
import numpy as np
import requests

st.set_page_config(
    page_title="AesthsAI",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════
# LOAD DATA
# ══════════════════════════════════════════════════════

@st.cache_data
def load_data():
    df                 = pickle.load(open('artifacts/feature_engineering/featured_data/featured_data.pkl', 'rb'))
    df['price']        = np.expm1(df['price']).round(0).astype(int)
    df['review_count'] = np.expm1(df['review_count']).round(0).astype(int)
    return df

df = load_data()

@st.cache_data
def get_homepage_products():
    return (
        df.groupby('aesthetic', group_keys=False)
          .apply(lambda x: x.sample(min(3, len(x)), random_state=42), include_groups=False)
          .reset_index(drop=True)
          .to_dict(orient='records')
    )

HOMEPAGE = get_homepage_products()
API_URL  = "http://localhost:8000"

# ══════════════════════════════════════════════════════
# AESTHETICS META
# ══════════════════════════════════════════════════════

AESTHETICS_META = {
    "streetwear":     {"label":"Streetwear",       "emoji":"🔥", "color":"#E63A00", "desc":"Bold graphics · oversized fits · urban edge"},
    "old_money":      {"label":"Old Money",        "emoji":"✦",  "color":"#8B6200", "desc":"Linen shirts · quiet luxury · timeless pieces"},
    "college_casual": {"label":"College Casual",   "emoji":"🎓", "color":"#1A56DB", "desc":"Solid tees · comfortable · everyday wear"},
    "date_clean":     {"label":"Date Clean",       "emoji":"🌸", "color":"#B5006B", "desc":"Satin shirts · polished · effortlessly sharp"},
    "gym_athleisure": {"label":"Gym & Athleisure", "emoji":"⚡", "color":"#057A55", "desc":"Quick-dry · performance fit · active lifestyle"},
    "y2k_party":      {"label":"Y2K Party",        "emoji":"💫", "color":"#6C2BD9", "desc":"Bold prints · sequins · maximalist energy"},
    "office_smart":   {"label":"Office Smart",     "emoji":"◈",  "color":"#374151", "desc":"Crisp formals · clean lines · boardroom ready"},
}

# ══════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --red:     #E63A00;
    --red-lt:  #FFF0EB;
    --black:   #1C1C1C;
    --dark:    #3D3D3D;
    --mid:     #888888;
    --border:  #EBEBEB;
    --bg:      #F5F5F5;
    --white:   #FFFFFF;
    --green:   #2E7D32;
}

*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
section.main,
[data-testid="stAppViewBlockContainer"] {
    background: var(--bg) !important;
    color: var(--black) !important;
}
[data-testid="block-container"] {
    padding: 0 0 5rem !important;
    max-width: 100% !important;
}

.ticker {
    background: var(--black); color: #AAA;
    font-family: 'Inter', sans-serif;
    font-size: 0.65rem; letter-spacing: 2px;
    text-transform: uppercase; text-align: center;
    padding: 0.4rem;
}
.ticker b { color: var(--white); }

.navbar {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0 3rem; height: 62px;
    display: flex; align-items: center;
    justify-content: space-between;
    position: sticky; top: 0; z-index: 999;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.nav-logo {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.55rem; font-weight: 900;
    color: var(--black); letter-spacing: -0.5px;
}
.nav-logo span { color: var(--red); }
.nav-right { display: flex; gap: 1.8rem; align-items: center; }
.nav-icon {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem; color: var(--mid);
    cursor: pointer; display: flex;
    flex-direction: column; align-items: center; gap: 2px;
}

.catbar {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0 3rem; display: flex;
    gap: 0; overflow-x: auto; scrollbar-width: none;
}
.cat {
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem; font-weight: 600;
    letter-spacing: 0.5px; text-transform: uppercase;
    color: var(--mid); padding: 0.85rem 1.3rem;
    white-space: nowrap; cursor: pointer;
    border-bottom: 2px solid transparent;
}
.cat.active { color: var(--red); border-bottom-color: var(--red); }

.search-section {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0.7rem 3rem;
}
.stTextInput input {
    background: var(--bg) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 2px !important;
    color: var(--black) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    padding: 0.6rem 1rem !important;
}
.stTextInput input:focus {
    border-color: var(--red) !important;
    box-shadow: 0 0 0 3px rgba(230,58,0,0.08) !important;
}
.stTextInput input::placeholder { color: #BBBBBB !important; }
.stTextInput label,
[data-testid="textInputRootElement"] label { display: none !important; }

.result-bar {
    padding: 0.65rem 3rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
    display: flex; align-items: center;
    justify-content: space-between;
}
.result-count { font-family: 'Inter', sans-serif; font-size: 0.72rem; color: var(--mid); }
.result-count b { color: var(--black); font-weight: 700; }
.result-hint { font-family: 'Inter', sans-serif; font-size: 0.68rem; color: var(--mid); }

.stButton > button {
    background: var(--white) !important;
    border: 1.5px solid var(--border) !important;
    color: var(--dark) !important;
    font-family: 'Nunito Sans', sans-serif !important;
    font-size: 0.62rem !important; font-weight: 700 !important;
    letter-spacing: 1px !important; text-transform: uppercase !important;
    padding: 0.45rem 0 !important; border-radius: 2px !important;
    width: 100% !important; margin-top: 0.3rem !important;
}
.stButton > button:hover {
    background: var(--black) !important;
    border-color: var(--black) !important;
    color: var(--white) !important;
}

div[data-testid="stTabs"] [role="tablist"] {
    background: var(--white) !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important; padding: 0 3rem !important;
}
div[data-testid="stTabs"] button[role="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.68rem !important; font-weight: 600 !important;
    letter-spacing: 1.5px !important; text-transform: uppercase !important;
    color: var(--mid) !important; padding: 1rem 1.5rem !important;
    border: none !important; background: transparent !important;
    border-radius: 0 !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--red) !important;
    border-bottom: 2px solid var(--red) !important;
}

.sel-banner {
    background: var(--red-lt);
    border-top: 3px solid var(--red);
    padding: 1rem 3rem;
    display: flex; gap: 1.2rem; align-items: center;
    margin-bottom: 1.2rem;
}
.sel-img {
    width: 60px; height: 76px; object-fit: cover;
    border-radius: 2px; flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.sel-tag {
    font-family: 'Inter', sans-serif;
    font-size: 0.58rem; font-weight: 600;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--red); margin-bottom: 0.2rem;
}
.sel-name {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem; color: var(--dark);
    line-height: 1.4; margin-bottom: 0.3rem;
}
.sel-price {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1rem; font-weight: 800; color: var(--black);
}

.sec-head {
    padding: 1.2rem 3rem 0.8rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
    display: flex; align-items: baseline; gap: 1rem;
}
.sec-title { font-family: 'Nunito Sans', sans-serif; font-size: 1.3rem; font-weight: 900; color: var(--black); }
.sec-sub { font-family: 'Inter', sans-serif; font-size: 0.68rem; color: var(--mid); }

.aes-btn-wrap {
    padding: 0.8rem 3rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
}
.aes-hero {
    background: var(--white);
    padding: 1.2rem 3rem 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}
.aes-eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 0.6rem; font-weight: 600;
    letter-spacing: 3px; text-transform: uppercase;
    color: var(--red); margin-bottom: 0.25rem;
}
.aes-title {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.8rem; font-weight: 900;
    color: var(--black); letter-spacing: -0.5px;
    line-height: 1; margin-bottom: 0.2rem;
}
.aes-desc { font-family: 'Inter', sans-serif; font-size: 0.72rem; color: var(--mid); }

.grid-wrap { padding: 0 3rem; }

.footer {
    background: var(--black); padding: 1.8rem 3rem;
    display: flex; align-items: center;
    justify-content: space-between; margin-top: 3rem;
}

#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { visibility: hidden !important; height: 0 !important; }
.stDeployButton { display: none !important; }

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #CCC; border-radius: 2px; }
[data-testid="stHorizontalBlock"] { gap: 0.8rem !important; }

@media screen and (max-width: 768px) {
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
    }
    [data-testid="column"] {
        min-width: 48% !important;
        max-width: 48% !important;
        flex: 0 0 48% !important;
    }
    .grid-wrap { padding: 0 0.5rem !important; }
    .navbar { padding: 0 1rem !important; height: 52px !important; }
    .nav-logo { font-size: 1.2rem !important; }
    .catbar { padding: 0 0.5rem !important; }
    .cat { font-size: 0.6rem !important; padding: 0.7rem 0.8rem !important; }
    .search-section { padding: 0.7rem 1rem !important; }
    .result-bar { padding: 0.5rem 1rem !important; flex-direction: column !important; gap: 0.2rem !important; }
    .sec-head { padding: 1rem 1rem 0.8rem !important; }
    .aes-hero { padding: 1rem !important; }
    .aes-title { font-size: 1.3rem !important; }
    .sel-banner { padding: 1rem !important; }
    .aes-btn-wrap { padding: 0.8rem 0.5rem !important; }
    .footer { padding: 1rem !important; flex-direction: column !important; gap: 0.5rem !important; text-align: center !important; }
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════

def safe_int(val, default=0):
    try:
        v = float(val)
        if np.isinf(v) or np.isnan(v):
            return default
        return int(v)
    except:
        return default


def card_html(p, sim=None):
    aesthetic = p.get("aesthetic", "streetwear")
    meta      = AESTHETICS_META.get(aesthetic, AESTHETICS_META["streetwear"])
    discount  = safe_int(p.get("discount", 0))
    price     = safe_int(p.get("price", 0))
    rating    = float(p.get("rating", 0))
    image     = p.get("image_url", "")
    link      = p.get("product_link", "#")
    name      = p.get("product_name_clean", "")
    brand     = name.split()[0].upper() if name else ""
    mrp       = int(price / (1 - discount / 100)) if discount > 0 and discount < 100 else price

    disc    = '<div style="position:absolute;top:0;left:0;background:#E63A00;color:white;font-size:0.6rem;font-weight:800;padding:4px 8px;letter-spacing:0.5px">{d}% OFF</div>'.format(d=discount) if discount > 0 else ""
    #aestag  = '<div style="position:absolute;top:8px;right:8px;background:{c}22;color:{c};font-size:0.52rem;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;padding:3px 7px;border-radius:2px">{e} {l}</div>'.format(c=meta["color"], e=meta["emoji"], l=meta["label"])
    matchb  = '<div style="position:absolute;bottom:0;left:0;right:0;background:rgba(28,28,28,0.82);color:white;font-size:0.6rem;font-weight:800;letter-spacing:1.5px;padding:5px 8px;text-align:center">● {s:.0%} MATCH</div>'.format(s=sim) if sim else ""
    mrp_str = '<span style="font-size:0.68rem;color:#BBBBBB;text-decoration:line-through">₹{m:,}</span>'.format(m=mrp) if discount > 0 else ""
    off_str = '<span style="font-size:0.68rem;font-weight:700;color:#E63A00">{d}% off</span>'.format(d=discount) if discount > 0 else ""

    html = """<!DOCTYPE html>
<html>
<head>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Inter, sans-serif; background: white; }}
  .card {{ background: white; overflow: hidden; position: relative; border-radius: 3px; transition: box-shadow 0.2s, transform 0.2s; }}
  .card:hover {{ box-shadow: 0 4px 20px rgba(0,0,0,0.10); transform: translateY(-2px); }}
  .card-img-wrap {{ position: relative; overflow: hidden; background: #F9F9F9; }}
  .card-img {{ width: 100%; aspect-ratio: 3/4; object-fit: cover; display: block; transition: transform 0.4s ease; }}
  .card:hover .card-img {{ transform: scale(1.05); }}
  .card-body {{ padding: 0.55rem 0.7rem 0.7rem; }}
  .brand {{ font-size: 0.72rem; font-weight: 800; color: #1C1C1C; text-transform: uppercase; letter-spacing: 0.3px; margin-bottom: 0.1rem; }}
  .pname {{ font-size: 0.7rem; color: #888888; line-height: 1.35; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 0.45rem; }}
  .price-row {{ display: flex; align-items: baseline; gap: 0.4rem; margin-bottom: 0.25rem; flex-wrap: wrap; }}
  .price-now {{ font-size: 0.92rem; font-weight: 800; color: #1C1C1C; }}
  .rating-row {{ display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.5rem; }}
  .rtag {{ background: #2E7D32; color: white; font-size: 0.58rem; font-weight: 800; padding: 2px 6px; border-radius: 2px; }}
  .rcount {{ font-size: 0.62rem; color: #BBBBBB; }}
  .view-btn {{ display: block; text-align: center; text-decoration: none; border: 1.5px solid #1C1C1C; color: #1C1C1C; font-size: 0.62rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; padding: 0.45rem 0; border-radius: 2px; transition: all 0.15s; }}
  .view-btn:hover {{ background: #E63A00; border-color: #E63A00; color: white; }}
</style>
</head>
<body>
<div class="card">
  <div class="card-img-wrap">
    <img class="card-img" src="{image}" onerror="this.style.background='#F0F0F0';this.src=''" />
    {disc}{matchb}
  </div>
  <div class="card-body">
    <div class="brand">{brand}</div>
    <div class="pname">{name}</div>
    <div class="price-row">
      <span class="price-now">₹{price:,}</span>
      {mrp_str}{off_str}
    </div>
    <div class="rating-row">
      <span class="rtag">★ {rating}</span>
      <span class="rcount">Rated</span>
    </div>
    <a href="{link}" target="_blank" class="view-btn">View on Amazon</a>
  </div>
</div>
</body>
</html>""".format(
        image   = image,
        disc    = disc,
        #aestag  = aestag,
        matchb  = matchb,
        brand   = brand,
        name    = name,
        price   = price,
        mrp_str = mrp_str,
        off_str = off_str,
        rating  = rating,
        link    = link
    )
    return html


def render_grid(products, prefix, sim_scores=None, ncols=5):
    st.markdown('<div class="grid-wrap">', unsafe_allow_html=True)
    for row_start in range(0, len(products), ncols):
        row  = products[row_start: row_start + ncols]
        cols = st.columns(ncols, gap="small")
        for ci, p in enumerate(row):
            idx   = row_start + ci
            score = sim_scores[idx] if sim_scores and idx < len(sim_scores) else None
            with cols[ci]:
                components.html(
                    card_html(p, sim=score),
                    height=550,
                    scrolling=False
                )
                btn_key = f"{prefix}_{idx}_{str(p.get('product_name_clean',''))[:15]}"
                if st.button("Find Similar", key=btn_key):
                    st.session_state["sel_product"] = p
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def call_similar(product_name, top_k=10):
    try:
        r = requests.post(f"{API_URL}/recommend/similar", json={
            "product_name": product_name,
            "top_k"       : top_k
        }, timeout=10)
        if r.status_code == 200:
            return r.json()["recommendations"]
        return []
    except:
        return []


def call_aesthetic(aesthetic, top_k=20):
    try:
        r = requests.post(f"{API_URL}/recommend/aesthetic", json={
            "aesthetic": aesthetic,
            "top_k"    : top_k
        }, timeout=10)
        if r.status_code == 200:
            return r.json()["recommendations"]
        return []
    except:
        return []

# ══════════════════════════════════════════════════════
# NAVBAR
# ══════════════════════════════════════════════════════

st.markdown(f"""
<div class="ticker">
    <b>FLAT 40–80% OFF</b> on {len(df):,} Products &nbsp;·&nbsp;
    <b>AI-Powered</b> Style Recommendations for Gen Z
</div>
<div class="navbar">
  <div class="nav-logo">AETH<span>S</span>AI</div>
  <div class="nav-right">
    <div class="nav-icon">♡<br>Wishlist</div>
    <div class="nav-icon">🛍<br>Bag</div>
  </div>
</div>
<div class="catbar">
  <span class="cat active">Streetwear</span>
  <span class="cat">Old Money</span>
  <span class="cat">College</span>
  <span class="cat">Date Clean</span>
  <span class="cat">Athleisure</span>
  <span class="cat">Y2K Party</span>
  <span class="cat">Office</span>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════

tab1, tab2 = st.tabs(["  Find Similar  ", "  Browse Aesthetics  "])

# ══════════════════════════════════════════════════════
# TAB 1 — FIND SIMILAR
# ══════════════════════════════════════════════════════

with tab1:

    st.markdown('<div class="search-section">', unsafe_allow_html=True)
    search = st.text_input(
        "Search",
        placeholder=" oversized tshirt, linen shirt, cargo pants...",
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if "sel_product" in st.session_state:
        sel  = st.session_state["sel_product"]
        meta = AESTHETICS_META.get(sel.get("aesthetic", "streetwear"), AESTHETICS_META["streetwear"])

        st.markdown(f"""
<div class="sel-banner">
  <img class="sel-img" src="{sel.get('image_url','')}"
       onerror="this.style.background='#EEE';this.src=''" />
  <div>
    <div class="sel-tag">{meta['emoji']} {meta['label']} &nbsp;·&nbsp; Showing Similar Products</div>
    <div class="sel-name">{sel.get('product_name_clean','')}</div>
    <div class="sel-price">₹{safe_int(sel.get('price',0)):,}
      {'&nbsp;<span style="font-size:0.78rem;color:var(--red);font-family:Inter">' + str(safe_int(sel.get('discount',0))) + '% off</span>' if safe_int(sel.get('discount',0)) > 0 else ''}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="sec-head">
  <span class="sec-title">Similar Products</span>
  <span class="sec-sub">Powered by Cosine Similarity Engine</span>
</div>
""", unsafe_allow_html=True)

        with st.spinner("Finding similar products..."):
            recs = call_similar(sel.get("product_name_clean", ""), top_k=10)

        if recs:
            sim_scores = [r.get("similarity", 0) for r in recs]
            render_grid(recs, prefix="sim", sim_scores=sim_scores, ncols=5)
        else:
            st.warning("Could not fetch recommendations. Is FastAPI running on port 8000?")

        st.markdown('<div class="grid-wrap" style="margin-top:1rem">', unsafe_allow_html=True)
        if st.button("← Back to All Products", key="back_btn"):
            del st.session_state["sel_product"]
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        if search.strip():
            q    = search.strip().lower()
            pool = df[df['product_name_clean'].str.contains(q, case=False, na=False)].head(25).to_dict(orient='records')
        else:
            pool = HOMEPAGE

        st.markdown(f"""
<div class="result-bar">
  <div class="result-count">Showing <b>{len(pool)} products</b></div>
  <div class="result-hint">Click <b>Find Similar</b> on any product</div>
</div>
""", unsafe_allow_html=True)

        if not pool:
            st.markdown('<div style="padding:3rem;color:#999;font-family:Inter;font-size:0.85rem">No products found.</div>', unsafe_allow_html=True)
        else:
            render_grid(pool, prefix="all", ncols=5)

# ══════════════════════════════════════════════════════
# TAB 2 — BROWSE BY AESTHETIC
# ══════════════════════════════════════════════════════
with tab2:

    if "sel_product" in st.session_state:
        sel       = st.session_state["sel_product"]
        meta      = AESTHETICS_META.get(sel.get("aesthetic", "streetwear"), AESTHETICS_META["streetwear"])
        disc_html = f'&nbsp;<span style="font-size:0.78rem;color:#E63A00;font-family:Inter">{safe_int(sel.get("discount",0))}% off</span>' if safe_int(sel.get("discount", 0)) > 0 else ""

        st.markdown(f"""
<div class="sel-banner">
  <img class="sel-img" src="{sel.get('image_url','')}"
       onerror="this.style.background='#EEE';this.src=''" />
  <div>
    <div class="sel-tag">{meta['emoji']} {meta['label']} &nbsp;·&nbsp; Showing Similar Products</div>
    <div class="sel-name">{sel.get('product_name_clean','')}</div>
    <div class="sel-price">₹{safe_int(sel.get('price',0)):,}{disc_html}</div>
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="sec-head">
  <span class="sec-title">Similar Products</span>
  <span class="sec-sub">Powered by Cosine Similarity Engine</span>
</div>
""", unsafe_allow_html=True)

        with st.spinner("Finding similar products..."):
            recs = call_similar(sel.get("product_name_clean", ""), top_k=10)

        if recs:
            sim_scores = [r.get("similarity", 0) for r in recs]
            render_grid(recs, prefix="sim2", sim_scores=sim_scores, ncols=5)
        else:
            st.warning("Could not fetch recommendations. Is FastAPI running on port 8000?")

        st.markdown('<div class="grid-wrap" style="margin-top:1rem">', unsafe_allow_html=True)
        if st.button("← Back to Aesthetics", key="back_btn2"):
            del st.session_state["sel_product"]
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="aes-btn-wrap">', unsafe_allow_html=True)
        btn_cols = st.columns(7, gap="small")
        for i, (aes_key, meta) in enumerate(AESTHETICS_META.items()):
            with btn_cols[i]:
                if st.button(f"{meta['emoji']} {meta['label']}", key=f"aes_btn_{aes_key}"):
                    st.session_state["browse_aes"] = aes_key
        st.markdown('</div>', unsafe_allow_html=True)

        if "browse_aes" not in st.session_state:
            st.session_state["browse_aes"] = "streetwear"

        cur = st.session_state["browse_aes"]
        m   = AESTHETICS_META[cur]

        with st.spinner(f"Loading {m['label']} products..."):
            pool = call_aesthetic(cur, top_k=20)

        if not pool:
            pool = (
                df[df['aesthetic'] == cur]
                  .sort_values('score', ascending=False)
                  .head(20)
                  .to_dict(orient='records')
            )

        st.markdown(f"""
<div class="aes-hero">
  <div class="aes-eyebrow">Aesthetic Collection</div>
  <div class="aes-title">{m['emoji']} {m['label']}</div>
  <div class="aes-desc">{m['desc']} &nbsp;·&nbsp; {len(df[df['aesthetic']==cur])} products</div>
</div>
""", unsafe_allow_html=True)

        render_grid(pool, prefix=f"br_{cur}", ncols=5)
# ══════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════

st.markdown(f"""
<div class="footer">
  <div style="font-family:'Nunito Sans',sans-serif;font-size:1.1rem;
              font-weight:900;color:white;letter-spacing:-0.3px">
    AETH<span style="color:#E63A00">S</span>AI
  </div>
  <div style="font-family:'Inter',sans-serif;font-size:0.62rem;
              color:#555;letter-spacing:2px;text-transform:uppercase">
    AI-Powered Fashion Recommendation Engine
  </div>
  <div style="font-family:'Inter',sans-serif;font-size:0.62rem;
              color:#555;letter-spacing:1.5px;text-transform:uppercase">
    {len(df):,} Products &nbsp;·&nbsp; 7 Aesthetics
  </div>
</div>
""", unsafe_allow_html=True)