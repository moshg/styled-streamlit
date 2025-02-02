from pathlib import Path

import streamlit as st

from styled_streamlit.routes.execution_flow import execution_flow_page
from styled_streamlit.routes.index import index_page
from styled_streamlit.routes.input_widgets import input_widgets_page
from styled_streamlit.routes.layout_and_containers import layout_and_containers_page
from styled_streamlit.routes.status import status_page
from styled_streamlit.routes.text_elements import text_elements_page
from styled_streamlit.routes.write import write_page

with open(Path(__file__).parent / "style.css", encoding="utf-8") as f:
    css: str = f.read()

# style
st.html(f"<style>{css}</style>")

pg = st.navigation(
    [
        index_page,
        write_page,
        text_elements_page,
        input_widgets_page,
        layout_and_containers_page,
        status_page,
        execution_flow_page,
    ]
)
pg.run()
