import time

import streamlit as st


def _execution_flow_page() -> None:
    st.title("Execution Flow")

    st.subheader("st.stop")
    if st.button("Click to stop execution"):
        st.write("Execution will stop here")
        st.stop()
        st.write("This will never be printed")

    st.subheader("st.form")
    with st.form("my_form"):
        st.write("Inside the form")
        name = st.text_input("Enter your name")
        submit = st.form_submit_button("Submit")
        if submit:
            st.write(f"Hello, {name}!")

    st.subheader("st.spinner")
    if st.button("Start long running task"):
        with st.spinner("Processing..."):
            time.sleep(2)
        st.success("Done!")

    st.subheader("st.progress")
    progress_button = st.button("Run Progress Bar")
    if progress_button:
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        st.success("Completed!")

    st.subheader("st.empty")
    placeholder = st.empty()
    if st.button("Update placeholder"):
        with placeholder.container():
            st.write("This content can be dynamically updated")

    st.subheader("st.rerun")
    if st.button("Rerun app"):
        st.write("Rerunning...")
        time.sleep(1)
        st.rerun()


execution_flow_page = st.Page(
    _execution_flow_page, title="Execution flow", url_path="execution-flow", icon="⚡️"
)
