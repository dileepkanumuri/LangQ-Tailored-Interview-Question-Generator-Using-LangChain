# LangQ: Your AI-Powered Interview Prep Curator

**LangQ** is an AI-powered application designed to assist users in preparing for interviews by generating tailored questions and answers. This app utilizes OpenAI’s language model to read and analyze a provided PDF document, producing insightful Q&A pairs. The app is built using **Streamlit** for a seamless, interactive, and user-friendly experience.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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

## Project Structure
The project is organized to maintain modularity and ease of maintenance.

```
LangQ-Tailored-Interview-Question-Generator-Using-LangChain/
├── .env                     # Environment variables (e.g., OpenAI API Key)
├── app.py                   # Main Streamlit app
├── requirements.txt         # Langchain,faiss,Python dependencies
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
- **Environment Variable Issues**: Double-check that your `.env` file is correctly set up in the root directory.
- **API Key Errors**: If you encounter issues with the OpenAI API, ensure your API key is active and has sufficient quota.

