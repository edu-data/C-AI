"""
고급 분석 엔진 - GAIM Lab v3.0
교사별, 학년별, 과목별 심화 분석
"""

import json
from typing import List, Dict
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class AdvancedAnalyzer:
    """고급 분석 기능"""
    
    def __init__(self, results_data: List[Dict]):
        """
        분석 데이터 로드
        
        Args:
            results_data: batch_results.json의 분석 결과
        """
        self.results = results_data
        self.teacher_profiles = self._build_teacher_profiles()
        self.subject_stats = self._build_subject_stats()
        self.grade_stats = self._build_grade_stats()
    
    def _build_teacher_profiles(self) -> Dict:
        """교사별 성과 프로필 구성"""
        profiles = defaultdict(lambda: {
            "count": 0,
            "avg_score": 0,
            "scores": [],
            "dimensions": defaultdict(list),
            "strengths": [],
            "improvements": [],
            "videos": []
        })
        
        for result in self.results:
            teacher = result["teacher"]
            profiles[teacher]["count"] += 1
            profiles[teacher]["scores"].append(result["total_score"])
            profiles[teacher]["videos"].append({
                "name": result["video"],
                "score": result["total_score"],
                "grade": result["grade_letter"]
            })
            
            # 각 차원별 점수 수집
            for dim_name, dim_data in result["dimensions"].items():
                profiles[teacher]["dimensions"][dim_name].append(dim_data["score"])
        
        # 평균 계산
        for teacher, profile in profiles.items():
            if profile["scores"]:
                profile["avg_score"] = round(sum(profile["scores"]) / len(profile["scores"]), 1)
                
                # 각 차원별 평균
                dim_averages = {}
                for dim_name, scores in profile["dimensions"].items():
                    dim_averages[dim_name] = round(sum(scores) / len(scores), 1)
                
                # 강점 (상위 3개)
                profile["strengths"] = sorted(
                    dim_averages.items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:3]
                
                # 개선점 (하위 2개)
                profile["improvements"] = sorted(
                    dim_averages.items(),
                    key=lambda x: x[1]
                )[:2]
        
        return dict(profiles)
    
    def _build_subject_stats(self) -> Dict:
        """과목별 통계"""
        stats = defaultdict(lambda: {
            "count": 0,
            "scores": [],
            "avg_score": 0,
            "max_score": 0,
            "min_score": 100,
            "teachers": set(),
            "grades": set()
        })
        
        for result in self.results:
            subject = result["subject"]
            stats[subject]["count"] += 1
            stats[subject]["scores"].append(result["total_score"])
            stats[subject]["teachers"].add(result["teacher"])
            stats[subject]["grades"].add(result["grade"])
            
            avg = sum(stats[subject]["scores"]) / len(stats[subject]["scores"])
            stats[subject]["avg_score"] = round(avg, 1)
            stats[subject]["max_score"] = max(stats[subject]["scores"])
            stats[subject]["min_score"] = min(stats[subject]["scores"])
        
        return {k: {**v, "teachers": list(v["teachers"]), "grades": list(v["grades"])} 
                for k, v in stats.items()}
    
    def _build_grade_stats(self) -> Dict:
        """학년별 통계"""
        stats = defaultdict(lambda: {
            "count": 0,
            "scores": [],
            "avg_score": 0,
            "subjects": set()
        })
        
        for result in self.results:
            grade = result["grade"]
            stats[grade]["count"] += 1
            stats[grade]["scores"].append(result["total_score"])
            stats[grade]["subjects"].add(result["subject"])
            
            avg = sum(stats[grade]["scores"]) / len(stats[grade]["scores"])
            stats[grade]["avg_score"] = round(avg, 1)
        
        return {k: {**v, "subjects": list(v["subjects"])} for k, v in stats.items()}
    
    def generate_teacher_report(self, teacher_name: str) -> Dict:
        """특정 교사의 상세 리포트 생성"""
        if teacher_name not in self.teacher_profiles:
            return {"error": f"Teacher '{teacher_name}' not found"}
        
        profile = self.teacher_profiles[teacher_name]
        
        return {
            "teacher": teacher_name,
            "analysis_count": profile["count"],
            "average_score": profile["avg_score"],
            "grade_distribution": self._get_grade_distribution(teacher_name),
            "performance_trend": self._get_performance_trend(teacher_name),
            "strengths": [{"dimension": dim, "score": score} 
                         for dim, score in profile["strengths"]],
            "improvements": [{"dimension": dim, "score": score} 
                            for dim, score in profile["improvements"]],
            "videos": profile["videos"],
            "recommendations": self._generate_recommendations(teacher_name)
        }
    
    def _get_grade_distribution(self, teacher_name: str) -> Dict:
        """등급 분포"""
        profile = self.teacher_profiles[teacher_name]
        grades = defaultdict(int)
        
        for video in profile["videos"]:
            grade = video["grade"]
            grades[grade] += 1
        
        return dict(grades)
    
    def _get_performance_trend(self, teacher_name: str) -> List:
        """성과 추이"""
        profile = self.teacher_profiles[teacher_name]
        return sorted([v["score"] for v in profile["videos"]])
    
    def _generate_recommendations(self, teacher_name: str) -> List[str]:
        """맞춤형 권장사항"""
        profile = self.teacher_profiles[teacher_name]
        recommendations = []
        
        # 개선 영역 분석
        if profile["improvements"]:
            worst_dim = profile["improvements"][0][0]
            recommendations.append(
                f"'{worst_dim}' 영역 개선을 위해 전문 연수 참여 권장"
            )
        
        # 강점 활용
        if profile["strengths"]:
            best_dim = profile["strengths"][0][0]
            recommendations.append(
                f"우수한 '{best_dim}' 능력을 다른 영역에도 적극 활용하세요"
            )
        
        # 평균 점수에 따른 권장사항
        avg = profile["avg_score"]
        if avg >= 85:
            recommendations.append("현재 수준을 유지하면서 심화 교수 기법 개발 권장")
        elif avg >= 80:
            recommendations.append("1-2개 영역 집중 개선으로 A급 강사 도달 가능")
        else:
            recommendations.append("종합적인 수업 컨설팅을 통한 개선 계획 수립 필요")
        
        return recommendations
    
    def get_subject_comparison(self) -> Dict:
        """과목별 비교 분석"""
        comparison = {}
        
        for subject, stats in self.subject_stats.items():
            comparison[subject] = {
                "영상_개수": stats["count"],
                "평균_점수": stats["avg_score"],
                "최고_점수": stats["max_score"],
                "최저_점수": stats["min_score"],
                "교사_수": len(stats["teachers"]),
                "학년": stats["grades"]
            }
        
        return comparison
    
    def get_teacher_ranking(self) -> List[Dict]:
        """교사 성과 순위"""
        ranking = []
        
        for teacher, profile in sorted(
            self.teacher_profiles.items(),
            key=lambda x: x[1]["avg_score"],
            reverse=True
        ):
            ranking.append({
                "순위": len(ranking) + 1,
                "교사명": teacher,
                "평균점수": profile["avg_score"],
                "수업_개수": profile["count"],
                "등급분포": self._get_grade_distribution(teacher)
            })
        
        return ranking
    
    def get_improvement_areas(self) -> Dict:
        """전체 개선 필요 영역"""
        dim_scores = defaultdict(list)
        
        for result in self.results:
            for dim_name, dim_data in result["dimensions"].items():
                dim_scores[dim_name].append(dim_data["score"])
        
        improvements = {}
        for dim_name, scores in dim_scores.items():
            avg = sum(scores) / len(scores)
            improvements[dim_name] = {
                "평균": round(avg, 1),
                "최고": max(scores),
                "최저": min(scores),
                "표준편차": round(self._calculate_std_dev(scores), 1)
            }
        
        return dict(sorted(improvements.items(), key=lambda x: x[1]["평균"]))
    
    @staticmethod
    def _calculate_std_dev(values: List[float]) -> float:
        """표준편차 계산"""
        if len(values) < 2:
            return 0
        
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance ** 0.5
    
    def export_all_analysis(self, output_path: str) -> Dict:
        """모든 분석 결과 내보내기"""
        output = {
            "분석_일시": datetime.now().isoformat(),
            "분석_영상_수": len(self.results),
            "교사_성과_순위": self.get_teacher_ranking(),
            "과목별_비교": self.get_subject_comparison(),
            "개선_필요_영역": self.get_improvement_areas(),
            "교사별_상세_리포트": {
                teacher: self.generate_teacher_report(teacher)
                for teacher in self.teacher_profiles.keys()
            }
        }
        
        # JSON으로 저장
        output_file = Path(output_path) / "advanced_analysis.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        return output


if __name__ == "__main__":
    # 테스트
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    # batch_results.json 로드
    results_file = Path(__file__).parent.parent / "output" / "batch_analysis_20260207_005428" / "batch_results.json"
    
    if results_file.exists():
        with open(results_file, encoding="utf-8") as f:
            results = json.load(f)
        
        analyzer = AdvancedAnalyzer(results)
        
        print("=" * 70)
        print("🎓 고급 분석 결과")
        print("=" * 70)
        
        print("\n📊 교사 성과 순위:")
        for rank in analyzer.get_teacher_ranking():
            print(f"  {rank['순위']}. {rank['교사명']:10s} - {rank['평균점수']:.1f}점 ({rank['수업_개수']}개)")
        
        print("\n📚 과목별 비교:")
        for subject, stats in analyzer.get_subject_comparison().items():
            print(f"  {subject}: {stats['평균_점수']:.1f}점 (개수: {stats['영상_개수']})")
        
        print("\n⚠️  개선 필요 영역:")
        for dim, stats in analyzer.get_improvement_areas().items():
            print(f"  {dim.replace('_', ' ')}: {stats['평균']:.1f}점")
    else:
        print("❌ batch_results.json 파일을 찾을 수 없습니다.")
