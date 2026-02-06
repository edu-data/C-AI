# GAIM Lab v3.0 - 설치 가이드

이 가이드는 GAIM Lab v3.0을 로컬 환경에 설치하는 방법을 단계별로 설명합니다.

## 📋 목차

1. [시스템 요구사항](#시스템-요구사항)
2. [기타 의존성](#기타-의존성)
3. [설치 단계](#설치-단계)
4. [검증](#검증)
5. [문제 해결](#문제-해결)

---

## 시스템 요구사항

### 하드웨어
| 항목 | 최소 | 권장 |
|------|------|------|
| **CPU** | Intel i5 / AMD Ryzen 5 | Intel i7 / AMD Ryzen 7+ |
| **RAM** | 8GB | 16GB+ |
| **저장소** | 10GB SSD | 20GB+ SSD |
| **GPU** | 옵션 | NVIDIA CUDA (선택) |

### 소프트웨어
- **Python**: 3.14+ (또는 3.11.x, 3.12.x)
- **pip**: 최신 버전
- **Git**: 버전 관리 (선택)
- **FFmpeg**: 비디오 처리 (권장)

---

## 기타 의존성

### Windows 10/11
```powershell
# FFmpeg 설치 (Chocolatey 이용)
choco install ffmpeg

# 또는 직접 다운로드
# https://ffmpeg.org/download.html
```

### macOS
```bash
# Homebrew로 설치
brew install ffmpeg
brew install portaudio  # pyaudio 필요
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt-get install portaudio19-dev  # pyaudio 필요
sudo apt-get install libssl-dev libffi-dev python3-dev
```

---

## 설치 단계

### 1단계: 저장소 복제

```bash
git clone https://github.com/yourname/gaim-lab-v3.git
cd gaim-lab-v3
```

또는 ZIP으로 다운로드 후 압축 해제

### 2단계: Python 가상 환경 생성

#### Windows
```powershell
# PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

# 또는 Command Prompt
python -m venv .venv
.venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**가상 환경 활성화 확인**: 터미널 앞에 `(.venv)`가 표시되어야 함

### 3단계: pip 업그레이드 (선택)

```bash
pip install --upgrade pip setuptools wheel
```

### 4단계: 의존성 설치

```bash
pip install -r requirements.txt
```

**설치 시간**: 약 10-15분 (네트워크 속도에 따라 가변)

### 5단계: 추가 설정 (선택)

#### 5-1. PyAudio 문제 해결 (Windows)

Windows에서 `pyaudio` 설치 실패 시:

```bash
# 방법 1: 바이너리 파일 사용
pip install pipwin
pipwin install pyaudio

# 방법 2: Conda 사용
conda install -c conda-forge pyaudio
```

#### 5-2. CUDA 지원 (GPU 가속)

NVIDIA GPU가 있는 경우:

```bash
# CUDA 12.4 지원 PyTorch 설치
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

#### 5-3. MPS 지원 (Apple Silicon)

Apple Silicon Mac의 경우:

```bash
# CPU 전용 PyTorch 설치 (MPS는 자동 지원)
pip install torch torchvision torchaudio
```

---

## 검증

### 1. Python 버전 확인

```bash
python --version
```

**출력 예**:
```
Python 3.14.2
```

### 2. 주요 라이브러리 확인

```bash
python -c "
import fastapi; print(f'✓ FastAPI {fastapi.__version__}')
import torch; print(f'✓ PyTorch {torch.__version__}')
import mediapipe; print(f'✓ MediaPipe OK')
from faster_whisper import WhisperModel; print(f'✓ Faster-Whisper OK')
import librosa; print(f'✓ LibROSA {librosa.__version__}')
import cv2; print(f'✓ OpenCV {cv2.__version__}')
"
```

**성공 시**:
```
✓ FastAPI 0.128.2
✓ PyTorch 2.11.0
✓ MediaPipe OK
✓ Faster-Whisper OK
✓ LibROSA 0.11.0
✓ OpenCV 4.13.0.0
```

### 3. 샘플 앱 실행

```bash
# FastAPI 서버 시작
uvicorn backend.app.main:app --reload

# 브라우저 접속
# http://localhost:8000
# http://localhost:8000/docs (API 문서)
```

### 4. 배치 분석 테스트

```bash
python scripts/batch_analysis_18videos.py
```

이 명령은 18개 영상을 분석하고 결과를 생성합니다.

---

## 문제 해결

### 문제 1: ModuleNotFoundError

```
ModuleNotFoundError: No module named 'faster_whisper'
```

**해결책**:
1. 가상 환경이 활성화되어 있는지 확인
2. `pip install faster-whisper` 재실행
3. 파이썬 경로 확인:
   ```bash
   which python  # macOS/Linux
   where python  # Windows
   ```

### 문제 2: FFmpeg를 찾을 수 없음

```
OSError: ffmpeg not found!
```

**해결책**:

#### Windows (Chocolatey)
```powershell
choco install ffmpeg
```

#### Windows (수동)
1. https://ffmpeg.org/download.html에서 다운로드
2. `C:\ffmpeg` 폴더 생성
3. 환경 변수 PATH에 추가

#### macOS
```bash
brew install ffmpeg
```

#### Linux
```bash
sudo apt-get install ffmpeg
```

### 문제 3: PyAudio 설치 실패

```
error: Microsoft Visual C++ 14.0 or greater is required
```

**해결책** (Windows):

```bash
# 방법 1: Visual C++ Build Tools 설치
# https://visualstudio.microsoft.com/downloads/
# → C++ 빌드 도구 설치

# 방법 2: Conda 사용
conda install -c conda-forge pyaudio

# 방법 3: 사전 컴파일 바이너리 사용
pip install pipwin
pipwin install pyaudio
```

### 문제 4: TensorFlow/DeepFace 호환성

```
ERROR: Could not find a version that satisfies the requirement tensorflow
```

**이유**: TensorFlow는 Python 3.14를 아직 지원하지 않음

**해결책**:

#### 옵션 1: InsightFace 사용 (권장)
```bash
pip install insightface
```

#### 옵션 2: Python 3.13으로 다운그레이드
```bash
# Python 3.13 설치 (https://www.python.org/)
python3.13 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

#### 옵션 3: DeepFace 제외
- `scripts/*.py`에서 DeepFace 관련 코드 주석 처리
- MediaPipe 사용으로 대체

### 문제 5: CUDA 관련 오류

```
RuntimeError: CUDA out of memory
```

**해결책**:

```python
# Python 코드에서 CPU 강제 사용
import torch
device = torch.device('cpu')  # GPU 대신 CPU 사용
```

또는:

```bash
# 배치 크기 축소
python scripts/batch_analysis_18videos.py --batch-size 2
```

### 문제 6: 포트 8000 이미 사용 중

```
OSError: [WinError 10048] 주소를 할당할 수 없습니다
```

**해결책**:

```bash
# 다른 포트 사용
uvicorn backend.app.main:app --reload --port 8001

# 또는 기존 프로세스 종료 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### 문제 7: 느린 GPU 또는 OOM

**권장**:

1. **배치 크기 축소**
   - `scripts/batch_analysis_18videos.py`의 `batch_size` 변경

2. **영상 해상도 축소**
   - 입력 영상을 720p 또는 480p로 전처리

3. **CPU 전용 모드**
   ```bash
   export CUDA_VISIBLE_DEVICES=""  # Linux/macOS
   set CUDA_VISIBLE_DEVICES=""     # Windows
   ```

---

## 환경 변수 설정

`.env` 파일 생성 (선택):

```bash
# 파일명: .env

# 서버 설정
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
DEBUG=True

# 데이터베이스
DATABASE_URL=sqlite:///./test.db

# 캐시
REDIS_URL=redis://localhost:6379

# API 키 (필요시)
OPENAI_API_KEY=your_api_key_here
HF_TOKEN=your_huggingface_token

# 분석 설정
MAX_VIDEO_DURATION=3600  # 초단위
MAX_WORKERS=4
OUTPUT_DIR=./output
```

---

## 다음 단계

설치 완료 후:

1. **[USAGE.md](USAGE.md)** - 사용 방법 확인
2. **[API.md](API.md)** - API 문서 읽기
3. **샘플 실행**: `python scripts/batch_analysis_18videos.py`
4. **보고서 확인**: `output/batch_analysis_*/최종_통합_보고서.html`

---

## 버전 관리

### 업그레이드하기

```bash
# 최신 버전 확인
git pull origin main

# 새 의존성 설치
pip install -r requirements.txt --upgrade
```

### 특정 패키지만 업그레이드

```bash
pip install --upgrade torch mediapipe faster-whisper
```

---

## 지원

문제가 발생하면:

1. **README.md** - 소개 및 개요
2. **이 파일 (SETUP.md)** - 설치 문제
3. **TROUBLESHOOTING.md** - 런타임 문제
4. **[GitHub Issues](https://github.com/yourname/gaim-lab-v3/issues)** - 버그 보고

---

**마지막 업데이트**: 2026년 2월 7일  
**버전**: 3.0.0
