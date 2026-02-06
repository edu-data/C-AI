"""
설정 파일
"""

import os
from pathlib import Path

# 기본 설정
PROJECT_ROOT = Path(__file__).parent.parent
DEBUG = os.getenv("DEBUG", "True") == "True"

# 파일 경로
OUTPUT_DIR = os.getenv("OUTPUT_DIR", str(PROJECT_ROOT.parent / "output"))
CACHE_DIR = os.getenv("CACHE_DIR", str(PROJECT_ROOT.parent / "cache"))

# 분석 설정
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))
ANALYSIS_TIMEOUT = int(os.getenv("ANALYSIS_TIMEOUT", "3600"))

# 모델 설정
MODEL_DEVICE = os.getenv("MODEL_DEVICE", "cuda")  # cuda or cpu
