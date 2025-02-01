import streamlit as st


def _input_widgets_page() -> None:
    st.title("Input Widgets")

    st.subheader("st.button")
    st.button("Click Me!")

    st.subheader("st.checkbox")
    st.checkbox("Check me out")

    st.subheader("st.radio")
    st.radio("Choose one", ["Option 1", "Option 2", "Option 3"])

    st.subheader("st.selectbox")
    st.selectbox("Select an option", ["Choice 1", "Choice 2", "Choice 3"])

    st.subheader("st.multiselect")
    st.multiselect("Select multiple", ["A", "B", "C"])

    st.subheader("st.slider")
    st.slider("Select a value", 0, 100, 50)

    st.subheader("st.text_input")
    st.text_input("Enter some text")

    st.subheader("st.number_input")
    st.number_input("Enter a number", min_value=0, max_value=100, value=50)

    st.subheader("st.text_area")
    st.text_area("Enter multiple lines")

    st.subheader("st.date_input")
    st.date_input("Pick a date")

    st.subheader("st.time_input")
    st.time_input("Pick a time")

    st.subheader("st.color_picker")
    st.color_picker("Pick a color")


input_widgets_page = st.Page(
    _input_widgets_page, title="Input Widgets", url_path="input-widgets", icon="🔘"
)
