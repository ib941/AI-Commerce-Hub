import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# 1. CORE SETUP
st.set_page_config(page_title="Ibrahim | Solutions", layout="centered")

# Basic styling for luxury theme
st.markdown("""
    <style>
        .stApp { background-color: #0b0c10; color: #e5e7eb; }
        .custom-card {
            background-color: #12141c; border: 1px solid rgba(0, 229, 147, 0.2);
            border-radius: 16px; padding: 20px; margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# 2. SIDEBAR
st.sidebar.title("✨ Workspace Menu")
current_page = st.sidebar.radio(
    "Navigate:",
    ["🏠 Creative Portfolio Showcase", "🛍️ AI E-Commerce Content Hub", "🎬 Cinematic Storyboard Architect"]
)

# 3. PAGE LOGIC
if current_page == "🏠 Creative Portfolio Showcase":
    st.title("Ibrahim")
    st.subheader("Complete Solutions Center")
    
    # These three are now explicitly rendered together
    st.markdown("""
        <div class="custom-card"><h3>📸 Product Photography</h3><p>High-end commercial & luxury product shots.</p></div>
        <div class="custom-card"><h3>🛒 Salla Store Setup</h3><p>Professional end-to-end e-commerce configurations.</p></div>
        <div class="custom-card"><h3>🎨 Poster Design</h3><p>Dynamic, premium social media posters.</p></div>
    """, unsafe_allow_html=True)
    st.link_button("💬 Chat on WhatsApp", "https://wa.me/966534657849")

elif current_page == "🛍️ AI E-Commerce Content Hub":
    st.title("🛍️ AI E-Commerce Content Hub")
    # Add your logic back here in a clean way...

elif current_page == "🎬 Cinematic Storyboard Architect":
    st.title("🎬 Cinematic Storyboard Architect")
    # Add your logic back here in a clean way...

# 4. WIDGET
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