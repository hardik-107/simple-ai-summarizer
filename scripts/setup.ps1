py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
if (-Not (Test-Path ".env")) {
    Copy-Item .env.example .env
}
Write-Host "Setup complete. Add GROQ_API_KEY in .env and run: streamlit run app.py"
