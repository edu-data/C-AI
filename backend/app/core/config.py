"""
설정 파일
"""

import os
from pathlib import Path

# 기본 설정
PROJECT_ROOT = Path(__file__).parent.parent.parent
DEBUG = os.getenv("DEBUG", "True") == "True"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# 데이터베이스
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Redis 캐시
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# 파일 경로
OUTPUT_DIR = os.getenv("OUTPUT_DIR", str(PROJECT_ROOT / "output"))
CACHE_DIR = os.getenv("CACHE_DIR", str(PROJECT_ROOT / "cache"))
UPLOADS_DIR = os.getenv("UPLOADS_DIR", str(PROJECT_ROOT / "uploads"))

# 분석 설정
MAX_VIDEO_SIZE_MB = int(os.getenv("MAX_VIDEO_SIZE_MB", "1000"))
MAX_VIDEO_DURATION = int(os.getenv("MAX_VIDEO_DURATION", "3600"))
ANALYSIS_WORKERS = int(os.getenv("ANALYSIS_WORKERS", "4"))

# API 설정
API_TITLE = "GAIM Lab v3.0"
API_VERSION = "3.0.0"

# 로깅
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", str(PROJECT_ROOT / "logs" / "app.log"))
