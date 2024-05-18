import streamlit as st
from multiapp import MultiApp
import Home
import Page1
import Page2

app = MultiApp()

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("Page 1", Page1.app)
app.add_app("Page 2", Page2.app)

# The main app
app.run()
