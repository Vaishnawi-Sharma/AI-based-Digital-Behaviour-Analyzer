import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from ai_utils import classify_with_ai, generate_summary


st.markdown("""
<style>

/* Remove top white padding */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* Hide Streamlit default header */
header {
    visibility: hidden;
}

/* Hide hamburger menu */
#MainMenu {
    visibility: hidden;
}

/* Hide footer */
footer {
    visibility: hidden;
}

/* Remove toolbar gap */
[data-testid="stToolbar"] {
    display: none;
}

/* App background */
.stApp {
    background: linear-gradient(135deg, #000000, #050505, #00111a);
    color: white;
}

</style>
""", unsafe_allow_html=True)
# ---------------- PAGE ----------------
st.set_page_config(page_title="Digital Behavior Analyzer", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #111 0%, #000 45%, #050505 100%);
    color: white;
}
h1,h2,h3 {
    color:white !important;
    text-shadow:0 0 8px rgba(0,255,255,0.5);
}
[data-testid="stMetric"]{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(0,255,255,0.3);
    padding:15px;
    border-radius:15px;
    box-shadow:0 0 12px rgba(0,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("AI-Based Digital Behavior Analyzer")
st.write("Browser activity insights dashboard")

# ---------------- DB ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="browser_ai"
)

df = pd.read_sql("SELECT * FROM history_data", conn)

# ---------------- LIGHT RULE CLEANING ----------------
df["category"] = df["category"].fillna("Unknown")

# ---------------- LOW QUOTA AI ----------------
st.subheader("AI Enhancement")

# Only top 5 unknown rows
unknown_rows = df[df["category"] == "Unknown"].head(5)

for i in unknown_rows.index:
    title = str(df.loc[i, "title"])
    url = str(df.loc[i, "url"])

    try:
        df.loc[i, "category"] = classify_with_ai(title, url)
    except:
        df.loc[i, "category"] = "Unknown"

st.success("Smart AI enhancement completed (limited mode)")

# ---------------- METRICS ----------------
st.subheader("Quick Stats")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Unique Categories", df["category"].nunique())
col3.metric("Total Visits", int(df["visit_count"].sum()))

# ---------------- PRODUCTIVITY SCORE ----------------
productive = ["Learning", "Career", "Productivity", "Utility", "Government/Utility"]

good_visits = df[df["category"].isin(productive)]["visit_count"].sum()
total_visits = df["visit_count"].sum()

score = int((good_visits / total_visits) * 100) if total_visits > 0 else 0

st.metric("Productivity Score", f"{score}/100")

# ---------------- CHARTS ----------------
colA, colB = st.columns(2)

with colA:
    st.subheader("Category Distribution")
    cat_df = df.groupby("category")["visit_count"].sum().reset_index()
    fig = px.pie(cat_df, names="category", values="visit_count")
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Top Visited Titles")
    top_df = df.groupby("title")["visit_count"].sum().reset_index()
    top_df = top_df.sort_values(by="visit_count", ascending=False).head(10)
    fig2 = px.bar(top_df, x="visit_count", y="title", orientation="h")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- AI SUMMARY CALL ----------------
stats_text = f"""
Total Records: {len(df)}
Total Visits: {int(total_visits)}

Category Totals:
{df.groupby('category')['visit_count'].sum().to_string()}
"""

try:
    summary = generate_summary(stats_text)
except:
    summary = "User shows mixed browsing behavior with productive and neutral activities."

st.subheader("AI Behavior Summary")
st.info(summary)

# ---------------- TABLE ----------------
st.subheader("History Data")
st.dataframe(df[["title", "category", "visit_count", "visit_time"]])