
import streamlit as st

def calculate_pos_rating(total_verified_sales, verified_returns, verified_reviews, avg_verified_star_rating, silent_star_value=5.0):
    satisfied_silent = total_verified_sales - verified_returns - verified_reviews
    if satisfied_silent < 0:
        satisfied_silent = 0

    review_contribution = verified_reviews * avg_verified_star_rating
    silent_contribution = satisfied_silent * silent_star_value

    total_contributors = verified_reviews + satisfied_silent
    if total_contributors == 0:
        return 0.0

    pos_score = (review_contribution + silent_contribution) / total_contributors
    return round(pos_score, 2)

# Streamlit Interface
st.title("📦 Probability of Satisfaction (P.O.S.) Calculator")
st.write("Use this tool to estimate customer satisfaction based on **verified purchases** — not just written reviews.")

sales = st.number_input("🛒 Total Verified Sales", min_value=0, value=10000)
returns = st.number_input("↩️ Verified Returns", min_value=0, value=500)
reviews = st.number_input("📝 Verified Reviews", min_value=0, value=1000)
avg_rating = st.slider("⭐ Average Verified Star Rating", min_value=1.0, max_value=5.0, value=4.3, step=0.1)
silent_star = st.slider("🤫 Assumed Silent Buyer Star Value", min_value=1.0, max_value=5.0, value=5.0, step=0.1)

if st.button("🎯 Calculate P.O.S. Rating"):
    pos = calculate_pos_rating(sales, returns, reviews, avg_rating, silent_star)
    stars = "⭐" * int(round(pos)) + "✩" * (5 - int(round(pos)))
    st.markdown(f"### ✅ Estimated P.O.S. Rating: **{pos} / 5**")
    st.markdown(f"### {stars}")
