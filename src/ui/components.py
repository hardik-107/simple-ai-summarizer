from __future__ import annotations

import streamlit as st

from src.models.output_schema import SummaryResult


def inject_styles() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(180deg, #0f172a 0%, #111827 45%, #030712 100%);
                color: #f8fafc;
            }
            .main-title {
                font-size: 2.3rem;
                font-weight: 700;
                letter-spacing: 0.3px;
                margin-bottom: 0.2rem;
            }
            .subtitle {
                color: #cbd5e1;
                margin-bottom: 1.4rem;
            }
            .card {
                border: 1px solid rgba(148, 163, 184, 0.25);
                border-radius: 14px;
                padding: 1rem 1.2rem;
                background: rgba(17, 24, 39, 0.6);
                backdrop-filter: blur(4px);
            }
            .chip {
                display: inline-block;
                padding: 0.3rem 0.7rem;
                margin: 0.2rem 0.35rem 0.2rem 0;
                border-radius: 999px;
                background-color: #1e293b;
                border: 1px solid #334155;
                font-size: 0.82rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown('<div class="main-title">AI Text Summarizer</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Free API powered • Structured insights • Deployment-ready</div>',
        unsafe_allow_html=True,
    )


def render_result(result: SummaryResult) -> None:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(result.title)
    st.write(result.concise_summary)

    st.markdown("### Key Points")
    for point in result.key_points:
        st.markdown(f"- {point}")

    st.markdown("### Keywords")
    chips_html = "".join([f'<span class="chip">{word}</span>' for word in result.keywords])
    st.markdown(chips_html, unsafe_allow_html=True)

    st.markdown("### Statistics")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Original Words", result.statistics["original_word_count"])
    c2.metric("Summary Words", result.statistics["summary_word_count"])
    c3.metric("Compression", f'{result.statistics["compression_percent"]}%')
    c4.metric("Read Time", f'{result.statistics["estimated_read_time_seconds"]}s')
    st.markdown("</div>", unsafe_allow_html=True)
