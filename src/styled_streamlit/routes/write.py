import streamlit as st


def _write_page() -> None:
    st.title("Write Components")

    st.subheader("st.write")
    st.write("Basic write function that can handle multiple data types")
    st.write("Hello, *World!* :sunglasses:")

    st.subheader("st.markdown")
    st.markdown("**Bold** and *italic* text with markdown")

    st.subheader("st.title/header/subheader")
    st.write("Examples shown throughout this page")

    st.subheader("st.code")
    st.code(
        """
    def hello():
        print("Hello, World!")
        """,
        language="python",
    )

    st.subheader("st.latex")
    st.latex(r"E = mc^2")


write_page = st.Page(_write_page, title="Write", url_path="write", icon="📝")
