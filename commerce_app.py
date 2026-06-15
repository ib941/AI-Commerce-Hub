import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration & Styling (Clean & Premium Layout)
st.set_page_config(page_title="AI E-Commerce Content Hub", page_icon="🛍️", layout="centered")

st.title("🛍️ AI E-Commerce Content Hub")
st.subheader("Instant Bilingual Product Descriptions & SEO Architect")
st.write("Upload a product photograph to instantly generate premium high-converting copies, technical data grids, and optimized tags.")

# 2. Sleek Sidebar Controls (No API Key inputs needed on frontend!)
st.sidebar.header("Content Controls")
tone_choice = st.sidebar.selectbox(
    "Select Tone of Voice",
    ["Luxury & Premium (Luxury, High-End)", "Casual & Friendly (Modern, Trendy)", "Technical & Explanatory (Detailed, Clear)"]
)

st.sidebar.markdown("---")
st.sidebar.write("🔒 *Security Status: Server-Secured Key Active*")

# 3. Main Dashboard File Uploader
uploaded_file = st.file_uploader("Drag and drop your product image here (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Render a clean image preview for the merchant user
    st.image(uploaded_file, caption="Target Product Asset Loaded", use_container_width=True)
    
    # Read image into raw binary packets
    image_bytes = uploaded_file.read()
    mime_type = uploaded_file.type
    
    # Generation Action Trigger Button
    if st.button("Generate E-Commerce Assets"):
        with st.spinner("Analyzing product aesthetics and formulating copy structures..."):
            try:
                # Silently pull the credential directly out of your local private background vault
                secure_api_key = st.secrets["GEMINI_API_KEY"]
                
                # Initialize the official client layout
                client = genai.Client(api_key=secure_api_key)
                
                # Custom bilingual architecture instructions
                system_instruction = (
                    f"You are a master E-Commerce Copywriter and SEO expert who understands retail platforms like Salla. "
                    f"Analyze the uploaded product image. Your task is to generate premium, high-converting content "
                    f"written in the following tone: '{tone_choice}'.\n\n"
                    f"Structure your entire output beautifully using standard Markdown. Include the following sections clearly labeled:\n"
                    f"1. 📝 MARKETING COPY (Write a compelling product narrative, features, and emotional hooks in both professional English and Arabic).\n"
                    f"2. 📊 TECHNICAL SPECIFICATIONS (Create a clean Markdown data table with columns for Feature, Detail, and Notes listing colors, materials, and design properties in both languages).\n"
                    f"3. 🔍 SEO SPECIFICATIONS (List high-traffic search terms, keywords, and platform tags optimized for search discoverability)."
                )
                
                # Package image bytes natively
                image_part = types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type
                )
                
                # Request generation from the stable 2.5 Flash model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_part],
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction
                    ),
                )
                
                # 4. Clean Layout Presentation
                st.markdown("---")
                st.subheader("📋 Generated Product Content Package")
                
                # Print out the beautifully formatted markdown response natively
                st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"System compilation error: {e}")