import streamlit as st
import pandas as pd
st.set_page_config(page_title="Marks Viewer", layout="centered")
st.title("Student Marks Viewer")
uploaded = st.sidebar.file_uploader("Marks file (CSV)", type="csv")
if uploaded is None: st.info("Upload a marks file to start."); st.stop()
df = pd.read_csv(uploaded)
num_cols = df.select_dtypes(include="number").columns.tolist()
subject = st.sidebar.selectbox("Subject", num_cols)
pass_mark = st.sidebar.slider("Pass mark", 0, 100, 50)
avg = df[subject].mean()
pass_rate = (df[subject] >= pass_mark).mean() * 100
c1, c2 = st.columns(2)
c1.metric("Average", f"{avg:.1f}")
c2.metric("Pass rate", f"{pass_rate:.1f}%")
show_fails = st.checkbox("Show students below the pass mark")
if show_fails:
    st.dataframe(df[df[subject] < pass_mark])
bands = (df[subject] // 10 * 10).value_counts().sort_index()
st.bar_chart(bands)
st.download_button("Download ranked list", df.sort_values(subject, ascending=False).to_csv(index=False), "ranked.csv", "text/csv")
