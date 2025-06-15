# Probability of Satisfaction (P.O.S.) Demo

This Streamlit app calculates a new 5-star metric called **P.O.S. (Probability of Satisfaction)** based on verified purchase behavior.

## How It Works
- Uses verified sales, returns, and reviews
- Assumes silent, non-returning verified buyers are satisfied
- Combines review average with estimated satisfaction for a more accurate score

## Run It Locally
```
pip install streamlit
streamlit run pos_rating_calculator.py
```
