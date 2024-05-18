import streamlit as st
from multiapp import MultiApp
import Home
import Page1

app = MultiApp()

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("Page 1", Page1.app)

# The main app
app.run()
