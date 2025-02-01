from pathlib import Path

import streamlit as st

with open(Path(__file__).parent / "style.css") as f:
    css = f.read()


def main():
    # style
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
