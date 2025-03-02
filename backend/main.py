import logging
from fastapi import FastAPI, UploadFile, File, HTTPException

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

@app.get("/")
def home():
    logging.info("API Home oldal betöltve")
    return {"message": "AI-Based Code Reviewer API is running!"}

@app.post("/review/")
async def review_code(file: UploadFile = File(...)):
    try:
        content = await file.read()
        logging.info("Kód feltöltve és elemzésre küldve.")
        analysis = analyze_code(content.decode("utf-8"))
        logging.info("AI válasz generálva.")
        return {"analysis": analysis}
    except Exception as e:
        logging.error(f"Hiba történt: {e}")
        raise HTTPException(status_code=500, detail="Belső szerverhiba")
