from __future__ import annotations

import re
from collections import Counter

STOPWORDS = {
    "a",
    "an",
    "the",
    "and",
    "or",
    "but",
    "if",
    "to",
    "of",
    "in",
    "on",
    "for",
    "with",
    "at",
    "by",
    "from",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "this",
    "that",
    "these",
    "those",
    "it",
    "as",
    "into",
    "about",
    "can",
    "will",
    "you",
    "your",
    "we",
    "our",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", clean_text(text))
    return [p.strip() for p in parts if p.strip()]


def get_title(text: str, fallback: str = "Summary Report") -> str:
    sentences = split_sentences(text)
    if not sentences:
        return fallback
    title_candidate = sentences[0]
    return title_candidate[:60] + ("..." if len(title_candidate) > 60 else "")


def extract_keywords(text: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z\-']+", text.lower())
    filtered = [w for w in words if w not in STOPWORDS and len(w) > 2]
    counts = Counter(filtered)
    return [w for w, _ in counts.most_common(limit)]


def basic_stats(original_text: str, summary_text: str) -> dict[str, int | float]:
    original_words = re.findall(r"\S+", original_text)
    summary_words = re.findall(r"\S+", summary_text)
    original_count = len(original_words)
    summary_count = len(summary_words)
    compression = 0.0
    if original_count > 0:
        compression = round((1 - (summary_count / original_count)) * 100, 2)
    return {
        "original_word_count": original_count,
        "summary_word_count": summary_count,
        "compression_percent": compression,
        "estimated_read_time_seconds": round(summary_count / 3.2, 1),
    }
