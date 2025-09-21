import streamlit as st
import os

st.title("Image Test")

# Test if images folder exists
st.write("Testing image folder access...")
if os.path.exists("images"):
    st.success("Images folder exists!")
    files = os.listdir("images")
    st.write("Files in images folder:")
    for file in files:
        st.write(f"- {file}")
        
    st.write("\nTesting specific images:")
    
    # Test key images
    test_images = [
        "images/AiLaw.jpeg",
        "images/law 2.png", 
        "images/Bharath.jpg",
        "images/Sai Ram.jpg",
        "images/RamaTulasi.jpg",
        "images/shailendra.jpg",
        "images/ailogo.png",
        "images/about.png"
    ]
    
    for img_path in test_images:
        st.write(f"\nTesting: {img_path}")
        try:
            if os.path.exists(img_path):
                st.image(img_path, caption=f"✅ {img_path}")
            else:
                st.error(f"❌ File not found: {img_path}")
        except Exception as e:
            st.error(f"❌ Error loading {img_path}: {str(e)}")
            
else:
    st.error("Images folder not found!")