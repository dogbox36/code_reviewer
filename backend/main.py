import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from backend.code_analyzer import analyze_code

# FastAPI alkalmazás inicializálása (EZ HIÁNYZOTT)
app = FastAPI()

# Logging beállítása
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.get("/")
def home():
    logging.info("API Home oldal betöltve")
    return {"message": "AI-Based Code Reviewer API is running!"}

@app.post("/review/")
async def review_code(file: UploadFile = File(...), model_name: str = "CodeBERT"):
    try:
        content = await file.read()
        logging.info(f"Kód feltöltve, AI elemzés indítása a {model_name} modellel.")
        analysis = analyze_code(content.decode("utf-8"), model_name)
        logging.info("AI válasz generálva.")
        return {"analysis": analysis}
    except Exception as e:
        logging.error(f"Hiba történt: {e}")
        raise HTTPException(status_code=500, detail="Belső szerverhiba")
