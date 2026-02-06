# GAIM Lab v3.0 - 사용 가이드

GAIM Lab v3.0의 주요 기능 및 사용 방법을 설명합니다.

## 📋 목차

1. [환경 설정](#환경-설정)
2. [스크립트 실행 가이드](#스크립트-실행-가이드)
3. [분석 보고서 해석](#분석-보고서-해석)
4. [API 사용 방법 (FastAPI)](#api-사용-방법-fastapi)
5. [주요 기능 설명](#주요-기능-설명)
6. [FAQ](#faq)

---

## 환경 설정

### 1. 가상 환경 활성화

#### Windows (PowerShell)
```powershell
.venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)
```cmd
.venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
source .venv/bin/activate
```

확인: 터미널 앞에 `(.venv)`가 표시되어야 함

### 2. 설정 파일 작성 (선택)

`.env` 파일을 프로젝트 루트에 생성:

```bash
# 서버 설정
SERVER_HOST=localhost
SERVER_PORT=8000
DEBUG=True

# 분석 설정
MAX_VIDEO_SIZE_MB=1000
ANALYSIS_WORKERS=4
OUTPUT_DIRECTORY=./output
CACHE_DIRECTORY=./cache
```

---

## 스크립트 실행 가이드

### 1️⃣ 배치 분석 (권장 - 모든 샘플 영상 분석)

```bash
python scripts/batch_analysis_18videos.py
```

**기능**:
- ✅ 18개 교실 수업 영상 동시 분석
- ✅ 7차원 평가 점수 산출
- ✅ 최종 통합 보고서 생성 (HTML)
- ✅ 대시보드 생성 (Chart.js)
- ✅ 개별 분석 데이터 내보내기 (JSON, CSV)

**실행 시간**: 약 5-10분

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

✅ 분석 완료!
```

**생성된 파일**:
```
output/batch_analysis_YYYYMMDD_HHMMSS/
├── 최종_통합_보고서.html          # 📊 메인 보고서
├── batch_dashboard.html            # 📈 인터랙티브 대시보드
├── batch_results.json              # 📄 분석 데이터 (JSON)
├── batch_summary.csv               # 📋 요약 (CSV)
└── individual_reports/             # 📑 개별 분석 (마크다운)
    ├── class_001_상세분석.md
    ├── class_002_상세분석.md
    └── ... (총 18개)
```

### 2️⃣ 단일 영상 분석

```bash
python scripts/enhanced_demo_analysis.py <영상_파일경로>
```

**예시**:
```bash
python scripts/enhanced_demo_analysis.py "C:\Videos\수학_수업.mp4"
```

**기능**:
- ✅ 한 개의 영상 상세 분석
- ✅ 프레임 추출 및 시각화
- ✅ JSON 형식 결과 저장
- ✅ HTML 보고서 생성

**출력 위치**: `output/demo_analysis_v2/`

### 3️⃣ 개별 보고서 생성

```bash
python scripts/generate_individual_reports.py
```

**기능**:
- ✅ 분석된 18개 영상별 마크다운 보고서 생성
- ✅ 각 영상별 7차원 상세 평가
- ✅ 강점 및 개선점 명시
- ✅ 맞춤형 권장사항 제공

**출력 위치**: `output/batch_analysis_XXX/individual_reports/`

### 4️⃣ 최종 통합 보고서 생성

```bash
python scripts/generate_final_report.py
```

**기능**:
- ✅ 18개 영상의 종합 평가
- ✅ 과목별 / 교사별 비교 분석
- ✅ 인터랙티브 통계 및 차트
- ✅ 종합 권장사항 제시

**출력**: `output/batch_analysis_XXX/최종_통합_보고서.html`

---

## 분석 보고서 해석

### 1. 점수 및 등급

#### 등급 시스템
| 등급 | 점수 | 의미 | 설명 |
|------|------|------|------|
| **A+** | 95-100 | 최우수 | 거의 완벽한 교수 능력 |
| **A** | 85-94 | 우수 | 정상 범위의 최상 수준 |
| **B+** | 80-84 | 양호 | 개선 필요 없는 현재 수준 |
| **B** | 75-79 | 중상 | 1-2개 영역 개선 권장 |
| **C+** | 70-74 | 중 | 여러 영역 개선 필요 |

### 2. 7개 평가 차원

#### 📚 수업 전문성 (Lecture Expertise)
- **의미**: 과목 지식의 깊이와 수업 설명의 체계성
- **평가 포인트**:
  - 정확한 개념 설명
  - 체계적인 내용 전개
  - 예시 활용의 적절성
- **최적 점수**: 85점 이상

#### 🎯 교수학습 방법론 (Teaching Methodology)
- **의미**: 다양한 교수 전략 활용도
- **평가 포인트**:
  - 강의식 수업의 다양성
  - 학생 참여형 활동 포함
  - 토론, 협력학습 활용
- **최적 점수**: 85점 이상

#### ✍️ 판서 및 언어 (Presentation & Communication)
- **의미**: 명확한 의사소통 능력
- **평가 포인트**:
  - 명확한 발장
  - 적절한 말의 속도
  - 체계적 판서 구성
- **최적 점수**: 80점 이상

#### 💪 수업 태도 (Teaching Attitude)
- **의미**: 교사의 열정도와 자신감
- **평가 포인트**:
  - 적극적이고 긍정적인 태도
  - 학생과의 라포 형성
  - 수업에 대한 애정
- **최적 점수**: 85점 이상

#### 🤝 학생 참여 유도 (Student Engagement)
- **의미**: 학생의 적극적 수업 참여 유도
- **평가 포인트**:
  - 질문과 상호작용 빈도
  - 학생 발표 기회 제공
  - 피드백 제공 수준
- **최적 점수**: 80점 이상

#### ⏱️ 시간 배분 (Time Management)
- **의미**: 수업 내용에 대한 효율적 시간 분배
- **평가 포인트**:
  - 정해진 시간 내 내용 완성
  - 핵심 내용 강조 시간 확보
  - 복습 시간 운영
- **최적 점수**: 80점 이상

#### 🌟 창의성 (Creativity)
- **의미**: 혁신적이고 창의적인 교수 방법 활용
- **평가 포인트**:
  - 새로운 교수 자료 활용
  - 흥미로운 예시 제시
  - 학습 동기 부여 방법의 창의성
- **최적 점수**: 80점 이상

### 3. 샘플 보고서 읽기

#### 샘플: 한국어 수업
```
🎓 분석 제목: class_001_korean_literature_상세분석.md

📊 종합 평가: 85.0점 (등급: A)

분석 대상:
- 과목: 한국어 문학
- 학년: 고등학교 2학년
- 교사: 최정윤
- 영상 길이: 45분 28초

7차원 점수:
  ├─ 수업 전문성: 88점 ✅ 우수
  ├─ 교수학습 방법론: 86점 ✅ 우수
  ├─ 판서 및 언어: 85점 ✅ 우수
  ├─ 수업 태도: 87점 ✅ 우수
  ├─ 학생 참여 유도: 82점 ✅ 양호
  ├─ 시간 배분: 84점 ✅ 양호
  └─ 창의성: 83점 ✅ 양호

주요 강점:
1. 한문학에 대한 깊이있는 지식 전달
2. 시와 산문의 다양한 작품 비교 분석
3. 학생의 감정 표현 유도 효과적

개선 사항:
1. 학생 발표 시간 조금 더 확보
2. 디지털 자료(영상, 이미지) 활용 증대

맞춤형 권장사항:
→ 시간이 허락한다면 특정 작품에 대해 학생 소그룹 토론 시간 추가
→ 사전에 작품 관련 영상 자료 준비하면 학생 몰입도 증가 가능
```

---

## API 사용 방법 (FastAPI)

### 1. FastAPI 서버 시작

```bash
uvicorn backend.app.main:app --reload
```

**출력**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### 2. API 문서 확인

브라우저에서 다음 URL 접속:

- **Swagger UI** (권장): http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 3. 주요 API 엔드포인트

#### 분석 요청
```http
POST /api/v1/analysis/video
Content-Type: multipart/form-data

file: <영상 파일>
```

**응답**:
```json
{
  "id": "analysis_12345",
  "status": "completed",
  "scores": {
    "lecture_expertise": 88,
    "teaching_methodology": 86,
    "presentation": 85,
    "attitude": 87,
    "student_engagement": 82,
    "time_management": 84,
    "creativity": 83
  },
  "total_score": 85.0,
  "grade": "A",
  "report_url": "/reports/analysis_12345.html"
}
```

#### 분석 상태 조회
```http
GET /api/v1/analysis/{analysis_id}
```

#### 채팅 (AI 피드백)
```http
POST /api/v1/chat
Content-Type: application/json

{
  "analysis_id": "analysis_12345",
  "message": "수업 어떤 부분을 개선하면 좋을까요?"
}
```

---

## 주요 기능 설명

### 1. 영상 처리 파이프라인

```
📹 입력 영상
   ↓
🎬 [영상 전처리]
   └─ 해상도 정규화 (720p)
   └─ 프레임 추출 (1fps)
   └─ 음성 추출
   ↓
👁️ [Vision 분석]
   └─ 프레임 분석
   └─ 시각자료 감지
   └─ 교사 움직임 추적
   ↓
🎤 [Audio 분석]
   ├─ [STT] 음성 → 텍스트 변환
   ├─ [Speech Rate] 말하기 속도 분석
   ├─ [Emotion] 감정 분석 (톤, 강도)
   └─ [Silence] 침묵 구간 분석
   ↓
🧠 [자연어 처리]
   └─ 텍스트 질의응답 분석
   └─ 학생 참여 언어 분석
   ↓
📊 [7차원 점수 산출]
   ↓
⭐ [최종 등급 부여] (A+ ~ D)
   ↓
📝 [보고서 생성]
   └─ HTML
   └─ Markdown
   └─ JSON
   └─ CSV
```

### 2. 캐싱 메커니즘

자주 사용되는 분석은 캐시되어 속도가 빨라집니다:

```python
from core.config import get_cache
cache = get_cache()

# 캐시에서 조회
cached = cache.get('analysis_key')

# 캐시에 저장
cache.set('analysis_key', result)
```

### 3. 배치 처리

대량의 영상을 동시에 처리:

```python
from scripts.batch_analysis_18videos import main

# 18개 영상 배치 처리
results = main()
```

---

## FAQ

### Q1. 분석이 너무 오래 걸려요
**A**: 
- GPU 사용 여부 확인: 약 5분 (GPU) vs 20분 (CPU)
- FFmpeg 설치 확인
- RAM 메모리 상태 확인

### Q2. 영상이 지원되지 않습니다
**A**: 
지원 형식:
- MP4 (H.264 코덱)
- AVI
- MOV
- MKV

FFmpeg로 변환:
```bash
ffmpeg -i input.webm -c:v libx264 -c:a aac output.mp4
```

### Q3. 보고서 HTML이 열리지 않습니다
**A**:
1. 다른 브라우저 시도 (Chrome, Edge, Firefox)
2. VS Code Live Server 사용:
   ```bash
   # 확장 설치: Live Server
   # HTML 파일 우클릭 → Open with Live Server
   ```

### Q4. 특정 영상만 분석하고 싶어요
**A**:
```bash
# enhanced_demo_analysis.py 사용
python scripts/enhanced_demo_analysis.py "path/to/your/video.mp4"
```

### Q5. API를 외부에서 접근하고 싶어요
**A**:
```bash
# 모든 인터페이스에서 리스닝
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

### Q6. 결과를 엑셀 파일로 내보내고 싶어요
**A**:
```python
import pandas as pd
import json

# JSON 파일 읽기
with open('batch_results.json') as f:
    data = json.load(f)

# DataFrame으로 변환
df = pd.DataFrame(data)

# Excel 저장
df.to_excel('results.xlsx', index=False)
```

### Q7. 특정 차원의 점수만 보고 싶어요
**A**:
```bash
# CSV 파일에서 필터링
python -c "
import pandas as pd
df = pd.read_csv('batch_summary.csv')
print(df[['class_name', 'lecture_expertise', 'teaching_methodology']])
"
```

### Q8. 커스텀 분석지표를 추가하고 싶어요
**A**:

`core/analyzers/turbo_analyzer.py` 수정:

```python
def calculate_custom_score(self, video_data):
    # 커스텀 로직 추가
    custom_score = ...
    return custom_score
```

---

## 다음 단계

1. **[SETUP.md](SETUP.md)** - 설치 문제
2. **[API.md](API.md)** - API 상세 문서
3. **샘플 실행**: `python scripts/batch_analysis_18videos.py`
4. **보고서 확인**: 생성된 HTML 파일 열기

---

**마지막 업데이트**: 2026년 2월 7일  
**버전**: 3.0.0
