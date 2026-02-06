"""
기본 분석기
"""

class BaseAnalyzer:
    """기본 분석기 클래스"""
    
    def __init__(self):
        self.name = "GAIM Lab Analyzer"
    
    def analyze(self, video_path):
        """영상 분석"""
        return {
            "status": "completed",
            "message": "분석 완료"
        }
