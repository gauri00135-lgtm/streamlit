
import streamlit as st
import pandas as pd

st.title("📊 Student Marks Analysis App")

# Upload CSV file
file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write(df.columns)


    # Display dataset
    st.subheader("📄 Student Dataset")
    st.dataframe(df)

    # Subject filter
    df.columns = df.columns.str.strip().str.capitalize()
    subjects = df["Subject"].unique()
 
    selected_subject = st.selectbox("Filter by Subject", subjects)

    filtered_df = df[df["Subject"] == selected_subject]

    # Basic insights
    avg_marks = filtered_df["Marks"].mean()
    max_marks = filtered_df["Marks"].max()
    min_marks = filtered_df["Marks"].min()

    st.subheader("📈 Insights")
    st.write("Average Marks:", round(avg_marks, 2))
    st.write("Highest Marks:", max_marks)
    st.write("Lowest Marks:", min_marks)

    # Bar chart
    st.subheader("📊 Student Marks Bar Chart")
    st.bar_chart(filtered_df.set_index("Name")["Marks"])
