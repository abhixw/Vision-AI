import streamlit as st
from main import generate_caption

st.set_page_config(page_title="Image → Text (Groq)", layout="centered")

# 🎨 Half Blue / Half Green Button
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #1e90ff 0%, #1e90ff 50%, #1e90ff 50%, #1e90ff 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 1.4rem;
    font-weight: 600;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #2aa4ff 0%, #2aa4ff 50%, #38d17a 50%, #38d17a 100%);
}
</style>
""", unsafe_allow_html=True)

st.title("🖼️ Image to Text ")
st.write("Paste an image URL and get an AI-generated description.")

image_url = st.text_input("Enter Image URL")

if image_url:
    st.image(image_url, width=700)

if st.button("Generate Description"):
    if not image_url:
        st.warning("Please enter an image URL")
    else:
        with st.spinner("Analyzing image..."):
            try:
                caption = generate_caption(image_url)
                st.success("Result")
                st.write(caption)
            except Exception as e:
                st.error(str(e))
