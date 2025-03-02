from fastapi import FastAPI, UploadFile, File, HTTPException
from backend.code_analyzer import analyze_code

@app.post("/review/")
async def review_code(file: UploadFile = File(...), model_name: str = "StarCoder"):
    try:
        content = await file.read()
        logging.info(f"Kód feltöltve, AI elemzés indítása a {model_name} modellel.")
        analysis = analyze_code(content.decode("utf-8"), model_name)
        logging.info("AI válasz generálva.")
        return {"analysis": analysis}
    except Exception as e:
        logging.error(f"Hiba történt: {e}")
        raise HTTPException(status_code=500, detail="Belső szerverhiba")
