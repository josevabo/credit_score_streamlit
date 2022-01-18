import streamlit as st
import pandas as pd

st.write("# Avaliação de crédito")

df = pd.DataFrame({"coluna1": [1,2,3],"coluna2": [4,5,6],"coluna3": [7,8,9]}, index=['a', 'b','c'])

st.line_chart(df)