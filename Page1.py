import streamlit as st

def app():
    st.title("Page 1")
    st.write("This is Page 1. Here is another sample table:")

    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [24, 27, 22, 32],
        "City": ["New York", "San Francisco", "Chicago", "Boston"]
    }
    st.table(data)
