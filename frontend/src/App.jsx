import './App.css'

function App() {
  return (
    <div className="App">
      <header>
        <h1>🎓 GAIM Lab v3.0</h1>
        <p>AI 기반 교육 수업 분석 플랫폼</p>
        <p className="info">
          스크립트를 실행하여 분석을 시작하세요:<br/>
          <code>python scripts/batch_analysis_18videos.py</code>
        </p>
      </header>
      
      <main>
        <section>
          <h2>📊 분석 기능</h2>
          <ul>
            <li>18개 교실 수업 영상 배치 분석</li>
            <li>7차원 다중 평가 체계</li>
            <li>자동 보고서 생성</li>
            <li>대시보드 시각화</li>
          </ul>
        </section>

        <section>
          <h2>🚀 빠른 시작</h2>
          <ol>
            <li>requirements.txt에서 의존성 설치: <code>pip install -r requirements.txt</code></li>
            <li>배치 분석 실행: <code>python scripts/batch_analysis_18videos.py</code></li>
            <li>생성된 보고서 확인: <code>output/batch_analysis_*/최종_통합_보고서.html</code></li>
          </ol>
        </section>

        <section>
          <h2>📚 가이드</h2>
          <ul>
            <li><a href="./docs/SETUP.md">설치 가이드</a></li>
            <li><a href="./docs/USAGE.md">사용 설명서</a></li>
            <li><a href="./README.md">프로젝트 개요</a></li>
          </ul>
        </section>
      </main>

      <footer>
        <p>© 2026 경인교육대학교 GAIM Lab | MIT License</p>
      </footer>
    </div>
  )
}

export default App
