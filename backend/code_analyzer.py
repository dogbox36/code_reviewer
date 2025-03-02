from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Nyilvánosan elérhető AI modellek
MODELS = {
    "CodeT5": "Salesforce/codet5-base",
    "CodeBERT": "microsoft/codebert-base"
}

# Modellek betöltése
tokenizers = {name: AutoTokenizer.from_pretrained(model) for name, model in MODELS.items()}
models = {name: AutoModelForSeq2SeqLM.from_pretrained(model) for name, model in MODELS.items()}
analyzers = {name: pipeline("text2text-generation", model=models[name], tokenizer=tokenizers[name]) for name in MODELS}

def analyze_code(code: str, model_name: str = "CodeT5") -> str:
    if model_name not in MODELS:
        return "⚠️ Hiba: A választott AI modell nem létezik!"
    
    analyzer = analyzers[model_name]
    prompt = f"Elemezd az alábbi kódot és adj részletes javaslatokat:\n\n{code}"
    response = analyzer(prompt, max_length=300)[0]["generated_text"]
    return response
