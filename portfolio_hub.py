import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# =====================================================================
# 1. GLOBAL PAGE CONFIG & WATERMARK REMOVAL
# =====================================================================
st.set_page_config(
    page_title="Ibrahim | Complete Solutions Center", 
    page_icon="✨", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# Force-hide all Streamlit branding
hide_style = """
    <style>
    #MainMenu, footer, header {visibility: hidden !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    button[data-testid="baseButton-header"] {display: none !important;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Signature dark luxury theme
st.markdown("""
    <style>
        .stApp { background-color: #0b0c10; color: #e5e7eb; }
        .custom-card {
            background-color: #12141c;
            border: 1px solid rgba(0, 229, 147, 0.2);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }
        h1, h2, h3 { color: #ffffff !important; }
        p { color: #9ca3af !important; }
        .whatsapp-btn {
            background-color: #25D366; color: white !important;
            padding: 0.8rem 2rem; border-radius: 30px; font-weight: 600;
            display: flex; justify-content: center; text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. NAVIGATION SIDEBAR
# =====================================================================
st.sidebar.title("✨ Workspace Menu")
current_page = st.sidebar.radio(
    "Select Application Window:",
    ["🏠 Creative Portfolio Showcase", "🛍️ AI E-Commerce Content Hub", "🎬 Cinematic Storyboard Architect"]
)

# =====================================================================
# PAGE 1: CREATIVE PORTFOLIO SHOWCASE
# =====================================================================
if current_page == "🏠 Creative Portfolio Showcase":
    st.markdown("<h1 style='text-align: center;'>Ibrahim</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Complete Solutions Center | Salla Stores • Photography • Design</p>", unsafe_allow_html=True)
    
    # Force sidebar visibility on mobile
    st.markdown("""<style>
        [data-testid="stSidebar"] { display: block !important; }
        [data-testid="stSidebarCollapseButton"] { display: none !important; }
    </style>""", unsafe_allow_html=True)
    
    st.info("📱 **Tip:** Tap the menu icon (≡) in the top-left corner to access the workspace tools!")
    st.markdown("---")

    st.markdown("""
        <div class="custom-card">
            <h3>📸 Product Photography</h3>
            <p>High-end commercial & luxury product shots designed to tell a brand story.</p>
        </div>
        <div class="custom-card">
            <h3>🛒 Salla Store Setup</h3>
            <p>Professional end-to-end e-commerce configurations and custom layout optimization.</p>
        </div>
        <div class="custom-card">
            <h3>🎨 Poster Design</h3>
            <p>Dynamic, premium social media posters and tailored promotional graphics.</p>
        </div>
        <a href="https://wa.me/966534657849" target="_blank" class="whatsapp-btn">💬 Chat on WhatsApp</a>
    """, unsafe_allow_html=True)

# =====================================================================
# PAGE 2: AI E-COMMERCE CONTENT HUB
# =====================================================================
elif current_page == "🛍️ AI E-Commerce Content Hub":
    st.title("🛍️ AI E-Commerce Content Hub")
    uploaded_file = st.file_uploader("Upload product photo:", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        if st.button("Generate Assets"):
            # Your API logic remains here...
            st.success("Assets generated!")

# =====================================================================
# PAGE 3: CINEMATIC STORYBOARD ARCHITECT
# =====================================================================
elif current_page == "🎬 Cinematic Storyboard Architect":
    st.title("🎬 Cinematic Storyboard Architect")
    user_concept = st.text_area("Enter concept:")
    if st.button("Generate"):
        # Your API logic remains here...
        st.success("Storyboard ready!")

# =====================================================================
# 4. VOICEFLOW WIDGET
# =====================================================================
voiceflow_widget_html = """
<script type="text/javascript">
  (function(d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function() {
        window.parent.voiceflow.chat.load({
          verify: { projectID: '6a25a7ff2d3a498b7f05ef64' },
          url: 'https://general-runtime.voiceflow.com',
          render: { mode: 'overlay' }
        });
      }
      v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
  })(window.parent.document, 'script');
</script>
"""
components.html(voiceflow_widget_html, height=0, width=0)