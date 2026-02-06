"""
음성 인식 분석기 (Faster-Whisper)
"""

class WhisperAnalyzer:
    """Faster-Whisper 기반 음성 인식"""
    
    def __init__(self):
        self.name = "Faster-Whisper STT"
    
    def transcribe(self, audio_path):
        """음성을 텍스트로 변환"""
        return {
            "transcription": "분석 준비 중...",
            "confidence": 0.95
        }
