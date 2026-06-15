import streamlit as st
from google import genai
from google.genai import types
import streamlit.components.v1 as components

# =====================================================================
# 1. GLOBAL PAGE CONFIG & LUXURY STYLING
# =====================================================================
st.set_page_config(page_title="Ibrahim | Complete Solutions Center", page_icon="✨", layout="centered")

# Inject your signature dark luxury theme styling directly into Streamlit
st.markdown("""
    <style>
        /* Main page background tracking */
        .stApp {
            background-color: #0b0c10;
            color: #e5e7eb;
        }
        
        /* Premium Card Layout structures */
        .custom-card {
            background-color: #12141c;
            border: 1px solid rgba(0, 229, 147, 0.2);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .custom-card:hover {
            border-color: #00e593;
            transform: translateY(-4px);
        }
        
        /* Text Color overrides */
        h1, h2, h3 {
            color: #ffffff !important;
            font-family: 'Segoe UI', Roboto, sans-serif;
        }
        p {
            color: #9ca3af !important;
        }
        
        /* WhatsApp Button Custom Styling */
        .whatsapp-wrapper {
            display: flex;
            justify-content: center;
            margin-top: 1.5rem;
        }
        .whatsapp-btn {
            background-color: #25D366;
            color: white !important;
            text-decoration: none;
            padding: 0.8rem 2rem;
            border-radius: 30px;
            font-weight: 600;
            font-size: 1.05rem;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
            transition: transform 0.3s;
        }
        .whatsapp-btn:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.5);
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. NAVIGATION SIDEBAR MENU
# =====================================================================
st.sidebar.title("✨ Workspace Menu")
st.sidebar.write("Navigate between my background showcase and live AI production suites.")

# The master selector tab mechanism
current_page = st.sidebar.radio(
    "Select Application Window:",
    ["🏠 Creative Portfolio Showcase", "🛍️ AI E-Commerce Content Hub", "🎬 Cinematic Storyboard Architect"]
)

st.sidebar.markdown("---")
st.sidebar.write("🔒 *Security Status: Server-Secured Key Active*")

# =====================================================================
# PAGE 1: CREATIVE PORTFOLIO SHOWCASE
# =====================================================================
if current_page == "🏠 Creative Portfolio Showcase":
    st.markdown("<h1 style='text-align: center;'>Ibrahim</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Complete Solutions Center | Salla Stores • Photography • Design</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Displaying your services in your card structure layout
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
        
        <div class="whatsapp-wrapper">
            <a href="https://wa.me/966534657849" target="_blank" class="whatsapp-btn">
                <span>💬 Chat on WhatsApp</span>
            </a>
        </div>
    """, unsafe_allow_html=True)

# =====================================================================
# PAGE 2: AI E-COMMERCE CONTENT HUB
# =====================================================================
elif current_page == "🛍️ AI E-Commerce Content Hub":
    st.title("🛍️ AI E-Commerce Content Hub")
    st.subheader("Instant Bilingual Product Descriptions & SEO Architect")
    st.write("Upload a product photograph to instantly generate premium high-converting copies, technical data grids, and optimized tags.")
    
    tone_choice = st.selectbox(
        "Select Tone of Voice",
        ["Luxury & Premium (Luxury, High-End)", "Casual & Friendly (Modern, Trendy)", "Technical & Explanatory (Detailed, Clear)"]
    )
    
    uploaded_file = st.file_uploader("Drag and drop your product image here (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Target Product Asset Loaded", use_container_width=True)
        image_bytes = uploaded_file.read()
        mime_type = uploaded_file.type
        
        if st.button("Generate E-Commerce Assets"):
            with st.spinner("Analyzing product aesthetics and formulating copy structures..."):
                try:
                    secure_api_key = st.secrets["GEMINI_API_KEY"]
                    client = genai.Client(api_key=secure_api_key)
                    
                    system_instruction = (
                        f"You are a master E-Commerce Copywriter and SEO expert who understands retail platforms like Salla. "
                        f"Analyze the uploaded product image. Your task is to generate premium, high-converting content written in the tone: '{tone_choice}'.\n\n"
                        f"Structure your entire output beautifully using standard Markdown. Include sections for:\n"
                        f"1. 📝 MARKETING COPY (Bilingual narrative, features, hooks in English and Arabic).\n"
                        f"2. 📊 TECHNICAL SPECIFICATIONS (Clean data table listing colors, materials, design properties).\n"
                        f"3. 🔍 SEO SPECIFICATIONS (High-traffic search terms, keywords, platform tags)."
                    )
                    
                    image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image_part],
                        config=types.GenerateContentConfig(system_instruction=system_instruction),
                    )
                    st.markdown("---")
                    st.subheader("📋 Generated Product Content Package")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"System compilation error: {e}")

# =====================================================================
# PAGE 3: CINEMATIC STORYBOARD ARCHITECT
# =====================================================================
elif current_page == "🎬 Cinematic Storyboard Architect":
    st.title("🎬 Cinematic Storyboard & Video Prompt Architect")
    st.subheader("Transform Raw Concepts into Production-Ready AI Video Scripts")
    st.write("Type a brief advertising concept below to unlock detailed scene storyboards and camera settings.")
    
    user_concept = st.text_area(
        "Enter your rough commercial concept or fragrance notes:",
        placeholder="Example: A luxury perfume bottle sitting on a dark volcanic rock, high-end dramatic lighting."
    )
    
    if st.button("Generate Director's Storyboard"):
        if not user_concept.strip():
            st.warning("Please type a concept idea first!")
        else:
            with st.spinner("Deconstructing concept aesthetics..."):
                try:
                    secure_api_key = st.secrets["GEMINI_API_KEY"]
                    client = genai.Client(api_key=secure_api_key)
                    
                    system_instruction = (
                        "You are an elite commercial video director and expert prompt engineer for AI video tools like Kling or Runway. "
                        "Expand the user's concept into a structured, 3-scene cinematic storyboard. "
                        "For EACH scene, format exactly with markdown headers detailing visual sequences in English/Arabic, camera movements, lighting, and an optimized English AI Video Prompt string."
                    )
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[user_concept],
                        config=types.GenerateContentConfig(system_instruction=system_instruction),
                    )
                    st.markdown("---")
                    st.subheader("📋 Production Storyboard Blueprint")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"System compilation error: {e}")

# =====================================================================
# 4. GLOBAL FLOATING VOICEFLOW AI CHAT WIDGET
# =====================================================================
# Using window.parent forces the widget to break out of its container frame and render globally
voiceflow_widget_html = """
<script type="text/javascript">
  (function(d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function() {
        window.parent.voiceflow.chat.load({
          verify: { projectID: '6a25a7ff2d3a498b7f05ef64' },
          url: 'https://general-runtime.voiceflow.com',
          voice: {
            url: "https://runtime-api.voiceflow.com"
          }
        });
      }
      v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
  })(window.parent.document, 'script');
</script>
"""
components.html(voiceflow_widget_html, height=0, width=0)