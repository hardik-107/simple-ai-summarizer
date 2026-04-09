from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    model_id: str
    base_url: str = "https://api.groq.com/openai/v1/chat/completions"
    models_url: str = "https://api.groq.com/openai/v1/models"


def get_settings() -> Settings:
    token_raw = os.getenv("GROQ_API_KEY", "")
    model_raw = os.getenv("GROQ_MODEL_ID", "llama-3.1-8b-instant")
    token_stripped = token_raw.strip()
    model_stripped = model_raw.strip()

    return Settings(
        api_key=token_stripped,
        model_id=model_stripped,
    )