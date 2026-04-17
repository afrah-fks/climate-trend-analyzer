import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/climate_data.csv")

st.title("Climate Trend Analyzer")

st.line_chart(df['Temperature'])

st.write("Dataset Preview")
st.write(df.head())