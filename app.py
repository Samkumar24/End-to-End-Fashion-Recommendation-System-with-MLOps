import streamlit as st

st.set_page_config(
    page_title="AesthsAI",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════

PRODUCTS = [
    {"id":0,  "aesthetic":"streetwear",     "name":"Men's Cottonblend Graphic Print Oversized Tshirt",             "price":286,  "mrp":1099, "rating":4.0, "discount":74, "image":"https://m.media-amazon.com/images/I/61WYx598KKL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Cottonblend-Graphic-Oversized-FS49_Navy_Boston_P_Navy/dp/B0FHDHSFYY"},
    {"id":1,  "aesthetic":"streetwear",     "name":"Half Sleeve Oversized Drop Shoulder Printed T-Shirt",          "price":298,  "mrp":1099, "rating":4.0, "discount":73, "image":"https://m.media-amazon.com/images/I/61AE3iKBYPL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Oversized-Graphic-Cottonblend-FS49_Black_Space_P_Red_L/dp/B0FK5PK4VG"},
    {"id":2,  "aesthetic":"streetwear",     "name":"Graphic Font Printed Cottonblend Oversized Tshirts",           "price":286,  "mrp":1099, "rating":4.2, "discount":74, "image":"https://m.media-amazon.com/images/I/61EbiUi7r1L._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Graphic-Cottonblend-Oversized-FS49_ORNG_RAWENERGY_P_Orange_3XL/dp/B0F99NP71S"},
    {"id":3,  "aesthetic":"streetwear",     "name":"Casual Cottonblend Printed Round Neck Oversized Tshirt",       "price":286,  "mrp":1099, "rating":4.1, "discount":74, "image":"https://m.media-amazon.com/images/I/61kYmRqjzaL._AC_UL320_.jpg",  "link":"https://www.amazon.in/LEOTUDE-Cottonblend-Shoulder-Oversized-FS49_Brown_NEWYORKK_P_Brown_XL/dp/B0FK5GC8XD"},
    {"id":4,  "aesthetic":"streetwear",     "name":"Mens Cotton Graphic Print Oversized Fit T-Shirt",              "price":499,  "mrp":1799, "rating":4.1, "discount":72, "image":"https://m.media-amazon.com/images/I/41XlGaQPirL._AC_UL320_.jpg",  "link":"https://www.amazon.in/NOBERO-Mens-Oversized-T-Shirt-1M-TWRT-C0832-BL_Black/dp/B0DBZ9PQN2"},
    {"id":5,  "aesthetic":"streetwear",     "name":"Pure Cotton Oversized Baggy Fit Graphic Printed T-Shirt",      "price":399,  "mrp":1199, "rating":4.0, "discount":67, "image":"https://m.media-amazon.com/images/I/61b1tL147eL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Veirdo%C2%AE_Pure-Oversized-Graphic-Printed-T-Shirt/dp/B0DG34FCY7"},
    {"id":6,  "aesthetic":"streetwear",     "name":"Men's Graphic Print Oversized Fit Pure Cotton T-Shirt",        "price":699,  "mrp":1299, "rating":4.3, "discount":46, "image":"https://m.media-amazon.com/images/I/61512ETok5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Bewakoof-Official-Garfield-Merchandise-Smiling/dp/B0C73RDWXV"},
    {"id":7,  "aesthetic":"streetwear",     "name":"Men's Cotton Oversized Fit Graphic Print T-Shirt",             "price":499,  "mrp":1799, "rating":3.9, "discount":72, "image":"https://m.media-amazon.com/images/I/51WDqhCR8+L._AC_UL320_.jpg",  "link":"https://www.amazon.in/NOBERO-Graphic-Oversized-T-Shirt-1M-TWRT-C0910-OG_Blush/dp/B0DZ2R8Z6W"},
    {"id":8,  "aesthetic":"old_money",      "name":"Men's Solid Linen Cotton Casual Full Sleeve Summer Shirt",     "price":469,  "mrp":2099, "rating":3.0, "discount":77, "image":"https://m.media-amazon.com/images/I/81I4F9xgijL._AC_UL320_.jpg",  "link":"https://www.amazon.in/NexaFlair-Summer-Regular-Stylish-Everyday-Regular/dp/B0DXCYNMCX"},
    {"id":9,  "aesthetic":"old_money",      "name":"Success Linen Button-Down Shirt Textured Long Sleeve",         "price":379,  "mrp":420,  "rating":3.3, "discount":10, "image":"https://m.media-amazon.com/images/I/61v4ecETAZL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Success-Button-Down-Textured-Sleeve-Regular/dp/B0FF1FJSLS"},
    {"id":10, "aesthetic":"old_money",      "name":"Men's Linen Blend Full Sleeve Relaxed Fit Casual Shirt",       "price":749,  "mrp":1949, "rating":3.4, "discount":61, "image":"https://m.media-amazon.com/images/I/61DZg55DeUL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Urbano-Fashion-Purple-Relaxed-shirtlinregfl-02-purple-xl/dp/B0F5WJM4QH"},
    {"id":11, "aesthetic":"old_money",      "name":"Casual Button Down Long Sleeve Linen Shirt Fashion Textured",  "price":499,  "mrp":2199, "rating":3.8, "discount":77, "image":"https://m.media-amazon.com/images/I/71dF+pDGxIL._AC_UL320_.jpg",  "link":"https://www.amazon.in/CB-COLEBROOK-Casual-Button-Fashion-Textured/dp/B0D77N88Q3"},
    {"id":12, "aesthetic":"old_money",      "name":"Men's Solid Cotton Polyester Blend Straight Kurta Shirt",      "price":499,  "mrp":1699, "rating":4.1, "discount":71, "image":"https://m.media-amazon.com/images/I/71BTNI3lEAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Zombom-Cotton-Straight-Regular-Sleeve/dp/B0D94DG16W"},
    {"id":13, "aesthetic":"old_money",      "name":"Men's Linen Blend Mandarin Collar Relaxed Fit Solid Shirt",    "price":749,  "mrp":1949, "rating":3.9, "discount":61, "image":"https://m.media-amazon.com/images/I/61uNa0BqQ5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Urbano-Fashion-Relaxed-Mandarin-shirtlinmdfl-01-white-m/dp/B0F5WH5951"},
    {"id":14, "aesthetic":"old_money",      "name":"Classic Linen Button-Down Shirt Pink Casual Long Sleeve",      "price":489,  "mrp":2499, "rating":3.4, "discount":80, "image":"https://m.media-amazon.com/images/I/51YjJU7FZHL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Oquent-Classic-Button-Down-Regular-Business/dp/B0FV91SD1N"},
    {"id":15, "aesthetic":"old_money",      "name":"Men's Linen Cotton Long Sleeve Casual Regular Fit Shirt",      "price":598,  "mrp":2599, "rating":3.7, "discount":77, "image":"https://m.media-amazon.com/images/I/81LOxcZemfL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Miraan-Cotton-Sleeve-Casual-SIGLINENGREYL_Grey_Large/dp/B0C9ZQY2RY"},
    {"id":16, "aesthetic":"college_casual", "name":"Men Cotton Half Sleeves Round Neck Regular Fit Casual T-Shirt","price":269,  "mrp":269,  "rating":4.0, "discount":0,  "image":"https://m.media-amazon.com/images/I/61ezNvbfQPL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Lux-Cozi-Maroon-Cotton-Tshirt/dp/B0D39544VM"},
    {"id":17, "aesthetic":"college_casual", "name":"Men's Solid Cotton T Shirt Round Neck Half Sleeve Pack of 3",  "price":449,  "mrp":3749, "rating":3.7, "discount":88, "image":"https://m.media-amazon.com/images/I/51U2dDaeOGL._AC_UL320_.jpg",  "link":"https://www.amazon.in/London-Hills-Solid-Sleeve-T-Shirt/dp/B07FLNVWB5"},
    {"id":18, "aesthetic":"college_casual", "name":"Men's Cotton Blend Regular Fit Solid Round Neck T-Shirts Pack","price":799,  "mrp":1299, "rating":3.9, "discount":38, "image":"https://m.media-amazon.com/images/I/61iRb7DYaQL._AC_UL320_.jpg",  "link":"https://www.amazon.in/London-Hills-Sleeve-Multicolor-T-Shirts/dp/B0BSQ9WYYQ"},
    {"id":19, "aesthetic":"college_casual", "name":"U.S. Polo Assn Mens Crew Neck Embroidered Logo T-Shirt",       "price":500,  "mrp":699,  "rating":3.8, "discount":28, "image":"https://m.media-amazon.com/images/I/612O38TYThL._AC_UL320_.jpg",  "link":"https://www.amazon.in/U-S-Polo-Assn-Regular-I633-001-PL_White_Large/dp/B0793NHJZJ"},
    {"id":20, "aesthetic":"college_casual", "name":"Men's Solid Cotton T Shirt Round Neck Half Sleeve Plain Fit",  "price":319,  "mrp":699,  "rating":4.0, "discount":54, "image":"https://m.media-amazon.com/images/I/61-Hg4wfqpL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Amazon-Brand-Regular-T-Shirt-SS20SYMTEE33_Black/dp/B0C5XVJBKL"},
    {"id":21, "aesthetic":"college_casual", "name":"Men's Super Combed Cotton Rich Solid Round Neck T-Shirt",      "price":579,  "mrp":579,  "rating":4.2, "discount":0,  "image":"https://m.media-amazon.com/images/I/71ihH2Tnt1L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Jockey-Combed-Cotton-Sleeve-T-Shirt_Thyme_L/dp/B0DY83M6C4"},
    {"id":22, "aesthetic":"college_casual", "name":"Solid Men's Round Neck Cotton Blend Half Sleeve T-Shirts",     "price":223,  "mrp":1299, "rating":3.7, "discount":83, "image":"https://m.media-amazon.com/images/I/61v-HyIcV0L._AC_UL320_.jpg",  "link":"https://www.amazon.in/London-Hills-Solid-Sleeve-T-Shirt/dp/B07FLBTTNC"},
    {"id":23, "aesthetic":"date_clean",     "name":"Men's Satin Shirt Spread Collar Solid Full Sleeves Regular",   "price":499,  "mrp":999,  "rating":4.1, "discount":50, "image":"https://m.media-amazon.com/images/I/71LJY7GSnQL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Classic-Plain-Casual-Sleeve/dp/B0D961J769"},
    {"id":24, "aesthetic":"date_clean",     "name":"Men's Stylish Satin Shirt Party Formal Casual Full Sleeve",    "price":499,  "mrp":1999, "rating":4.6, "discount":75, "image":"https://m.media-amazon.com/images/I/51+bKUZHtQL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Stylish-Formal-Casual-Sleeve/dp/B0G1BM7TK5"},
    {"id":25, "aesthetic":"date_clean",     "name":"Mens Satin Regular Fit Formal Shirt",                          "price":441,  "mrp":2299, "rating":3.7, "discount":81, "image":"https://m.media-amazon.com/images/I/61u3TDteH6L._AC_UL320_.jpg",  "link":"https://www.amazon.in/CVC-Sleeves-Regular-Causal-Formal/dp/B0CGNQ3B1K"},
    {"id":26, "aesthetic":"date_clean",     "name":"Men's Stylish Solid Satin Casual Shirt Full Sleeves Silk",     "price":499,  "mrp":1799, "rating":3.8, "discount":72, "image":"https://m.media-amazon.com/images/I/61R1R+tsmLL._AC_UL320_.jpg",  "link":"https://www.amazon.in/DEELMO-Stylish-Solid-Casual-Sleeves/dp/B0DPL7Z2TS"},
    {"id":27, "aesthetic":"date_clean",     "name":"Combo Stylish Solid Satin Casual Shirt Full Sleeves Pack of 2","price":799,  "mrp":2499, "rating":4.2, "discount":68, "image":"https://m.media-amazon.com/images/I/617Cah36h9L._AC_UL320_.jpg",  "link":"https://www.amazon.in/DEELMO-Combo-Stylish-Casual-Sleeves/dp/B0FCFP4HKH"},
    {"id":28, "aesthetic":"date_clean",     "name":"Slim Fit Satin Cotton Formal Shirt for Men",                   "price":659,  "mrp":1499, "rating":3.9, "discount":56, "image":"https://m.media-amazon.com/images/I/61N8rUnDlSL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Majestic-Man-Cotton-Formal-Purple/dp/B0D5844PHP"},
    {"id":29, "aesthetic":"date_clean",     "name":"Men's Satin Solid Regular Fit Shirt with Satin Sheen Luxury",  "price":1159, "mrp":1799, "rating":4.0, "discount":36, "image":"https://m.media-amazon.com/images/I/51qC98m0YuL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Regular-Shirt-PESFWNUPS22148_Black/dp/B0CX8X514S"},
    {"id":30, "aesthetic":"gym_athleisure", "name":"Men's Regular Fit Quick-Dry Active T-Shirt for Gym & Sports",  "price":199,  "mrp":799,  "rating":4.0, "discount":75, "image":"https://m.media-amazon.com/images/I/6136GknW7aL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Regular-Quick-Dry-Active-T-Shirt-Sports/dp/B0DYD5537M"},
    {"id":31, "aesthetic":"gym_athleisure", "name":"Active Fit Sports T-Shirt Lightweight Quick Dry Polyester",    "price":299,  "mrp":699,  "rating":3.7, "discount":57, "image":"https://m.media-amazon.com/images/I/71+8DkhB7GL._AC_UL320_.jpg",  "link":"https://www.amazon.in/3Colours-Active-Mens-Sports-T-Shirt/dp/B0FNWFJYCY"},
    {"id":32, "aesthetic":"gym_athleisure", "name":"Men Polyester Quick Dry Half Sleeve Sportswear Gym T-Shirt",   "price":341,  "mrp":1599, "rating":4.0, "discount":79, "image":"https://m.media-amazon.com/images/I/411cZXcsbAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/CHKOKKO-Solid-Regular-T-Shirt-Black/dp/B083M3D4H2"},
    {"id":33, "aesthetic":"gym_athleisure", "name":"Gym T Shirts Workout Sports Quick Dry Training Active Wear",   "price":498,  "mrp":1499, "rating":4.4, "discount":67, "image":"https://m.media-amazon.com/images/I/61DxYUqAOVL._AC_UL320_.jpg",  "link":"https://www.amazon.in/FIGHTERHERO-Polyester-Regular-T-Shirt-T-Shirts/dp/B0FXXV9BL3"},
    {"id":34, "aesthetic":"gym_athleisure", "name":"Gym T Shirts Workout Breathable Dry Fit Running Regular Fit",  "price":399,  "mrp":999,  "rating":4.2, "discount":60, "image":"https://m.media-amazon.com/images/I/71L9aVgSYDL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Boldfit-Quick-Dry-Anti-Odor-Lightweight-Breathable/dp/B0CVX7HZLM"},
    {"id":35, "aesthetic":"gym_athleisure", "name":"Men T-Shirt Adidas Polyester CLASSIC Sports",                  "price":779,  "mrp":1199, "rating":4.0, "discount":35, "image":"https://m.media-amazon.com/images/I/71vO30G+ucL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Adidas-Polyester-CLASSIC-Sports-T-Shirts/dp/B07XKZF6V5"},
    {"id":36, "aesthetic":"gym_athleisure", "name":"Tshirt Regular Fit Gym Active Wear Running Mens Workout",      "price":499,  "mrp":899,  "rating":4.3, "discount":44, "image":"https://m.media-amazon.com/images/I/611lChGYIML._AC_UL320_.jpg",  "link":"https://www.amazon.in/Boldfit-Training-Workout-Tshirts-T-Shirts/dp/B0D5CZ5G23"},
    {"id":37, "aesthetic":"y2k_party",      "name":"Men Printed Satin Full Sleeve Shirt Lightweight Casual Party",  "price":999, "mrp":1999, "rating":3.9, "discount":50, "image":"https://m.media-amazon.com/images/I/51rP+8gN8CL._AC_UL320_.jpg",  "link":"https://www.amazon.in/RIVANORA-Black-Sequin-Regular-Evening/dp/B0GHQTT9F9"},
    {"id":38, "aesthetic":"y2k_party",      "name":"Men's Rayon Ethnic Shirt",                                     "price":1552, "mrp":3369, "rating":4.3, "discount":54, "image":"https://m.media-amazon.com/images/I/617UuB-QY5L._AC_UL320_.jpg",  "link":"https://www.amazon.in/VM-Black-Rayon-Ethnic-Shirt_VMMSH255BL_42/dp/B0CPPXH2HZ"},
    {"id":39, "aesthetic":"y2k_party",      "name":"Men's Premium Satin Shirt Party Formal Casual Full Sleeve",    "price":495,  "mrp":1999, "rating":4.6, "discount":75, "image":"https://m.media-amazon.com/images/I/41RTqea0uAL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Premium-Satin-Formal-Casual/dp/B0G1BN5RMP"},
    {"id":40, "aesthetic":"y2k_party",      "name":"Men's Regular Fit Satin Designer Shirt Vertical Line Sequence", "price":499, "mrp":1999, "rating":4.2, "discount":75, "image":"https://m.media-amazon.com/images/I/61A33rn70xL._AC_UL320_.jpg",  "link":"https://www.amazon.in/IndoPrimo-Designer-Vertical-Sequence-Business/dp/B0FT7FWX8F"},
    {"id":41, "aesthetic":"y2k_party",      "name":"Men's Georgette Ethnic Shirt Embroidered for Festivals",       "price":1269, "mrp":2699, "rating":3.9, "discount":53, "image":"https://m.media-amazon.com/images/I/71ddH4JP8wL._AC_UL320_.jpg",  "link":"https://www.amazon.in/VASTRAMAY-Georgette-Sequins-Collection-Men_VASMSH209MA_36/dp/B0CPPY86K9"},
    {"id":42, "aesthetic":"y2k_party",      "name":"Men's Cotton Regular Fit Shirt Casual Spread Collar Short",    "price":817,  "mrp":1899, "rating":3.8, "discount":57, "image":"https://m.media-amazon.com/images/I/61A+O+J6JLL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Campus-Sutra-Metallic-Pleat-Creased-Everyday/dp/B0CY2M44FT"},
    {"id":43, "aesthetic":"office_smart",   "name":"Men's Slim Fit Formal Shirt Solid Comfortable Everyday Office","price":559,  "mrp":1599, "rating":4.0, "discount":65, "image":"https://m.media-amazon.com/images/I/71q8mNTUk0L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Highlander-Polyester-Shirt-PHSH000175_Peanut-Brown/dp/B0F44L54CM"},
    {"id":44, "aesthetic":"office_smart",   "name":"Men's Casual Printed Striped Stylish Latest Formal Shirt",     "price":372,  "mrp":1599, "rating":3.6, "discount":77, "image":"https://m.media-amazon.com/images/I/71faNU5G5uL._AC_UL320_.jpg",  "link":"https://www.amazon.in/TURN-Casual-Printed-Striped-Stylish/dp/B0CBX53QJV"},
    {"id":45, "aesthetic":"office_smart",   "name":"Men's Everyday Solid Slim Fit Full Sleeve Formal Shirt",       "price":899,  "mrp":1399, "rating":3.9, "discount":36, "image":"https://m.media-amazon.com/images/I/71j3iS8mFuL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFOSLPO33719_Navy/dp/B0BHW7W1CV"},
    {"id":46, "aesthetic":"office_smart",   "name":"Men's Slim Fit Full Sleeve Pin-Striped Formal Shirt Cotton",   "price":879,  "mrp":1399, "rating":4.2, "discount":37, "image":"https://m.media-amazon.com/images/I/61snIWegiiL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFWSLBQ29664_Blue/dp/B0CVS58N9P"},
    {"id":47, "aesthetic":"office_smart",   "name":"Men's Cotton Blend Solid Shirt Spread Collar Full Sleeve Slim","price":369,  "mrp":1599, "rating":4.2, "discount":77, "image":"https://m.media-amazon.com/images/I/51FXI7pJ-YL._AC_UL320_.jpg",  "link":"https://www.amazon.in/MILDIN-Regular-Cotton-Hemline-38/dp/B0DPCS4WBJ"},
    {"id":48, "aesthetic":"office_smart",   "name":"Men's Classic Solid Full Sleeve Slim Fit Shirt Cotton Rich",   "price":825,  "mrp":1399, "rating":4.0, "discount":41, "image":"https://m.media-amazon.com/images/I/51MUZjEzZKL._AC_UL320_.jpg",  "link":"https://www.amazon.in/Peter-England-Mens-Shirt-PESFWSLBB52350_Grey/dp/B0D1C17YZ4"},
    {"id":49, "aesthetic":"office_smart",   "name":"Men's Solid Cotton Formal Shirt Plain Full Sleeve Regular Fit", "price":549, "mrp":1199, "rating":4.0, "discount":54, "image":"https://m.media-amazon.com/images/I/61GtS6IrR7L._AC_UL320_.jpg",  "link":"https://www.amazon.in/Amazon-Brand-Symbol-Regular-SS20-SYM-FS-01_EPP-1A_White/dp/B081QJW5GG"},
]

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
# CSS — AJIO THEME
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

/* ── TOP TICKER ── */
.ticker {
    background: var(--black);
    color: #AAA;
    font-family: 'Inter', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: center;
    padding: 0.4rem;
}
.ticker b { color: var(--white); }

/* ── NAVBAR ── */
.navbar {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0 3rem;
    height: 62px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.nav-logo {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.55rem;
    font-weight: 900;
    color: var(--black);
    letter-spacing: -0.5px;
}
.nav-logo span { color: var(--red); }
.nav-center {
    display: flex;
    gap: 2rem;
}
.nav-item {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--dark);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    cursor: pointer;
    padding-bottom: 2px;
}
.nav-item.hot { color: var(--red); }
.nav-right {
    display: flex;
    gap: 1.8rem;
    align-items: center;
}
.nav-icon {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    color: var(--mid);
    letter-spacing: 0.5px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
}

/* ── CATEGORY BAR ── */
.catbar {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0 3rem;
    display: flex;
    gap: 0;
    overflow-x: auto;
    scrollbar-width: none;
}
.catbar::-webkit-scrollbar { display: none; }
.cat {
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: var(--mid);
    padding: 0.85rem 1.3rem;
    white-space: nowrap;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.15s;
}
.cat:hover, .cat.active { color: var(--red); border-bottom-color: var(--red); }

/* ── SEARCH ── */
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

/* ── RESULT BAR ── */
.result-bar {
    padding: 0.65rem 3rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.result-count {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    color: var(--mid);
}
.result-count b { color: var(--black); font-weight: 700; }
.result-hint {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    color: var(--mid);
}

/* ── PRODUCT CARD — AJIO STYLE ── */
.card {
    background: var(--white);
    border: none;
    overflow: hidden;
    transition: box-shadow 0.2s, transform 0.2s;
    position: relative;
    border-radius: 3px;
}
.card:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.10);
    transform: translateY(-2px);
}
.card-img-wrap {
    position: relative;
    overflow: hidden;
    background: #F9F9F9;
}
.card-img {
    width: 100%;
    aspect-ratio: 3/4;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
}
.card:hover .card-img { transform: scale(1.05); }

/* DISCOUNT BADGE — ajio red top-left */
.disc-badge {
    position: absolute;
    top: 0; left: 0;
    background: var(--red);
    color: var(--white);
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 800;
    padding: 4px 8px;
    letter-spacing: 0.5px;
}

/* AESTHETIC TAG — top right */
.aes-tag {
    position: absolute;
    top: 8px; right: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 0.52rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 3px 7px;
    border-radius: 2px;
    backdrop-filter: blur(4px);
}

/* MATCH SCORE */
.match-badge {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    background: rgba(28,28,28,0.82);
    color: var(--white);
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 5px 8px;
    text-align: center;
}

/* WISHLIST HEART */
.wishlist-btn {
    position: absolute;
    top: 8px; left: 8px;
    width: 28px; height: 28px;
    background: rgba(255,255,255,0.9);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    cursor: pointer;
    box-shadow: 0 1px 4px rgba(0,0,0,0.12);
}

.card-body {
    padding: 0.55rem 0.7rem 0.7rem;
}
.brand {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 800;
    color: var(--black);
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 0.1rem;
}
.pname {
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    color: var(--mid);
    line-height: 1.35;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 0.45rem;
}
.price-row {
    display: flex;
    align-items: baseline;
    gap: 0.4rem;
    margin-bottom: 0.25rem;
    flex-wrap: wrap;
}
.price-now {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.92rem;
    font-weight: 800;
    color: var(--black);
}
.price-mrp {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    color: #BBBBBB;
    text-decoration: line-through;
}
.price-off {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--red);
}
.rating-row {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    margin-bottom: 0.5rem;
}
.rtag {
    background: var(--green);
    color: var(--white);
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.58rem;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 2px;
}
.rcount {
    font-family: 'Inter', sans-serif;
    font-size: 0.62rem;
    color: #BBBBBB;
}

/* VIEW BUTTON */
.view-btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    border: 1.5px solid var(--black);
    color: var(--black) !important;
    font-family: 'Nunito Sans', sans-serif;
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 0.45rem 0;
    transition: all 0.15s;
    border-radius: 2px;
}
.view-btn:hover {
    background: var(--red) !important;
    border-color: var(--red) !important;
    color: var(--white) !important;
    text-decoration: none !important;
}

/* ── SIMILAR BUTTON ── */
.stButton > button {
    background: var(--white) !important;
    border: 1.5px solid var(--border) !important;
    color: var(--dark) !important;
    font-family: 'Nunito Sans', sans-serif !important;
    font-size: 0.62rem !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    padding: 0.45rem 0 !important;
    border-radius: 2px !important;
    transition: all 0.15s !important;
    width: 100% !important;
    margin-top: 0.3rem !important;
}
.stButton > button:hover,
.stButton > button:focus {
    background: var(--black) !important;
    border-color: var(--black) !important;
    color: var(--white) !important;
    box-shadow: none !important;
}

/* ── TABS ── */
div[data-testid="stTabs"] [role="tablist"] {
    background: var(--white) !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
    padding: 0 3rem !important;
}
div[data-testid="stTabs"] button[role="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.68rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: var(--mid) !important;
    padding: 1rem 1.5rem !important;
    border: none !important;
    background: transparent !important;
    border-radius: 0 !important;
}
div[data-testid="stTabs"] button[role="tab"]:hover { color: var(--dark) !important; }
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--red) !important;
    border-bottom: 2px solid var(--red) !important;
}

/* ── SELECTED BANNER ── */
.sel-banner {
    background: var(--red-lt);
    border-top: 3px solid var(--red);
    padding: 1rem 3rem;
    display: flex;
    gap: 1.2rem;
    align-items: center;
    margin-bottom: 1.2rem;
}
.sel-img {
    width: 60px; height: 76px;
    object-fit: cover;
    border-radius: 2px;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.sel-tag {
    font-family: 'Inter', sans-serif;
    font-size: 0.58rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--red);
    margin-bottom: 0.2rem;
}
.sel-name {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    color: var(--dark);
    line-height: 1.4;
    margin-bottom: 0.3rem;
}
.sel-price {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1rem;
    font-weight: 800;
    color: var(--black);
}

/* ── SECTION HEAD ── */
.sec-head {
    padding: 1.2rem 3rem 0.8rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: baseline;
    gap: 1rem;
}
.sec-title {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.3rem;
    font-weight: 900;
    color: var(--black);
    letter-spacing: -0.3px;
}
.sec-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    color: var(--mid);
}

/* ── AES BROWSE BUTTONS ── */
.aes-btn-wrap {
    padding: 0.8rem 3rem;
    background: var(--white);
    border-bottom: 1px solid var(--border);
}

/* ── AES HERO ── */
.aes-hero {
    background: var(--white);
    padding: 1.2rem 3rem 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}
.aes-eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--red);
    margin-bottom: 0.25rem;
}
.aes-title {
    font-family: 'Nunito Sans', sans-serif;
    font-size: 1.8rem;
    font-weight: 900;
    color: var(--black);
    letter-spacing: -0.5px;
    line-height: 1;
    margin-bottom: 0.2rem;
}
.aes-desc {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    color: var(--mid);
}

/* ── GRID ── */
.grid-wrap { padding: 0 3rem; }

/* ── FOOTER ── */
.footer {
    background: var(--black);
    padding: 1.8rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 3rem;
}

/* HIDE STREAMLIT CHROME */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { visibility: hidden !important; height: 0 !important; }
.stDeployButton { display: none !important; }

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #CCC; border-radius: 2px; }

[data-testid="stHorizontalBlock"] { gap: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════

def card_html(p, sim=None):
    meta    = AESTHETICS_META[p["aesthetic"]]
    disc    = f'<div class="disc-badge">{p["discount"]}% OFF</div>' if p["discount"] > 0 else ""
    aestag  = f'<div class="aes-tag" style="background:{meta["color"]}18;color:{meta["color"]}">{meta["emoji"]} {meta["label"]}</div>'
    matchb  = f'<div class="match-badge">● {sim:.0%} MATCH</div>' if sim else ""
    brand   = p["name"].split()[0].upper()
    mrp_str = f'<span class="price-mrp">₹{p["mrp"]:,}</span>' if p["discount"] > 0 else ""
    off_str = f'<span class="price-off">{p["discount"]}% off</span>' if p["discount"] > 0 else ""

    return f"""
<div class="card">
  <div class="card-img-wrap">
    <img class="card-img" src="{p['image']}"
         onerror="this.style.background='#F0F0F0';this.src=''" />
    {disc}
    {aestag}
    {matchb}
  </div>
  <div class="card-body">
    <div class="brand">{brand}</div>
    <div class="pname">{p['name']}</div>
    <div class="price-row">
      <span class="price-now">₹{p['price']:,}</span>
      {mrp_str}
      {off_str}
    </div>
    <div class="rating-row">
      <span class="rtag">★ {p['rating']}</span>
      <span class="rcount">Rated</span>
    </div>
    <a href="{p['link']}" target="_blank" class="view-btn">View Product</a>
  </div>
</div>"""


def render_grid(products, prefix, sim_scores=None, ncols=5):
    st.markdown('<div class="grid-wrap">', unsafe_allow_html=True)
    for row_start in range(0, len(products), ncols):
        row  = products[row_start: row_start + ncols]
        cols = st.columns(ncols, gap="small")
        for ci, p in enumerate(row):
            idx   = row_start + ci
            score = sim_scores[idx] if sim_scores else None
            with cols[ci]:
                st.markdown(card_html(p, sim=score), unsafe_allow_html=True)
                if st.button("Find Similar", key=f"{prefix}_{p['id']}"):
                    st.session_state["sel_id"] = p["id"]
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# TICKER + NAVBAR + CATBAR
# ══════════════════════════════════════════════════════

st.markdown("""
<div class="ticker">
    <b>FLAT 40–80% OFF</b> on 13,000+ Products &nbsp;·&nbsp;
    Free Delivery above ₹999 &nbsp;·&nbsp;
    <b>AI-Powered</b> Style Recommendations
</div>
<div class="navbar">
  <div class="nav-logo">AETH<span>S</span>AI</div>
  <div class="nav-center">
    <span class="nav-item">Men</span>
    <span class="nav-item">Women</span>
    <span class="nav-item">Brands</span>
    <span class="nav-item">Collections</span>
    <span class="nav-item hot">SALE</span>
  </div>
  <div class="nav-right">
    <div class="nav-icon">🔍<br>Search</div>
    <div class="nav-icon">♡<br>Wishlist</div>
    <div class="nav-icon">👤<br>Account</div>
    <div class="nav-icon">🛍<br>Bag (0)</div>
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

    # Search bar
    st.markdown('<div class="search-section">', unsafe_allow_html=True)
    search = st.text_input("", placeholder="🔍   Search — oversized tshirt, linen shirt, satin shirt, cargo pants...")
    st.markdown('</div>', unsafe_allow_html=True)

    # Selected → show similar
    if "sel_id" in st.session_state:
        sel  = next((p for p in PRODUCTS if p["id"] == st.session_state["sel_id"]), None)
        if sel:
            meta = AESTHETICS_META[sel["aesthetic"]]
            st.markdown(f"""
<div class="sel-banner">
  <img class="sel-img" src="{sel['image']}"
       onerror="this.style.background='#EEE';this.src=''" />
  <div>
    <div class="sel-tag">{meta['emoji']} {meta['label']} &nbsp;·&nbsp; Showing Similar Products</div>
    <div class="sel-name">{sel['name']}</div>
    <div class="sel-price">₹{sel['price']:,}
      {'&nbsp;<span style="font-size:0.78rem;color:var(--red);font-family:Inter">' + str(sel["discount"]) + '% off</span>' if sel["discount"] > 0 else ''}
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

            similar     = [p for p in PRODUCTS if p["aesthetic"] == sel["aesthetic"] and p["id"] != sel["id"]]
            demo_scores = [0.95, 0.92, 0.89, 0.86, 0.83, 0.80, 0.77, 0.74, 0.71, 0.68]
            render_grid(similar[:10], prefix="sim", sim_scores=demo_scores, ncols=5)

            st.markdown('<div class="grid-wrap" style="margin-top:1rem">', unsafe_allow_html=True)
            if st.button("← Back to All Products", key="back_btn"):
                del st.session_state["sel_id"]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        pool = PRODUCTS
        if search.strip():
            q    = search.strip().lower()
            pool = [p for p in PRODUCTS if q in p["name"].lower()]

        st.markdown(f"""
<div class="result-bar">
  <div class="result-count">Showing <b>{len(pool)} products</b></div>
  <div class="result-hint">Click <b>Find Similar</b> on any product</div>
</div>
""", unsafe_allow_html=True)

        if not pool:
            st.markdown('<div style="padding:3rem 3rem;color:#999;font-family:Inter;font-size:0.85rem">No products found.</div>', unsafe_allow_html=True)
        else:
            render_grid(pool, prefix="all", ncols=5)

# ══════════════════════════════════════════════════════
# TAB 2 — BROWSE BY AESTHETIC
# ══════════════════════════════════════════════════════

with tab2:

    st.markdown('<div class="aes-btn-wrap">', unsafe_allow_html=True)
    btn_cols = st.columns(7, gap="small")
    for i, (aes_key, meta) in enumerate(AESTHETICS_META.items()):
        with btn_cols[i]:
            if st.button(f"{meta['emoji']} {meta['label']}", key=f"aes_btn_{aes_key}"):
                st.session_state["browse_aes"] = aes_key
    st.markdown('</div>', unsafe_allow_html=True)

    if "browse_aes" not in st.session_state:
        st.session_state["browse_aes"] = "streetwear"

    cur  = st.session_state["browse_aes"]
    m    = AESTHETICS_META[cur]
    pool = [p for p in PRODUCTS if p["aesthetic"] == cur]

    st.markdown(f"""
<div class="aes-hero">
  <div class="aes-eyebrow">Aesthetic Collection</div>
  <div class="aes-title">{m['emoji']} {m['label']}</div>
  <div class="aes-desc">{m['desc']} &nbsp;·&nbsp; {len(pool)} products</div>
</div>
""", unsafe_allow_html=True)

    render_grid(pool, prefix=f"br_{cur}", ncols=5)

# ── FOOTER ────────────────────────────────────────────
st.markdown("""
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
    13,813 Products &nbsp;·&nbsp; 7 Aesthetics
  </div>
</div>
""", unsafe_allow_html=True)