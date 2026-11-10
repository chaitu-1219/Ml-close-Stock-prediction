import joblib
import streamlit as st
import pandas as pd


#load trained model

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "Model" / "stock_price_model.pkl"

model = joblib.load(MODEL_PATH)
st.title('Stock Closing Price Prediction ')

st.write("Enter Open,High,Low prices:")
open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")

if st.button('Predict Closing Price'):
    input_data = pd.DataFrame([[open_price, high_price, low_price]])
    prediction = model.predict(input_data)
    st.success(f'The predicted closing price is: {prediction[0]}')