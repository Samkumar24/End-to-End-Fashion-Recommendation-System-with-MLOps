import streamlit as st

st.set_page_config(
    page_title="AesthsAI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════
# DATA — real images + links from your dataset
# ══════════════════════════════════════════════════════

PRODUCTS = [
    # streetwear
    {"id":0,  "aesthetic":"streetwear",     "name":"Men's Cottonblend Graphic Print Oversized Tshirt",            "price":286,  "rating":4.0, "discount":74, "image":"https://m.media-amazon.com/images/I/61WYx598KKL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Cottonblend-Graphic-Oversized-FS49_Navy_Boston_P_Navy/dp/B0FHDHSFYY"},
    {"id":1,  "aesthetic":"streetwear",     "name":"Half Sleeve Oversized Drop Shoulder Printed T-Shirt",         "price":298,  "rating":4.0, "discount":73, "image":"https://m.media-amazon.com/images/I/61AE3iKBYPL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Oversized-Graphic-Cottonblend-FS49_Black_Space_P_Red_L/dp/B0FK5PK4VG"},
    {"id":2,  "aesthetic":"streetwear",     "name":"Graphic Font Printed Cottonblend Oversized Tshirts",          "price":286,  "rating":4.2, "discount":74, "image":"https://m.media-amazon.com/images/I/61EbiUi7r1L._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Graphic-Cottonblend-Oversized-FS49_ORNG_RAWENERGY_P_Orange_3XL/dp/B0F99NP71S"},
    {"id":3,  "aesthetic":"streetwear",     "name":"Casual Cottonblend Printed Round Neck Oversized Tshirt",      "price":286,  "rating":4.1, "discount":74, "image":"https://m.media-amazon.com/images/I/61kYmRqjzaL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Cottonblend-Shoulder-Oversized-FS49_Brown_NEWYORKK_P_Brown_XL/dp/B0FK5GC8XD"},
    {"id":4,  "aesthetic":"streetwear",     "name":"Mens Cotton Graphic Print Oversized Fit T-Shirt",             "price":499,  "rating":4.1, "discount":72, "image":"https://m.media-amazon.com/images/I/41XlGaQPirL._AC_UL320_.jpg",  "link":"https://www.amazon.in/NOBERO-Mens-Oversized-T-Shirt-1M-TWRT-C0832-BL_Black/dp/B0DBZ9PQN2"},
    {"id":5,  "aesthetic":"streetwear",     "name":"Pure Cotton Oversized Baggy Fit Graphic Printed T-Shirt",     "price":399,  "rating":4.0, "discount":67, "image":"https://m.media-amazon.com/images/I/61b1tL147eL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Veirdo%C2%AE_Pure-Oversized-Graphic-Printed-T-Shirt/dp/B0DG34FCY7"},
    {"id":6,  "aesthetic":"streetwear",     "name":"Men's Graphic Print Oversized Fit Pure Cotton T-Shirt",       "price":699,  "rating":4.3, "discount":46, "image":"https://m.media-amazon.com/images/I/61512ETok5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Bewakoof-Official-Garfield-Merchandise-Smiling/dp/B0C73RDWXV"},
    {"id":7,  "aesthetic":"streetwear",     "name":"Men's Cotton Oversized Fit Graphic Print T-Shirt",            "price":499,  "rating":3.9, "discount":72, "image":"https://m.media-amazon.com/images/I/51WDqhCR8+L._AC_UL320_.jpg",  "link":"https://www.amazon.in/NOBERO-Graphic-Oversized-T-Shirt-1M-TWRT-C0910-OG_Blush/dp/B0DZ2R8Z6W"},

    # old_money
    {"id":8,  "aesthetic":"old_money",      "name":"Men's Solid Linen Cotton Casual Full Sleeve Summer Shirt",    "price":469,  "rating":3.0, "discount":77, "image":"https://m.media-amazon.com/images/I/81I4F9xgijL._AC_UL320_.jpg",  "link":"https://www.amazon.in/NexaFlair-Summer-Regular-Stylish-Everyday-Regular/dp/B0DXCYNMCX"},
    {"id":9,  "aesthetic":"old_money",      "name":"Success Linen Button-Down Shirt Textured Long Sleeve",        "price":379,  "rating":3.3, "discount":10, "image":"https://m.media-amazon.com/images/I/61v4ecETAZL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Success-Button-Down-Textured-Sleeve-Regular/dp/B0FF1FJSLS"},
    {"id":10, "aesthetic":"old_money",      "name":"Men's Linen Blend Full Sleeve Relaxed Fit Casual Shirt",      "price":749,  "rating":3.4, "discount":61, "image":"https://m.media-amazon.com/images/I/61DZg55DeUL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Urbano-Fashion-Purple-Relaxed-shirtlinregfl-02-purple-xl/dp/B0F5WJM4QH"},
    {"id":11, "aesthetic":"old_money",      "name":"Casual Button Down Long Sleeve Linen Shirt Fashion Textured",  "price":499,  "rating":3.8, "discount":77, "image":"https://m.media-amazon.com/images/I/71dF+pDGxIL._AC_UL320_.jpg",  "link":"https://www.amazon.in/CB-COLEBROOK-Casual-Button-Fashion-Textured/dp/B0D77N88Q3"},
    {"id":12, "aesthetic":"old_money",      "name":"Men's Solid Cotton Polyester Blend Straight Kurta Shirt",     "price":499,  "rating":4.1, "discount":71, "image":"https://m.media-amazon.com/images/I/71BTNI3lEAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Zombom-Cotton-Straight-Regular-Sleeve/dp/B0D94DG16W"},
    {"id":13, "aesthetic":"old_money",      "name":"Men's Linen Blend Mandarin Collar Relaxed Fit Solid Shirt",   "price":749,  "rating":3.9, "discount":61, "image":"https://m.media-amazon.com/images/I/61uNa0BqQ5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Urbano-Fashion-Relaxed-Mandarin-shirtlinmdfl-01-white-m/dp/B0F5WH5951"},
    {"id":14, "aesthetic":"old_money",      "name":"Classic Linen Button-Down Shirt Pink Casual Long Sleeve",     "price":489,  "rating":3.4, "discount":80, "image":"https://m.media-amazon.com/images/I/51YjJU7FZHL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Oquent-Classic-Button-Down-Regular-Business/dp/B0FV91SD1N"},
    {"id":15, "aesthetic":"old_money",      "name":"Men's Linen Cotton Long Sleeve Casual Regular Fit Shirt",     "price":598,  "rating":3.7, "discount":77, "image":"https://m.media-amazon.com/images/I/81LOxcZemfL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Miraan-Cotton-Sleeve-Casual-SIGLINENGREYL_Grey_Large/dp/B0C9ZQY2RY"},

    # college_casual
    {"id":16, "aesthetic":"college_casual", "name":"Men Cotton Half Sleeves Round Neck Regular Fit Casual T-Shirt","price":269, "rating":4.0, "discount":0,  "image":"https://m.media-amazon.com/images/I/61ezNvbfQPL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Lux-Cozi-Maroon-Cotton-Tshirt/dp/B0D39544VM"},
    {"id":17, "aesthetic":"college_casual", "name":"Men's Solid Cotton T Shirt Round Neck Half Sleeve Pack of 3", "price":449,  "rating":3.7, "discount":88, "image":"https://m.media-amazon.com/images/I/51U2dDaeOGL._AC_UL320_.jpg",  "link":"https://www.amazon.in/London-Hills-Solid-Sleeve-T-Shirt/dp/B07FLNVWB5"},
    {"id":18, "aesthetic":"college_casual", "name":"Men's Cotton Blend Regular Fit Solid Round Neck T-Shirts Pack of 4","price":799,"rating":3.9,"discount":38,"image":"https://m.media-amazon.com/images/I/61iRb7DYaQL._AC_UL320_.jpg","link":"https://www.amazon.in/London-Hills-Sleeve-Multicolor-T-Shirts/dp/B0BSQ9WYYQ"},
    {"id":19, "aesthetic":"college_casual", "name":"U.S. Polo Assn Mens Crew Neck Embroidered Logo T-Shirt",      "price":500,  "rating":3.8, "discount":28, "image":"https://m.media-amazon.com/images/I/612O38TYThL._AC_UL320_.jpg",  "link":"https://www.amazon.in/U-S-Polo-Assn-Regular-I633-001-PL_White_Large/dp/B0793NHJZJ"},
    {"id":20, "aesthetic":"college_casual", "name":"Men's Solid Cotton T Shirt Round Neck Half Sleeve Plain Fit",  "price":319,  "rating":4.0, "discount":54, "image":"https://m.media-amazon.com/images/I/61-Hg4wfqpL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Amazon-Brand-Regular-T-Shirt-SS20SYMTEE33_Black/dp/B0C5XVJBKL"},
    {"id":21, "aesthetic":"college_casual", "name":"Men's Super Combed Cotton Rich Solid Round Neck T-Shirt",      "price":579,  "rating":4.2, "discount":0,  "image":"https://m.media-amazon.com/images/I/71ihH2Tnt1L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Jockey-Combed-Cotton-Sleeve-T-Shirt_Thyme_L/dp/B0DY83M6C4"},
    {"id":22, "aesthetic":"college_casual", "name":"Solid Men's Round Neck Cotton Blend Half Sleeve T-Shirts",     "price":223,  "rating":3.7, "discount":83, "image":"https://m.media-amazon.com/images/I/61v-HyIcV0L._AC_UL320_.jpg",  "link":"https://www.amazon.in/London-Hills-Solid-Sleeve-T-Shirt/dp/B07FLBTTNC"},

    # date_clean
    {"id":23, "aesthetic":"date_clean",     "name":"Men's Satin Shirt Spread Collar Solid Full Sleeves Regular Fit","price":499,"rating":4.1,"discount":50,"image":"https://m.media-amazon.com/images/I/71LJY7GSnQL._AC_UL320_.jpg","link":"https://www.amazon.in/IndoPrimo-Classic-Plain-Casual-Sleeve/dp/B0D961J769"},
    {"id":24, "aesthetic":"date_clean",     "name":"Men's Stylish Satin Shirt Party Formal Casual Full Sleeve",   "price":499,  "rating":4.6, "discount":75, "image":"https://m.media-amazon.com/images/I/51+bKUZHtQL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Stylish-Formal-Casual-Sleeve/dp/B0G1BM7TK5"},
    {"id":25, "aesthetic":"date_clean",     "name":"Mens Satin Regular Fit Formal Shirt",                         "price":441,  "rating":3.7, "discount":81, "image":"https://m.media-amazon.com/images/I/61u3TDteH6L._AC_UL320_.jpg",  "link":"https://www.amazon.in/CVC-Sleeves-Regular-Causal-Formal/dp/B0CGNQ3B1K"},
    {"id":26, "aesthetic":"date_clean",     "name":"Men's Stylish Solid Satin Casual Shirt Full Sleeves Silk",    "price":499,  "rating":3.8, "discount":72, "image":"https://m.media-amazon.com/images/I/61R1R+tsmLL._AC_UL320_.jpg",  "link":"https://www.amazon.in/DEELMO-Stylish-Solid-Casual-Sleeves/dp/B0DPL7Z2TS"},
    {"id":27, "aesthetic":"date_clean",     "name":"Combo Stylish Solid Satin Casual Shirt Full Sleeves Pack of 2","price":799, "rating":4.2, "discount":68, "image":"https://m.media-amazon.com/images/I/617Cah36h9L._AC_UL320_.jpg",  "link":"https://www.amazon.in/DEELMO-Combo-Stylish-Casual-Sleeves/dp/B0FCFP4HKH"},
    {"id":28, "aesthetic":"date_clean",     "name":"Slim Fit Satin Cotton Formal Shirt for Men",                  "price":659,  "rating":3.9, "discount":56, "image":"https://m.media-amazon.com/images/I/61N8rUnDlSL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Majestic-Man-Cotton-Formal-Purple/dp/B0D5844PHP"},
    {"id":29, "aesthetic":"date_clean",     "name":"Men's Satin Solid Regular Fit Shirt with Satin Sheen Luxury", "price":1159, "rating":4.0, "discount":36, "image":"https://m.media-amazon.com/images/I/51qC98m0YuL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Regular-Shirt-PESFWNUPS22148_Black/dp/B0CX8X514S"},

    # gym_athleisure
    {"id":30, "aesthetic":"gym_athleisure", "name":"Men's Regular Fit Quick-Dry Active T-Shirt for Gym & Sports", "price":199,  "rating":4.0, "discount":75, "image":"https://m.media-amazon.com/images/I/6136GknW7aL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Regular-Quick-Dry-Active-T-Shirt-Sports/dp/B0DYD5537M"},
    {"id":31, "aesthetic":"gym_athleisure", "name":"Active Fit Sports T-Shirt Lightweight Quick Dry Polyester",   "price":299,  "rating":3.7, "discount":57, "image":"https://m.media-amazon.com/images/I/71+8DkhB7GL._AC_UL320_.jpg",  "link":"https://www.amazon.in/3Colours-Active-Mens-Sports-T-Shirt/dp/B0FNWFJYCY"},
    {"id":32, "aesthetic":"gym_athleisure", "name":"Men Polyester Quick Dry Half Sleeve Sportswear Gym T-Shirt",  "price":341,  "rating":4.0, "discount":79, "image":"https://m.media-amazon.com/images/I/411cZXcsbAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/CHKOKKO-Solid-Regular-T-Shirt-Black/dp/B083M3D4H2"},
    {"id":33, "aesthetic":"gym_athleisure", "name":"Gym T Shirts Workout Sports Quick Dry Training Active Wear",  "price":498,  "rating":4.4, "discount":67, "image":"https://m.media-amazon.com/images/I/61DxYUqAOVL._AC_UL320_.jpg",  "link":"https://www.amazon.in/FIGHTERHERO-Polyester-Regular-T-Shirt-T-Shirts/dp/B0FXXV9BL3"},
    {"id":34, "aesthetic":"gym_athleisure", "name":"Gym T Shirts Workout Breathable Dry Fit Running Regular Fit", "price":399,  "rating":4.2, "discount":60, "image":"https://m.media-amazon.com/images/I/71L9aVgSYDL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Boldfit-Quick-Dry-Anti-Odor-Lightweight-Breathable/dp/B0CVX7HZLM"},
    {"id":35, "aesthetic":"gym_athleisure", "name":"Men T-Shirt Adidas Polyester CLASSIC Sports",                 "price":779,  "rating":4.0, "discount":35, "image":"https://m.media-amazon.com/images/I/71vO30G+ucL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Adidas-Polyester-CLASSIC-Sports-T-Shirts/dp/B07XKZF6V5"},
    {"id":36, "aesthetic":"gym_athleisure", "name":"Tshirt Regular Fit Gym Active Wear Running Mens Workout",     "price":499,  "rating":4.3, "discount":44, "image":"https://m.media-amazon.com/images/I/611lChGYIML._AC_UL320_.jpg",  "link":"https://www.amazon.in/Boldfit-Training-Workout-Tshirts-T-Shirts/dp/B0D5CZ5G23"},

    # y2k_party
    {"id":37, "aesthetic":"y2k_party",      "name":"Men Printed Satin Full Sleeve Shirt Lightweight Casual Party", "price":999, "rating":3.9, "discount":50, "image":"https://m.media-amazon.com/images/I/51rP+8gN8CL._AC_UL320_.jpg",  "link":"https://www.amazon.in/RIVANORA-Black-Sequin-Regular-Evening/dp/B0GHQTT9F9"},
    {"id":38, "aesthetic":"y2k_party",      "name":"Men's Rayon Ethnic Shirt",                                    "price":1552, "rating":4.3, "discount":54, "image":"https://m.media-amazon.com/images/I/617UuB-QY5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/VM-Black-Rayon-Ethnic-Shirt_VMMSH255BL_42/dp/B0CPPXH2HZ"},
    {"id":39, "aesthetic":"y2k_party",      "name":"Men's Premium Satin Shirt Party Formal Casual Full Sleeve",   "price":495,  "rating":4.6, "discount":75, "image":"https://m.media-amazon.com/images/I/41RTqea0uAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Premium-Satin-Formal-Casual/dp/B0G1BN5RMP"},
    {"id":40, "aesthetic":"y2k_party",      "name":"Men's Regular Fit Satin Designer Shirt Vertical Line Sequence","price":499, "rating":4.2, "discount":75, "image":"https://m.media-amazon.com/images/I/61A33rn70xL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Designer-Vertical-Sequence-Business/dp/B0FT7FWX8F"},
    {"id":41, "aesthetic":"y2k_party",      "name":"Men's Georgette Ethnic Shirt Embroidered for Festivals",      "price":1269, "rating":3.9, "discount":53, "image":"https://m.media-amazon.com/images/I/71ddH4JP8wL._AC_UL320_.jpg",  "link":"https://www.amazon.in/VASTRAMAY-Georgette-Sequins-Collection-Men_VASMSH209MA_36/dp/B0CPPY86K9"},
    {"id":42, "aesthetic":"y2k_party",      "name":"Men's Cotton Regular Fit Shirt Casual Spread Collar Short Sleeve","price":817,"rating":3.8,"discount":57,"image":"https://m.media-amazon.com/images/I/61A+O+J6JLL._AC_UL320_.jpg","link":"https://www.amazon.in/Campus-Sutra-Metallic-Pleat-Creased-Everyday/dp/B0CY2M44FT"},

    # office_smart
    {"id":43, "aesthetic":"office_smart",   "name":"Men's Slim Fit Formal Shirt Solid Comfortable Everyday Office", "price":559,"rating":4.0, "discount":65, "image":"https://m.media-amazon.com/images/I/71q8mNTUk0L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Highlander-Polyester-Shirt-PHSH000175_Peanut-Brown/dp/B0F44L54CM"},
    {"id":44, "aesthetic":"office_smart",   "name":"Men's Casual Printed Striped Stylish Latest Formal Shirt",     "price":372,  "rating":3.6, "discount":77, "image":"https://m.media-amazon.com/images/I/71faNU5G5uL._AC_UL320_.jpg",  "link":"https://www.amazon.in/TURN-Casual-Printed-Striped-Stylish/dp/B0CBX53QJV"},
    {"id":45, "aesthetic":"office_smart",   "name":"Men's Everyday Solid Slim Fit Full Sleeve Formal Shirt",       "price":899,  "rating":3.9, "discount":36, "image":"https://m.media-amazon.com/images/I/71j3iS8mFuL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFOSLPO33719_Navy/dp/B0BHW7W1CV"},
    {"id":46, "aesthetic":"office_smart",   "name":"Men's Slim Fit Full Sleeve Pin-Striped Formal Shirt Cotton Rich","price":879,"rating":4.2, "discount":37, "image":"https://m.media-amazon.com/images/I/61snIWegiiL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFWSLBQ29664_Blue/dp/B0CVS58N9P"},
    {"id":47, "aesthetic":"office_smart",   "name":"Men's Cotton Blend Solid Shirt Spread Collar Full Sleeve Slim Fit","price":369,"rating":4.2,"discount":77,"image":"https://m.media-amazon.com/images/I/51FXI7pJ-YL._AC_UL320_.jpg","link":"https://www.amazon.in/MILDIN-Regular-Cotton-Hemline-38/dp/B0DPCS4WBJ"},
    {"id":48, "aesthetic":"office_smart",   "name":"Men's Classic Solid Full Sleeve Slim Fit Shirt Cotton Rich",   "price":825,  "rating":4.0, "discount":41, "image":"https://m.media-amazon.com/images/I/51MUZjEzZKL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFWSLBB52350_Grey/dp/B0D1C17YZ4"},
    {"id":49, "aesthetic":"office_smart",   "name":"Men's Solid Cotton Formal Shirt Plain Full Sleeve Regular Fit", "price":549, "rating":4.0, "discount":54, "image":"https://m.media-amazon.com/images/I/61GtS6IrR7L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Amazon-Brand-Symbol-Regular-SS20-SYM-FS-01_EPP-1A_White/dp/B081QJW5GG"},
]

AESTHETICS_META = {
    "streetwear":     {"label":"Streetwear",       "emoji":"🔥", "color":"#FF4D00", "desc":"Bold graphics · oversized fits · urban edge"},
    "old_money":      {"label":"Old Money",        "emoji":"✦",  "color":"#C9A84C", "desc":"Linen shirts · quiet luxury · timeless pieces"},
    "college_casual": {"label":"College Casual",   "emoji":"🎓", "color":"#4A90D9", "desc":"Solid tees · comfortable · everyday wear"},
    "date_clean":     {"label":"Date Clean",       "emoji":"🌸", "color":"#E8A0BF", "desc":"Satin shirts · polished · effortlessly sharp"},
    "gym_athleisure": {"label":"Gym & Athleisure", "emoji":"⚡", "color":"#00E5A0", "desc":"Quick-dry · performance fit · active lifestyle"},
    "y2k_party":      {"label":"Y2K Party",        "emoji":"💫", "color":"#BF5FFF", "desc":"Bold prints · sequins · maximalist energy"},
    "office_smart":   {"label":"Office Smart",     "emoji":"◈",  "color":"#A0B4C8", "desc":"Crisp formals · clean lines · boardroom ready"},
}

# ══════════════════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
section.main,
[data-testid="stAppViewBlockContainer"] {
    background: #080808 !important;
}

[data-testid="block-container"] {
    padding: 0 2.5rem 4rem !important;
    max-width: 1440px !important;
}

/* HEADER */
.hdr {
    display:flex; justify-content:space-between;
    align-items:center; padding:1.8rem 0 1.5rem;
    border-bottom:1px solid #181818; margin-bottom:0;
}
.logo {
    font-family:'Cormorant Garamond',serif;
    font-size:2rem; font-weight:700;
    color:#F2EFE9; letter-spacing:4px; text-transform:uppercase;
}
.logo em { color:#C9A84C; font-style:normal; }
.tagline {
    font-family:'DM Sans',sans-serif;
    font-size:0.6rem; color:#2A2A2A;
    letter-spacing:4px; text-transform:uppercase;
}

/* TABS */
div[data-testid="stTabs"] [role="tablist"] {
    background:transparent !important;
    border-bottom:1px solid #181818 !important;
    gap:0 !important; padding:0 !important;
}
div[data-testid="stTabs"] button[role="tab"] {
    font-family:'DM Sans',sans-serif !important;
    font-size:0.68rem !important; letter-spacing:3px !important;
    text-transform:uppercase !important; color:#2E2E2E !important;
    padding:1rem 1.6rem !important; border:none !important;
    background:transparent !important; border-radius:0 !important;
    transition:color 0.2s !important;
}
div[data-testid="stTabs"] button[role="tab"]:hover { color:#666 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] {
    color:#F2EFE9 !important;
    border-bottom:1px solid #C9A84C !important;
}

/* PRODUCT CARD */
.card {
    background:#0C0C0C; border:1px solid #161616;
    border-radius:2px; overflow:hidden;
    transition:border-color 0.25s,transform 0.25s;
    height:100%;
}
.card:hover { border-color:#252525; transform:translateY(-2px); }
.card-img-wrap { position:relative; overflow:hidden; }
.card-img {
    width:100%; aspect-ratio:1/1; object-fit:cover;
    background:#111; display:block;
    transition:transform 0.5s ease;
}
.card:hover .card-img { transform:scale(1.04); }
.disc-badge {
    position:absolute; top:8px; left:8px;
    background:#C9A84C; color:#080808;
    font-family:'DM Sans',sans-serif; font-size:0.58rem;
    font-weight:600; letter-spacing:1px;
    padding:3px 6px; border-radius:1px;
}
.card-body { padding:0.8rem 0.85rem 0.85rem; }
.card-aes {
    font-family:'DM Sans',sans-serif; font-size:0.56rem;
    letter-spacing:2.5px; text-transform:uppercase; margin-bottom:0.35rem;
}
.card-name {
    font-family:'DM Sans',sans-serif; font-size:0.72rem;
    color:#888; line-height:1.45;
    display:-webkit-box; -webkit-line-clamp:2;
    -webkit-box-orient:vertical; overflow:hidden;
    min-height:2.1em; margin-bottom:0.6rem;
}
.card-row {
    display:flex; justify-content:space-between;
    align-items:baseline; margin-bottom:0.65rem;
}
.card-price {
    font-family:'Cormorant Garamond',serif;
    font-size:1.2rem; font-weight:600; color:#F2EFE9;
}
.card-rating { font-family:'DM Sans',sans-serif; font-size:0.68rem; color:#444; }
.card-rating b { color:#C9A84C; }
.sim-score {
    font-family:'DM Sans',sans-serif; font-size:0.58rem;
    color:#2E2E2E; letter-spacing:1.5px; margin-bottom:0.5rem;
}
.buy-btn {
    display:block; text-align:center; text-decoration:none !important;
    border:1px solid #1E1E1E; color:#555 !important;
    font-family:'DM Sans',sans-serif; font-size:0.6rem;
    letter-spacing:2px; text-transform:uppercase;
    padding:0.48rem 0; border-radius:1px;
    transition:all 0.2s;
}
.buy-btn:hover {
    border-color:#C9A84C; color:#C9A84C !important;
    background:rgba(201,168,76,0.04);
    text-decoration:none !important;
}

/* SECTION */
.sec-label {
    font-family:'DM Sans',sans-serif; font-size:0.58rem;
    letter-spacing:4px; text-transform:uppercase;
    color:#2A2A2A; margin-bottom:0.35rem;
}
.sec-title {
    font-family:'Cormorant Garamond',serif;
    font-size:2rem; font-weight:600;
    color:#F2EFE9; line-height:1; margin-bottom:1.5rem;
}

/* SELECTED BANNER */
.sel-banner {
    display:flex; gap:1.1rem; align-items:center;
    background:#0C0C0C; border:1px solid #1A1A1A;
    border-left:2px solid #C9A84C;
    padding:1rem 1.1rem; border-radius:2px; margin-bottom:1.8rem;
}
.sel-img {
    width:68px; height:68px; object-fit:cover;
    border-radius:1px; flex-shrink:0;
}
.sel-name { font-family:'DM Sans',sans-serif; font-size:0.78rem; color:#888; line-height:1.4; margin-bottom:0.3rem; }
.sel-meta { font-family:'Cormorant Garamond',serif; font-size:1.1rem; color:#F2EFE9; }

/* AES HERO */
.aes-hero { padding:1.6rem 0 1.4rem; border-bottom:1px solid #131313; margin-bottom:1.8rem; }
.aes-title { font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700; line-height:1; margin-bottom:0.3rem; }
.aes-desc { font-family:'DM Sans',sans-serif; font-size:0.7rem; color:#333; letter-spacing:1px; }

/* AESTHETIC PILL BUTTONS */
.stButton > button {
    background:#0C0C0C !important; border:1px solid #181818 !important;
    color:#333 !important; font-family:'DM Sans',sans-serif !important;
    font-size:0.62rem !important; letter-spacing:2px !important;
    text-transform:uppercase !important;
    padding:0.55rem 0 !important; border-radius:1px !important;
    transition:all 0.2s !important; width:100% !important;
}
.stButton > button:hover,
.stButton > button:focus {
    border-color:#C9A84C !important; color:#C9A84C !important;
    background:rgba(201,168,76,0.04) !important;
    box-shadow:none !important;
}

/* SEARCH */
.stTextInput input {
    background:#0C0C0C !important; border:1px solid #181818 !important;
    border-radius:1px !important; color:#F2EFE9 !important;
    font-family:'DM Sans',sans-serif !important; font-size:0.82rem !important;
}
.stTextInput input:focus { border-color:#C9A84C !important; box-shadow:none !important; }
.stTextInput input::placeholder { color:#2A2A2A !important; }
.stTextInput label { display:none !important; }
[data-testid="textInputRootElement"] label { display:none !important; }

/* DIVIDER */
.divider { border:none; border-top:1px solid #131313; margin:1.8rem 0; }

/* HIDE STREAMLIT CHROME */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { visibility:hidden !important; height:0 !important; }
.stDeployButton { display:none !important; }

/* SCROLLBAR */
::-webkit-scrollbar { width:3px; height:3px; }
::-webkit-scrollbar-track { background:#080808; }
::-webkit-scrollbar-thumb { background:#1A1A1A; border-radius:2px; }

/* COLUMN GAP */
[data-testid="stHorizontalBlock"] { gap:0.6rem !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════

def card_html(p, sim=None):
    meta  = AESTHETICS_META[p["aesthetic"]]
    disc  = f'<div class="disc-badge">−{p["discount"]}%</div>' if p["discount"] > 0 else ""
    sim_s = f'<div class="sim-score">{sim:.0%} MATCH</div>' if sim else ""
    return f"""
<div class="card">
  <div class="card-img-wrap">
    <img class="card-img" src="{p['image']}"
         onerror="this.style.opacity='0'" />
    {disc}
  </div>
  <div class="card-body">
    <div class="card-aes" style="color:{meta['color']}">{meta['emoji']} {meta['label']}</div>
    <div class="card-name">{p['name']}</div>
    {sim_s}
    <div class="card-row">
      <span class="card-price">₹{p['price']:,}</span>
      <span class="card-rating"><b>★ {p['rating']}</b></span>
    </div>
    <a href="{p['link']}" target="_blank" class="buy-btn">View on Amazon ↗</a>
  </div>
</div>"""


def render_grid(products, prefix, sim_scores=None, ncols=4):
    """Render product grid. prefix must be unique per call site."""
    for row_start in range(0, len(products), ncols):
        row  = products[row_start : row_start + ncols]
        cols = st.columns(ncols, gap="small")
        for ci, p in enumerate(row):
            idx   = row_start + ci
            score = sim_scores[idx] if sim_scores else None
            with cols[ci]:
                st.markdown(card_html(p, sim=score), unsafe_allow_html=True)
                btn_key = f"{prefix}_{p['id']}"
                if st.button("Similar ↗", key=btn_key):
                    st.session_state["sel_id"] = p["id"]
                    st.rerun()


# ══════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════

st.markdown("""
<div class="hdr">
  <div>
    <div class="logo">Aeth<em>s</em>AI</div>
    <div class="tagline">Fashion Recommendation Engine</div>
  </div>
  <div style="font-family:'DM Sans';font-size:0.6rem;color:#202020;letter-spacing:3px;text-transform:uppercase">
    13,813 Products &nbsp;·&nbsp; 7 Aesthetics
  </div>
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
    st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)

    search = st.text_input("", placeholder="Search — oversized tshirt, linen shirt, satin shirt...")

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── If a product was selected → show similar ──────
    if "sel_id" in st.session_state:
        sel = next((p for p in PRODUCTS if p["id"] == st.session_state["sel_id"]), None)

        if sel:
            meta = AESTHETICS_META[sel["aesthetic"]]

            # Selected banner
            st.markdown(f"""
<div class="sel-banner">
  <img class="sel-img" src="{sel['image']}" onerror="this.style.opacity='0'" />
  <div>
    <div style="font-size:0.55rem;letter-spacing:3px;
                color:{meta['color']};text-transform:uppercase;margin-bottom:0.3rem">
      {meta['emoji']} {meta['label']} &nbsp;·&nbsp; Showing similar products
    </div>
    <div class="sel-name">{sel['name']}</div>
    <div class="sel-meta">₹{sel['price']:,} &nbsp;·&nbsp; ★ {sel['rating']}</div>
  </div>
</div>
""", unsafe_allow_html=True)

            st.markdown('<div class="sec-label">Engine 1 — Cosine Similarity</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Similar Products</div>', unsafe_allow_html=True)

            # Demo: show other products from same aesthetic
            similar = [p for p in PRODUCTS if p["aesthetic"] == sel["aesthetic"] and p["id"] != sel["id"]]
            demo_scores = [0.95, 0.91, 0.88, 0.85, 0.82, 0.79, 0.76, 0.73]
            render_grid(similar[:8], prefix="sim", sim_scores=demo_scores, ncols=4)

            st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
            if st.button("← Back to all products", key="back_btn"):
                del st.session_state["sel_id"]
                st.rerun()

    # ── Default: show all products ────────────────────
    else:
        pool = PRODUCTS
        if search.strip():
            q    = search.strip().lower()
            pool = [p for p in PRODUCTS if q in p["name"].lower()]

        st.markdown(f'<div class="sec-label">{len(pool)} Products · Click "Similar ↗" on any product</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">All Products</div>', unsafe_allow_html=True)

        if not pool:
            st.markdown('<div style="color:#2A2A2A;padding:3rem 0;font-family:DM Sans;font-size:0.8rem;">No products found.</div>', unsafe_allow_html=True)
        else:
            render_grid(pool, prefix="all", ncols=4)


# ══════════════════════════════════════════════════════
# TAB 2 — BROWSE BY AESTHETIC
# ══════════════════════════════════════════════════════

with tab2:
    st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)

    # 7 aesthetic buttons
    btn_cols = st.columns(7, gap="small")
    for i, (aes_key, meta) in enumerate(AESTHETICS_META.items()):
        with btn_cols[i]:
            if st.button(f"{meta['emoji']} {meta['label']}", key=f"aes_btn_{aes_key}"):
                st.session_state["browse_aes"] = aes_key

    if "browse_aes" not in st.session_state:
        st.session_state["browse_aes"] = "streetwear"

    cur = st.session_state["browse_aes"]
    m   = AESTHETICS_META[cur]

    # Hero
    st.markdown(f"""
<div class="aes-hero">
  <div class="aes-title" style="color:{m['color']}">{m['emoji']} {m['label']}</div>
  <div class="aes-desc">{m['desc']}</div>
</div>
""", unsafe_allow_html=True)

    aes_pool = [p for p in PRODUCTS if p["aesthetic"] == cur]
    st.markdown(f'<div class="sec-label">{len(aes_pool)} Products</div>', unsafe_allow_html=True)

    render_grid(aes_pool, prefix=f"browse_{cur}", ncols=4)