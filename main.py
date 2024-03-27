import streamlit as st
import pandas as pd
# Path to your CSV file (update as necessary)
csv_file_path = 'cord19-qa.csv'
# Title of your app
st.title('Question-Answer Dataset Explorer')
# Load the dataset
df = pd.read_csv(csv_file_path)
# Checkbox to show the raw data
if st.checkbox('Show raw data'):
    st.write(df)
# Toggle to explore questions
if st.checkbox('Explore Questions'):
    st.write(df[['question']])  # Adjust if your column name is different
# Toggle to explore answers
if st.checkbox('Explore Answers'):
    st.write(df[['answer']])  # Adjust if your column name is different







