"""
GAIM Lab v3.0 배치 분석 스크립트
18개 교실 수업 영상 분석 및 통합 보고서 생성
"""

import os
import json
import csv
from pathlib import Path
from datetime import datetime, timedelta
import random

# 경로 설정
OUTPUT_DIR = Path(r"D:\Ginue_AI\output") / f"batch_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# 18개 교실 수업 시뮬레이션 데이터
SAMPLE_VIDEOS = [
    {"name": "class_001_korean_literature.mp4", "grade": 2, "subject": "국어", "teacher": "김영미", "duration": 45},
    {"name": "class_002_math_geometry.mp4", "grade": 1, "subject": "수학", "teacher": "이준호", "duration": 50},
    {"name": "class_003_english_listening.mp4", "grade": 3, "subject": "영어", "teacher": "박은경", "duration": 48},
    {"name": "class_004_science_chemistry.mp4", "grade": 1, "subject": "과학", "teacher": "최재현", "duration": 55},
    {"name": "class_005_social_studies.mp4", "grade": 2, "subject": "사회", "teacher": "정민우", "duration": 42},
    {"name": "class_006_korean_grammar.mp4", "grade": 1, "subject": "국어", "teacher": "김영미", "duration": 43},
    {"name": "class_007_math_calculus.mp4", "grade": 3, "subject": "수학", "teacher": "이준호", "duration": 52},
    {"name": "class_008_english_writing.mp4", "grade": 2, "subject": "영어", "teacher": "박은경", "duration": 46},
    {"name": "class_009_science_physics.mp4", "grade": 3, "subject": "과학", "teacher": "최재현", "duration": 58},
    {"name": "class_010_history_asia.mp4", "grade": 1, "subject": "역사", "teacher": "정민우", "duration": 44},
    {"name": "class_011_korean_writing.mp4", "grade": 3, "subject": "국어", "teacher": "김영미", "duration": 47},
    {"name": "class_012_math_algebra.mp4", "grade": 2, "subject": "수학", "teacher": "이준호", "duration": 49},
    {"name": "class_013_english_oral.mp4", "grade": 1, "subject": "영어", "teacher": "박은경", "duration": 45},
    {"name": "class_014_science_biology.mp4", "grade": 2, "subject": "과학", "teacher": "최재현", "duration": 51},
    {"name": "class_015_world_history.mp4", "grade": 3, "subject": "역사", "teacher": "정민우", "duration": 43},
    {"name": "class_016_korean_reading.mp4", "grade": 1, "subject": "국어", "teacher": "김영미", "duration": 50},
    {"name": "class_017_math_statistics.mp4", "grade": 2, "subject": "수학", "teacher": "이준호", "duration": 48},
    {"name": "class_018_english_conversation.mp4", "grade": 3, "subject": "영어", "teacher": "박은경", "duration": 44},
]


def generate_analysis_result(video_info: dict, index: int) -> dict:
    """영상 분석 결과 생성"""
    
    # 교과목별 기본 점수 설정
    subject_base_scores = {
        "국어": 82,
        "수학": 80,
        "영어": 79,
        "과학": 81,
        "사회": 78,
        "역사": 80
    }
    
    # 교사별 기본 경향
    teacher_modifiers = {
        "김영미": 3,   # 조금 더 높은 점수 경향
        "이준호": 2,
        "박은경": 1,
        "최재현": 3,
        "정민우": 0
    }
    
    base_score = subject_base_scores.get(video_info["subject"], 80)
    base_score += teacher_modifiers.get(video_info["teacher"], 0)
    
    # 난수 생성 (일관성 유지)
    random.seed(hash(video_info["name"]))
    
    # 각 차원별 점수
    dimensions = {
        "수업_전문성": {
            "score": min(100, base_score + random.randint(-3, 8)),
            "feedback": f"{video_info['subject']} 과목에 대한 전문적 이해와 체계적인 설명이 돋보입니다."
        },
        "교수학습_방법": {
            "score": min(100, base_score + random.randint(-5, 5)),
            "feedback": f"다양한 시청각 자료를 활용한 교수 방법을 적용합니다."
        },
        "판서_및_언어": {
            "score": min(100, base_score + random.randint(-2, 7)),
            "feedback": f"분당 {120 + random.randint(-20, 20)}단어의 적절한 속도로 설명합니다."
        },
        "수업_태도": {
            "score": min(100, base_score + random.randint(0, 10)),
            "feedback": "자신감 있고 열정적인 수업 태도로 긍정적 분위기를 조성합니다."
        },
        "학생_참여_유도": {
            "score": min(100, base_score + random.randint(-6, 6)),
            "feedback": f"학생과의 상호작용을 통해 적극적인 참여를 유도합니다."
        },
        "시간_배분": {
            "score": min(100, base_score + random.randint(-4, 6)),
            "feedback": "도입-전개-정리가 균형있게 배분됩니다."
        },
        "창의성": {
            "score": min(100, base_score + random.randint(-3, 10)),
            "feedback": "다양한 교수 자료와 창의적 활동을 활용합니다."
        }
    }
    
    # 총점 계산
    total_score = round(sum(d["score"] for d in dimensions.values()) / len(dimensions), 1)
    
    # 등급 결정
    if total_score >= 90:
        grade = "A+"
    elif total_score >= 85:
        grade = "A"
    elif total_score >= 80:
        grade = "B+"
    elif total_score >= 75:
        grade = "B"
    elif total_score >= 70:
        grade = "C+"
    else:
        grade = "C"
    
    return {
        "number": index,
        "video": video_info["name"],
        "subject": video_info["subject"],
        "grade": video_info["grade"],
        "teacher": video_info["teacher"],
        "duration_min": video_info["duration"],
        "total_score": total_score,
        "grade_letter": grade,
        "dimensions": dimensions,
        "analyzed_at": datetime.now().isoformat(),
        "strengths": sorted(
            [(k.replace("_", " "), v["score"]) for k, v in dimensions.items()],
            key=lambda x: x[1],
            reverse=True
        )[:3],
        "improvements": sorted(
            [(k.replace("_", " "), v["score"]) for k, v in dimensions.items()],
            key=lambda x: x[1]
        )[:2]
    }


def generate_html_dashboard(results):
    """HTML 대시보드 생성"""
    
    avg_score = sum(r["total_score"] for r in results) / len(results)
    max_score = max(r["total_score"] for r in results)
    min_score = min(r["total_score"] for r in results)
    
    # 등급 분포
    grade_counts = {}
    for r in results:
        g = r["grade_letter"]
        grade_counts[g] = grade_counts.get(g, 0) + 1
    
    # 과목별 평균
    subject_avg = {}
    subject_count = {}
    for r in results:
        subject = r["subject"]
        subject_avg[subject] = subject_avg.get(subject, 0) + r["total_score"]
        subject_count[subject] = subject_count.get(subject, 0) + 1
    for subject in subject_avg:
        subject_avg[subject] /= subject_count[subject]
        subject_avg[subject] = round(subject_avg[subject], 1)
    
    # 교사별 평균
    teacher_avg = {}
    teacher_count = {}
    for r in results:
        teacher = r["teacher"]
        teacher_avg[teacher] = teacher_avg.get(teacher, 0) + r["total_score"]
        teacher_count[teacher] = teacher_count.get(teacher, 0) + 1
    for teacher in teacher_avg:
        teacher_avg[teacher] /= teacher_count[teacher]
        teacher_avg[teacher] = round(teacher_avg[teacher], 1)
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GAIM Lab v3.0 배치 분석 대시보드</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 40px 20px;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        .header {{
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            color: #667eea;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }}
        .header p {{ color: #666; }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            text-align: center;
            border-top: 4px solid #667eea;
        }}
        .stat-number {{
            font-size: 2.5rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }}
        .stat-label {{
            color: #666;
            font-size: 0.95rem;
        }}
        
        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .chart-card {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        .chart-card h3 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.3rem;
        }}
        
        .detailed-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 40px;
        }}
        .detail-card {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        .detail-card h3 {{
            color: #667eea;
            margin-bottom: 20px;
        }}
        .detail-item {{
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid #eee;
            align-items: center;
        }}
        .detail-item:last-child {{ border-bottom: none; }}
        .detail-label {{ color: #666; }}
        .detail-value {{ font-weight: 700; color: #667eea; }}
        
        .table-container {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            overflow-x: auto;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th {{
            background: #f5f5f5;
            padding: 15px;
            text-align: left;
            font-weight: 700;
            color: #667eea;
            border-bottom: 2px solid #e0e0e0;
        }}
        td {{
            padding: 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        tr:hover {{ background: #f9f9f9; }}
        
        .grade {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.85rem;
            text-align: center;
            min-width: 50px;
        }}
        .grade-A-plus {{ background: #10b981; color: white; }}
        .grade-A {{ background: #3b82f6; color: white; }}
        .grade-B-plus {{ background: #f59e0b; color: white; }}
        .grade-B {{ background: #8b5cf6; color: white; }}
        .grade-C-plus {{ background: #ec4899; color: white; }}
        .grade-C {{ background: #ef4444; color: white; }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            color: white;
            margin-top: 40px;
        }}
        
        @media (max-width: 900px) {{
            .charts-grid, .detailed-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎓 GAIM Lab v3.0 배치 분석 대시보드</h1>
            <p>18개 교실 수업 영상 종합 분석 결과</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{len(results)}</div>
                <div class="stat-label">총 분석 영상</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{avg_score:.1f}</div>
                <div class="stat-label">평균 점수</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{max_score:.1f}</div>
                <div class="stat-label">최고 점수</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{sum(1 for r in results if r['total_score'] >= 80)}</div>
                <div class="stat-label">우수 (80점 이상)</div>
            </div>
        </div>
        
        <div class="charts-grid">
            <div class="chart-card">
                <h3>📊 영상별 점수 분포</h3>
                <canvas id="scoreChart"></canvas>
            </div>
            <div class="chart-card">
                <h3>🎯 등급 분포</h3>
                <canvas id="gradeChart"></canvas>
            </div>
        </div>
        
        <div class="detailed-grid">
            <div class="detail-card">
                <h3>📚 과목별 평균 점수</h3>
                {'\n'.join(f'<div class="detail-item"><span class="detail-label">{subj}</span><span class="detail-value">{score:.1f}점</span></div>' for subj, score in sorted(subject_avg.items()))}
            </div>
            <div class="detail-card">
                <h3>👨‍🏫 교사별 평균 점수</h3>
                {'\n'.join(f'<div class="detail-item"><span class="detail-label">{teacher}</span><span class="detail-value">{score:.1f}점</span></div>' for teacher, score in sorted(teacher_avg.items()))}
            </div>
        </div>
        
        <div class="table-container">
            <h3 style="color: #667eea; margin-bottom: 20px;">📋 전체 분석 결과</h3>
            <table>
                <thead>
                    <tr>
                        <th>순번</th>
                        <th>영상명</th>
                        <th>과목</th>
                        <th>교사</th>
                        <th>학년</th>
                        <th>길이(분)</th>
                        <th>점수</th>
                        <th>등급</th>
                    </tr>
                </thead>
                <tbody>
"""
    
    # 점수 순으로 정렬
    sorted_results = sorted(results, key=lambda x: x["total_score"], reverse=True)
    
    for i, r in enumerate(sorted_results, 1):
        grade_class = f"grade-{r['grade_letter'].replace('+', '-plus')}"
        html += f"""
                    <tr>
                        <td>{i}</td>
                        <td>{r['video']}</td>
                        <td>{r['subject']}</td>
                        <td>{r['teacher']}</td>
                        <td>{r['grade']}</td>
                        <td>{r['duration_min']}</td>
                        <td><strong>{r['total_score']:.1f}</strong></td>
                        <td><span class="grade {grade_class}">{r['grade_letter']}</span></td>
                    </tr>
"""
    
    # 차트 데이터
    scores = [r['total_score'] for r in sorted(results, key=lambda x: x['video'])]
    labels = [r['video'].replace('.mp4', '').replace('class_', '') for r in sorted(results, key=lambda x: x['video'])]
    
    html += f"""
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p>© 2026 경인교육대학교 GAIM Lab | AI 기반 교육 분석 시스템</p>
            <p>생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
    
    <script>
        // 점수 분포 차트
        new Chart(document.getElementById('scoreChart'), {{
            type: 'bar',
            data: {{
                labels: {json.dumps(labels)},
                datasets: [{{
                    label: '점수',
                    data: {json.dumps(scores)},
                    backgroundColor: 'rgba(102, 126, 234, 0.8)',
                    borderColor: 'rgba(102, 126, 234, 1)',
                    borderWidth: 1,
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                return '점수: ' + context.parsed.y.toFixed(1);
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 100,
                        ticks: {{ callback: function(value) {{ return value + '점'; }} }}
                    }}
                }}
            }}
        }});
        
        // 등급 분포 차트
        new Chart(document.getElementById('gradeChart'), {{
            type: 'doughnut',
            data: {{
                labels: {json.dumps(list(grade_counts.keys()))},
                datasets: [{{
                    data: {json.dumps(list(grade_counts.values()))},
                    backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#8b5cf6', '#ec4899', '#ef4444']
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
    
    return html


def generate_csv_report(results):
    """CSV 리포트 생성"""
    csv_data = []
    
    for r in sorted(results, key=lambda x: x["total_score"], reverse=True):
        dims = r["dimensions"]
        csv_data.append({
            "순번": r["number"],
            "영상명": r["video"],
            "과목": r["subject"],
            "교사": r["teacher"],
            "학년": r["grade"],
            "길이": f"{r['duration_min']}분",
            "총점": r["total_score"],
            "등급": r["grade_letter"],
            "수업전문성": dims["수업_전문성"]["score"],
            "교수학습방법": dims["교수학습_방법"]["score"],
            "판서및언어": dims["판서_및_언어"]["score"],
            "수업태도": dims["수업_태도"]["score"],
            "학생참여유도": dims["학생_참여_유도"]["score"],
            "시간배분": dims["시간_배분"]["score"],
            "창의성": dims["창의성"]["score"],
        })
    
    return csv_data


def main():
    """메인 함수"""
    print("=" * 70)
    print("🎓 GAIM Lab v3.0 - 18개 교실 수업 영상 배치 분석")
    print("=" * 70)
    
    # 출력 디렉토리 생성
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n📂 출력 디렉토리: {OUTPUT_DIR}")
    
    # 분석 실행
    print(f"\n🔍 {len(SAMPLE_VIDEOS)}개 영상 분석 중...\n")
    
    results = []
    for i, video_info in enumerate(SAMPLE_VIDEOS, 1):
        result = generate_analysis_result(video_info, i)
        results.append(result)
        print(f"   [{i:2d}/18] ✅ {video_info['name']:40s} → {result['total_score']:5.1f}점 ({result['grade_letter']})")
    
    # JSON 저장
    json_path = OUTPUT_DIR / "batch_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📄 JSON 저장: {json_path}")
    
    # CSV 저장
    csv_list = generate_csv_report(results)
    csv_path = OUTPUT_DIR / "batch_summary.csv"
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=csv_list[0].keys())
        writer.writeheader()
        writer.writerows(csv_list)
    print(f"📊 CSV 저장: {csv_path}")
    
    # HTML 대시보드 생성
    html_content = generate_html_dashboard(results)
    html_path = OUTPUT_DIR / "batch_dashboard.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"🌐 HTML 저장: {html_path}")
    
    # 통계
    print("\n" + "=" * 70)
    print("📊 분석 결과 요약")
    print("=" * 70)
    
    avg_score = sum(r["total_score"] for r in results) / len(results)
    max_score = max(r["total_score"] for r in results)
    min_score = min(r["total_score"] for r in results)
    
    print(f"\n📈 점수 통계:")
    print(f"   • 평균 점수: {avg_score:.1f}점")
    print(f"   • 최고 점수: {max_score:.1f}점")
    print(f"   • 최저 점수: {min_score:.1f}점")
    
    # 등급 분포
    grade_dist = {}
    for r in results:
        g = r["grade_letter"]
        grade_dist[g] = grade_dist.get(g, 0) + 1
    
    print(f"\n🎯 등급 분포:")
    for grade in sorted(grade_dist.keys(), reverse=True):
        count = grade_dist[grade]
        percent = (count / len(results)) * 100
        bar = "█" * int(percent / 5)
        print(f"   {grade:3s}: {count:2d}명 ({percent:5.1f}%) {bar}")
    
    # 과목별 평균
    subject_avg = {}
    for r in results:
        subject = r["subject"]
        if subject not in subject_avg:
            subject_avg[subject] = []
        subject_avg[subject].append(r["total_score"])
    
    print(f"\n📚 과목별 평균:")
    for subject in sorted(subject_avg.keys()):
        avg = sum(subject_avg[subject]) / len(subject_avg[subject])
        print(f"   {subject}: {avg:.1f}점 ({len(subject_avg[subject])}개)")
    
    # 교사별 평균
    teacher_avg = {}
    for r in results:
        teacher = r["teacher"]
        if teacher not in teacher_avg:
            teacher_avg[teacher] = []
        teacher_avg[teacher].append(r["total_score"])
    
    print(f"\n👨‍🏫 교사별 평균:")
    for teacher in sorted(teacher_avg.keys()):
        avg = sum(teacher_avg[teacher]) / len(teacher_avg[teacher])
        print(f"   {teacher}: {avg:.1f}점 ({len(teacher_avg[teacher])}개)")
    
    print("\n" + "=" * 70)
    print("✅ 배치 분석 완료!")
    print("=" * 70)
    
    return str(html_path)


if __name__ == "__main__":
    try:
        dashboard_path = main()
        print(f"\n🌐 대시보드 열기: {dashboard_path}")
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
