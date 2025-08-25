import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 YouTube Dashboard")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Analytics", "Upload"])

# Pages
if page == "Home":
    st.write("👋 Welcome to the YouTube Dashboard!")
    st.write("Here you will be able to analyze YouTube data.")

elif page == "Analytics":
    st.subheader("📈 Video Analytics")

    # sample data
    data = {
        "Video": ["Video 1", "Video 2", "Video 3", "Video 4"],
        "Views": [1200, 3400, 2900, 4100],
        "Likes": [120, 560, 430, 600]
    }
    df = pd.DataFrame(data)

    fig = px.bar(df, x="Video", y="Views", title="Views per Video", color="Video")
    st.plotly_chart(fig)

    fig2 = px.bar(df, x="Video", y="Likes", title="Likes per Video", color="Video")
    st.plotly_chart(fig2)

elif page == "Upload":
    st.subheader("📤 Upload Your CSV File")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Preview of Data")
        st.dataframe(df)

        # Show chart from uploaded data
        fig = px.bar(df, x="Video", y="Views", title="Views per Video", color="Video")
        st.plotly_chart(fig)