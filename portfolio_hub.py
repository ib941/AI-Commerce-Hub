import streamlit as st
import base64
import requests
import json

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ibrahim | Solutions Center",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #0B1628 !important;
    color: #F0EDE8 !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="collapsedControl"],
.stDeployButton { display: none !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #071020 !important;
    border-right: 1px solid rgba(180,160,100,0.18) !important;
    padding-top: 2rem !important;
}
[data-testid="stSidebar"] * { color: #F0EDE8 !important; }

.sidebar-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.7rem;
    font-weight: 300;
    letter-spacing: 0.12em;
    color: #C9A84C !important;
    padding: 0 1.4rem 0.3rem;
    border-bottom: 1px solid rgba(180,160,100,0.2);
    margin-bottom: 1.6rem;
}
.sidebar-sub {
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #7A8FA6 !important;
    padding: 0 1.4rem;
    margin-bottom: 1.8rem;
}
.nav-label {
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #4A6080 !important;
    padding: 0 1.4rem;
    margin-bottom: 0.6rem;
}

[data-testid="stSidebar"] .stRadio > label { display: none !important; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
    padding: 0 0.8rem;
}
[data-testid="stSidebar"] .stRadio label {
    display: flex !important;
    align-items: center;
    gap: 0.7rem;
    padding: 0.65rem 0.9rem !important;
    border-radius: 6px !important;
    cursor: pointer !important;
    transition: background 0.2s, color 0.2s !important;
    font-size: 0.88rem !important;
    font-weight: 400 !important;
    color: #8FA8C0 !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(201,168,76,0.08) !important;
    color: #F0EDE8 !important;
}
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"]:has(input:checked),
[data-testid="stSidebar"] .stRadio [aria-checked="true"] ~ span,
[data-testid="stSidebar"] .stRadio input:checked + div ~ div {
    color: #C9A84C !important;
}
[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] { display: none !important; }

/* ── Main content area ── */
[data-testid="stMainBlockContainer"], .main .block-container {
    padding: 3rem 3.5rem 4rem !important;
    max-width: 1100px !important;
}

/* ── Typography ── */
h1 { font-family: 'Cormorant Garamond', serif !important; font-weight: 300 !important;
     font-size: 3.2rem !important; letter-spacing: 0.04em !important; color: #F0EDE8 !important; }
h2 { font-family: 'Cormorant Garamond', serif !important; font-weight: 400 !important;
     font-size: 1.9rem !important; color: #F0EDE8 !important; }
h3 { font-family: 'Inter', sans-serif !important; font-weight: 500 !important;
     font-size: 1rem !important; letter-spacing: 0.06em !important; color: #C9A84C !important; }

/* ── Gold divider ── */
.gold-line {
    height: 1px;
    background: linear-gradient(90deg, #C9A84C 0%, rgba(201,168,76,0.15) 100%);
    margin: 2rem 0;
}

/* ── Eyebrow label ── */
.eyebrow {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #C9A84C;
    margin-bottom: 0.5rem;
}

/* ── Service cards ── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.4rem;
    margin-top: 2rem;
}
.card {
    background: #0F1E35;
    border: 1px solid rgba(180,160,100,0.15);
    border-radius: 10px;
    padding: 2rem 1.6rem;
    transition: border-color 0.25s, transform 0.25s;
}
.card:hover {
    border-color: rgba(201,168,76,0.5);
    transform: translateY(-3px);
}
.card-icon { font-size: 2rem; margin-bottom: 1rem; }
.card-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    font-weight: 400;
    color: #F0EDE8;
    margin-bottom: 0.4rem;
}
.card-title-ar {
    font-size: 0.9rem;
    color: #7A8FA6;
    margin-bottom: 0.8rem;
    direction: rtl;
}
.card-desc { font-size: 0.83rem; color: #8FA8C0; line-height: 1.6; }

/* ── CTA button ── */
.cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 2.2rem;
    padding: 0.75rem 1.8rem;
    background: transparent;
    border: 1px solid #C9A84C;
    border-radius: 6px;
    color: #C9A84C !important;
    font-size: 0.82rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-decoration: none !important;
    transition: background 0.2s;
}
.cta-btn:hover { background: rgba(201,168,76,0.1); }

/* ── AI tool sections ── */
.tool-header {
    background: linear-gradient(135deg, #0F1E35 0%, #071020 100%);
    border: 1px solid rgba(201,168,76,0.2);
    border-radius: 12px;
    padding: 2rem 2.2rem;
    margin-bottom: 2rem;
}
.tool-badge {
    display: inline-block;
    background: rgba(201,168,76,0.12);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.68rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #C9A84C;
    margin-bottom: 1rem;
}

/* ── Streamlit widgets override ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: #0F1E35 !important;
    border: 1px solid rgba(180,160,100,0.25) !important;
    border-radius: 7px !important;
    color: #F0EDE8 !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #C9A84C !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label,
.stFileUploader label, .stFileUploader p {
    color: #8FA8C0 !important;
    font-size: 0.83rem !important;
}

/* Primary button */
.stButton > button {
    background: #C9A84C !important;
    color: #071020 !important;
    border: none !important;
    border-radius: 7px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 0.6rem 1.6rem !important;
    letter-spacing: 0.05em !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

/* File uploader */
[data-testid="stFileUploader"] {
    background: #0F1E35 !important;
    border: 1px dashed rgba(180,160,100,0.3) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
}

/* Result boxes */
.result-box {
    background: #0F1E35;
    border: 1px solid rgba(180,160,100,0.2);
    border-left: 3px solid #C9A84C;
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    margin-top: 1.2rem;
    font-size: 0.88rem;
    line-height: 1.75;
    color: #D0CBBE;
    white-space: pre-wrap;
}
.result-label {
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #C9A84C;
    margin-bottom: 0.5rem;
}

/* Spinner */
.stSpinner > div { border-top-color: #C9A84C !important; }

/* Info/success boxes */
.stAlert { background: #0F1E35 !important; border-color: rgba(201,168,76,0.3) !important; color: #D0CBBE !important; }

/* Columns gap */
[data-testid="column"] { padding: 0 0.5rem !important; }

@media (max-width: 768px) {
    .cards-grid { grid-template-columns: 1fr !important; }
    [data-testid="stMainBlockContainer"], .main .block-container { padding: 1.5rem !important; }
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar navigation ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">IBRAHIM</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Solutions Center</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["🏛️  Portfolio", "🛍️  E-Commerce Hub", "🎬  Storyboard Architect"],
        label_visibility="hidden"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:0 1.4rem; font-size:0.72rem; color:#3A5070; line-height:1.8;">
        <div style="color:#C9A84C; font-size:0.62rem; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:0.5rem;">Contact</div>
        Ibrahim Abdulwahab Alkabsi<br>
        <span style="color:#4A6080;">Graphic Designer · Photographer<br>E-Commerce Architect · AI Integrator</span>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  PAGE 1 — PORTFOLIO
# ═══════════════════════════════════════════════════════════════
if "Portfolio" in page:
    st.markdown('<div class="eyebrow">Creative & Digital Services</div>', unsafe_allow_html=True)
    st.markdown("# Ibrahim Alkabsi")
    st.markdown("### Complete Solutions Center — مركز الحلول المتكاملة")
    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#8FA8C0; font-size:0.95rem; line-height:1.85; max-width:640px;">
    Premium creative and digital services — from luxury product photography to AI-powered 
    e-commerce solutions. Every deliverable is crafted to the highest professional standard.
    <br><br>
    <span style="direction:rtl; display:block; color:#7A8FA6; font-size:0.88rem;">
    خدمات إبداعية ورقمية متميزة — من تصوير المنتجات الفاخرة إلى حلول التجارة الإلكترونية بالذكاء الاصطناعي.
    </span>
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cards-grid">
        <div class="card">
            <div class="card-icon">📷</div>
            <div class="card-title">Product Photography</div>
            <div class="card-title-ar">تصوير المنتجات</div>
            <div class="card-desc">Luxury, high-end commercial product photography with dramatic custom lighting and cinematic composition for brands that demand the best.</div>
        </div>
        <div class="card">
            <div class="card-icon">🛒</div>
            <div class="card-title">Salla Store Setup</div>
            <div class="card-title-ar">إعداد متجر سلة</div>
            <div class="card-desc">Professional end-to-end e-commerce configuration on Salla — store architecture, product listings, payment gateways, and brand identity.</div>
        </div>
        <div class="card">
            <div class="card-icon">🎨</div>
            <div class="card-title">Poster Design</div>
            <div class="card-title-ar">تصميم الملصقات</div>
            <div class="card-desc">Dynamic, premium social media posters and marketing materials. Bold visual identity that stops the scroll and drives engagement.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown("""
    <a class="cta-btn" href="https://wa.me/966500000000" target="_blank">
        💬 &nbsp; Chat on WhatsApp &nbsp;·&nbsp; تواصل معي
    </a>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
#  PAGE 2 — E-COMMERCE HUB
# ═══════════════════════════════════════════════════════════════
elif "E-Commerce" in page:
    st.markdown('<div class="eyebrow">AI Production Suite</div>', unsafe_allow_html=True)
    st.markdown("# E-Commerce Content Hub")
    st.markdown("### مولّد المحتوى التجاري")
    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tool-header">
        <div class="tool-badge">✦ Powered by AI — Free & Instant</div>
        <p style="color:#8FA8C0; font-size:0.88rem; line-height:1.75; margin:0;">
        Upload your product image and describe your product. The AI will generate 
        bilingual marketing copy, SEO titles, and social media captions — ready to publish.
        <br><span style="direction:rtl; display:block; margin-top:0.4rem; color:#6A7F96; font-size:0.82rem;">
        ارفع صورة منتجك وصفه، وسيولّد الذكاء الاصطناعي محتوى تسويقياً احترافياً باللغتين.
        </span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        uploaded_file = st.file_uploader(
            "Upload Product Image — ارفع صورة المنتج",
            type=["jpg", "jpeg", "png", "webp"],
            help="Upload a clear product photo for best results"
        )
        if uploaded_file:
            st.image(uploaded_file, use_container_width=True)

    with col2:
        product_name = st.text_input(
            "Product Name — اسم المنتج",
            placeholder="e.g. Luxury Oud Perfume / عطر العود الفاخر"
        )
        product_desc = st.text_area(
            "Brief Description — وصف مختصر",
            placeholder="Key features, materials, target audience...",
            height=100
        )
        platform = st.selectbox(
            "Target Platform — المنصة المستهدفة",
            ["Salla Store (Arabic + English)", "Instagram / Social Media", "Amazon / Noon", "Full Package (All Platforms)"]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✦ Generate Content — توليد المحتوى", use_container_width=True):
        if not product_name:
            st.warning("Please enter a product name first. / الرجاء إدخال اسم المنتج.")
        else:
            with st.spinner("Crafting your content... جارٍ توليد المحتوى..."):
                # Build prompt
                prompt = f"""You are an expert bilingual (Arabic & English) e-commerce copywriter specializing in premium Saudi/Gulf market products.

Product Name: {product_name}
Description: {product_desc if product_desc else 'Not provided'}
Target Platform: {platform}

Generate professional marketing content in this EXACT structure:

---
🇸🇦 ARABIC CONTENT / المحتوى العربي
---

**عنوان المنتج (SEO):**
[Compelling Arabic product title, 60-70 chars]

**وصف المنتج:**
[3-4 sentences, persuasive Arabic product description highlighting benefits]

**كابشن سوشيال ميديا:**
[Engaging Arabic social caption with 5 relevant hashtags]

---
🇬🇧 ENGLISH CONTENT
---

**Product Title (SEO):**
[Compelling English product title, 60-70 chars]

**Product Description:**
[3-4 sentences, persuasive English product description highlighting benefits]

**Social Media Caption:**
[Engaging English caption with 5 relevant hashtags]

---
📊 SEO KEYWORDS
---

**Arabic Keywords:** [5 Arabic search keywords]
**English Keywords:** [5 English search keywords]

Keep the tone premium, persuasive, and tailored to the Gulf/Saudi market."""

                try:
                    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
                    headers = {"Content-Type": "application/json"}
                    payload = {
                        "inputs": f"<s>[INST] {prompt} [/INST]",
                        "parameters": {"max_new_tokens": 1200, "temperature": 0.7, "return_full_text": False}
                    }
                    resp = requests.post(api_url, headers=headers, json=payload, timeout=60)
                    resp.raise_for_status()
                    data = resp.json()
                    if isinstance(data, list) and len(data) > 0:
                        result = data[0].get("generated_text", "No output returned.")
                    else:
                        result = str(data)

                    st.markdown('<div class="result-label">✦ Generated Content — المحتوى المولَّد</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error generating content: {str(e)}")

# ═══════════════════════════════════════════════════════════════
#  PAGE 3 — STORYBOARD ARCHITECT
# ═══════════════════════════════════════════════════════════════
elif "Storyboard" in page:
    st.markdown('<div class="eyebrow">AI Production Suite</div>', unsafe_allow_html=True)
    st.markdown("# Cinematic Storyboard Architect")
    st.markdown("### مهندس اللوحة القصصية السينمائية")
    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tool-header">
        <div class="tool-badge">✦ Powered by AI — Free & Instant</div>
        <p style="color:#8FA8C0; font-size:0.88rem; line-height:1.75; margin:0;">
        Describe your commercial concept in plain words. The AI transforms it into a 
        structured, director-level video production brief with shot lists, camera directions, 
        and scene-by-scene breakdowns.
        <br><span style="direction:rtl; display:block; margin-top:0.4rem; color:#6A7F96; font-size:0.82rem;">
        صِف فكرتك التجارية بكلماتك، وسيحوّلها الذكاء الاصطناعي إلى سكريبت إنتاج احترافي.
        </span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        brand_name = st.text_input(
            "Brand / Product Name — اسم العلامة التجارية",
            placeholder="e.g. Noir Oud / نوار للعطور"
        )
        concept = st.text_area(
            "Your Concept — فكرتك",
            placeholder="Describe your video idea... e.g. A luxury perfume ad set in a desert at golden hour, showing a man in traditional Saudi dress...",
            height=130
        )
        video_type = st.selectbox(
            "Video Type — نوع الفيديو",
            ["Brand Commercial (30 sec)", "Product Showcase (60 sec)", "Social Media Reel (15 sec)", "Brand Documentary (2 min)"]
        )
        mood = st.selectbox(
            "Mood & Tone — المزاج والأسلوب",
            ["Luxury & Cinematic", "Energetic & Bold", "Warm & Emotional", "Minimalist & Clean", "Epic & Dramatic"]
        )

    with col2:
        st.markdown("""
        <div style="background:#071020; border:1px solid rgba(201,168,76,0.15); border-radius:10px; padding:1.4rem; height:100%;">
            <div style="font-size:0.62rem; letter-spacing:0.2em; text-transform:uppercase; color:#C9A84C; margin-bottom:1rem;">What You'll Get</div>
            <div style="font-size:0.83rem; color:#7A8FA6; line-height:2;">
                ✦ Scene-by-scene breakdown<br>
                ✦ Camera angles & movements<br>
                ✦ Lighting & color direction<br>
                ✦ Talent & wardrobe notes<br>
                ✦ Music & sound design cues<br>
                ✦ Arabic & English script lines<br>
                ✦ Production timeline estimate
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✦ Build Storyboard — بناء اللوحة القصصية", use_container_width=True):
        if not concept:
            st.warning("Please describe your concept first. / الرجاء وصف فكرتك أولاً.")
        else:
            with st.spinner("Architecting your storyboard... جارٍ بناء اللوحة القصصية..."):
                prompt = f"""You are an award-winning commercial director and storyboard architect with expertise in luxury brand filmmaking for the Gulf/Saudi market.

Brand: {brand_name if brand_name else 'Not specified'}
Concept: {concept}
Video Type: {video_type}
Mood & Tone: {mood}

Create a detailed, professional storyboard brief in this EXACT structure:

---
🎬 PRODUCTION BRIEF
---

**Project Title:** [Cinematic title for this commercial]
**Duration:** [Based on video type]
**Overall Vision:** [2-sentence director's vision statement]

---
📋 SCENE BREAKDOWN
---

**SCENE 01 — [Scene Name]**
• Shot Type: [e.g. Aerial establishing shot / ECU / Wide]
• Camera Movement: [e.g. Slow drone push-in / Static / Dolly left]
• Lighting: [e.g. Golden hour backlight, practical candles]
• Action: [What happens in this scene]
• Duration: [e.g. 0:00 – 0:05]
• Arabic Line: [Voiceover or on-screen text in Arabic if applicable]
• English Line: [Voiceover or on-screen text in English if applicable]

[Continue for 4-6 scenes total depending on video length]

---
🎨 VISUAL DIRECTION
---

**Color Palette:** [3-4 descriptive colors/moods]
**Wardrobe:** [Key wardrobe notes]
**Location:** [Recommended shooting locations]
**Props:** [Key props needed]

---
🎵 AUDIO DIRECTION
---

**Music Style:** [e.g. Orchestral Arabic fusion, building tempo]
**Sound Design:** [Key ambient/foley sounds]
**Voiceover Tone:** [e.g. Deep, authoritative Arabic male voice]

---
⏱️ PRODUCTION NOTES
---

**Shooting Days:** [Estimate]
**Key Equipment:** [Camera, lenses, special gear]
**Director's Note:** [One powerful closing statement about the vision]

Make it feel like a real premium production document a Saudi commercial director would be proud to execute."""

                try:
                    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
                    headers = {"Content-Type": "application/json"}
                    payload = {
                        "inputs": f"<s>[INST] {prompt} [/INST]",
                        "parameters": {"max_new_tokens": 1500, "temperature": 0.7, "return_full_text": False}
                    }
                    resp = requests.post(api_url, headers=headers, json=payload, timeout=60)
                    resp.raise_for_status()
                    data = resp.json()
                    if isinstance(data, list) and len(data) > 0:
                        result = data[0].get("generated_text", "No output returned.")
                    else:
                        result = str(data)

                    st.markdown('<div class="result-label">✦ Your Storyboard Brief — اللوحة القصصية</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error generating storyboard: {str(e)}")

# ── Voiceflow widget placeholder ─────────────────────────────────────────────
# REPLACE the script below with your actual Voiceflow embed code
st.markdown("""
<div id="voiceflow-placeholder" style="
    position:fixed; bottom:24px; right:24px; z-index:9999;
    width:52px; height:52px; border-radius:50%;
    background:linear-gradient(135deg,#C9A84C,#A07830);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 4px 20px rgba(201,168,76,0.35);
    cursor:pointer; font-size:1.4rem;
    " title="AI Assistant — coming soon">
    💬
</div>
<!-- PASTE YOUR VOICEFLOW SCRIPT HERE -->
""", unsafe_allow_html=True)
