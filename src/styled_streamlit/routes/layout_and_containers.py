import streamlit as st


def _layout_and_containers_page() -> None:
    st.title("Layout & Containers")

    st.subheader("st.columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")

    st.subheader("st.expander")
    with st.expander("Click to expand"):
        st.write("This content is hidden by default")

    st.subheader("st.container")
    container = st.container()
    container.write("This is inside a container")

    st.subheader("st.tabs")
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("Content of tab 1")
    with tab2:
        st.write("Content of tab 2")


layout_and_containers_page = st.Page(
    _layout_and_containers_page,
    title="Layout & Containers",
    url_path="layout-and-containers",
    icon="📐",
)
