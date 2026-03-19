import streamlit as st
import random

st.set_page_config(page_title="궁합 테스트", page_icon="💖")

st.title("💖 이름 궁합 테스트")
st.write("✨ 두 사람의 이름으로 운명의 궁합을 확인해보세요 ✨")

# 입력
name1 = st.text_input("첫 번째 이름")
name2 = st.text_input("두 번째 이름")

# 궁합 계산
def calculate_compatibility(n1, n2):
    combined = n1 + n2
    score = sum(ord(c) for c in combined) % 101
    return score

# 💌 덕담 리스트
best_msgs = [
    "두 사람은 서로의 운명이에요 💍",
    "평생 함께해도 좋을 최고의 궁합 💖",
    "주변 사람들이 부러워할 관계예요 🔥"
]

good_msgs = [
    "서로를 잘 이해하는 좋은 관계예요 😊",
    "함께하면 즐거운 시간이 많을 거예요 💕",
    "지금처럼만 하면 오래 갈 수 있어요!"
]

mid_msgs = [
    "조금씩 맞춰가면 더 좋아질 거예요 🙂",
    "대화가 중요한 관계예요!",
    "친구처럼 편한 사이가 될 수 있어요 😉"
]

bad_msgs = [
    "서로 노력하면 달라질 수 있어요 💔",
    "조금 더 이해가 필요해요 😢",
    "시간을 두고 천천히 알아가 보세요"
]

# 버튼
if st.button("💘 궁합 확인하기"):
    if name1 and name2:
        score = calculate_compatibility(name1, name2)

        st.subheader(f"💯 궁합 점수: {score}점")

        # 🎯 게이지 바
        st.progress(score)

        st.markdown("---")

        # 🎉 점수별 효과 + 덕담
        if score > 80:
            st.success("🔥💖 완벽한 궁합! 💖🔥")
            st.markdown("💘💘💘 💕🔥 💘💘💘 💖💖💖")
            st.write(random.choice(best_msgs))
            st.balloons()

        elif score > 60:
            st.info("😍 잘 맞는 좋은 궁합!")
            st.markdown("😍💕😍 💓💓")
            st.write(random.choice(good_msgs))

        elif score > 40:
            st.warning("🙂 무난한 궁합")
            st.markdown("🙂🙂🙂")
            st.write(random.choice(mid_msgs))

        else:
            st.error("💔 조금 어려운 궁합...")
            st.markdown("💔💔 😭 💔💔")
            st.write(random.choice(bad_msgs))

        # ✨ 추가 효과 (결과 강조)
        st.markdown("---")
        st.caption("🔮 결과는 재미로 보는 것이에요!")

    else:
        st.warning("⚠️ 이름을 모두 입력해주세요!")
