"""
분석 API 라우트
"""

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/video")
async def analyze_video(file: UploadFile = File(...)):
    """영상 분석"""
    return {
        "status": "success",
        "message": "분석 기능은 스크립트에서 실행하세요",
        "script": "python scripts/batch_analysis_18videos.py"
    }

@router.get("/status/{analysis_id}")
async def get_analysis_status(analysis_id: str):
    """분석 상태 조회"""
    return {
        "analysis_id": analysis_id,
        "status": "completed"
    }

@router.get("/results/{analysis_id}")
async def get_analysis_results(analysis_id: str):
    """분석 결과 조회"""
    return {
        "analysis_id": analysis_id,
        "status": "completed",
        "total_score": 84.5,
        "grade": "B+"
    }
