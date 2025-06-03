import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

st.title("FX Converter")

currencies = get_currencies_list()

if currencies is None:
    st.error("Error fetching currencies. Please try again later.")
else:
    amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=1.0)

    from_currency = st.selectbox("From Currency:", options=currencies)
    to_currency = st.selectbox("To Currency:", options=currencies)

    if st.button("Get Latest Rate"):
        date, rate = get_latest_rates(from_currency, to_currency, amount)
        if rate is None:
            st.error("Error fetching the latest conversion rate.")
        else:
            st.markdown("### **Latest Conversion Rate**")
            st.success(format_output(date, from_currency, to_currency, rate, amount))
            
    st.write("Select a date for historical rates:")
    selected_date = st.date_input("Select Date", value=datetime.date.today())
    
    
    if selected_date > datetime.date.today():
        st.error("Selected date is in the future. Please choose a valid past date.")
        
        
    if st.button("Conversion Rate"):
        historical_rate = get_historical_rate(from_currency, to_currency, selected_date.strftime('%Y-%m-%d'), amount)
        if historical_rate is None:
            st.error("Error fetching the historical conversion rate.")
        else:
            st.markdown("### **Latest Conversion Rate**")
            st.success(format_output(selected_date, from_currency, to_currency, historical_rate, amount))
