import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="KMRL Train Scheduling", layout="wide")

st.title(" KMRL Train Scheduling Dashboard")
st.markdown("### Live Maintenance & Scheduling Status")

# -------------------------------
# Load Data
# -------------------------------
try:
    schedule_df = pd.read_csv("data/final_schedule.csv")
    st.success(" Final optimized schedule loaded successfully!")
except FileNotFoundError:
    st.error(" final_schedule.csv not found. Run optimization first.")
    st.stop()

# -------------------------------
# Main Table
# -------------------------------
st.subheader(" Optimized Train Allocation")
st.dataframe(schedule_df, use_container_width=True)

# -------------------------------
# Decision Distribution Pie Chart
# -------------------------------
st.subheader(" Allocation Distribution")
fig, ax = plt.subplots(figsize=(6,6))
schedule_df["OptimizedDecision"].value_counts().plot.pie(
    autopct="%1.1f%%", ax=ax
)
ax.set_ylabel("")
st.pyplot(fig)

# -------------------------------
# Filter by Decision Type
# -------------------------------
st.subheader("Filter by Decision")
decision_types = schedule_df["OptimizedDecision"].unique()
selected = st.multiselect("Select Decision Type(s):", decision_types, default=list(decision_types))

filtered_df = schedule_df[schedule_df["OptimizedDecision"].isin(selected)]
st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# Download Option
# -------------------------------
st.download_button(
    label=" Download Final Schedule CSV",
    data=schedule_df.to_csv(index=False).encode("utf-8"),
    file_name="final_schedule.csv",
    mime="text/csv"
)
