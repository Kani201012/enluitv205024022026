import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture removes the hacker's primary entry point.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Titan Architect | Layout Master", layout="wide", page_icon="⚡", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { background: linear-gradient(90deg, #0f172a, #ef4444); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900 !important; font-size: 1.8rem !important; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5rem; background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; font-weight: 800; border: none; box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px; transition: transform 0.2s; }
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NEW LAYOUT CONTROLS) ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v50.5 | Layout Master Edition")
    st.divider()

    with st.expander("🎨 Color & Typography", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate (Light)", "Midnight SaaS (Dark)"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#3b82f6")  
        h_font = st.selectbox("Headings Font", ["Space Grotesk", "Montserrat", "Playfair Display", "Clash Display"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Satoshi"])

    # 🔥 NEW: COMBINATORIAL LAYOUT ENGINE
    with st.expander("📐 Layout & Structure Engine", expanded=True):
        ui_style = st.selectbox("UI Component Style", ["Modern Clean", "Neo-Brutalism", "Glassmorphism", "Soft Neumorphism"], help="Changes how cards and buttons look.")
        nav_style = st.selectbox("Navigation Layout", ["Standard Top", "Floating Pill", "Centered Logo"])
        hero_layout = st.selectbox("Hero Layout", ["Classic Centered", "Modern Split (Left/Right)", "Cinematic (Bottom Left)"])
        feat_layout = st.selectbox("Feature Grid Layout", ["3-Column Grid", "2-Column Grid", "Stacked List"])
        btn_style = st.selectbox("Button Shape", ["Rounded (Default)", "Sharp (Square)", "Pill (Full Round)"])
        border_rad = "8px" if btn_style == "Rounded (Default)" else ("0px" if btn_style == "Sharp (Square)" else "50px")

    with st.expander("🚀 2050 Feature Flags"):
        enable_ar = st.checkbox("Spatial Web (AR 3D Models)", value=True)
        enable_voice = st.checkbox("Voice Command Search", value=True)
        enable_context = st.checkbox("Context-Aware UI", value=True)
        enable_ab = st.checkbox("Edge A/B Testing", value=True)

    with st.expander("🧩 Section Manager"):
        show_hero = st.checkbox("Hero Section", value=True)
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_pricing = st.checkbox("Pricing Table", value=True)
        show_inventory = st.checkbox("Store/Inventory", value=True)
        show_blog = st.checkbox("Blog Engine", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_booking = st.checkbox("Booking Engine", value=True)

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ StopWebRent Workspace")

tabs = st.tabs(["1. Identity", "2. Content", "3. Dynamic Feeds", "4. Marketing", "5. Legal & Web3"])

with tabs[0]:
    c1, c2 = st.columns(2)
    biz_name = c1.text_input("Business Name", "StopWebRent.com")
    biz_tagline = c1.text_input("Tagline", "Own Your Digital Empire.")
    logo_url = c1.text_input("Logo URL (PNG/SVG)")
    prod_url = c2.text_input("Website URL", "https://www.stopwebrent.com")
    wa_num = c2.text_input("WhatsApp Number (No +)", "966572562151")
    seo_d = c2.text_input("Meta Description", "Stop paying monthly fees for web hosting.")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "The Last Website You Will Ever Buy.")
    hero_sub = st.text_input("Hero Subtext", "We’ve eliminated hosting fees, database vulnerabilities, and loading screens.")
    hc1, hc2 = st.columns(2)
    hero_img_1 = hc1.text_input("Hero Image 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Hero Image 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    feat_data_input = st.text_area("Features (icon|Title|Desc)", key="feat_data", height=150)
    about_h_in = st.text_input("About Title", "The Great Digital Liberation")
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("About Text", "Stop being a tenant on your own domain...", height=100)

with tabs[2]:
    sheet_url = st.text_input("Store CSV URL")
    blog_sheet_url = st.text_input("Blog CSV URL")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    lang_sheet = st.text_input("Multi-Lang CSV URL (Optional)")

with tabs[3]:
    top_bar_enabled = st.checkbox("Enable Top Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale!")
    col_p1, col_p2 = st.columns(2)
    titan_price = col_p1.text_input("Setup Price", "$499")
    wix_name = col_p2.text_input("Competitor", "Wix / Shopify")
    save_val = st.text_input("5-Year Savings", "$1,750")

with tabs[4]:
    priv_txt = st.text_area("Privacy", "We collect minimum data.")
    term_txt = st.text_area("Terms", "You own the code.")
    pinata_jwt = st.text_input("Pinata API JWT (For Web3/IPFS)", type="password")


# --- 5. COMPILER ENGINE (LAYOUT MASTER EDITION) ---

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = processed_text.split('\n')
    return "".join([f"<p style='margin-bottom:1rem; opacity:0.9;'>{line.strip()}</p>" for line in lines if line.strip()])

def get_theme_css():
    bg_color, text_color, card_bg, glass_nav = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.95)"
    if "Midnight" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.9)"
    
    # DYNAMIC UI STYLING ENGINE
    card_css = ""
    btn_extra_css = ""
    nav_extra_css = ""

    if ui_style == "Neo-Brutalism":
        card_css = f"border: 3px solid {text_color}; box-shadow: 6px 6px 0px {text_color}; border-radius: 0px;"
        btn_extra_css = f"border: 3px solid {text_color}; box-shadow: 4px 4px 0px {text_color}; border-radius: 0px;"
    elif ui_style == "Glassmorphism":
        card_css = "background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.2);"
        if "Midnight" not in theme_mode: card_css = "background: rgba(0, 0, 0, 0.03); backdrop-filter: blur(16px); border: 1px solid rgba(0, 0, 0, 0.05);"
    elif ui_style == "Soft Neumorphism":
        if "Midnight" in theme_mode: card_css = "background: #0f172a; box-shadow:  10px 10px 20px #060911, -10px -10px 20px #182543; border: none;"
        else: card_css = "background: #ffffff; box-shadow:  10px 10px 20px #d9d9d9, -10px -10px 20px #ffffff; border: none;"
    else: # Modern Clean
        card_css = f"background: {card_bg}; border: 1px solid rgba(128,128,128,0.1); box-shadow: 0 4px 6px rgba(0,0,0,0.05);"

    # NAVBAR STYLING ENGINE
    if nav_style == "Floating Pill":
        nav_extra_css = "top: 20px !important; width: 90% !important; left: 5%; border-radius: 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"
    elif nav_style == "Centered Logo":
        nav_extra_css = ".nav-flex { flex-direction: column; justify-content: center; gap: 10px; height: auto; padding: 10px 0; }"

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {text_color}; --card: {card_bg}; --radius: {border_rad}; --nav: {glass_nav}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }} html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); line-height: 1.6; overflow-x: hidden; transition: background 0.3s, color 0.3s; }}
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: #1e293b; --nav: rgba(15, 23, 42, 0.95); }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--p); line-height: 1.2; margin-bottom: 1rem; }}
    strong {{ color: var(--p); font-weight: 800; }} h1 {{ font-size: clamp(2.5rem, 5vw, 4.5rem); }} h2 {{ font-size: clamp(2rem, 4vw, 3rem); }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 20px; }}
    
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-radius: var(--radius); font-weight: 700; text-decoration: none; transition: 0.3s; cursor: pointer; text-align: center; {btn_extra_css} }}
    .btn-primary {{ background: var(--p); color: white !important; }}
    .btn-accent {{ background: var(--s); color: white !important; }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.15); }}
    
    header {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(100,100,100,0.1); padding: 0.5rem 0; transition: all 0.3s; {nav_extra_css} }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; min-height: 60px; }}
    .nav-links {{ display: flex; align-items: center; gap: 2rem; }}
    .nav-links a {{ text-decoration: none; font-weight: 600; color: var(--txt); transition:0.2s; }}
    .nav-links a:hover {{ color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; position: absolute; right: 20px; top: 20px; }}
    
    main section {{ padding: clamp(4rem, 8vw, 6rem) 0; }}
    .section-head {{ text-align: center; margin-bottom: clamp(2rem, 4vw, 3rem); }}
    
    /* DYNAMIC FEATURE GRIDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .grid-2 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 3rem; }}
    .grid-list {{ display: flex; flex-direction: column; gap: 1.5rem; max-width: 800px; margin: 0 auto; }}
    
    .about-grid, .detail-view {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    
    /* DYNAMIC CARD STYLING */
    .card {{ {card_css} padding: 2rem; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s; border-radius: var(--radius); }}
    .card:hover {{ transform: translateY(-5px); { 'box-shadow: 10px 10px 0px ' + text_color if ui_style == 'Neo-Brutalism' else 'box-shadow: 0 20px 40px -10px rgba(0,0,0,0.15); border-color: var(--p);' } }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: var(--radius); margin-bottom: 1.5rem; background: #f1f5f9; }}
    
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(100,100,100,0.1); background: var(--card); }}

    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.8) !important; text-decoration: none; display: block; margin-bottom: 0.5rem; transition: 0.3s; }}
    footer a:hover {{ color: #ffffff !important; text-decoration: underline; }}
    
    /* 2050 MODALS & UTILS */
    .reveal {{ opacity: 0; transform: translateY(30px); transition: 0.8s ease-out; }} .reveal.active {{ opacity: 1; transform: translateY(0); }}
    #cart-float {{ position: fixed; bottom: 30px; right: 30px; background: var(--p); color: white; padding: 15px 20px; border-radius: 50px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); cursor: pointer; z-index: 998; font-weight: bold; }}
    #cart-modal, #lang-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 500px; padding: 2rem; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); z-index: 1001; }}
    #cart-overlay, #lang-overlay {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 1000; backdrop-filter: blur(5px); }}
    .local-vault {{ background: rgba(128,128,128,0.05); padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid rgba(128,128,128,0.1); }}
    .local-vault input {{ width: 100%; padding: 0.8rem; margin-top: 0.5rem; border-radius: 6px; border: 1px solid #ccc; background: var(--bg); color: var(--txt); }}
    
    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .detail-view {{ grid-template-columns: 1fr !important; }}
    }}
    """

def gen_hero():
    bg_media = f"""<div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div><div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div><script defer>let slides = document.querySelectorAll('.carousel-slide'); let currentSlide = 0; setInterval(() => {{ slides[currentSlide].classList.remove('active'); currentSlide = (currentSlide + 1) % slides.length; slides[currentSlide].classList.add('active'); }}, 4000);</script>"""
    
    # LAYOUT ENGINE: HERO
    if hero_layout == "Modern Split (Left/Right)":
        return f"""
        <section style="min-height: 90vh; display: flex; align-items: center; padding-top:100px;">
            <div class="container about-grid">
                <div class="reveal">
                    <h1 style="font-size:clamp(3rem, 5vw, 4.5rem); line-height:1.1;">{hero_h}</h1>
                    <p style="font-size:1.2rem; opacity:0.8; margin-bottom:2rem;">{hero_sub}</p>
                    <div style="display:flex; gap:1rem;"><a href="#inventory" class="btn btn-accent">Explore Now</a></div>
                </div>
                <div class="reveal" style="position:relative; height:500px; border-radius:var(--radius); overflow:hidden;">{bg_media}</div>
            </div>
        </section>
        """
    elif hero_layout == "Cinematic (Bottom Left)":
        return f"""
        <section style="position:relative; min-height:100vh; display:flex; align-items:flex-end; padding-bottom:5rem; color:white;">
            <div style="position:absolute; inset:0; z-index:0;">{bg_media}</div>
            <div style="position:absolute; inset:0; background:linear-gradient(to top, rgba(0,0,0,0.9), transparent); z-index:1;"></div>
            <div class="container reveal" style="position:relative; z-index:2; max-width:800px; margin-left:0;">
                <h1 style="color:white!important; font-size:clamp(3.5rem, 6vw, 5rem); text-shadow:none;">{hero_h}</h1>
                <p style="color:rgba(255,255,255,0.8)!important; font-size:1.5rem; margin-bottom:2rem;">{hero_sub}</p>
                <a href="#inventory" class="btn btn-primary">Start Exploring</a>
            </div>
        </section>
        """
    else: # Classic Centered
        return f"""
        <section style="position:relative; min-height:90vh; display:flex; align-items:center; text-align:center; color:white;">
            <div style="position:absolute; inset:0; z-index:0;">{bg_media}</div>
            <div style="position:absolute; inset:0; background:rgba(0,0,0,0.6); z-index:1;"></div>
            <div class="container reveal" style="position:relative; z-index:2;">
                <h1 style="color:white!important;">{hero_h}</h1>
                <p style="color:rgba(255,255,255,0.9)!important; font-size:1.2rem; max-width:700px; margin:0 auto 2rem;">{hero_sub}</p>
                <div style="display:flex; gap:1rem; justify-content:center;"><a href="#inventory" class="btn btn-accent">Explore Now</a></div>
            </div>
        </section>
        """

def gen_features():
    if not show_features: return ""
    # LAYOUT ENGINE: FEATURES
    grid_class = "grid-3" if feat_layout == "3-Column Grid" else ("grid-2" if feat_layout == "2-Column Grid" else "grid-list")
    
    cards = "".join([f'<div class="card reveal"><div style="color:var(--s); font-size:2rem; margin-bottom:1rem;">{p[0][:2]}</div><h3>{p[1].strip()}</h3><div>{format_text(p[2].strip())}</div></div>' for l in feat_data_input.split('\n') if (p:=l.split('|')) and len(p)>=3])
    return f'<section id="features"><div class="container"><div class="section-head reveal"><h2>Value Pillars</h2></div><div class="{grid_class}">{cards}</div></div></section>'

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <script defer>
    function parseCSVLine(str) {{ const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) {{ const c = str[i]; if (c === '"') {{ if (inQuote && str[i+1] === '"') {{ cur += '"'; i++; }} else {{ inQuote = !inQuote; }} }} else if (c === ',' && !inQuote) {{ res.push(cur.trim()); cur = ''; }} else {{ cur += c; }} }} res.push(cur.trim()); return res; }}
    {demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('inv-grid'); if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                if(!lines[i].trim()) continue;
                const c = parseCSVLine(lines[i]);
                let mainImg = c[3] ? c[3].split('|')[0] : '{custom_feat}';
                if(c.length > 1) {{
                    box.innerHTML += `<div class="card reveal"><img src="${{mainImg}}" class="prod-img" loading="lazy"><h3>${{c[0]}}</h3><p style="color:var(--s); font-weight:bold; font-size:1.2rem; margin-bottom:1rem;">${{c[1]}}</p><div style="margin-top:auto; display:flex; gap:10px;"><button onclick="addToCart('${{c[0]}}', '${{c[1]}}')" class="btn btn-primary" style="flex:1;">Add</button></div></div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_cart_system():
    return f"""
    <div id="cart-float" onclick="toggleCart()">🛒 <span id="cart-count">0</span></div>
    <div id="cart-overlay" onclick="toggleCart()"></div>
    <div id="cart-modal">
        <h3>Your Cart</h3><div id="cart-items" style="max-height:200px; overflow-y:auto; margin:1rem 0;"></div>
        <div style="font-weight:bold; font-size:1.2rem; margin-bottom:1rem; text-align:right;">Total: <span id="cart-total">0.00</span></div>
        <div class="local-vault"><h4 style="font-size:0.9rem;">🔒 Fast Checkout Vault (Saved Locally)</h4><input type="text" id="vault-name" placeholder="Full Name"><input type="text" id="vault-address" placeholder="Delivery Address"></div>
        <button onclick="checkoutWhatsApp()" class="btn btn-accent" style="width:100%; margin-top:1rem;">1-Click Checkout via WhatsApp</button>
    </div>
    <script defer>
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    document.getElementById('vault-name').value = localStorage.getItem('t_name') || ''; document.getElementById('vault-address').value = localStorage.getItem('t_addr') || '';
    function renderCart() {{
        const box = document.getElementById('cart-items'); if(!box) return; box.innerHTML = ''; let total = 0;
        cart.forEach((item, i) => {{ total += parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0; box.innerHTML += `<div class="cart-item"><span>${{item.name}}</span><span>${{item.price}} <span onclick="cart.splice(${{i}},1);renderCart()" style="color:red;cursor:pointer;">x</span></span></div>`; }});
        document.getElementById('cart-count').innerText = cart.length; document.getElementById('cart-total').innerText = total.toFixed(2);
        document.getElementById('cart-float').style.display = cart.length > 0 ? 'flex' : 'none';
        localStorage.setItem('titanCart', JSON.stringify(cart));
    }}
    function addToCart(name, price) {{ cart.push({{name, price}}); renderCart(); alert(name + " added!"); }}
    function toggleCart() {{ const m = document.getElementById('cart-modal'); m.style.display = m.style.display === 'block' ? 'none' : 'block'; document.getElementById('cart-overlay').style.display = m.style.display; }}
    function checkoutWhatsApp() {{
        const n = document.getElementById('vault-name').value; const a = document.getElementById('vault-address').value;
        localStorage.setItem('t_name', n); localStorage.setItem('t_addr', a);
        let msg = "New Order:%0A"; let total = 0; cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; total += parseFloat(i.price.replace(/[^0-9.]/g,'')) || 0; }});
        msg += `%0ATotal: ${{total.toFixed(2)}}%0A`; if(n) msg += `%0ADeliver to: ${{n}}, ${{a}}`;
        {f"msg += '%0A(Variant: ' + localStorage.getItem('titan_ab') + ')';" if enable_ab else ""}
        window.open(`https://wa.me/{wa_num}?text=${{msg}}`, '_blank'); cart = []; renderCart(); toggleCart();
    }}
    window.addEventListener('load', renderCart);
    </script>
    """

def gen_2050_scripts():
    context_js = "if(new Date().getHours() >= 19 || new Date().getHours() <= 6) document.body.classList.add('dark-mode');" if enable_context else ""
    ab_js = "let variant = localStorage.getItem('titan_ab') || (Math.random() > 0.5 ? 'A' : 'B'); localStorage.setItem('titan_ab', variant); if(variant === 'B') document.documentElement.style.setProperty('--s', '#10b981');" if enable_ab else ""
    return f"<script defer>{context_js} {ab_js}</script>"

def build_page(title, content):
    logo_display = f'<img src="{logo_url}" height="40" alt="{biz_name}">' if logo_url else f'<span style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</span>'
    nav_html = f"""
    {f'<div id="top-bar">{top_bar_text}</div>' if top_bar_enabled else ''}
    <header><div class="container nav-flex"><a href="index.html">{logo_display}</a><div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div><nav class="nav-links"><a href="index.html">Home</a><a href="index.html#features">Features</a><a href="index.html#inventory">Store</a><a href="tel:{biz_phone}" class="btn-accent" style="padding:0.5rem 1.5rem; border-radius:50px; color:white!important;">Call</a></nav></div></header>
    """
    footer_html = f"""<footer><div class="container"><div class="footer-grid"><div><h3>{biz_name}</h3><p>{biz_addr}</p></div><div><h4>Legal</h4><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></div></div><div style="margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(255,255,255,0.1); text-align:center; opacity:0.6;">&copy; {datetime.datetime.now().year} {biz_name}. Built with Titan Engine.</div></div></footer>"""
    
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title><link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;600&display=swap" rel="stylesheet"><style>{get_theme_css()}</style>{gen_2050_scripts()}</head><body><main>{nav_html}{content}{footer_html}{gen_cart_system()}<script defer>window.addEventListener('scroll', () => {{ document.querySelectorAll('.reveal').forEach(r => {{ if (r.getBoundingClientRect().top < window.innerHeight - 100) r.classList.add('active'); }}); }}); window.dispatchEvent(new Event('scroll'));</script></main></body></html>"""

# --- 6. PAGE ASSEMBLY ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_features: home_content += gen_features()
if show_inventory: home_content += f'<section id="inventory" style="background:var(--surface)"><div class="container"><div class="section-head reveal"><h2>Our Store</h2></div><div id="inv-grid" class="grid-3">Loading Edge Data...</div></div></section>{gen_inventory_js(is_demo=False)}'
if show_gallery: home_content += f'<section id="about"><div class="container about-grid"><div class="reveal"><h2>{about_h_in}</h2><div>{format_text(about_short_in)}</div></div><img src="{about_img}" class="reveal prod-img" style="height:400px;"></div></section>'
if show_pricing: home_content += f'<section id="pricing"><div class="container section-head reveal"><h2>Pricing</h2><table class="pricing-table"><tr><th>Titan Engine</th><th>{wix_name}</th></tr><tr><td>{titan_price} Setup<br><b>$0/mo</b></td><td>{wix_mo}</td></tr></table></div></section>'

# --- 7. DEPLOYMENT ---
st.divider()
st.subheader("🚀 Space Control: Build & Deploy")

c1, c2 = st.columns([3, 1])
with c1:
    st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)

with c2:
    st.success("Layout Engine Initialized.")
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", build_page("Home", home_content))
        zf.writestr("privacy.html", build_page("Privacy", f"<section style='padding-top:120px'><div class='container'><h1>Privacy</h1><p>{priv_txt}</p></div></section>"))
        zf.writestr("terms.html", build_page("Terms", f"<section style='padding-top:120px'><div class='container'><h1>Terms</h1><p>{term_txt}</p></div></section>"))

    if pinata_jwt:
        if st.button("🌌 PUSH TO Web3 (IPFS)", type="primary"):
            with st.spinner("Uploading to IPFS Blockchain..."):
                try:
                    res = requests.post("https://api.pinata.cloud/pinning/pinFileToIPFS", headers={"Authorization": f"Bearer {pinata_jwt}"}, files={"file": ("site.zip", z_b.getvalue())})
                    if res.status_code == 200: st.success(f"Live forever! Gateway: ipfs.io/ipfs/{res.json()['IpfsHash']}")
                except Exception as e: st.error(f"Error: {e}")
    else:
        st.download_button("📥 DOWNLOAD SITE PACKAGE", z_b.getvalue(), f"{biz_name.replace(' ','_')}_LayoutMaster.zip", "application/zip", type="primary")
