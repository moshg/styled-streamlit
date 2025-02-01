import streamlit as st


def _index_page() -> None:
    st.title("Streamlit Components Catalog")
    st.markdown(
        """
        This catalog showcases various Streamlit components categorized by their functionality.
        
        ### Available Categories:
        
        1. **Write Components** - Basic text and data display components
        2. **Text Elements** - Various text styling and display elements
        3. **Input Widgets** - Interactive input components
        4. **Layout & Containers** - Page layout and container components
        5. **Status** - Progress indicators and notifications
        6. **Execution Flow** - Components for controlling app execution
        
        ### How to Use
        
        Use the sidebar navigation to explore different categories of components.
        Each page demonstrates the usage of related components with live examples.
        
        ### Getting Started
        
        Select a category from the sidebar to begin exploring the components!
        """
    )


index_page = st.Page(_index_page, title="Home", default=True, icon="🏠")
