import streamlit as st
import requests

st.title("AI-Based Code Reviewer")

uploaded_file = st.file_uploader("Tölts fel egy kódfájlt!", type=["py", "js", "java", "cpp"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.code(content, language="python")
    st.sidebar.title("🧠 AI Modell kiválasztása")
    model_name = st.sidebar.selectbox("Válassz AI modellt:", ["StarCoder", "CodeT5", "CodeBERT"])


    if st.button("Kód ellenőrzése AI-val"):
        response = requests.post("http://localhost:8000/review/", files={"file": uploaded_file})
        analysis = response.json()["analysis"]
        st.subheader("AI Javaslatok:")
        st.write(analysis)

    if st.button("Statikus elemzés futtatása"):
        response = requests.post("http://localhost:8000/static-analysis/", files={"file": uploaded_file})
        pylint_result = response.json()["pylint"]
        flake8_result = response.json()["flake8"]
        
        st.subheader("Pylint eredmény:")
        st.code(pylint_result, language="text")

        st.subheader("Flake8 eredmény:")
        st.code(flake8_result, language="text")
