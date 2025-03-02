from transformers import AutoModelForMaskedLM, AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# AI modellek típus szerint
MODELS = {
    "CodeBERT": ("microsoft/codebert-base", AutoModelForMaskedLM),
    "CodeT5": ("Salesforce/codet5-base", AutoModelForSeq2SeqLM)
}

# Modellek betöltése
tokenizers = {name: AutoTokenizer.from_pretrained(model[0]) for name, model in MODELS.items()}
models = {name: model_class.from_pretrained(model[0]) for name, (model_name, model_class) in MODELS.items()}
analyzers = {name: pipeline("fill-mask" if model_class == AutoModelForMaskedLM else "text2text-generation",
                            model=models[name], tokenizer=tokenizers[name])
             for name, model_class in MODELS.values()}

def analyze_code(code: str, model_name: str = "CodeBERT") -> str:
    if model_name not in MODELS:
        return "⚠️ Hiba: A választott AI modell nem létezik!"
    
    analyzer = analyzers[model_name]
    if model_name == "CodeBERT":
        prompt = f"{code[:50]} <mask> {code[50:100]}"
    else:
        prompt = f"Elemezd az alábbi kódot:\n\n{code}"
    
    response = analyzer(prompt, max_length=300)
    
    if isinstance(response, list):
        return response[0]["sequence"] if model_name == "CodeBERT" else response[0]["generated_text"]
    else:
        return "⚠️ Hiba az AI válasz feldolgozásában."
