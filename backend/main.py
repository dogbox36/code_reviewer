from fastapi import FastAPI, UploadFile, File
from backend.code_analyzer import analyze_code
from backend.github_integration import post_github_comment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI-Based Code Reviewer API is running!"}

@app.post("/review/")
async def review_code(file: UploadFile = File(...)):
    content = await file.read()
    analysis = analyze_code(content.decode("utf-8"))
    return {"analysis": analysis}

@app.post("/github-review/")
async def review_github_pr(repo: str, pr_number: int):
    analysis = analyze_code(f"Fetching PR {pr_number} from {repo}")
    post_github_comment(repo, pr_number, analysis)
    return {"message": f"Review posted to PR {pr_number}"}
