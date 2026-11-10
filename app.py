import joblib
import streamlit as st
import pandas as pd


#load trained model

model = joblib.load(r'C:\\Users\\pchai\\OneDrive\\Desktop\\nasscom\\Ml-close-Stock-prediction\\Model\\stock_price_model.pkl')
st.title('Stock Closing Price Prediction ')

st.write("Enter Open,High,Low prices:")
open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")

if st.button('Predict Closing Price'):
    input_data = pd.DataFrame([[open_price, high_price, low_price]])
    prediction = model.predict(input_data)
    st.success(f'The predicted closing price is: {prediction[0]}')