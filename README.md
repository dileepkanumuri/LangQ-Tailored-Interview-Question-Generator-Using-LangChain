# LangQ: Your AI-Powered Interview Prep Curator

**LangQ** is an end-to-end deployed AI-powered application designed to assist users in preparing for interviews by generating tailored questions and answers. 

Deployed & Live at [LangQ - LLM](https://langqllm.streamlit.app/), this app utilizes OpenAI’s language model with LangChain to analyze any PDF document (study materials, documentation, cheat sheets, etc.) and produce insightful Q&A pairs. Built on **Streamlit** for an interactive, user-friendly experience.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Methodology](#methodology)
- [Step-by-Step Project Implementation](#step-by-step-project-implementation)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Troubleshooting](#troubleshooting)

---

## Features
- **AI-Driven Q&A Generation**: Upload any PDF file, and LangQ will create interview-style questions and answers based on the content.
- **Streamlit Interface**: Responsive, user-friendly UI powered by Streamlit, featuring color themes and a clean layout.
- **PDF Upload and Processing**: Supports PDF uploads, analyzes content, and generates Q&A in real time.
- **Modular Codebase**: Designed with modularity, making it easy to extend and customize features.

---

## Demo
Here are some screenshots showcasing LangQ in action:

### Screenshot 1
![Screenshot 1](https://github.com/dileepkanumuri/LangQ-Tailored-Interview-Question-Generator-Using-LangChain/blob/main/Images/Screenshot%201.png)

### Screenshot 2
![Screenshot 2](https://github.com/dileepkanumuri/LangQ-Tailored-Interview-Question-Generator-Using-LangChain/blob/main/Images/Screenshot%202.png)

### Screenshot 3
![Screenshot 3](https://github.com/dileepkanumuri/LangQ-Tailored-Interview-Question-Generator-Using-LangChain/blob/main/Images/Screenshot%203.png)

---

## Tech Stack
This project uses the following technologies:

- **Python**: Core programming language for backend and data processing.
- **Streamlit**: Framework for building interactive and responsive web applications.
- **OpenAI GPT-3 (via LangChain)**: Language model API for generating questions and answers.
- **PyPDF2**: Library for reading and extracting text from PDF files.
- **dotenv**: For securely managing environment variables, such as API keys.
- **FAISS**: A library for efficient similarity search, used here via LangChain.

---

## Project Structure
The project is organized to maintain modularity and ease of maintenance.

```
LangQ-Tailored-Interview-Question-Generator-Using-LangChain/
├── .env                     # Environment variables (e.g., OpenAI API Key)
├── app.py                   # Main Streamlit app
├── requirements.txt         # Project dependencies
├── src/
│   └── helper.py            # Helper functions for Q&A generation
├── uploads/                 # Directory for storing uploaded PDF files
└── README.md                # Project documentation
```

---

## Setup and Installation
### Prerequisites
- **Python 3.8+**: Ensure you have Python installed on your machine.
- **OpenAI API Key**: You will need an OpenAI API key to enable AI-driven Q&A generation.

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dileepkanumuri/LangQ-Tailored-Interview-Question-Generator-Using-LangChain.git
   cd LangQ-Tailored-Interview-Question-Generator-Using-LangChain
   ```

2. **Set Up Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Use `requirements.txt` to install all necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API key as follows:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Application**:
   Start the Streamlit application using:
   ```bash
   streamlit run app.py
   ```

   The application should now be accessible on `http://localhost:8501`.

---

## Usage
1. **Open the Application**:
   - After running the app, go to `http://localhost:8501` in your browser.

2. **Upload a PDF Document**:
   - Use the file uploader in the app interface to upload any PDF file. Ensure the file size is under 200MB.

3. **Generate Q&A**:
   - Click on the "Generate Q&A" button to create a list of interview-style questions and answers based on the content of the uploaded PDF.

4. **View Results**:
   - The generated Q&A pairs will be displayed below, with questions in bold and answers in italicized text.

---

## Environment Variables
This project requires an `.env` file to store sensitive information securely. Create a `.env` file in the root directory of the project with the following:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

- **`OPENAI_API_KEY`**: Your API key for accessing OpenAI's language model. Sign up at [OpenAI](https://beta.openai.com/signup/) to get an API key.

---

## Methodology
1. **PDF Upload and Parsing**:
   - The user uploads a PDF document, which is saved in the `uploads/` directory.
   - The **PyPDF2** library reads and extracts the text from the PDF file.

2. **Question and Answer Generation**:
   - The extracted text is processed through LangChain, leveraging OpenAI's GPT-3 to generate interview-style questions.
   - For each generated question, LangChain produces a corresponding answer, forming a Q&A pair.

3. **Display and Interactivity**:
   - Streamlit dynamically displays the generated Q&A pairs in a visually appealing format.
   - Users can interact with the app, viewing each Q&A pair in an accordion-style layout.

---

## Step-by-Step Project Implementation

1. **PDF Text Extraction**: 
   - Use `PyPDF2` to read and extract raw text data from the uploaded PDF file.
   
2. **Q&A Generation Pipeline**:
   - Use `src/helper.py` where the function `llm_pipeline` utilizes the LangChain and OpenAI API to generate a list of questions based on the text content.
   - The function runs each question through the OpenAI model to generate answers.

3. **Display in Streamlit**:
   - In `app.py`, Streamlit is used to build the web interface, including the file upload widget, the "Generate Q&A" button, and the Q&A display area.
   - Custom CSS styles are applied for enhanced visual appeal and better user experience.

4. **Environment Variable Setup**:
   - `.env` file stores sensitive information like the OpenAI API key, which is loaded by `dotenv` for security.

5. **Error Handling and User Feedback**:
   - The application provides error messages and user feedback using Streamlit’s inbuilt notification features, improving robustness and user experience.

---

## File Descriptions

- **app.py**: 
  - Main application file that runs the Streamlit app. 
  - Manages user interactions, file uploads, and displays the generated Q&A pairs.

- **src/helper.py**:
  - Contains the `llm_pipeline` function responsible for processing the PDF text and generating the Q&A pairs.
  - Interfaces with LangChain and the OpenAI API to create questions and answers based on the provided content.

- **uploads/**:
  - Directory where uploaded PDF files are temporarily stored during each session.

- **requirements.txt**:
  - Lists all dependencies required to run the project, including `streamlit`, `langchain`, `faiss`, `PyPDF2`, and `dotenv`.

- **.env**:
  - Stores environment variables securely. This file should include `OPENAI_API_KEY`, used to authenticate requests to OpenAI's API.

---

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments
Special thanks to OpenAI for providing the powerful language models that make this project possible.

---

## Troubleshooting

- **Streamlit Errors**: Ensure all required libraries are installed. Run `pip install -r requirements.txt` if needed.
-

 **Environment Variable Issues**: Double-check that your `.env` file is correctly set up in the root directory.
- **API Key Errors**: If you encounter issues with the OpenAI API, ensure your API key is active and has sufficient quota.
