import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# =====================================================================
# 1. PAGE CONFIG & STYLING
# =====================================================================
st.set_page_config(page_title="Ibrahim | Solutions", layout="wide", initial_sidebar_state="expanded")

# Master CSS: Force mobile sidebar, hide watermarks, style buttons
st.markdown("""
    <style>
        /* Force Sidebar Visibility */
        [data-testid="stSidebar"] { display: block !important; }
        section[data-testid="stSidebar"] { z-index: 9999 !important; }
        
        /* Clean Branding */
        #MainMenu, footer, header { visibility: hidden !important; }
        div[data-testid="stDecoration"] { display: none !important; }
        
        /* Layout */
        .stApp { background-color: #0b0c10; color: #e5e7eb; }
        .custom-card {
            background-color: #12141c; border: 1px solid rgba(0, 229, 147, 0.2);
            border-radius: 16px; padding: 25px; margin-bottom: 20px;
        }
        
        /* WhatsApp Button Motion */
        .whatsapp-btn {
            background-color: #25D366; color: white !important;
            padding: 12px 30px; border-radius: 30px; font-weight: 700;
            display: inline-block; text-decoration: none;
            transition: all 0.3s ease;
        }
        .whatsapp-btn:hover { transform: scale(1.05); box-shadow: 0 0 15px #25D366; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. SIDEBAR (The Single Source of Truth)
# =====================================================================
st.sidebar.title("✨ Workspace Menu")
current_page = st.sidebar.radio(
    "Select Application Window:",
    ["🏠 Creative Portfolio Showcase", "🛍️ AI E-Commerce Content Hub", "🎬 Cinematic Storyboard Architect"]
)

# =====================================================================
# 3. PAGES
# =====================================================================
if current_page == "🏠 Creative Portfolio Showcase":
    st.title("Ibrahim")
    st.subheader("Complete Solutions Center")
    
    st.markdown("""
        <div class="custom-card">
            <h3>📸 Product Photography</h3>
            <p>High-end commercial & luxury product shots.</p>
        </div>
        <a href="https://wa.me/966534657849" target="_blank" class="whatsapp-btn">💬 Chat on WhatsApp</a>
    """, unsafe_allow_html=True)

elif current_page == "🛍️ AI E-Commerce Content Hub":
    st.title("🛍️ AI E-Commerce Content Hub")
    # ... your existing logic here ...

elif current_page == "🎬 Cinematic Storyboard Architect":
    st.title("🎬 Cinematic Storyboard Architect")
    # ... your existing logic here ...

# =====================================================================
# 4. WIDGET
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