# AI-Based Code Reviewer
Ez a projekt egy AI-alapú kódellenőrző rendszer, amely automatikusan javaslatokat ad és GitHub PR-eket is képes ellenőrizni.

## 🚀 Használat
1. **Backend indítása:** `uvicorn backend.main:app --reload`
2. **Frontend indítása:** `streamlit run frontend/app.py`
3. **GitHub API beállítása:** Hozz létre egy GitHub Token-t és állítsd be az `backend/github_integration.py` fájlban.
