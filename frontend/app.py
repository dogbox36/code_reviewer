import streamlit as st
import requests

st.title("AI-Based Code Reviewer")

uploaded_file = st.file_uploader("Tölts fel egy kódfájlt!", type=["py", "js", "java", "cpp"])
st.sidebar.title("AI Modell kiválasztása")
model_name = st.sidebar.selectbox("Válassz AI modellt:", ["CodeBERT", "CodeT5"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.code(content, language="python")

    if st.button("Kód ellenőrzése AI-val"):
        st.write("Küldés a szerverre...")

        # Ellenőrizzük, hogy a fájl valóban létezik és nem üres
        file_content = uploaded_file.read()
        if not file_content:
            st.error("A feltöltött fájl üres!")
        else:
            try:
                # API kérés a modellválasztó változóval
                response = requests.post(
                    "http://127.0.0.1:8000/review/",
                    files={"file": (uploaded_file.name, file_content)},
                    data={"model_name": model_name}
                )
                st.write(f"API válasz kód: {response.status_code}")

                if response.status_code == 200:
                    analysis = response.json().get("analysis", "Az AI nem adott választ.")
                    st.subheader("AI Javaslatok:")
                    st.write(analysis)
                else:
                    st.error(f"Hiba történt az API hívás során! {response.text}")

            except Exception as e:
                st.error(f"Kivétel történt az API hívás közben: {e}")
