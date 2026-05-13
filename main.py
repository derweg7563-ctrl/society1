import streamlit as st
import activity2_1
import activity2_2

# 1. 앱 기본 설정
st.set_page_config(page_title="미니 역사 탐험대", layout="wide")

# 2. 혹시 기존 활동 코드에서 학생 이름(username)을 부르는 경우가 있을까 봐 기본값 설정
if "username" not in st.session_state:
    st.session_state.username = "우리반 탐험대원"

# 3. 왼쪽 사이드바 메뉴 만들기
st.sidebar.title("🔍 미니 탐험 메뉴")
menu = st.sidebar.radio("활동을 선택하세요:", ["옛 물건 살펴보기", "AI 유물 탐정"])

st.sidebar.markdown("---")
st.sidebar.info("안성 교육지원청 수업 페스티벌\n\n'여러가지 자료를 통해 과거의 모습 상상하기' 미니 탐험 일지입니다.")

# 4. 메뉴 선택에 따라 화면 띄워주기
if menu == "옛 물건 살펴보기":
    activity2_1.show_page()
elif menu == "AI 유물 탐정":
    activity2_2.show_page()