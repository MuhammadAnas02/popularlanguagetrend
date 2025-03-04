import streamlit as st
import pandas as pd

st.title("Popular Programming Languages (Yearly Trends)")


df = pd.read_excel("lanuage.xlsx", engine='openpyxl')

st.subheader("Data Preview")
st.dataframe(df.head())

all_columns = df.columns.tolist()
if 'Year' in all_columns:
    all_columns.remove('Year')

st.subheader("Select Languages to Display")
lang_choice = st.multiselect(
    "Choose one or more languages:",
    options=all_columns,
    default=["Python"]  
)

st.subheader("Filter by Year Range")
min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

start_year, end_year = st.slider(
    "Select the year range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

filtered_df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

if lang_choice:
    filtered_df = filtered_df[["Year"] + lang_choice]
else:
    st.warning("Please select at least one language to display.")
    st.stop()

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.subheader("Line Chart of Selected Languages")
chart_data = filtered_df.set_index("Year")
st.bar_chart(chart_data)

