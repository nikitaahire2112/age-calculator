import streamlit as st
from datetime import date

# Title
st.title("🎂 Age Calculator")

# User input: Date of Birth
dob = st.date_input("Select your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Button
if st.button("Calculate Age"):
    today = date.today()
    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    # Adjust negative values
    if age_days < 0:
        age_months -= 1
        age_days += 30  # approx adjustment

    if age_months < 0:
        age_years -= 1
        age_months += 12

    # Display result
    st.success(f"✅ Your Age is: {age_years} years, {age_months} months, {age_days} days.")
