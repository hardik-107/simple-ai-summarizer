# AI Text Summarizer (Free API + Streamlit)

A professional Streamlit app that:
- accepts user text input
- summarizes it using a free Groq model API
- returns a structured output (title, concise summary, key points, keywords, stats)

## Project Structure

```text
Simple tool/
├─ app.py
├─ requirements.txt
├─ .env.example
├─ .streamlit/config.toml
├─ src/
│  ├─ config.py
│  ├─ models/output_schema.py
│  ├─ services/summarizer.py
│  ├─ ui/components.py
│  └─ utils/text_processing.py
└─ scripts/
   └─ setup.ps1
```

## Local Setup (Windows PowerShell)

1. Create and activate virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Create your env file:
   ```powershell
   Copy-Item .env.example .env
   ```

4. Add your Groq API key in `.env`:
   - `GROQ_API_KEY=...`
   - optional: `GROQ_MODEL_ID=llama-3.1-8b-instant`

5. Run app:
   ```powershell
   streamlit run app.py
   ```

## Free API Used

- Groq API (OpenAI-compatible): https://console.groq.com/docs/quickstart
- Recommended free model: `llama-3.1-8b-instant`
- Model availability is checked at runtime via `/openai/v1/models` before summarization.

## Streamlit Deployment

1. Push this project to GitHub.
2. Open [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Deploy repository with:
   - Main file path: `app.py`
   - Python dependencies from `requirements.txt`
4. In Streamlit app settings, add secret:
   - `GROQ_API_KEY = "your_key"`

## Notes

- If model warm-up takes time, first request may be slower.
- Keep input length reasonable for free-tier limits.
