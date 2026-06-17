import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# 1. PAGE CONFIG
st.set_page_config(page_title="Ibrahim | Solutions", layout="wide", initial_sidebar_state="expanded")

# 2. NAVIGATION SIDEBAR
st.sidebar.title("✨ Workspace Menu")
current_page = st.sidebar.radio(
    "Select Application Window:",
    ["🏠 Creative Portfolio Showcase", "🛍️ AI E-Commerce Content Hub", "🎬 Cinematic Storyboard Architect"]
)

# 3. PAGE CONTENT
if current_page == "🏠 Creative Portfolio Showcase":
    st.title("Ibrahim")
    st.subheader("Complete Solutions Center")
    
    # Simple, stable card rendering
    st.markdown("""
        ### 📸 Product Photography
        High-end commercial & luxury product shots.
        ---
        ### 🛒 Salla Store Setup
        Professional end-to-end e-commerce configurations.
        ---
        ### 🎨 Poster Design
        Dynamic, premium social media posters.
    """)
    st.link_button("💬 Chat on WhatsApp", "https://wa.me/966534657849")

# ... (Rest of your tool pages would follow here)

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