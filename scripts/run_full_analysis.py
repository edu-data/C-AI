"""
통합 분석 및 리포트 생성 스크립트
GAIM Lab v3.0 - 모든 기능을 한 번에 실행
"""

import sys
import json
from pathlib import Path

# 경로 설정
PROJECT_ROOT = Path(__file__).parent.parent


def main():
    """메인 실행 함수"""
    
    print("=" * 80)
    print("🎓 GAIM Lab v3.0 - 통합 분석 및 리포트 생성")
    print("=" * 80)
    
    # 1. 배치 분석 실행
    print("\n[1/4] 📊 배치 분석 실행 중...")
    try:
        from scripts.batch_analysis_18videos import main as batch_main
        dashboard_path = batch_main()
        print("✅ 배치 분석 완료!")
    except Exception as e:
        print(f"❌ 배치 분석 오류: {e}")
        return
    
    # batch_results.json 파일 찾기
    output_dirs = list((PROJECT_ROOT / "output").glob("batch_analysis_*"))
    if not output_dirs:
        print("❌ output 디렉토리에 분석 결과가 없습니다.")
        return
    
    latest_output = max(output_dirs, key=lambda p: p.stat().st_mtime)
    results_file = latest_output / "batch_results.json"
    
    if not results_file.exists():
        print(f"❌ {results_file} 파일을 찾을 수 없습니다.")
        return
    
    with open(results_file, encoding="utf-8") as f:
        results = json.load(f)
    
    print(f"📂 분석 결과 디렉토리: {latest_output}")
    
    # 2. 고급 분석 실행
    print("\n[2/4] 🔬 고급 분석 실행 중...")
    try:
        from scripts.advanced_analyzer import AdvancedAnalyzer
        
        analyzer = AdvancedAnalyzer(results)
        
        # 분석 결과 출력
        print("\n📊 교사 성과 순위:")
        for rank in analyzer.get_teacher_ranking():
            print(f"  {rank['순위']}. {rank['교사명']:10s} - {rank['평균점수']:.1f}점 ({rank['수업_개수']}개)")
        
        print("\n📚 과목별 비교:")
        for subject, stats in analyzer.get_subject_comparison().items():
            print(f"  {subject}: {stats['평균_점수']:.1f}점 (개수: {stats['영상_개수']})")
        
        print("\n⚠️  개선 필요 영역 TOP 3:")
        improvements = analyzer.get_improvement_areas()
        for idx, (dim, stats) in enumerate(list(improvements.items())[:3], 1):
            print(f"  {idx}. {dim.replace('_', ' ')}: {stats['평균']:.1f}점")
        
        # JSON 저장
        advanced_results = analyzer.export_all_analysis(str(latest_output))
        print("✅ 고급 분석 완료!")
        
    except Exception as e:
        print(f"❌ 고급 분석 오류: {e}")
        import traceback
        traceback.print_exc()
    
    # 3. 다중 형식 리포트 생성
    print("\n[3/4] 📄 다중 형식 리포트 생성 중...")
    try:
        from scripts.report_generator import ReportGenerator
        
        generator = ReportGenerator(results, str(latest_output))
        
        # Excel 리포트
        excel_result = generator.generate_excel_report("advanced_analysis_report.xlsx")
        print(excel_result)
        
        # PDF 리포트 (선택)
        try:
            pdf_result = generator.generate_pdf_report("advanced_analysis_report.pdf")
            print(pdf_result)
        except ImportError:
            print("⚠️  PDF 생성을 위해서는 'pip install reportlab' 실행 필요")
        
        # PowerPoint 리포트 (선택)
        try:
            ppt_result = generator.generate_powerpoint_report("advanced_analysis_report.pptx")
            print(ppt_result)
        except ImportError:
            print("⚠️  PowerPoint 생성을 위해서는 'pip install python-pptx' 실행 필요")
        
        print("✅ 리포트 생성 완료!")
        
    except Exception as e:
        print(f"❌ 리포트 생성 오류: {e}")
        import traceback
        traceback.print_exc()
    
    # 4. 최종 요약
    print("\n[4/4] 📋 분석 완료 요약")
    print("=" * 80)
    
    print("\n✅ 생성된 파일 목록:")
    print(f"  📊 배치 분석:")
    print(f"     - {latest_output}/batch_results.json")
    print(f"     - {latest_output}/batch_summary.csv")
    print(f"     - {latest_output}/batch_dashboard.html")
    print(f"     - {latest_output}/최종_통합_보고서.html")
    
    print(f"\n  🔬 고급 분석:")
    print(f"     - {latest_output}/advanced_analysis.json")
    
    print(f"\n  📄 다중 형식 리포트:")
    excel_file = latest_output / "advanced_analysis_report.xlsx"
    if excel_file.exists():
        print(f"     - {excel_file}")
    
    pdf_file = latest_output / "advanced_analysis_report.pdf"
    if pdf_file.exists():
        print(f"     - {pdf_file}")
    
    ppt_file = latest_output / "advanced_analysis_report.pptx"
    if ppt_file.exists():
        print(f"     - {ppt_file}")
    
    individual_reports = list((latest_output / "individual_reports").glob("*.md"))
    if individual_reports:
        print(f"\n  📑 개별 분석 보고서:")
        print(f"     - {len(individual_reports)}개 파일 생성됨")
    
    print("\n" + "=" * 80)
    print("🎉 분석 완료!")
    print("=" * 80)
    
    print(f"\n💡 다음 단계:")
    print(f"   1. 📊 대시보드 보기: {latest_output}/batch_dashboard.html")
    print(f"   2. 📄 통합 보고서: {latest_output}/최종_통합_보고서.html")
    print(f"   3. 📋 상세 분석: Excel 또는 CSV 파일 확인")
    print(f"   4. 🎨 웹 UI: npm run dev (frontend 디렉토리에서)")
    
    print("\n📚 문서 참고:")
    print(f"   - docs/SETUP.md: 설치 가이드")
    print(f"   - docs/USAGE.md: 사용 설명서")
    print(f"   - README.md: 프로젝트 개요")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ 사용자에 의해 중단됨")
    except Exception as e:
        print(f"\n\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
