from transformers import pipeline

# Ingyenes kódértékelő AI (Hugging Face)
analyzer = pipeline("text2text-generation", model="microsoft/codebert-base")

def analyze_code(code: str) -> str:
    prompt = f"A következő kódot elemezd és javasolj fejlesztéseket:\n\n{code}"
    response = analyzer(prompt, max_length=200)[0]["generated_text"]
    return response
