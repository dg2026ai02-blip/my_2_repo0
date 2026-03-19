import streamlit as st
import random

st.title("💖 이름 궁합 테스트")
st.write("두 사람의 이름을 입력하면 궁합을 알려드려요!")

# 입력
name1 = st.text_input("첫 번째 이름")
name2 = st.text_input("두 번째 이름")

# 궁합 계산
def calculate_compatibility(n1, n2):
    combined = n1 + n2
    score = sum(ord(c) for c in combined) % 101
    return score

# 랜덤 멘트
best_msgs = ["운명 그 자체 💕", "결혼각입니다 💍", "천생연분 🔥"]
good_msgs = ["잘 어울려요 😊", "좋은 관계예요!", "설레는 사이 💓"]
mid_msgs = ["무난한 관계 🙂", "친구로 좋아요!", "노력해보세요 😉"]
bad_msgs = ["조금 힘들 수도 😢", "갈등 주의 ⚠️", "거리두기 추천 💔"]

# 버튼
if st.button("궁합 확인하기"):
    if name1 and name2:
        score = calculate_compatibility(name1, name2)

        # 점수 표시
        st.subheader(f"궁합 점수: {score}점 💘")

        # 🔥 게이지 바
        st.progress(score)

        # 🎉 효과 + 멘트
        if score > 80:
            st.success("🔥💖 완벽한 궁합! 💖🔥")
            st.markdown("💘💘💘 💕🔥 💘💘💘 💖💖💖")
            st.write(random.choice(best_msgs))

            # 풍선 효과
            st.balloons()

        elif score > 60:
            st.info("😍 꽤 잘 맞는 사이!")
            st.markdown("😍💕😍 💓💓")
            st.write(random.choice(good_msgs))

        elif score > 40:
            st.warning("🙂 무난한 궁합")
            st.markdown("🙂🙂🙂")
            st.write(random.choice(mid_msgs))

        else:
            st.error("💔😭 쉽지 않은 관계...")
            st.markdown("💔💔 😭 💔💔")
            st.write(random.choice(bad_msgs))

    else:
        st.warning("이름을 모두 입력해주세요!")
