# 📝 AI Text Summarizer 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![API](https://img.shields.io/badge/API-Groq%20(OpenAI%20Compatible)-success)

A highly optimized, professional Streamlit application that takes any long-form text and instantly generates a clear, structured summary. Built to demonstrate clean architecture, modular design, and seamless third-party API integration.

## ✨ Key Features
* **Intelligent Summarization**: Powered by the blazing-fast `llama-3.1-8b-instant` model via Groq's OpenAI-compatible API.
* **Structured Output**: Doesn't just return a block of text. It intelligently breaks down the result into:
    * 🏷️ Suggested Title
    * 📝 Concise Summary
    * 📌 Key Takeaways (Bullet points)
    * 🔑 Extracted Keywords
    * 📊 Text Statistics (Word count, etc.)
* **Customizable Constraints**: Users can set the desired minimum and maximum length of the summary via intuitive UI sliders.
* **Clean Architecture**: Separated concerns with dedicated folders for services, UI components, data models, and configurations.

## 🛠️ Tech Stack
* **Frontend & Framework:** Streamlit
* **Backend Logic:** Python 3
* **LLM Integration:** Groq API (OpenAI Standard Format)
* **Environment Management:** `python-dotenv`

## 📂 Project Structure

```text
Simple tool/
├─ app.py                       # Main Streamlit application entry point
├─ requirements.txt             # Python dependencies
├─ .env.example                 # Template for environment variables
├─ .streamlit/config.toml       # Streamlit UI configuration
├─ src/
│  ├─ config.py                 # Environment variable management
│  ├─ models/output_schema.py   # Dataclasses for structured AI output
│  ├─ services/summarizer.py    # Core logic and API integration
│  ├─ ui/components.py          # Reusable UI rendering functions
│  └─ utils/text_processing.py  # Helper functions for text analysis
└─ scripts/
   └─ setup.ps1                 # Optional quick-setup script
