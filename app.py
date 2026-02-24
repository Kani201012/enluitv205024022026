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

# Default Values tailored for StopWebRent
init_state('hero_h', "Own Your Digital Empire.")
init_state('hero_sub', "Wix and Shopify are digital landlords. We build 0.1s hyper-static, edge-deployed architecture with $0 monthly fees. Pay once, own the code forever.")
init_state('about_h', "The Digital Landlord Trap.")
init_state('about_short', "When you use traditional web builders, you are just renting space. The moment you stop paying, your business vanishes.")
init_state('feat_data', "bolt | The Speed Pillar | **0.1s Load Times.** We bypass traditional servers for instant global edge delivery.\nwallet | The Economic Pillar | **$0 Monthly Hosting.** No database limits, no plugin fees. You own it forever.\nshield | The Security Pillar | **Unhackable Architecture.** Zero databases means zero entry points for hackers.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="StopWebRent | Variation Engine", layout="wide", page_icon="⚡", initial_sidebar_state="expanded")

# --- 2. ADVANCED UI SYSTEM ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { background: linear-gradient(90deg, #0f172a, #ef4444); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900 !important; font-size: 1.8rem !important; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] { background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; border-radius: 8px !important; color: #0f172a !important; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5rem; background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; font-weight: 800; border: none; box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px; transition: transform 0.2s; }
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NEW VARIATION CONTROLS) ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v50.1 | Custom Variation Engine")
    st.divider()

    with st.expander("🎨 Design Studio (Colors & Fonts)", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate (Light)", "Midnight SaaS (Dark)", "Cyberpunk Neon", "Luxury Gold"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#3b82f6")  
        h_font = st.selectbox("Headings Font", ["Space Grotesk", "Montserrat", "Playfair Display", "Clash Display"])
        b_font = st.selectbox("Body Font", ["Inter", "Open Sans", "Roboto"])

    with st.expander("📐 UI Variations (Layout)", expanded=True):
        st.write("Customize Hover Effects & Geometry:")
        card_hover_style = st.selectbox("Card Hover Style", ["Soft Shadow (Clean)", "Primary Color Border", "Accent Color Border"])
        btn_style = st.selectbox("Button Shape", ["Rounded (Modern)", "Sharp (Aggressive)", "Pill (Friendly)"])
        hero_layout = st.selectbox("Hero Alignment", ["Center Aligned", "Left Aligned"])
        overlay_opacity = st.slider("Hero Image Darkness", 0.1, 0.9, 0.6, help="Higher number makes text easier to read over images.")
        
        # Translate settings to CSS variables
        border_rad = "8px" if btn_style == "Rounded (Modern)" else ("0px" if btn_style == "Sharp (Aggressive)" else "50px")

    with st.expander("🚀 2050 Feature Flags", expanded=False):
        enable_ar = st.checkbox("Spatial Web (AR 3D Models)", value=True)
        enable_voice = st.checkbox("Voice Command Search", value=True)
        enable_context = st.checkbox("Context-Aware UI", value=True)
        enable_ab = st.checkbox("Edge A/B Testing", value=True)

    with st.expander("🧩 Module Manager", expanded=False):
        show_hero = st.checkbox("Hero Section", value=True)
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_pricing = st.checkbox("Pricing Table", value=True)
        show_inventory = st.checkbox("Store/Inventory", value=True)
        show_blog = st.checkbox("Blog Engine", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_cta = st.checkbox("Final CTA", value=True)
        show_booking = st.checkbox("Booking Engine", value=True)

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ StopWebRent Workspace")

tabs = st.tabs(["1. Identity", "2. Content Blocks", "3. Marketing", "4. Pricing", "5. Store", "6. Booking", "7. Blog", "8. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    biz_name = c1.text_input("Business Name", "StopWebRent")
    biz_tagline = c1.text_input("Tagline", "Stop Renting. Start Owning.")
    biz_phone = c1.text_input("Phone", "966572562151")
    biz_email = c1.text_input("Email", "hello@stopwebrent.com")
    prod_url = c2.text_input("Website URL", "https://www.stopwebrent.com")
    biz_addr = c2.text_area("Address", "Kolkata, India", height=100)
    seo_d = c2.text_area("Meta Description", "The world's first Zero-DB, 0.1s website architecture with $0 monthly fees.", height=100)
    logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 Progressive Web App (PWA)")
    pwa_short = st.text_input("App Short Name", biz_name[:12])
    pwa_desc = st.text_input("App Description", "Official App")
    pwa_icon = st.text_input("App Icon (512x512 PNG)", logo_url)
    
    st.subheader("Social Links & WhatsApp")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    ig_link = sc2.text_input("Instagram URL")
    x_link = sc3.text_input("X (Twitter) URL")
    wa_num = sc1.text_input("WhatsApp Number (No +)", "966572562151")
    lang_sheet = sc2.text_input("Language CSV URL")

with tabs[1]:
    st.subheader("Hero Carousel")
    hero_h = st.text_input("Hero Headline", key="hero_h")
    hero_sub = st.text_input("Hero Subtext", key="hero_sub")
    hero_video_id = st.text_input("YouTube Video ID (Background Override)", placeholder="e.g. dQw4w9WgXcQ")
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1600")
    
    st.divider()
    st.subheader("Stats & Features")
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Stat 1", "0.1s")
    label_1 = col_s1.text_input("Label 1", "Load Speed")
    stat_2 = col_s2.text_input("Stat 2", "$0")
    label_2 = col_s2.text_input("Label 2", "Monthly Fees")
    stat_3 = col_s3.text_input("Stat 3", "100%")
    label_3 = col_s3.text_input("Label 3", "Asset Ownership")

    f_title = st.text_input("Features Title", "The 2050 Architecture Pillars")
    feat_data_input = st.text_area("Features List", key="feat_data", height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", key="about_h")
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1600")
    about_short_in = st.text_area("Short Summary", key="about_short", height=100)
    about_long = st.text_area("Full Content", "StopWebRent was founded to give control back to business owners...", height=200)

with tabs[2]:
    st.subheader("📣 Marketing Suite")
    top_bar_enabled = st.checkbox("Enable Top Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale - Ends Soon!")
    top_bar_link = st.text_input("Promo Link", "#pricing")
    popup_enabled = st.checkbox("Enable Popup")
    popup_delay = st.slider("Delay (seconds)", 1, 30, 5)
    popup_title = st.text_input("Popup Headline", "Wait! Don't leave empty handed.")
    popup_text = st.text_input("Popup Body", "Get our free pricing guide on WhatsApp.")
    popup_cta = st.text_input("Popup Button", "Get it Now")

with tabs[3]:
    st.subheader("💰 Pricing")
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Setup Price", "$199")
    titan_mo = col_p1.text_input("Monthly Fee", "$0")
    wix_name = col_p2.text_input("Competitor", "Wix / Shopify")
    wix_mo = col_p2.text_input("Comp. Monthly", "$39/mo")
    save_val = col_p3.text_input("Savings", "$2,340")

with tabs[4]:
    st.subheader("🛒 Store & Payments")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/...")
    custom_feat = st.text_input("Default Product Img", "https://via.placeholder.com/800")
    col_pay1, col_pay2 = st.columns(2)
    paypal_link = col_pay1.text_input("PayPal Link")
    upi_id = col_pay2.text_input("UPI ID")

with tabs[5]:
    st.subheader("📅 Booking Engine")
    booking_embed = st.text_area("Embed Code", height=100, value='<!-- Calendly HTML -->')
    booking_title = st.text_input("Booking Title", "Book an Architecture Call")
    booking_desc = st.text_input("Booking Subtext", "Select a time slot.")

with tabs[6]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV")
    blog_hero_title = st.text_input("Blog Title", "The Builder's Log")
    blog_hero_sub = st.text_input("Blog Subtext", "Insights on Web Architecture.")

with tabs[7]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "John Doe | Titan stopped the bleeding of hosting fees.", height=100)
    faq_data = st.text_area("FAQ", "Do I pay $0 monthly? ? Yes.\nIs it secure? ? Yes, zero databases.", height=100)
    priv_txt = st.text_area("Privacy", "We collect minimum data.", height=100)
    term_txt = st.text_area("Terms", "You own the code.", height=100)


# --- 5. COMPILER ENGINE (WITH NEW VARIATIONS) ---

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = processed_text.split('\n')
    html_out = ""
    in_list = False
    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue
        if clean_line.startswith("* "):
            if not in_list: html_out += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'; in_list = True
            html_out += f'<li style="margin-bottom:0.5rem; opacity:0.9; color:inherit;">{clean_line[2:]}</li>'
        else:
            if in_list: html_out += "</ul>"; in_list = False
            html_out += f"<p style='margin-bottom:1rem; opacity:0.9; color:inherit;'>{clean_line}</p>"
    if in_list: html_out += "</ul>"
    return html_out

def get_theme_css():
    bg_color, text_color, card_bg, glass_nav = "#ffffff", "#0f172a", "#ffffff", "rgba(255, 255, 255, 0.95)"
    if "Midnight" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.9)"
    elif "Cyberpunk" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#050505", "#00ff9d", "#111", "rgba(0,0,0,0.8)"
    elif "Luxury" in theme_mode: bg_color, text_color, card_bg, glass_nav = "#1c1c1c", "#D4AF37", "#2a2a2a", "rgba(28,28,28,0.95)"

    # CARD HOVER VARIATION LOGIC
    card_hover_css = "box-shadow: 0 20px 40px -10px rgba(0,0,0,0.15); transform: translateY(-5px);"
    if card_hover_style == "Primary Color Border": card_hover_css += f" border-color: var(--p);"
    elif card_hover_style == "Accent Color Border": card_hover_css += f" border-color: var(--s);"

    hero_align = "text-align: left; justify-content: flex-start; align-items: center;" if hero_layout == "Left Aligned" else "text-align: center; justify-content: center;"

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {text_color}; --card: {card_bg}; --radius: {border_rad}; --nav: {glass_nav}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; }} html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; transition: background 0.3s, color 0.3s; }}
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: #1e293b; --nav: rgba(15, 23, 42, 0.95); }}
    
    p, h1, h2, h3, h4, h5, h6, span, li, div {{ color: inherit; }}
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--p); line-height: 1.2; margin-bottom: 1rem; }}
    strong {{ color: var(--p); font-weight: 800; }} h1 {{ font-size: clamp(2.5rem, 5vw, 4.5rem); }} h2 {{ font-size: clamp(2rem, 4vw, 3rem); }}
    
    .hero {{ position: relative; min-height: 90vh; overflow: hidden; display: flex; {hero_align} color: white; padding-top: 80px; background-color: var(--p); }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: 0; }}
    .carousel-slide.active {{ opacity: 1; }}
    
    /* OVERLAY SLIDER VARIATION */
    .hero-overlay {{ background: rgba(0,0,0,{overlay_opacity}); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
    
    .hero-content {{ z-index: 2; position: relative; width: 100%; padding: 0 20px; }}
    .hero h1 {{ color: #ffffff !important; text-shadow: 0 4px 20px rgba(0,0,0,0.4); }}
    .hero p {{ color: rgba(255,255,255,0.95) !important; font-size: clamp(1.1rem, 2vw, 1.3rem); max-width: 700px; margin: 0 auto 2rem auto; text-shadow: 0 2px 10px rgba(0,0,0,0.4); }}
    
    input, textarea, select {{ width: 100%; padding: 0.8rem; margin-bottom: 1rem; border: 1px solid #ccc; border-radius: 6px; font-family: inherit; background: var(--card); color: var(--txt); }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 20px; }}
    
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-radius: var(--radius); font-weight: 700; text-decoration: none; transition: 0.3s; text-transform: uppercase; cursor: pointer; border: none; text-align: center; min-height: 3.5rem; }}
    .btn-primary {{ background: var(--p); color: white !important; }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 25px -5px var(--s); }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.15); }}
    
    header {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(100,100,100,0.1); padding: 1rem 0; transition: top 0.3s; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); font-size: 0.9rem; transition:0.2s; }}
    .nav-links a:hover {{ color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    main section {{ padding: clamp(2rem, 4vw, 3rem) 0; }}
    .section-head {{ text-align: center; margin-bottom: clamp(1rem, 3vw, 2.5rem); }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .about-grid, .detail-view {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    
    .card {{ background: var(--card); border-radius: var(--radius); border: 1px solid rgba(100,100,100,0.1); transition: 0.3s; display: flex; flex-direction: column; overflow: hidden; }}
    
    /* DYNAMIC CARD HOVER */
    .card:hover {{ {card_hover_css} }}
    
    .card h3, .card h4, .card a {{ color: var(--txt) !important; text-decoration: none; }}
    .card-body {{ padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; background: #f1f5f9; }}
    
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(100,100,100,0.1); background: var(--card); color: var(--txt); }}

    details {{ background: var(--card); border: 1px solid rgba(100,100,100,0.1); border-radius: 8px; margin-bottom: 1rem; padding: 1rem; cursor: pointer; color: var(--txt); }}
    
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.8) !important; text-decoration: none; display: block; margin-bottom: 0.5rem; transition: 0.3s; }}
    footer a:hover {{ color: #ffffff !important; text-decoration: underline; }}
    .social-icon {{ width: 24px; height: 24px; fill: rgba(255,255,255,0.7); transition: 0.3s; }}
    .social-icon:hover {{ fill: #ffffff; transform: scale(1.1); }}

    #cart-float {{ position: fixed; bottom: 100px; right: 30px; background: var(--p); color: white; padding: 15px 20px; border-radius: 50px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); cursor: pointer; z-index: 998; display: flex; align-items: center; gap: 10px; font-weight: bold; }}
    #cart-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 500px; padding: 2rem; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); z-index: 1001; border: 1px solid rgba(128,128,128,0.2); color: var(--txt); }}
    #cart-overlay {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; }}
    
    .local-vault {{ background: rgba(128,128,128,0.05); padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid rgba(128,128,128,0.1); }}
    #voice-btn {{ position: fixed; bottom: 170px; right: 30px; background: var(--p); color: white; border-radius: 50px; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; cursor: pointer; box-shadow: 0 10px 20px rgba(0,0,0,0.2); z-index: 998; border: none; }}
    .listening {{ animation: pulse 1s infinite; background: var(--s) !important; }}
    @keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.1); }} 100% {{ transform: scale(1); }} }}
    model-viewer {{ width: 100%; height: 400px; background-color: transparent; border-radius: 12px; }}
    
    #theme-toggle {{ position: fixed; bottom: 30px; left: 30px; width: 40px; height: 40px; background: var(--card); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); cursor: pointer; z-index: 999; font-size: 1.2rem; border: 1px solid rgba(0,0,0,0.1); }}
    
    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 60px; left: -100%; width: 100%; height: calc(100vh - 60px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; gap: 1.5rem; }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .detail-view, .grid-3 {{ grid-template-columns: 1fr !important; }}
    }}
    """

def gen_2050_scripts():
    context_js = "if(new Date().getHours() >= 19 || new Date().getHours() <= 6) document.body.classList.add('dark-mode');" if enable_context else ""
    ab_js = "let variant = localStorage.getItem('titan_ab') || (Math.random() > 0.5 ? 'A' : 'B'); localStorage.setItem('titan_ab', variant); if(variant === 'B') document.documentElement.style.setProperty('--s', '#10b981');" if enable_ab else ""
    voice_js = "function startVoiceSearch() { if (!('webkitSpeechRecognition' in window)) return alert('Voice search not supported in this browser.'); const rec = new webkitSpeechRecognition(); rec.lang = 'en-US'; const btn = document.getElementById('voice-btn'); btn.classList.add('listening'); rec.onresult = (e) => { const transcript = e.results[0][0].transcript.toLowerCase(); alert('Searching for: ' + transcript); document.querySelectorAll('.card').forEach(c => { c.style.display = c.innerText.toLowerCase().includes(transcript) ? 'flex' : 'none'; }); }; rec.onend = () => btn.classList.remove('listening'); rec.start(); }" if enable_voice else ""
    return f"<script defer>{context_js} {ab_js} {voice_js}</script>"

def gen_nav():
    logo_display = f'<img src="{logo_url}" height="40" alt="{biz_name} Logo">' if logo_url else f'<span style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</span>'
    return f"""
    <header><div class="container nav-flex">
        <a href="index.html" style="text-decoration:none;">{logo_display}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            {'<a href="index.html#features">Features</a>' if show_features else ''}
            {'<a href="index.html#inventory">Store</a>' if show_inventory else ''}
            {'<a href="blog.html">Blog</a>' if show_blog else ''}
            <a href="contact.html">Contact</a>
            <a href="tel:{biz_phone}" class="btn-accent" style="padding:0.6rem 1.5rem; border-radius:50px; color:white !important;">Call Now</a>
        </nav>
    </div></header>
    <div id="theme-toggle" onclick="document.body.classList.toggle('dark-mode')">🌓</div>
    """

def gen_hero():
    bg_media = f"""<div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div><div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div><div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div><script defer>let slides = document.querySelectorAll('.carousel-slide'); let currentSlide = 0; setInterval(() => {{ slides[currentSlide].classList.remove('active'); currentSlide = (currentSlide + 1) % slides.length; slides[currentSlide].classList.add('active'); }}, 4000);</script>"""
    return f"""<section class="hero"><div class="hero-overlay"></div>{bg_media}<div class="container hero-content"><h1>{hero_h}</h1><p>{hero_sub}</p><div style="display:flex; gap:1rem; flex-wrap:wrap; {'justify-content:center;' if hero_layout == 'Center Aligned' else ''}"><a href="#inventory" class="btn btn-accent">Explore Now</a><a href="contact.html" class="btn" style="background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); color:white;">Contact Us</a></div></div></section>"""

def get_simple_icon(name):
    icon_map = {"bolt": "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z", "wallet": "M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z", "shield": "M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z", "table": "M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM5 19V5h14v14H5zm2-2h10v-2H7v2zm0-4h10v-2H7v2zm0-4h10V7H7v2z"}
    path = icon_map.get(name.lower().strip(), "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z")
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

def gen_features():
    if not show_features: return ""
    cards = "".join([f'<div class="card"><div style="color:var(--s); margin-bottom:1rem;">{get_simple_icon(p[0])}</div><h3>{p[1].strip()}</h3><div>{format_text(p[2].strip())}</div></div>' for l in feat_data_input.split('\n') if (p:=l.split('|')) and len(p)>=3])
    return f'<section id="features"><div class="container"><div class="section-head"><h2 id="feature-title">{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>'

def gen_stats():
    if not show_stats: return ""
    return f'<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_1}</h3><p style="color:rgba(255,255,255,0.7);">{label_1}</p></div><div><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_2}</h3><p style="color:rgba(255,255,255,0.7);">{label_2}</p></div><div><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_3}</h3><p style="color:rgba(255,255,255,0.7);">{label_3}</p></div></div></div>'

def gen_csv_parser():
    return """<script defer>function parseCSVLine(str) { const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) { const c = str[i]; if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } } else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; } } res.push(cur.trim()); return res; } function parseMarkdown(text) { return text ? text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>') : ''; }</script>"""

def gen_cart_system():
    if not wa_num: return ""
    return f"""
    <div id="cart-float" onclick="toggleCart()">🛒 <span id="cart-count">0</span></div>
    <div id="cart-overlay" onclick="toggleCart()"></div>
    <div id="cart-modal">
        <h3>Your Cart</h3><div id="cart-items" style="max-height:200px; overflow-y:auto; margin:1rem 0;"></div>
        <div style="font-weight:bold; font-size:1.2rem; margin-bottom:1rem; text-align:right;">Total: <span id="cart-total">0.00</span></div>
        <div class="local-vault"><h4 style="font-size:0.9rem;">🔒 Fast Checkout Vault</h4><input type="text" id="vault-name" placeholder="Full Name"><input type="text" id="vault-address" placeholder="Delivery Address"></div>
        <button onclick="checkoutWhatsApp()" class="btn btn-accent" style="width:100%; margin-top:1rem;">1-Click Checkout via WhatsApp</button>
    </div>
    <script defer>
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    document.getElementById('vault-name').value = localStorage.getItem('t_name') || ''; document.getElementById('vault-address').value = localStorage.getItem('t_addr') || '';
    function renderCart() {{ const box = document.getElementById('cart-items'); if(!box) return; box.innerHTML = ''; let total = 0; cart.forEach((item, i) => {{ total += parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0; box.innerHTML += `<div class="cart-item"><span>${{item.name}}</span><span>${{item.price}} <span onclick="remItem(${{i}})" style="color:red;cursor:pointer;">x</span></span></div>`; }}); document.getElementById('cart-count').innerText = cart.length; document.getElementById('cart-total').innerText = total.toFixed(2); document.getElementById('cart-float').style.display = cart.length > 0 ? 'flex' : 'none'; localStorage.setItem('titanCart', JSON.stringify(cart)); }}
    function addToCart(name, price) {{ cart.push({{name, price}}); renderCart(); alert(name + " added!"); }}
    function remItem(i) {{ cart.splice(i,1); renderCart(); }}
    function toggleCart() {{ const m = document.getElementById('cart-modal'); m.style.display = m.style.display === 'block' ? 'none' : 'block'; document.getElementById('cart-overlay').style.display = m.style.display; }}
    function checkoutWhatsApp() {{ const n = document.getElementById('vault-name').value; const a = document.getElementById('vault-address').value; localStorage.setItem('t_name', n); localStorage.setItem('t_addr', a); let msg = "New Order:%0A"; cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; }}); if(n) msg += `%0ADeliver to: ${{n}}, ${{a}}`; window.open(`https://wa.me/{wa_num}?text=${{msg}}`, '_blank'); cart = []; renderCart(); toggleCart(); }}
    window.addEventListener('load', renderCart);
    </script>
    """

def gen_inventory():
    if not show_inventory: return ""
    voice_btn = '<button id="voice-btn" onclick="startVoiceSearch()">🎤</button>' if enable_voice else ''
    return f"""
    <section id="inventory" style="background:rgba(0,0,0,0.02)"><div class="container"><h2 class="section-head">Store</h2><div id="inv-grid" class="grid-3">Loading Edge Data...</div></div>{voice_btn}</section>
    {gen_csv_parser()}
    <script defer>
    async function loadInv() {{
        try {{ const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/); const box = document.getElementById('inv-grid'); box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                const c = parseCSVLine(lines[i]); if(c.length > 1) {{ let mainImg = c[3] ? c[3].split('|')[0] : '{custom_feat}'; const pName = encodeURIComponent(c[0]);
                    box.innerHTML += `<div class="card"><img src="${{mainImg}}" class="prod-img" loading="lazy"><h3>${{c[0]}}</h3><p style="color:var(--s); font-weight:bold;">${{c[1]}}</p><p class="card-desc">${{c[2]}}</p><div style="margin-top:auto; display:grid; grid-template-columns:1fr 1fr; gap:10px;"><button onclick="addToCart('${{c[0]}}', '${{c[1]}}')" class="btn" style="padding:0.5rem; font-size:0.8rem; background:#e2e8f0; color:#333!important;">Add</button><a href="product.html?item=${{pName}}" class="btn btn-primary" style="padding:0.5rem; font-size:0.8rem;">Details</a></div></div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    window.addEventListener('load', loadInv);
    </script>
    """

def gen_about_section():
    if not show_gallery: return ""
    return f'<section id="about"><div class="container"><div class="about-grid"><div><h2>{about_h_in}</h2><div>{format_text(about_short_in)}</div><a href="about.html" class="btn btn-primary" style="margin-top:1rem;">Read More</a></div><img src="{about_img}" style="width:100%; border-radius:var(--radius);" loading="lazy"></div></div></section>'

def gen_footer():
    icons = f'<a href="{fb_link}" target="_blank" style="margin-right:15px;color:white;">FB</a>' if fb_link else ""
    return f"""<footer><div class="container"><div class="footer-grid"><div><h3 style="color:white; margin-bottom:1.5rem;">{biz_name}</h3><p style="color:rgba(255,255,255,0.7);">{biz_addr}</p><div style="margin-top:1.5rem;">{icons}</div></div><div><h4 style="color:white; text-transform:uppercase;">Links</h4><a href="index.html" style="color:white!important; display:block;">Home</a><a href="blog.html" style="color:white!important; display:block;">Blog</a></div><div><h4 style="color:white; text-transform:uppercase;">Legal</h4><a href="privacy.html" style="color:white!important; display:block;">Privacy</a><a href="terms.html" style="color:white!important; display:block;">Terms</a></div></div><div style="border-top:1px solid rgba(255,255,255,0.1); margin-top:3rem; padding-top:2rem; text-align:center; color:rgba(255,255,255,0.5);">&copy; {datetime.datetime.now().year} {biz_name}. Powered by Titan Engine.</div></div></footer>"""

def build_page(title, content):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title><link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;600&display=swap" rel="stylesheet"><style>{get_theme_css()}</style>{gen_2050_scripts()}</head><body><main>{gen_nav()}{content}{gen_footer()}{gen_cart_system()}</main></body></html>"""

def gen_inner_header(title):
    return f'<header class="hero" style="min-height: 40vh; background:var(--p);"><div class="container"><h1>{title}</h1></div></header>'

# --- 6. PAGE ASSEMBLY ---
home_content = gen_hero() + gen_stats() + gen_features() + gen_inventory() + gen_about_section()

# --- 7. DEPLOYMENT ---
st.divider()
c1, c2 = st.columns([3, 1])

with c1:
    st.subheader("🚀 Live Preview")
    st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)

with c2:
    st.success("Variations Applied. Ready to Compile.")
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", build_page("Home", home_content))
        zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container'>{format_text(about_long)}</div>"))
        zf.writestr("contact.html", build_page("Contact", f"{gen_inner_header('Contact Us')}<div class='container'><p>{biz_email}</p><p>{biz_phone}</p></div>"))
        zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container'>{format_text(priv_txt)}</div>"))
        zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms')}<div class='container'>{format_text(term_txt)}</div>"))
        
    st.download_button("📥 DOWNLOAD SITE PACKAGE", z_b.getvalue(), f"{biz_name.replace(' ','_')}_site.zip", "application/zip", type="primary")
