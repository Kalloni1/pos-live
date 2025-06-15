
import streamlit as st

def calculate_pos_from_average(total_sales, returns, reviews, avg_star, silent_star):
    silent = total_sales - returns - reviews
    if silent < 0:
        silent = 0
    review_score = reviews * avg_star
    silent_score = silent * silent_star
    total = reviews + silent
    if total == 0:
        return 0.0
    return round((review_score + silent_score) / total, 2)

def calculate_pos_from_distribution(total_sales, returns, stars_1, stars_2, stars_3, stars_4, stars_5, silent_star):
    reviews = stars_1 + stars_2 + stars_3 + stars_4 + stars_5
    silent = total_sales - returns - reviews
    if silent < 0:
        silent = 0
    review_score = (
        stars_1 * 1 +
        stars_2 * 2 +
        stars_3 * 3 +
        stars_4 * 4 +
        stars_5 * 5
    )
    silent_score = silent * silent_star
    total = reviews + silent
    if total == 0:
        return 0.0
    return round((review_score + silent_score) / total, 2)

# UI
st.title("📦 P.O.S. (Probability of Satisfaction) Calculator")
st.write("Estimate satisfaction using verified purchases and return behavior — not just written reviews.")

mode = st.radio("Choose input method:", ["🔢 Use average review rating", "📊 Use detailed star breakdown"])

sales = st.number_input("🛒 Total Verified Sales", min_value=0, value=10000)
returns = st.number_input("↩️ Verified Returns", min_value=0, value=500)
silent_star = st.slider("🤫 Assumed Silent Buyer Star Value", 1.0, 5.0, value=5.0, step=0.1)

if mode == "🔢 Use average review rating":
    reviews = st.number_input("📝 Verified Reviews", min_value=0, value=1000)
    avg_rating = st.slider("⭐ Average Verified Star Rating", 1.0, 5.0, value=4.3, step=0.1)
    if st.button("🎯 Calculate P.O.S."):
        pos = calculate_pos_from_average(sales, returns, reviews, avg_rating, silent_star)
        stars = "⭐" * int(round(pos)) + "✩" * (5 - int(round(pos)))
        st.markdown(f"### ✅ P.O.S. Score: **{pos} / 5**")
        st.markdown(f"### {stars}")

else:
    stars_1 = st.number_input("1⭐ Reviews", 0)
    stars_2 = st.number_input("2⭐ Reviews", 0)
    stars_3 = st.number_input("3⭐ Reviews", 0)
    stars_4 = st.number_input("4⭐ Reviews", 0)
    stars_5 = st.number_input("5⭐ Reviews", 0)
    if st.button("🎯 Calculate P.O.S."):
        pos = calculate_pos_from_distribution(sales, returns, stars_1, stars_2, stars_3, stars_4, stars_5, silent_star)
        stars = "⭐" * int(round(pos)) + "✩" * (5 - int(round(pos)))
        st.markdown(f"### ✅ P.O.S. Score: **{pos} / 5**")
        st.markdown(f"### {stars}")
