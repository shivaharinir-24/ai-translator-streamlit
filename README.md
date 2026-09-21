# 🌐 AI Translator

A Generative AI-powered multilingual translation application built using Python, Streamlit, and the OpenAI API.

## 📌 About the Project

AI Translator is an interactive web application that allows users to translate text between different languages using Generative AI.

Users can select a source language and a target language, enter the text they want to translate, and receive an AI-generated translation through a simple Streamlit interface.

## ✨ Features

- 🌍 Translation between multiple languages
- 🔄 Source and target language selection
- ✍️ User-friendly text input
- 🤖 AI-powered translations using the OpenAI API
- ⚠️ Input validation for empty text
- 🖥️ Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI API
- Generative AI

## 🚀 How to Run the Project

### 1. Install the required packages

```bash
pip install streamlit openai
```

### 2. Configure your OpenAI API key

Create a `.streamlit/secrets.toml` file and add your own OpenAI API key.

Never upload your API key to GitHub.

### 3. Run the application

```bash
streamlit run app.py
```

## 🔐 API Key Security

The OpenAI API key is not stored directly in the application code.

The application accesses the key securely using:

```python
st.secrets["OPENAI_API_KEY"]
```

## 📚 What I Learned

Through this project, I practiced:

- Building applications with Streamlit
- Integrating the OpenAI API with Python
- Working with Generative AI
- Creating source and target language selectors
- Processing user text input
- Prompt creation using Python f-strings
- Displaying AI-generated responses
- Managing API keys securely

## 🔮 Future Improvements

Future versions could include:

- More supported languages
- Automatic language detection
- Voice input and speech translation
- Translation history
- Downloadable translations
- Improved user interface
- Public web deployment

## 👩‍💻 Author

**Shiva Harini Rajkumar**

MBA in Data Science & AI | AI & Generative AI Learner
