import streamlit as st


def _text_elements_page() -> None:
    st.title("Text Elements")

    st.subheader("st.text")
    st.text("Simple plain text")

    st.subheader("st.caption")
    st.caption("This is a caption")

    st.subheader("st.info")
    st.info("This is an informational message")

    st.subheader("st.success")
    st.success("This is a success message")

    st.subheader("st.warning")
    st.warning("This is a warning message")

    st.subheader("st.error")
    st.error("This is an error message")

    st.subheader("st.metric")
    st.metric(label="Temperature", value="24 °C", delta="1.2 °C")


text_elements_page = st.Page(
    _text_elements_page, title="Text Elements", url_path="text-elements", icon="📄"
)
