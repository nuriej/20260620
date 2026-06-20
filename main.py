
import streamlit as st

st.set_page_config(page_title="AI 학습 성향 분석기")

st.title("🧠 AI 학습 성향 분석기")
st.write("간단한 질문에 답하면 학습 성향을 분석합니다.")

score = 0

q1 = st.slider(
    "1. 나는 수학이나 논리 문제를 푸는 것을 좋아한다.",
    1, 5, 3
)

q2 = st.slider(
    "2. 나는 그림이나 디자인에 관심이 많다.",
    1, 5, 3
)

q3 = st.slider(
    "3. 계획을 세우고 공부하는 편이다.",
    1, 5, 3
)

q4 = st.slider(
    "4. 새로운 아이디어를 생각하는 것을 좋아한다.",
    1, 5, 3
)

q5 = st.slider(
    "5. 데이터를 분석하는 것이 재미있다.",
    1, 5, 3
)

if st.button("분석하기"):

    left = q1 + q3 + q5
    right = q2 + q4

    if left >= right + 3:
        result = "📊 분석형 학습자"
        description = """
        • 논리적 사고를 선호함
        • 수학, 정보 과목에 강점
        • 체계적인 학습을 좋아함
        """

    elif right >= left:
        result = "🎨 창의형 학습자"
        description = """
        • 창의적 사고를 선호함
        • 예술, 디자인 분야에 강점
        • 새로운 아이디어를 좋아함
        """

    else:
        result = "⚖️ 균형형 학습자"
        description = """
        • 논리와 창의성의 균형
        • 다양한 방식으로 학습 가능
        • 적응력이 뛰어남
        """

    st.success(f"당신은 {result} 입니다!")

    st.write(description)

    st.subheader("AI 추천 학습 방법")

    if "분석형" in result:
        st.write("✔ 문제 풀이 중심 학습")
        st.write("✔ 오답노트 작성")
        st.write("✔ 단계별 계획 수립")

    elif "창의형" in result:
        st.write("✔ 마인드맵 활용")
        st.write("✔ 영상 기반 학습")
        st.write("✔ 프로젝트 활동")

    else:
        st.write("✔ 문제 풀이와 프로젝트 병행")
        st.write("✔ 다양한 학습 방법 시도")

