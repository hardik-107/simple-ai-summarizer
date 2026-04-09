from __future__ import annotations

import requests

from src.config import get_settings
from src.models.output_schema import SummaryResult
from src.utils.text_processing import basic_stats, extract_keywords, get_title, split_sentences

class SummarizerService:
    def __init__(self) -> None:
        self.settings = get_settings()

    def _ensure_model_available(self) -> None:
        headers = {"Authorization": f"Bearer {self.settings.api_key}"}
        response = requests.get(self.settings.models_url, headers=headers, timeout=30)
        response.raise_for_status()
        payload = response.json()
        model_ids = [item.get("id", "") for item in payload.get("data", []) if isinstance(item, dict)]
        if self.settings.model_id not in model_ids:
            raise ValueError(
                f"Configured model '{self.settings.model_id}' is not available in your Groq account. "
                "Use a supported model, e.g. llama-3.1-8b-instant."
            )

    def _summarize_with_api(self, text: str, min_length: int, max_length: int) -> str:
        api_key = self.settings.api_key
        model_id = self.settings.model_id

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing. Add it in .env file or sidebar.")
        if not api_key.startswith("gsk_"):
            raise ValueError("Invalid Groq key format. Use a GROQ_API_KEY that starts with 'gsk_'.")

        self._ensure_model_available()

        url = self.settings.base_url
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        prompt = (
            f"Summarize the following text clearly in {min_length}-{max_length} words. "
            "Return plain summary text only.\n\n"
            f"{text}"
        )

        data = {
            "model": model_id,
            "messages": [
                {"role": "system", "content": "You are a professional AI summarizer."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }

        try:
            response = requests.post(url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            response_data = response.json()
            summary = response_data["choices"][0]["message"]["content"].strip()
            if not summary:
                raise ValueError("Empty summary returned by Groq API.")
            return summary
        except Exception as exc:
            raise RuntimeError(f"API Request Failed: {exc}")

    def generate_structured_summary(self, text: str, min_length: int = 60, max_length: int = 180) -> SummaryResult:
        summary = self._summarize_with_api(text=text, min_length=min_length, max_length=max_length)
        key_points = split_sentences(summary)[:5]
        keywords = extract_keywords(summary)
        stats = basic_stats(original_text=text, summary_text=summary)
        title = get_title(summary)

        return SummaryResult(
            title=title,
            concise_summary=summary,
            key_points=key_points,
            keywords=keywords,
            statistics=stats,
        )