from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import resume, jobs, match, admin

app = FastAPI(
    title="Jobs SkillSync API",
    description="Intelligent Resume Job Matching System",
    version="1.0.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(match.router, prefix="/api/match", tags=["Matching"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

# Serve frontend files
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/health")
def health_check():
    return {"status": "SkillSync is running!"}