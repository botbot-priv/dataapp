import streamlit as st

def app():
    st.title("Home")
    st.write("Welcome to the multi-page app. Use the sidebar to navigate.")

    st.write("Here is a sample table:")
    data = {
        "Column 1": [1, 2, 3, 4],
        "Column 2": [10, 20, 30, 40],
    }
    st.table(data)
