from __future__ import annotations

import json
import os

import streamlit as st

from src.services.summarizer import SummarizerService
from src.ui.components import inject_styles, render_header, render_result
from src.utils.text_processing import clean_text


st.set_page_config(page_title="AI Summarizer Tool", page_icon=":memo:", layout="wide")
inject_styles()
render_header()

with st.sidebar:
    st.header("Configuration")
    min_length = st.slider("Min summary length", 20, 200, 60, step=10)
    max_length = st.slider("Max summary length", 60, 400, 180, step=20)
    groq_token_input = st.text_input("Groq API Key (optional)", type="password")
    st.caption("Tip: keep max length >= min length.")

text_input = st.text_area(
    "Enter text to summarize",
    height=260,
    placeholder="Paste your article, note, email, or any long text here...",
)

summarize_btn = st.button("Generate Summary", type="primary", use_container_width=True)

if summarize_btn:
    if not text_input.strip():
        st.warning("Please enter some text first.")
    elif max_length < min_length:
        st.error("Max length must be greater than or equal to min length.")
    else:
        with st.spinner("Generating structured summary..."):
            try:
                if groq_token_input.strip():
                    os.environ["GROQ_API_KEY"] = groq_token_input.strip()
                service = SummarizerService()
                result = service.generate_structured_summary(
                    text=clean_text(text_input),
                    min_length=min_length,
                    max_length=max_length,
                )
                render_result(result)
                st.download_button(
                    label="Download JSON",
                    data=json.dumps(result.to_dict(), indent=2),
                    file_name="summary_output.json",
                    mime="application/json",
                )
            except Exception as exc:  # broad on purpose to surface API/network/env failures in UI
                st.error(f"Failed to summarize text: {exc}")
