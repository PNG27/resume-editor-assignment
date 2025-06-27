from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeSection(BaseModel):
    section: str
    content: str

@app.post("/ai-enhance")
async def enhance_section(section: ResumeSection):
    return {
        "enhanced_content": f"{section.content} (Enhanced with AI 🚀)"
    }

@app.post("/save-resume")
async def save_resume(request: Request):
    data = await request.json()
    print("Resume received:", data)
    return {"message": "Resume saved successfully"}

@app.get("/")
async def root():
    return {"message": "Resume Editor Backend is running ✅"}
