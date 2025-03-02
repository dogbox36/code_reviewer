import streamlit as st
import requests

st.title("AI-Based Code Reviewer")

uploaded_file = st.file_uploader("Tölts fel egy kódfájlt!", type=["py", "js", "java", "cpp"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.code(content, language="python")

    if st.button("Elemzés indítása"):
        response = requests.post("http://localhost:8000/review/", files={"file": uploaded_file})
        analysis = response.json()["analysis"]
        st.subheader("AI javaslatok")
        st.write(analysis)

repo = st.text_input("GitHub Repository (pl.: user/repo)")
pr_number = st.number_input("PR szám", min_value=1, step=1)
if st.button("GitHub PR ellenőrzése"):
    response = requests.post(f"http://localhost:8000/github-review/?repo={repo}&pr_number={pr_number}")
    st.write(response.json()["message"])
