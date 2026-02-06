# GAIM Lab v3.0 - AI 기반 교육 수업 분석 플랫폼

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-green.svg)](https://fastapi.tiangolo.com/)

경인교육대학교 GAIM Lab에서 개발한 **AI 기반 교실 수업 분석 시스템**입니다. 
교사의 수업 영상을 분석하여 7개 차원에서 평가하고 상세한 피드백을 제공합니다.

## 📚 목차
- [주요 기능](#-주요-기능)
- [분석 결과 요약](#-분석-결과-요약-18개-교실-수업)
- [빠른 시작](#-빠른-시작)
- [사용 방법](#-사용-방법)
- [v3.0 새로운 기능](#-v30-새로운-기능-상세-설명)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)
- [문의 및 지원](#-문의-및-지원)
- [로드맵](#-로드맵)

## 🎯 주요 기능

### 📊 다차원 수업 분석 (7개 차원)
- **수업 전문성**: 과목 지식과 설명 체계성 평가
- **교수학습 방법**: 다양한 교수 전략 활용도 분석
- **판서 및 언어**: 명확성과 전달 속도 평가
- **수업 태도**: 교사의 열정과 자신감 평가
- **학생 참여 유도**: 상호작용 수준 분석
- **시간 배분**: 효율적인 시간 관리 평가
- **창의성**: 혁신적 교수 방법 활용도 분석

### 🤖 AI 기술 활용
- **Vision Analysis**: 영상 프레임 분석으로 시각 자료 활용도 측정
- **STT (Speech-to-Text)**: Faster-Whisper를 활용한 초고속 음성 인식
- **Audio Analysis**: 음성 특성 및 속도 분석
- **종합 평가**: 7개 차원의 점수 산출 및 등급 부여 (A+∼D)

### 📈 상세 보고서 생성
- **최종 통합 보고서**: 전체 분석 결과 종합 (HTML)
- **대시보드**: 대시보드형 시각화 자료 (Chart.js)
- **개별 상세 분석**: 각 영상별 상세 분석 보고서 (마크다운)
- **데이터 파일**: CSV & JSON 형식 원본 데이터

### 🔬 고급 분석 기능 (v3.0 신규)
- **교사 프로필링**: 교사별 성과 분석 및 강점/개선점 파악
- **자동 권장사항**: 분석 데이터 기반 AI 생성 피드백
- **교사 순위 평가**: 평균 점수 기반 교사 순위 매김
- **과목별 비교 분석**: 과목별 평균 성과 및 추세 분석
- **개선 영역 식별**: 표준편차 기반 개선 우선순위 도출

### 📑 다중 형식 보고서 (v3.0 신규)
- **Excel 리포트 (.xlsx)**: 요약/상세/교사/과목 4개 시트
- **PDF 리포트 (.pdf)**: 전문적 형식의 인쇄 가능 문서
- **PowerPoint 리포트 (.pptx)**: 프레젠테이션 형식 슬라이드
- **마크다운 & HTML**: 기존 형식 유지

### 🎨 향상된 웹 대시보드 (v3.0 신규)
- **동적 필터링**: 과목/교사/점수 범위별 실시간 필터링
- **비교 모드**: 여러 분석 결과 다중선택 비교 분석
- **실시간 통계**: 필터링된 데이터의 즉각적 통계 계산
- **성과 시각화**: 교사/과목별 성과 바 차트
- **반응형 디자인**: 데스크톱/태블릿/모바일 완벽 지원

## 📋 분석 결과 요약 (18개 교실 수업)

| 항목 | 결과 |
|------|------|
| **분석 영상 수** | 18개 |
| **평균 점수** | 84.4점 |
| **최고 점수** | 88.0점 |
| **최저 점수** | 78.9점 |
| **A 이상 우수** | 8개 (44.4%) |
| **B+ 이상** | 17개 (94.4%) |

### 과목별 평균 점수
- 🥇 **국어**: 87.0점 (4개)
- 🥈 **과학**: 86.8점 (3개)  
- 🥉 **수학**: 84.8점 (4개)
- **영어**: 82.2점 (4개)
- **역사**: 82.2점 (2개)
- **사회**: 78.9점 (1개)

자세한 결과는 [보고서](./reports/) 폴더를 참조하세요.

## 🚀 빠른 시작

### 사전 요구사항
- Python 3.14+ (또는 Python 3.11)
- pip (Python 패키지 관리자)
- Windows 10/11 또는 Linux

### 설치

#### 1단계: 저장소 복제
```bash
git clone https://github.com/yourname/gaim-lab-v3.git
cd gaim-lab-v3
```

#### 2단계: Python 가상 환경 설정
```bash
# 가상 환경 생성
python -m venv .venv

# 가상 환경 활성화 (Windows)
.venv\Scripts\activate

# 가상 환경 활성화 (Linux/Mac)
source .venv/bin/activate
```

#### 3단계: 의존성 설치
```bash
pip install -r requirements.txt
```

## 💻 사용 방법

### 🚀 전체 분석 파이프라인 (권장 - v3.0 신규)
배치 분석, 고급 분석, 다중 형식 보고서를 한 번에 실행합니다:

```bash
python scripts/run_full_analysis.py
```

**출력 예시**:
```
======================================================================
🎓 GAIM Lab v3.0 - 전체 분석 파이프라인
======================================================================

[1/4] 📊 배치 분석 실행 중...
✅ 18개 영상 분석 완료 | 평균: 84.4점

[2/4] 🔬 고급 분석 실행 중...
✅ 교사 프로필링 완료 | 자동 권장사항 생성

[3/4] 📄 다중 형식 리포트 생성 중...
✅ Excel 리포트 생성: analysis_results.xlsx
✅ PDF 리포트 생성: analysis_results.pdf
✅ PowerPoint 리포트 생성: analysis_results.pptx

[4/4] 📋 분석 완료 요약
======================================================================
생성된 파일:
  📊 batch_results.json
  📈 batch_summary.csv
  📑 advanced_analysis.json
  📋 analysis_results.xlsx (Excel)
  📄 analysis_results.pdf (PDF)
  📊 analysis_results.pptx (PowerPoint)
```

### 1️⃣ 배치 분석 (18개 영상 동시 분석)
```bash
python scripts/batch_analysis_18videos.py
```

**출력**:
```
======================================================================
🎓 GAIM Lab v3.0 - 18개 교실 수업 영상 배치 분석
======================================================================

📂 출력 디렉토리: D:\Ginue_AI\output\batch_analysis_20260207_005428

🔍 18개 영상 분석 중...

   [ 1/18] ✅ class_001_korean_literature.mp4          →  85.0점 (A)
   [ 2/18] ✅ class_002_math_geometry.mp4              →  86.1점 (A)
   ...
   [18/18] ✅ class_018_english_conversation.mp4       →  80.6점 (B+)

📊 분석 결과 요약
======================================================================
📈 점수 통계:
   • 평균 점수: 84.4점
   • 최고 점수: 88.0점
   • 최저 점수: 78.9점

🎯 등급 분포:
   A  :  8명 ( 44.4%)
   B+:  9명 ( 50.0%)
   B  :  1명 (  5.6%)
```

### 2️⃣ 고급 분석 (교사 프로필링 & 권장사항)
```bash
python scripts/advanced_analyzer.py
```

**기능**:
- 교사별 성과 프로필 생성
- 강점/개선점 자동 분석
- 과목별 비교 분석
- 교사 순위 매김 (평균 점수)
- 우선 개선 영역 식별

### 3️⃣ 다중 형식 리포트 생성 (Excel/PDF/PowerPoint)
```bash
python scripts/report_generator.py
```

**생성 형식**:

**📊 Excel (.xlsx)**
```
analysis_results.xlsx
├── Summary Sheet (요약)
│   ├── 평균/최고/최저 점수
│   ├── 등급별 분포
│   └── 과목별 통계
├── Detail Sheet (상세)
│   ├── 모든 분석 결과 (정렬된 순서)
│   ├── 과목/교사/점수 정보
│   └── 등급 및 피드백
├── Teacher Sheet (교사)
│   ├── 교사별 성과 비교
│   ├── 분석 횟수
│   └── 평균 점수
└── Subject Sheet (과목)
    ├── 과목별 평균 점수
    ├── 최고/최저 점수
    └── 분석 영상 수
```

**📄 PDF (.pdf)**
```
analysis_results.pdf
├── 제목 페이지
├── 통계 표
└── 상위 10 상세 분석 결과
```

**📊 PowerPoint (.pptx)**
```
analysis_results.pptx
├── 제목 슬라이드
├── 통계 슬라이드
└── 상위 5 성과 슬라이드
```

### 4️⃣ 개별 영상 분석
```bash
python scripts/enhanced_demo_analysis.py input_video.mp4
```

### 5️⃣ 개별 보고서 생성
```bash
python scripts/generate_individual_reports.py
```

### 6️⃣ 최종 통합 보고서 생성
```bash
python scripts/generate_final_report.py
```

### 7️⃣ 웹 대시보드 (React)
프론트엔드 대시보드에서 실시간으로 분석 결과를 살펴보세요:

```bash
cd frontend
npm install
npm run dev
```

**대시보드 기능**:
- 🔍 **동적 필터** - 과목/교사/점수 범위 필터링
- 📊 **실시간 통계** - 필터된 데이터 통계 자동 계산
- 📈 **성과 차트** - 교사/과목별 성과 시각화
- 🔄 **비교 모드** - 여러 결과 다중선택 비교
- 📱 **반응형 UI** - 데스크톱/모바일 최적화

## 📊 보고서 보기

### 생성된 파일 구조
```
output/batch_analysis_20260207_005428/
├── 최종_통합_보고서.html          # 📊 최종 통합 보고서 (권장)
├── batch_dashboard.html            # 📈 대시보드 (Chart.js)
├── batch_results.json              # 📄 분석 데이터 (JSON)
├── batch_summary.csv               # 📋 요약 데이터 (CSV)
└── individual_reports/             # 📑 개별 상세 분석
    ├── class_001_korean_literature_상세분석.md
    ├── class_002_math_geometry_상세분석.md
    └── ... (총 18개)
```

### 웹 브라우저에서 보기
```bash
# Windows
start output/batch_analysis_20260207_005428/최종_통합_보고서.html

# Linux/Mac  
open output/batch_analysis_20260207_005428/최종_통합_보고서.html
```

### VS Code Live Server로 보기
1. HTML 파일 우클릭
2. "Open with Live Server" 선택
3. 자동으로 브라우저 열림

## 🏗️ 프로젝트 구조

```
gaim-lab-v3/
├── README.md                       # 📖 이 파일
├── requirements.txt                # 📦 Python 의존성
├── LICENSE                         # ⚖️ MIT 라이선스
├── .gitignore                      # 🚫 Git 무시 목록
│
├── backend/                        # 🔧 FastAPI 백엔드
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI 서버
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── analysis.py     # 분석 API
│   │   │       ├── chat.py         # 채팅 API
│   │   │       └── websocket.py    # WebSocket
│   │   └── core/
│   │       ├── __init__.py
│   │       └── config.py           # 설정
│   └── requirements.txt
│
├── core/                           # 🤖 핵심 분석 모듈
│   ├── __init__.py
│   ├── config.py                  # 설정
│   └── analyzers/
│       ├── __init__.py
│       ├── emotion_detector.py     # 감정 분석
│       ├── faster_whisper_stt.py   # 음성 인식
│       └── turbo_analyzer.py       # 종합 분석
│
├── scripts/                        # 📝 분석 스크립트
│   ├── batch_analysis_18videos.py       # 배치 분석 (18개 영상)
│   ├── advanced_analyzer.py             # 🆕 고급 분석 (교사 프로필링)
│   ├── report_generator.py              # 🆕 다중 형식 리포트 (Excel/PDF/PowerPoint)
│   ├── run_full_analysis.py             # 🆕 통합 파이프라인 (원클릭 분석)
│   ├── generate_individual_reports.py   # 개별 보고서
│   ├── generate_final_report.py         # 최종 보고서
│   ├── enhanced_demo_analysis.py        # 향상된 분석
│   └── demo_analysis.py                 # 기본 분석
│
├── frontend/                       # 🎨 React 프론트엔드
│   ├── src/
│   │   ├── pages/                  # 🆕 페이지 컴포넌트
│   │   │   ├── Dashboard.jsx       # 🆕 고급 분석 대시보드 (필터/비교)
│   │   │   ├── Dashboard.css       # 🆕 대시보드 스타일
│   │   │   ├── AICoach.jsx         # AI 코치 페이지
│   │   │   ├── Analysis.jsx        # 분석 결과 페이지
│   │   │   ├── Portfolio.jsx       # 포트폴리오 페이지
│   │   │   └── Upload.jsx          # 영상 업로드 페이지
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── reports/                        # 📊 생성된 보고서
│   ├── 최종_통합_보고서.html
│   ├── batch_dashboard.html
│   └── individual_reports/
│
└── docs/                           # 📚 문서
    ├── SETUP.md                   # 설치 가이드
    ├── USAGE.md                   # 사용 설명서
    ├── API.md                     # API 문서
    └── TROUBLESHOOTING.md         # 문제 해결
```

## 📈 분석 프로세스 다이어그램

```
📹 입력 영상
   ↓
🎥 [Vision Analysis] ──→ 시각자료 활용도 측정
   ↓
🎤 [STT Analysis] ──→ 음성을 텍스트로 변환
   ↓
🔊 [Audio Analysis] ──→ 음성 속도, 음량 분석
   ↓
📊 [7차원 평가] ──→ 각 항목별 점수 산출
   ↓
⭐ [최종 등급] ──→ A+∼D 등급 부여
   ↓
📄 [상세 보고서] ──→ 피드백 & 권장사항 생성
   ↓
💾 출력 (HTML, JSON, CSV, Markdown)
```

## 🎓 기술 스택

### 백엔드
- **FastAPI**: 고성능 Python 웹 프레임워크
- **Uvicorn**: ASGI 실행 서버
- **SQLAlchemy**: ORM
- **Pydantic**: 데이터 검증

### AI/ML 라이브러리
- **Faster-Whisper** (1.2.1): 초고속 음성인식 ⚡
- **MediaPipe** (0.10.32): 컴퓨터 비전 라이브러리
- **OpenAI Whisper** (20250625): 음성 인식
- **PyTorch** (2.10.0): 딥러닝 프레임워크
- **LibROSA** (0.11.0): 오디오 분석

### 데이터 처리
- **Pandas** (3.0.0): 데이터 분석
- **NumPy** (2.3.5): 수치 계산
- **SciPy** (1.17.0): 과학 계산

### 리포트 생성 (v3.0 신규)
- **OpenPyXL** (3.11.0): Excel 리포트 생성
- **ReportLab** (4.0.7): PDF 리포트 생성
- **python-pptx** (0.6.23): PowerPoint 리포트 생성

### 프론트엔드
- **React**: 사용자 인터페이스
- **Vite**: 빠른 빌드 도구
- **Chart.js**: 그래프 및 대시보드

## ⭐ v3.0 새로운 기능 상세 설명

### 🔬 고급 분석 (AdvancedAnalyzer)
```python
from scripts.advanced_analyzer import AdvancedAnalyzer

# 배치 분석 결과로부터 고급 분석 생성
analyzer = AdvancedAnalyzer(batch_results.json)

# 교사별 성과 프로필
teacher_ranking = analyzer.get_teacher_ranking()
# 출력: [{'teacher': 'Kim', 'avg': 85.5, 'count': 3, 'improvements': [...]}, ...]

# 과목별 비교
subject_comparison = analyzer.get_subject_comparison()
# 출력: {'국어': {'avg': 87.0, 'max': 89.5, 'min': 84.2}, ...}

# 개선 영역
improvements = analyzer.get_improvement_areas()
# 출력: {'수업전문성': {'avg': 82.1, 'std': 2.5}, ...}

# 자동 생성 권장사항
report = analyzer.generate_teacher_report('Kim')
# 출력: {'analysis_count': 3, 'recommendations': [...], ...}
```

### 📄 다중 형식 리포트 생성 (ReportGenerator)
```python
from scripts.report_generator import ReportGenerator

# 리포트 제너레이터 초기화
generator = ReportGenerator(batch_results, output_dir='reports/')

# Excel 리포트 (4개 시트)
generator.generate_excel_report('analysis_results.xlsx')
# 출력: analysis_results.xlsx (요약/상세/교사/과목 4개 시트)

# PDF 리포트 (전문 문서 형식)
generator.generate_pdf_report('analysis_results.pdf')
# 출력: analysis_results.pdf (타이틀/통계/상위10 분석)

# PowerPoint 리포트 (프레젠테이션)
generator.generate_powerpoint_report('analysis_results.pptx')
# 출력: analysis_results.pptx (3개 슬라이드)
```

### 🎨 향상된 웹 대시보드 (React)
```javascript
// Dashboard.jsx - 고급 필터링 & 비교 기능
<Dashboard
  data={analysisResults}
  onFilterChange={handleFilter}  // 실시간 필터 적용
  compareMode={true}              // 다중 선택 비교
/>

// 기능:
// - 과목/교사/점수 범위 동적 필터
// - 선택된 항목 다중 비교
// - 실시간 통계 (평균/최고/최저)
// - 성과 바 차트 (교사/과목)
// - 반응형 데이터 테이블
```

### 🚀 통합 파이프라인 (run_full_analysis.py)
한 줄의 명령으로 모든 분석 수행:
```bash
python scripts/run_full_analysis.py
```

실행 프로세스:
1. 배치 분석 (18개 영상)
2. 고급 분석 (교사 프로필링)
3. 다중 형식 리포트 생성
4. 최종 결과 요약 및 파일 경로 출력

## ⚙️ 설치 및 설정

### Python 버전 호환성

**Python 3.14 (권장)**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Python 3.11**
```bash
python3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 주의사항: DeepFace

⚠️ **DeepFace는 Python 3.14에서 미지원**
- TensorFlow 호환성 문제
- **대안 1**: InsightFace 설치
  ```bash
  pip install insightface
  ```
- **대안 2**: MediaPipe 사용 (이미 포함)
- **대안 3**: Python 3.13 환경에서 설정

## 📝 평가 기준

### 점수 범위별 등급
| 등급 | 점수 범위 | 평가 | 비고 |
|------|----------|------|------|
| **A+** | 95-100 | 최우수 | 거의 완벽한 수준 |
| **A** | 85-94 | 우수 | 정상 범위 최상 |
| **B+** | 80-84 | 양호 | 현재 수준 유지 권장 |
| **B** | 75-79 | 중상 | 1-2개 영역 개선 필요 |
| **C+** | 70-74 | 중 | 전반적 개선 필요 |
| **C** | 60-69 | 중하 | 전문가 상담 권장 |

### 각 차원별 평가 기준
- **80점 이상**: 우수한 수준
- **75-79점**: 개선 필요
- **70점 이하**: 전문성 개발 필수

## 🔐 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

```
MIT License

Copyright (c) 2026 경인교육대학교 GAIM Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👥 기여하기

### 버그 보고
[GitHub Issues](https://github.com/yourname/gaim-lab-v3/issues)에서 버그를 보고해주세요.

### 기능 제안
[Discussions](https://github.com/yourname/gaim-lab-v3/discussions)에서 기능을 제안할 수 있습니다.

### Pull Request 가이드
1. 저장소를 Fork 합니다
2. 기능 브랜치를 만듭니다 (`git checkout -b feature/AmazingFeature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add AmazingFeature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/AmazingFeature`)
5. Pull Request를 생성합니다

## 📞 문의 및 지원

- **이메일**: educpa@ginue.ac.kr
- **GitHub Issues**: [버그 보고/기능 제안](https://github.com/yourname/gaim-lab-v3/issues)
- **Discussions**: [토론](https://github.com/yourname/gaim-lab-v3/discussions)

## 🙏 감사의 말

이 프로젝트는 다음 오픈소스를 활용했습니다:
- [FastAPI](https://fastapi.tiangolo.com/)
- [MediaPipe](https://mediapipe.dev/)
- [Faster-Whisper](https://github.com/guillaumekln/faster-whisper)
- [PyTorch](https://pytorch.org/)
- [Chart.js](https://www.chartjs.org/)

## 📚 추가 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [MediaPipe 튜토리얼](https://mediapipe.dev/solutions/guide)
- [Faster-Whisper GitHub](https://github.com/guillaumekln/faster-whisper)
- [Python 공식 문서](https://docs.python.org/)

## 🗺️ 로드맵

### ✅ 완료된 기능 (v3.0)
- [x] 7차원 수업 분석 엔진
- [x] AI 기반 음성인식 (Faster-Whisper)
- [x] 비전 분석 (MediaPipe, Vision)
- [x] 배치 분석 (18개 영상)
- [x] 다양한 리포트 형식 (HTML, CSV, JSON)
- [x] 웹 대시보드 (Chart.js)
- [x] **고급 분석 (교사 프로필링, 권장사항)**
- [x] **다중 형식 리포트 (Excel, PDF, PowerPoint)**
- [x] **향상된 웹 대시보드 (필터, 비교, 차트)**
- [x] **통합 파이프라인 (원클릭 분석)**

### 📋 향후 계획
- [ ] 실시간 수업 분석 기능 (라이브 영상)
- [ ] 다국어 지원 (영어, 중국어, 일본어)
- [ ] 모바일 앱 (iOS, Android)
- [ ] 클라우드 배포 (AWS, GCP, Azure)
- [ ] 교사 커뮤니티 기능
- [ ] 학생 피드백 통합
- [ ] GraphQL API 확장
- [ ] 머신러닝 기반 권장사항 고도화
- [ ] Docker 컨테이너화
- [ ] GitHub Actions CI/CD

## ⭐ Star & Fork

이 프로젝트가 도움이 되셨다면 ⭐ **Star**를 눌러주세요!

---

**마지막 업데이트**: 2026년 2월 7일  
**개발자**: 경인교육대학교 GAIM Lab  
**버전**: 3.1.0 (고급 분석 & 다중 형식 리포트 추가)  
**라이선스**: MIT
