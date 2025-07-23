import streamlit as st
import numpy as np
from PIL import Image
import io
from utils.sharpen import sharpen_image
from utils.background import remove_bg_and_apply_backgrounds
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Blur2Sharp", layout="centered")

# Theme toggle (requires streamlit-extras)
theme = st.radio("Choose Theme", ["Light", "Dark"], horizontal=True)
if theme == "Dark":
    st.markdown(
        """
        <style>
        body, .stApp { background-color: #0e1117; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("🔍 Blur2Sharp - Image Enhancer")

# Sidebar
st.sidebar.header("🧰 Settings")
intensity = st.sidebar.slider("Sharpening Intensity", 0.1, 3.0, 1.0, 0.1)
bg_option = st.sidebar.checkbox("Apply Backgrounds", value=True)

# Upload image
uploaded_file = st.file_uploader("Upload a blurry image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    # Sharpen image
    sharpened = sharpen_image(np.array(image), intensity)
    sharpened_pil = Image.fromarray(sharpened)

    # Show comparison
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original", use_column_width=True)
    with col2:
        st.image(sharpened_pil, caption="Sharpened", use_column_width=True)

    # Download Only Sharpened Image
    img_bytes = io.BytesIO()
    sharpened_pil.save(img_bytes, format="PNG")
    st.download_button("📥 Download Only Sharpened Image", data=img_bytes.getvalue(),
                       file_name="sharpened.png", mime="image/png")

    # Background Replacement
    if bg_option:
        st.subheader("🔄 Preview with Backgrounds")
        bg_outputs = remove_bg_and_apply_backgrounds(sharpened_pil)
        for idx, img in enumerate(bg_outputs):
            st.image(img, caption=f"Background {idx+1}", use_column_width=True)

    # Reset Button
    if st.button("🔄 Reset"):
        st.experimental_rerun()
else:
    st.info("👆 Upload a blurry image to begin.")

