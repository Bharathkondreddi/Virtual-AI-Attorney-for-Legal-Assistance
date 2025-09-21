import streamlit as st
import time
import os
from pathlib import Path

def get_image_path(image_name):
    """Get the correct image path for both local and deployment environments"""
    # Try different possible paths
    possible_paths = [
        f"images/{image_name}",  # Relative path
        f"./images/{image_name}",  # Current directory relative
        f"{os.getcwd()}/images/{image_name}",  # Absolute from current working directory
        f"ask-multiple-pdfs-main/ask-multiple-pdfs-main/images/{image_name}",  # Full relative path
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # If no path works, return the standard relative path
    return f"images/{image_name}"

def safe_image_display(image_name, caption="", width=None):
    """Safely display images with proper path resolution"""
    image_path = get_image_path(image_name)
    
    try:
        if width:
            st.image(image_path, caption=caption, width=width)
        else:
            st.image(image_path, caption=caption)
        return True
    except Exception as e:
        # Fallback: try with different encodings or display error info
        st.error(f"Could not load image: {image_name}")
        st.info(f"Path attempted: {image_path}")
        return False

def fade_in_animation(element, duration=0.5):
    st.markdown(
        f"""
        <style>
            @keyframes fade-in {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            {element} {{
                animation: fade-in {duration}s ease-in-out;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def about_page():
    st.title("About AI Attorney")
    st.subheader("Empowering Legal Excellence Through AI")
    
    col1, col2 = st.columns(2)
    with col2:
        safe_image_display("ailogo.png", "AI Attorney Logo")
    with col1:
        st.text(" ")
        st.text(" ")
        st.write("At AI Attorney, we are at the forefront of the legal technology revolution. Our mission is to empower legal professionals with cutting-edge AI solutions that redefine the practice of law. With a relentless commitment to innovation, we have developed a suite of services designed to enhance the legal industry's efficiency, accuracy, and client service. Here's what sets us apart:")
    st.write(" Expertise: Our team combines legal expertise with AI prowess to create solutions that truly understand the intricacies of the law.")
    st.write(" Innovation: We constantly push boundaries, developing custom AI tools that adapt to the ever-changing legal landscape.")
    st.write(" Efficiency: AI Attorney's solutions streamline legal processes, allowing you to focus on what matters most – your clients.")
    st.write(" Accuracy: Our AI algorithms deliver unparalleled precision in legal research, analysis, and document review.")
    st.write(" Client-Centric: We prioritize your success, aiming to elevate your practice to new heights while ensuring your clients receive top-notch service.")
    st.write("Join AI Attorney on the journey to redefine legal excellence in the digital age.")
    safe_image_display("about.png", "About AI Attorney")

    st.header("Product Features")
    st.markdown("AI Attorney stands as a pioneering force in the legal technology landscape, harnessing the power of Artificial Intelligence (AI) and Natural Language Processing (NLP) techniques to revolutionize legal research. Here are the key features that set AI Attorney apart")
    col1, col2 = st.columns(2)
    with col2:
        safe_image_display("img-1.png", "NLP Technology")
    with col1:
        st.subheader("Cutting-Edge NLP Technology")
        st.markdown(
            """
            - Utilizes advanced NLP algorithms for precise legal document analysis.
            - Ensures accurate keyword extraction, improving the relevance of search results.
            - Integrates the powerful Natural Language Toolkit (NLTK) library for robust language processing.
            - Enhances legal research efficiency with AI-driven language understanding.
            """
        )

    with col1:    
        safe_image_display("img-2.png")

    with col2:
        st.subheader("Scenario-Based Search")
        st.markdown(
            """
            - Empowers users to input specific legal scenarios for tailored research.
            - Aligns research outcomes with real-world legal situations.
            - Provides contextually relevant legal articles and sections.
            - Streamlines the process of finding pertinent legal information.
            """
        )

    with col2:
        safe_image_display("img-3.png")
    with col1:
        st.subheader("PDF File Analysis")
        st.markdown(
            """
            - Accelerates legal research by analyzing and interpreting case PDF files.
            - Intelligently identifies act names and relevant sections within uploaded documents.
            - Significantly reduces manual effort in reviewing case materials.
            - Enhances productivity for legal experts dealing with extensive case files.
            """
        )

    with col1:
        safe_image_display("img-4.png")
    with col2:
        st.subheader("Keyword Extraction Expertise")
        st.markdown(
            """
            - Meticulously crafted keyword extraction process for precision and relevance.
            - Guarantees contextually accurate and meaningful search results.
            - Improves the overall effectiveness of legal research.
            - Minimizes irrelevant content, saving users valuable time.
            """
        )

    with col2:
        safe_image_display("img-3.png", "Adaptive Learning Features")
    with col1:
        st.subheader("Adaptive Learning")
        st.markdown(
            """
            - Continuously refines keyword extraction based on user interactions.
            - Adapts to evolving legal language and terminology.
            - Ensures ongoing improvement in search accuracy.
            - Customizes results to match the evolving needs of legal professionals.
            """
        )

    with col1:
        safe_image_display("img-1.png", "Multilingual Translation")
    with col2:
        st.subheader("Multilingual Text Translation")
        st.markdown(
            """
            - Breaks language barriers by providing multilingual text translation.
            - Expands accessibility for legal professionals working in diverse linguistic contexts.
            - Enables seamless research in international legal scenarios.
            - Enhances collaboration and understanding in global legal environments.
            """
        )

    st.header(":mailbox: Get In Touch With Me!")
    
    # Streamlit-native contact form that works in deployment
    with st.form("contact_form_about"):
        st.write("Send me a message:")
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        message = st.text_area("Your Message", placeholder="Enter your message here...", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                # Create mailto link for email client
                import urllib.parse
                subject = f"Contact from AI Attorney - {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                mailto_link = f"mailto:bk2982689@gmail.com?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                
                st.success("✅ Thank you for your message!")
                st.info("📧 Click the link below to send your message:")
                st.markdown(f'<a href="{mailto_link}" target="_blank" style="background-color: #ff6b6b; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">📨 Send Email</a>', unsafe_allow_html=True)
                
                # Also show the message for copying
                st.write("**Or copy this message and send manually:**")
                st.code(f"To: bk2982689@gmail.com\nSubject: {subject}\n\n{body}")
            else:
                st.error("❌ Please fill in all fields!")

    st.write("---")

    # Use Local CSS File - commented out to avoid path issues on cloud deployment
    # def local_css(file_name):
    #     with open(file_name) as f:
    #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    # local_css("style/style.css")






 
 