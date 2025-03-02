import streamlit as st
import requests

st.title(" AI-Based Code Reviewer")

# Kódfájl feltöltés
uploaded_file = st.file_uploader("Tölts fel egy kódfájlt!", type=["py", "js", "java", "cpp"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.code(content, language="python")

    if st.button(" Kód ellenőrzése AI-val"):
        response = requests.post("http://localhost:8000/review/", files={"file": uploaded_file})
        analysis = response.json()["analysis"]
        st.subheader(" AI Javaslatok:")
        st.write(analysis)

# GitHub PR kommentáló szekció
st.sidebar.title(" GitHub PR Ellenőrző")
repo = st.sidebar.text_input(" GitHub Repository (pl.: user/repo)")
pr_number = st.sidebar.number_input(" PR Szám", min_value=1, step=1)

if st.sidebar.button(" PR elemzése és komment"):
    response = requests.post(f"http://localhost:8000/github-review/?repo={repo}&pr_number={pr_number}")
    st.sidebar.write(response.json()["message"])
