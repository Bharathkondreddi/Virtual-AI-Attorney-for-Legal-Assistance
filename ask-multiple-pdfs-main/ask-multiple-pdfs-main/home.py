# home.py
import streamlit as st
import os
import numpy as np
import pandas as pd
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email, message):
    """Send email using webhook service - REPLACE URL WITH YOUR FORMSPREE ENDPOINT"""
    try:
        import requests
        
        # STEP 1: Go to https://formspree.io and create a free account
        # STEP 2: Create a new form with target email: bk2982689@gmail.com  
        # STEP 3: Replace this URL with your actual Formspree endpoint
        formspree_url = "https://formspree.io/f/YOUR_FORM_ID"  # ⚠️ REPLACE THIS
        
        data = {
            "name": name,
            "email": email, 
            "message": message,
            "_replyto": email,
            "_subject": f"AI Attorney Contact: {name}",
        }
        
        # Try to send via Formspree
        response = requests.post(formspree_url, data=data, timeout=10)
        
        if response.status_code == 200:
            return "success"
        else:
            return "fallback"
            
    except Exception as e:
        return "fallback"  # Always fallback on error

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

def home_page():
    st.title("AI Attorney")
    st.markdown("Transforming the Legal Industry with AI")
    st.caption("AI Attorney is a cutting-edge legal technology firm revolutionizing the legal industry with advanced artificial intelligence solutions. We provide clients with efficient, accurate, and cost-effective legal services, powered by state-of-the-art AI algorithms and expert legal insights, ensuring seamless and precise legal support.")
    
    # Main image
    safe_image_display("AiLaw.jpeg", "AI Attorney - Revolutionizing Legal Services with AI")

    st.markdown(
    "AI Attorney is at the forefront of revolutionizing the legal industry by harnessing the power of artificial intelligence. "
    "Our commitment is to provide innovative and efficient solutions that transform traditional legal processes. "
    "With cutting-edge AI algorithms and expert legal insights, we strive to deliver accurate and cost-effective legal services to our clients."
    )

    st.markdown(
        "Our team of dedicated professionals is passionate about leveraging technology to address the complexities of the legal landscape. "
        "We believe in the seamless integration of AI into legal workflows, empowering legal professionals and organizations to work smarter and achieve better outcomes."
    )

    st.markdown(
        "At AI Attorney, we constantly push the boundaries of what AI can achieve in the legal domain. Our mission is to redefine how legal services are delivered, making them more accessible, precise, and adaptable to the evolving needs of our clients."
    )

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    st.header("OBJECTIVE")
    col1, col2 = st.columns(2)
    with col1:
        safe_image_display("law 2.png", "Legal Technology Innovation")
    with col2:
        st.write("""The objective of this presentation is to demonstrate the groundbreaking 
                capabilities and significant contributions of Ai Attorney, an advanced AI powered system, in revolutionizing legal research. Through its utilization of 
                cutting-edge Natural Language Processing (NLP) algorithms, Ai Attorney offers 
                users precise and pertinent legal materials based on input scenarios or case PDF 
                files. This presentation aims to highlight the system's meticulous keyword 
                extraction process, its ability to swiftly analyze and recognize relevant legal 
                sections within uploaded case files, and its ongoing enhancement through user 
                interactions. The presentation seeks to underscore how Ai Attorney substantially 
                improves the efficiency and accuracy of legal research, outperforming 
                conventional tools.""")


    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.header("Motivation: Revolutionizing Legal Assistance with AI")
    st.write("""Welcome to AI Attorney, where cutting-edge artificial intelligence meets legal documentation!
        Our motivation stems from a deep commitment to making legal processes more accessible, efficient, 
        and user-friendly. Here's why AI Attorney is poised to revolutionize the legal assistance landscape:""")
    
    st.markdown("""

        ### Bridging the Gap
        Legal documents can be complex and intimidating, often creating a significant barrier 
        between individuals and their understanding of legal matters. AI Attorney bridges this gap by 
        providing an intuitive platform where users can ask questions about their documents in plain language.

        ### Empowering Users
        We believe that everyone has the right to comprehend and engage with legal documents that concern them.
        AI Attorney empowers users by offering a conversational interface, enabling them to seek clarification, 
        explanations, and guidance on legal jargon, contracts, and other legal texts.

        ### Enhancing Efficiency
        Traditional legal processes can be time-consuming. AI Attorney streamlines the document review 
        and understanding process, offering quick and accurate responses to user queries. This efficiency 
        ensures that users can make informed decisions promptly.

        ### Leveraging Advanced AI Technology
        AI Attorney leverages state-of-the-art natural language processing and conversational AI models. 
        Our technology can understand and respond to a wide range of legal questions, providing users with 
        valuable insights and information.

        ### Continuous Improvement
        We are committed to constant improvement. AI Attorney's AI models learn and adapt over time, 
        ensuring that the platform evolves to meet the diverse and dynamic needs of its users.

        Explore AI Attorney and experience the future of legal assistance – where technology meets 
        accessibility, empowering individuals to navigate legal complexities with confidence.

        Remember, AI Attorney is here to assist, simplify, and make legal matters more understandable for everyone.
    """)

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    st.subheader("Team Members")
    col1, col2, col3 = st.columns(3)

    with col1:
        safe_image_display("RamaTulasi.jpg", "RAMA TULASI")
        st.subheader("RAMA TULASI")
        st.write("`Assistant Professor at VIT-AP University`")
    
    with col2:
        safe_image_display("Bharath.jpg", "BHARATH KUMAR")
        st.subheader("BHARATH KUMAR")
        st.write("`CSE`")

    with col3:
        safe_image_display("shailendra.jpg", "SHAILENDRA")
        st.subheader("SHAILENDRA")
        st.write("`CSE`")

    with col1:
        safe_image_display("Sai Ram.jpg", "SAI RAM")
        st.subheader("SAI RAM")
        st.write("`CSE`")

    # with col2:
    #     st.image(r"C:\Users\hp\Downloads\AI-Attorney-Using-LangChain-main\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\sreeven.png")
    #     st.subheader("N")
    #     st.write("`CSE (Spec. in Artificial Intelligence)`")

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    
    st.subheader("Current Location")

    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [16.4942796, 80.5007368],
    columns=['lat', 'lon'])

    st.map(df)


    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")


    st.header(":mailbox: Get In Touch With Me!")
    
    # Professional contact form with multiple contact options
    with st.form("contact_form"):
        st.write("Send me a message and I'll get back to you:")
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        message = st.text_area("Your Message", placeholder="Enter your message here...", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                with st.spinner("Sending your message..."):
                    result = send_email(name, email, message)
                    
                    if result == "success":
                        st.success("✅ Your message has been sent successfully!")
                        st.balloons()
                        st.info("📧 I'll get back to you as soon as possible.")
                    else:
                        # Show multiple contact options
                        st.warning("📧 Please use one of these methods to contact me:")
                        
                        # Method 1: Email
                        import urllib.parse
                        subject = f"AI Attorney Contact - {name}"
                        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                        mailto_link = f"mailto:bk2982689@gmail.com?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown(f'<a href="{mailto_link}" target="_blank" style="background-color: #ff6b6b; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; display: inline-block; width: 100%; text-align: center;">📧 Email Me</a>', unsafe_allow_html=True)
                        
                        with col2:
                            # WhatsApp
                            whatsapp_message = f"Hi! I'm {name} ({email}). {message}"
                            whatsapp_link = f"https://wa.me/919876543210?text={urllib.parse.quote(whatsapp_message)}"
                            st.markdown(f'<a href="{whatsapp_link}" target="_blank" style="background-color: #25D366; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; display: inline-block; width: 100%; text-align: center;">📱 WhatsApp</a>', unsafe_allow_html=True)
                        
                        with col3:
                            # LinkedIn or Phone
                            st.markdown('<div style="background-color: #0077B5; color: white; padding: 10px 15px; border-radius: 5px; text-align: center;">📞 Call Me<br>+91 98765 43210</div>', unsafe_allow_html=True)
                        
                        st.write("")
                        st.info("📋 **Copy this message:**")
                        st.code(f"To: bk2982689@gmail.com\nSubject: {subject}\n\n{body}")
            else:
                st.error("❌ Please fill in all fields!")
    
    # Quick contact info
    st.write("---")
    st.subheader("📞 Direct Contact Information")
    col1, col2 = st.columns(2)
    with col1:
        st.info("� **Email:**\nbk2982689@gmail.com")
    with col2:
        st.info("📱 **Phone/WhatsApp:**\n+91 98765 43210")

    st.write("---")

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css(r"C:\Users\hp\Downloads\AI-Attorney-Using-LangChain-main\ask-multiple-pdfs-main\style\style.css")



