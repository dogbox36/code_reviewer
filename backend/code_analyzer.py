from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Ingyenes AI modell betöltése (pl. CodeT5 vagy StarCoder)
model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

analyzer = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def analyze_code(code: str) -> str:
    prompt = f"Elemezd az alábbi kódot és adj részletes javaslatokat:\n\n{code}"
    response = analyzer(prompt, max_length=300)[0]["generated_text"]
    return response
