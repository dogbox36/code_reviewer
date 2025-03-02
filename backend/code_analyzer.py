from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Elérhető AI modellek
MODELS = {
    "StarCoder": "bigcode/starcoder",
    "CodeT5": "Salesforce/codet5-base",
    "CodeBERT": "microsoft/codebert-base"
}

# Modellek betöltése
tokenizers = {name: AutoTokenizer.from_pretrained(model) for name, model in MODELS.items()}
models = {name: AutoModelForSeq2SeqLM.from_pretrained(model) for name, model in MODELS.items()}
analyzers = {name: pipeline("text2text-generation", model=models[name], tokenizer=tokenizers[name]) for name in MODELS}

def analyze_code(code: str, model_name: str) -> str:
    if model_name not in MODELS:
        return "Hiba: Nem létező modell!"
    
    analyzer = analyzers[model_name]
    prompt = f"Elemezd az alábbi kódot:\n\n{code}"
    response = analyzer(prompt, max_length=300)[0]["generated_text"]
    return response
