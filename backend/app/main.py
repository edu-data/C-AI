"""
FastAPI Main Application
GAIM Lab v3.0 - AI 기반 교육 수업 분석 플랫폼
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

# FastAPI 앱 생성
app = FastAPI(
    title="GAIM Lab v3.0",
    description="AI 기반 교육 수업 분석 플랫폼",
    version="3.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우트
@app.get("/")
async def root():
    return {
        "message": "GAIM Lab v3.0 API",
        "status": "running",
        "version": "3.0.0",
        "docs_url": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
