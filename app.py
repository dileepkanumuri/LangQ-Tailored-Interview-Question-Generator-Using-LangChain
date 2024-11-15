import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import streamlit as st
from langchain.llms import OpenAI
from src.helper import llm_pipeline  # Importing llm_pipeline from src.helper

# Load environment variables (like OpenAI API key)
load_dotenv()

# Initialize OpenAI API using only the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API key not found. Please set it in the .env file.")

# Directory for uploaded files
UPLOAD_DIRECTORY = "uploads"
Path(UPLOAD_DIRECTORY).mkdir(exist_ok=True)

def generate_qa(file_path):
    # Generate questions and answers using the llm_pipeline from helper.py
    answer_generation_chain, ques_list = llm_pipeline(file_path)
    qa_list = []

    for question in ques_list:
        answer = answer_generation_chain.run(question)
        qa_list.append({"question": question, "answer": answer})

    return qa_list

# Apply custom CSS for enhanced styling with adjustments for title placement and spacing
st.markdown("""
    <style>
    /* General Background */
    .main {
        background-color: #2D2F33;
        color: #E0E0E0;
        font-family: Arial, sans-serif;
    }
    
    /* Title Styling */
    .title-container {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: #FFA500;
        margin-top: 10px;
        margin-bottom: 20px;
        white-space: nowrap;
    }

    /* Author Styling */
    .author-container {
        text-align: center;
        font-size: 1rem;
        color: #c89574;
        font-style: italic;
        margin-bottom: 51px;
    }
    
    /* Description Styling */
    .description {
        text-align: center;
        color: #D3D3D3;
        font-size: 1rem;
        margin-bottom: 70px;
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #005500;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #006400;
    }
    
    /* File Uploader Styling */
    .stFileUploader>div {
        background-color: #424549;
        padding: 10px;
        border-radius: 5px;
    }
    
    /* Q&A Section */
    .qa-section {
        background-color: #3E4147;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #5A5C60;
        margin-bottom: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .question {
        font-weight: bold;
        font-size: 1.1rem;
        color: #FFA500;
    }
    .answer {
        font-style: italic;
        color: #D3D3D3;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI Setup
st.markdown("<div class='title-container'>📚 LangQ: Your AI-Powered Interview Prep Curator</div>", unsafe_allow_html=True)

# Author names in italic, light yellow color
st.markdown("<div class='author-container'>By Dileep Kanumuri, Saranya Gopireddy, Satwik Dikkala</div>", unsafe_allow_html=True)

# Header Description with complementary color and centered alignment, with spacing adjusted
st.markdown(
    "<div class='description'>"
    "Upload your study materials, documentation, cheat sheets, or any text-based PDF files to automatically generate interview-style questions and answers. "
    "Powered by OpenAI’s advanced language model, this app provides insightful Q&A pairs to help you prepare with ease and precision."
    "</div>", 
    unsafe_allow_html=True
)

# Create columns for layout with a centered image for visual balance
col1, col2 = st.columns([2, 1])

with col1:
    # File Upload Section
    uploaded_file = st.file_uploader("Upload your PDF file here", type=["pdf"])

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/61/61456.png", width=80)  # Replace with a relevant icon

if uploaded_file:
    # Save the uploaded PDF file to the uploads directory
    file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
    with open(file_path, "wb") as file:
        shutil.copyfileobj(uploaded_file, file)

    # Display the PDF file name
    st.success(f"**Uploaded File:** {uploaded_file.name}", icon="📄")

    # Generate Q&A button with spinner and updated styling
    if st.button("Generate Q&A"):
        try:
            with st.spinner("Generating Q&A... Please wait."):
                # Generate Q&A list from the PDF file
                qa_list = generate_qa(file_path)

            # Display Q&A pairs on the page
            st.write("### Generated Q&A")
            for i, qa in enumerate(qa_list, start=1):
                with st.expander(f"Question {i}", expanded=True):
                    st.markdown(f"<div class='qa-section'><div class='question'>Q: {qa['question']}</div><div class='answer'>A: {qa['answer']}</div></div>", unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"Error generating Q&A: {str(e)}")
