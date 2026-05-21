import streamlit as st
import time
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="SafePass AI - 지능형 범죄 예방 시스템",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Styling & CSS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    /* ===== 밝은 테마 - 높은 가독성 ===== */
    .main {
        background-color: #f8fafc;
        color: #1e293b;
    }
    .stApp {
        background-color: #f8fafc;
    }

    /* 사이드바 */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    section[data-testid="stSidebar"] * {
        color: #1e293b !important;
    }

    /* 전체 텍스트 색상 강제 */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
        color: #1e293b;
    }

    /* 헤더 폰트 */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        color: #0f172a !important;
    }

    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .stTabs [data-baseweb="tab"] {
        color: #475569 !important;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        color: #0369a1 !important;
        font-weight: 700;
        border-bottom-color: #0369a1 !important;
    }

    /* 메트릭 카드 */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    [data-testid="stMetricLabel"] {
        color: #475569 !important;
    }
    [data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-weight: 700;
    }

    /* 커스텀 메트릭 카드 클래스 */
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    /* 강조 텍스트 */
    .glow-text-cyan {
        color: #0891b2;
        font-weight: bold;
    }
    .glow-text-emerald {
        color: #059669;
        font-weight: bold;
    }
    .glow-text-red {
        color: #dc2626;
        font-weight: bold;
    }

    /* 코드 블록 */
    .stCodeBlock, code, pre {
        background-color: #f1f5f9 !important;
        color: #334155 !important;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
    }

    /* 마크다운 텍스트 */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span {
        color: #334155 !important;
    }

    /* 라디오/셀렉트박스 */
    .stRadio label, .stSelectbox label {
        color: #1e293b !important;
    }

    /* 버튼 */
    .stButton > button {
        background-color: #0284c7;
        color: #ffffff !important;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1.25rem;
        transition: background-color 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #0369a1;
        color: #ffffff !important;
    }

    /* 알림 박스 텍스트 가독성 */
    .stAlert p, .stAlert span {
        color: inherit !important;
    }

    /* caption 텍스트 */
    .stCaption, small {
        color: #64748b !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("🛡️ SafePass AI")
    st.subheader("지능형 범죄 예방 시스템")
    st.markdown("---")
    
    st.info("💡 **지자체 관제 연동 작동 상태**\n\n🟢 24시간 감시 시스템 가동 중\n\n📍 서울시 강남구 역삼2동 일대")
    st.markdown("---")
    st.caption("© 2026 SafePass AI. 범죄 예방 및 안심 도보 환경 구축 프로젝트.")

# --- Header ---
st.title("🛡️ SafePass AI: 어두운 밤길을 지키는 지능형 안전망")
st.markdown("CCTV 비전 분석 행동 탐지와 스마트폰 오디오 AI 기반 112 연동 안심 귀가 케어 서비스")
st.markdown("---")

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 솔루션 비전 & 핵심 기술", 
    "👁️‍🗨️ CCTV 관제 시뮬레이션", 
    "🎙️ AI 모바일 안심 동행방", 
    "🗺️ 안심 최적 경로 설계", 
    "📰 [기획 보도] 뉴스 기사"
])

# ==========================================
# Tab 1: Vision & Pillars
# ==========================================
with tab1:
    col1, col2 = st.columns([1.2, 0.8])
    with col1:
        st.subheader("외롭고 어두운 밤길, AI가 2중 안전 장치로 지켜 드립니다.")
        st.write(
            "세이프패스 AI는 골목길의 치안 사각지대를 실시간 분석하는 **지능형 CCTV**와, "
            "보행자의 위험을 소리로 감지해 신속한 공조 수사를 도출하는 **모바일 오디오 AI**를 융합하여 "
            "시민들의 일상에 실질적인 범죄 예방 안전망을 구축합니다."
        )
        
        st.markdown("#### 🚀 SafePass AI가 입증한 시범 구역의 성과")
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="안심 구역 내 강력 범죄 감소율", value="98.4%", delta="시범 지구 3달 통계")
        with c2:
            st.metric(label="위기 신고 시 현장 경찰 평균 도착", value="2.5분", delta="-1.5분 단축")
            
    with col2:
        st.markdown("### 🛠️ 3대 핵심 안전 모델")
        st.markdown("🔹 **SafeWatcher AI (CCTV 비전)**: '뒤따름 행위', '배회 행위', '쓰러짐' 실시간 비전 판별 및 가로등 자동 제어.")
        st.markdown("🔹 **Companion AI (이어폰 오디오)**: 주변 환경 데시벨 상시 분석, 돌발 비명 주파수 추적 및 112 원스톱 자동 신고.")
        st.markdown("🔹 **SafeRouter (안심 지도 안내)**: 가로등 밝기밀도, 경찰 Patrol 밀도를 가중치로 한 동적 안전 경로 우선 매핑.")

# ==========================================
# Tab 2: CCTV Watcher Simulation
# ==========================================
with tab2:
    st.subheader("👁️‍🗨️ CCTV 관제 센터 실시간 비전 분석 시뮬레이터")
    st.write("의심 대상 출현 및 뒤따름 시나리오를 가동해 관제 센터의 지능형 통제를 실현해 보세요.")
    
    col_cctv1, col_cctv2 = st.columns([1, 1])
    
    with col_cctv1:
        st.markdown("#### 📺 모의 카메라 뷰포트 (CAM-042 역삼동 골목)")
        
        # State indicators
        cctv_state = st.radio(
            "시뮬레이션 단계를 선택해 주세요:",
            ["1단계: 평화로운 일상 도보", "2단계: 배회자 골목 초입 출현", "3단계: 뒤따름(스토킹) 위협 고조"]
        )
        
        if cctv_state == "1단계: 평화로운 일상 도보":
            st.success("🟢 보행자 안전 도보 감지됨 - CCTV 가로등 조도 30% 야간 절전 모드 유지")
        elif cctv_state == "2단계: 배회자 골목 초입 출현":
            st.warning("🟡 주의: 거동이 다소 수상한 배회 대상 포착. 비전 트래킹 프레임 추적 고정 가동.")
        elif cctv_state == "3단계: 뒤따름(스토킹) 위협 고조":
            st.error("🚨 위험!! 뒤따름 행동 패턴 감지! 보행자 간 거리 3.0m 근접. 궤적 동기화 98% 돌파.")
            st.markdown(
                "<span style='color:#fd3a4a; font-size:24px; font-weight:bold; animation:pulse 1s infinite;'>"
                "🔥 스마트 안심 가로등 조도 100% 극대화 가동 & 경고 음성 자동 송출</span>", 
                unsafe_allow_html=True
            )
            
    with col_cctv2:
        st.markdown("#### 📊 관제 대시보드 및 지능형 로그 분석")
        
        if cctv_state == "1단계: 평화로운 일상 도보":
            st.metric(label="뒤따름 위협 지수", value="5%", delta="정상 범주")
            st.metric(label="가로등 밝기 상태", value="30% (절전 조명)")
            st.code("[12:00:00] 시스템 정상 부팅 완료\n[12:00:05] 보행자 1인 감지 - 안전 도보 진행 중")
        elif cctv_state == "2단계: 배회자 골목 초입 출현":
            st.metric(label="뒤따름 위협 지수", value="35%", delta="+30% 급증")
            st.metric(label="가로등 밝기 상태", value="30% (절전 조명)")
            st.code("[12:00:00] 시스템 정상 부팅 완료\n[12:02:15] 배회 의심 대상 탐지 (CAM-042 골목 북서편)")
        elif cctv_state == "3단계: 뒤따름(스토킹) 위협 고조":
            st.metric(label="뒤따름 위협 지수", value="88%", delta="+53% 폭증", delta_color="inverse")
            st.metric(label="가로등 밝기 상태", value="100% (최고 조명 제어)")
            st.code(
                "[12:00:00] 시스템 정상 부팅 완료\n"
                "[12:02:15] 배회 의심 대상 탐지\n"
                "[12:04:10] 경보 발령: [뒤따름 위협 행동 감지]\n"
                "[12:04:11] 가로등 백색광 조도 제어 전원 인가 완료 (100%)\n"
                "[12:04:12] 현장 스피커 음성 송출: '보행자와 거리를 유지하십시오.'"
            )
            
            # Interactive action triggers
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("🚨 경찰 순찰차 긴급 배정"):
                    st.success("🚓 역삼 지구대 순찰 2호차에 실시간 위치 정보 공유 및 비상 출동 명령 접수 완료!")
            with col_b2:
                if st.button("📢 현장 직접 음성 경고 방송 송출"):
                    st.info("📢 안내 스피커 음성 긴급 수동 송출: '세이프패스 AI 보안 구역입니다. 거리를 즉각 이탈하십시오.'")

# ==========================================
# Tab 3: Mobile Companion
# ==========================================
with tab3:
    st.subheader("🎙️ Companion AI: 실시간 모바일 폰 음성 동행 및 비명 탐지 시뮬레이터")
    st.write("사용자 스마트폰 이어폰을 통해 작동하는 가상 통화방입니다. 위험 멘트를 눌러 AI의 반응을 확인하세요.")
    
    col_mob1, col_mob2 = st.columns([0.8, 1.2])
    
    with col_mob1:
        st.markdown("#### 📱 가상 모바일 앱 통화 화면")
        situation = st.selectbox(
            "보행자의 말(상황)을 선택해 주세요:",
            [
                "대기 모드 - 안전 귀가 서비스 가동",
                "😨 '어두운 골목으로 들어가려는데 사람이 없어 너무 무서워요'",
                "🚨 '뒤에서 누군가 검은 옷을 입고 계속 따라오고 있어요...'",
                "💥 '사람 살려!! 저리 가요!! 악!!!' (비명/마찰)"
            ]
        )
        
        st.markdown("---")
        st.markdown("**📱 AI 통화 음성 요약:**")
        if situation == "대기 모드 - 안전 귀가 서비스 가동":
            st.caption("“안심 귀가 동행 통화가 활성화되었습니다. 어두운 밤길을 지켜드릴게요.”")
        elif "무서워요" in situation:
            st.info("“불안하시군요. 가로등 지도를 분석해 보니 앞으로 50m만 가시면 밝은 안심 편의점과 건널목이 나옵니다. 제가 보행 속도에 맞춰 계속 걸으며 함께 할게요.”")
        elif "따라오고" in situation:
            st.warning("“침착하게 들어주세요. 절대 멈추지 마시고 바로 앞 10m 거리에 있는 비상벨 가로등 쪽으로 도보 속도를 조금만 올려주세요. 제가 관제 센터 경보 방송을 연동 대기 중입니다.”")
        elif "사람 살려" in situation:
            st.error("“🚨 [위기 감지] 비명 주파수 충격 감지 완료! 긴급 신고 전송 라인을 가동합니다. 보행자 님, 위기 상황이 아니라면 햅틱 버튼을 눌러 신고를 철회하세요!”")

    with col_cctv2:
        st.markdown("#### 📡 온디바이스 모바일 오디오 주파수 판독기")
        
        if "사람 살려" in situation:
            st.error("⚠️ **비정상 음향 유입 경보!!**")
            st.metric(label="주변 소리 측정 지수", value="95 dB", delta="돌발 비명음 주파수 스펙트럼 감지")
            
            # Simulated Alert Countdown
            st.markdown("🚨 **112 자동 경찰 신고 접수 5초 전...**")
            cancel = st.button("❌ 긴급 신고 오작동 터치 철회")
            if cancel:
                st.success("정상적으로 신고 접수가 보류되었으며, 일반 동행 대기 모드로 복귀하였습니다.")
            else:
                st.caption("※ 버튼을 누르지 않을 시 스마트폰 GPS 주소와 주변 녹취록 5초 분량이 112 관제실로 원스톱 패키지 무선 전송됩니다.")
        else:
            st.metric(label="주변 소리 측정 지수", value="45 dB", delta="정상 생활 소음")
            st.success("🟢 통화 마이크 안정 주파수 수치 유지 중")

# ==========================================
# Tab 4: Route Planner
# ==========================================
with tab4:
    st.subheader("🗺️ SafeRouter: 인프라 연동 최적 안심 도보 경로 연산")
    st.write("단순 최단 거리가 아닌, 치안 인프라 가중치가 융합된 최고의 안전 골목길 추천 엔진입니다.")
    
    col_map1, col_map2 = st.columns([1.2, 0.8])
    
    with col_map1:
        st.markdown("#### 🗺️ 역삼2동 안심 가중치 가이드 맵")
        # Visual diagram representation in streamlit markdown
        st.markdown("""
        ```
        [출발역 (강남역 인근)]
              │
              ├── (위험한 지름길: 가로등 없음, 으슥한 지대, CCTV 부족) ❌ [최단 도보 8분]
              │
              └── (SafePass AI 권장 경로: 안심 가로등 밀집, 경찰 순찰로와 70% 일치) ⭐ [안심 도보 11분]
                                                                                │
                                                                           [역삼2동 주거지]
        ```
        """)
        
    with col_map2:
        st.markdown("#### 🚦 경로 세부 분석 및 대피소 안내")
        
        st.error("❌ **일반 포털 최단 경로 안내 (도보 8분, 420m)**\n\n- 조도 10Lux 이하 어두운 사각지대 골목 3개소 포함\n- 최근 30일 내 거동 거동 배회자 다발 구역 관통\n- 치안 CCTV 비감시 블라인드 율 65%")
        st.markdown("---")
        st.success("⭐ **SafePass AI 추천 안전 경로 (도보 11분, 580m)**\n\n- 100% LED 고선명 안심 스마트 가로등 라인 경유\n- 24시간 운영 세이프 가드 편의점 3개소 포함\n- 112 관제실 직동 비상벨 타워 2개소 관통")

# ==========================================
# Tab 5: News Report
# ==========================================
with tab5:
    st.subheader("📰 [특집 보도 기획 기사] 세이프패스 AI 시범 도입 성공")
    
    # Path to the generated image
    img_path = "safepass_cctv_dashboard.png"
    
    if os.path.exists(img_path):
        st.image(img_path, caption="세이프패스 AI 범죄 예방 실시간 관제 대시보드 구동 시각화 모형", use_container_width=True)
    else:
        st.warning("⚠️ 이미지를 로드할 수 없습니다. 로컬 디렉토리 내 생성 여부를 확인해 주세요.")
        
    st.markdown("""
    ### '어두운 골목길의 보이지 않는 보디가드'… 범죄 예방 AI '세이프패스' 도입 대성공
    **서울 역삼동 시범 지구 도입 3달 만에 밤거리 치안 사고 '제로' 기록**
    
    **[서울=대한미래기술일보] 박선우 과학기술 전문기자** = 칠흑같이 어두운 주택가 골목길, 야근을 마치고 귀가하던 시민 A씨(28)의 뒤로 수상한 거동을 보이는 한 남성이 일정한 거리를 두고 따라붙기 시작했다. 골목길 사각지대 진입을 위해 남성이 발걸음을 재촉하던 그 순간, 머리 위 설치된 스마트 가로등의 불빛이 100% 조도로 강렬하게 눈부신 백색광을 뿜어냈다.
    
    동시에 골목 스피커에서 **“이곳은 실시간 안심 귀가 스마트 보안 구간입니다. 타 보행자와 거리를 유지하고 속히 통과해 주십시오”**라는 경고 음성이 쩌렁쩌렁 울려 퍼졌다. 갑작스러운 빛의 폭발과 AI 경고 방송에 당황한 남성은 즉시 방향을 꺾어 현장에서 도주했다.
    
    이는 사후 범인 추적에 머물렀던 아날로그 치안 환경을 실시간 선제 예방 구역으로 탈바꿈시킨 차세대 인공지능 범죄 예방 플랫폼, **'세이프패스 (SafePass) AI'**의 실제 위기 조치 상황이다.
    
    #### ■ 사후 검거 중심에서 '선제적 예방'으로의 대전환
    기존 골목길 안전의 핵심이었던 CCTV는 범죄가 완료된 뒤 범인의 도주 경로를 파악하는 사후 증거 수집용으로 주로 활용되었다. 현장에서 즉각 범행을 억제할 수 있는 힘이 결여되어 있다는 것이 가장 큰 페인 포인트였다.
    
    그러나 서울 강남구 역삼동 일대 시범 지구에 도입된 **세이프패스 AI**는 딥러닝 컴퓨터 비전 기술을 접목해 이러한 규칙을 완전히 바꿨다.
    
    CCTV 프레임 데이터 분석엔진은 일반적인 보행과 범행 직전의 **'뒤따름(Stalking)'**, 골목길 구석에서 오랜 시간 서성이는 **'장시간 배회(Loitering)'** 궤적을 98%의 정확도로 가려낸다. 위협 거리인 3m 이내 좁혀짐이 탐지되면 즉각 스마트 가로등과 연계하여 조도를 극대화하고 경고 방송을 보냄으로써 범행 시도 자체를 원천 봉쇄한다.
    """)
