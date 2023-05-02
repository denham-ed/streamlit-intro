import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page1 import page1_body
from app_pages.page2 import page2_body

app = MultiPage(app_name='Rock solid app discovery!')
app.app_page("Page The First", page1_body)
app.app_page("Page The Second", page2_body)

app.run()