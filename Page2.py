import streamlit as st
import pandas as pd

def app():
    st.title("Page 2")
    st.write("This is Page 2. Here is yet another sample table loaded from a CSV file:")

    data = pd.read_csv("data/page2_data.csv")
    st.table(data)
