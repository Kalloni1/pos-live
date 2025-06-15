
import streamlit as st

st.set_page_config(page_title="P.O.S. – Probability of Satisfaction", layout="centered")

st.title("📦 P.O.S. (Probability of Satisfaction)")
st.subheader("A smarter way to rate products beyond written reviews.")

st.markdown("""
**P.O.S.** (Probability of Satisfaction) introduces a new way to interpret product performance using real, verified purchase behavior — not just reviews.

📊 It blends:
- Verified **sales**
- Verified **returns**
- Verified **reviews**
- Silent, satisfied buyers (those who don't return or review)

The result: a transparent, behavior-based 5-star score to help shoppers and sellers better understand true product satisfaction.
""")

st.image("https://kalloni1-pos-live.streamlit.app/screenshot.png", caption="Live App Snapshot (Replace with your screenshot)")

st.markdown("### 🔗 Try the Live Calculator")
st.markdown("[Click here to open the live demo app](https://kalloni1-pos-live.streamlit.app)")

st.markdown("### 💡 Why P.O.S. Is Better Than Just Reviews")
st.markdown("""
- ✅ Includes silent verified buyers — the ones who never return the product
- ✅ Ignores unverified reviews and review manipulation
- ✅ Helps new products with few reviews shine if buyers are satisfied
- ✅ Easy to integrate with Amazon, Home Depot, or your own store
""")

st.markdown("### 📬 Contact")
st.markdown("Created by **George Eleftheriou**  
📧 [yiorgose@yahoo.com](mailto:yiorgose@yahoo.com)")
