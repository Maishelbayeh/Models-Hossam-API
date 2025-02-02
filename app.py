import os
import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume
# from career_model import CareerPathRecommender

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Career Path Recommendation System")

st.sidebar.header("Upload Your Resume")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    st.write("**Uploaded File:**", uploaded_file.name)
    
    try:
        # Parse the resume
        st.write("Parsing the resume...")
        resume_data = parse_resume(uploaded_file)
        st.write("### Extracted Resume Text:")
        st.text(resume_data)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF resume to get career path recommendations.")
