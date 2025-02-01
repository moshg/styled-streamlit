import time

import streamlit as st


def _status_page() -> None:
    st.title("Status Components")
    st.markdown(
        """
        This page demonstrates various status-related components in Streamlit.
        You can display progress indicators, loading states, notifications, and other status elements.
        """
    )

    # Progress bar
    st.subheader("Progress Bar")
    progress_text = "Processing..."
    progress_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1, text=progress_text)

    # Spinner
    st.subheader("Spinner")
    with st.spinner("Loading data..."):
        time.sleep(2)
    st.success("Done!")

    # Status
    st.subheader("Status")
    with st.status("Processing data...", expanded=True) as status:
        st.write("✅ Downloading data")
        time.sleep(1)
        st.write("✅ Preprocessing data")
        time.sleep(1)
        st.write("✅ Applying model")
        time.sleep(1)
        status.update(label="Processing complete!", state="complete")

    # Toast
    st.subheader("Toast")
    if st.button("Show Toast Notification"):
        st.toast("You have a new notification!")

    # Visual Effects
    st.subheader("Visual Effects")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎈 Show Balloons"):
            st.balloons()
    with col2:
        if st.button("❄️ Make it Snow"):
            st.snow()

    # Alert messages
    st.subheader("Alert Messages")
    st.error("This is an error message")
    st.warning("This is a warning message")
    st.info("This is an information message")
    st.success("This is a success message")


status_page = st.Page(_status_page, title="Status", icon="🔔")
