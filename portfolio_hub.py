import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# 1. CORE CONFIG & WATERMARK REMOVAL
st.set_page_config(page_title="Ibrahim | Solutions", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        #MainMenu, footer, header { visibility: hidden !important; }
        .stApp { background-color: #0b0c10; color: #e5e7eb; }
        .custom-card { background-color: #12141c; border: 1px solid rgba(0, 229, 147, 0.2); border-radius: 16px; padding: 25px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. SIDEBAR NAVIGATION
st.sidebar.title("✨ Workspace Menu")
page = st.sidebar.radio("Navigate:", ["🏠 Portfolio", "🛍️ E-Commerce Hub", "🎬 Storyboard Architect"])

# 3. PAGE CONTENT
if page == "🏠 Portfolio":
    st.title("Ibrahim | Complete Solutions Center")
    st.markdown("""
        <div class="custom-card"><h3>📸 Product Photography</h3><p>High-end commercial & luxury product shots.</p></div>
        <div class="custom-card"><h3>🛒 Salla Store Setup</h3><p>Professional end-to-end e-commerce configurations.</p></div>
        <div class="custom-card"><h3>🎨 Poster Design</h3><p>Dynamic, premium social media posters.</p></div>
    """, unsafe_allow_html=True)
    st.link_button("💬 Chat on WhatsApp", "https://wa.me/966534657849")

elif page == "🛍️ E-Commerce Hub":
    st.title("🛍️ AI E-Commerce Content Hub")
    st.write("Upload your product photo below to generate assets.")
    uploaded_file = st.file_uploader("Product Image", type=["jpg", "png"])
    if uploaded_file: st.image(uploaded_file)

elif page == "🎬 Storyboard Architect":
    st.title("🎬 Cinematic Storyboard Architect")
    concept = st.text_area("Enter your ad concept:")
    if st.button("Generate"): st.write("Generating your storyboard...")

# 4. VOICEFLOW WIDGET
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