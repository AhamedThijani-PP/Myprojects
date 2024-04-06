from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split as tts
import pandas as pd
import streamlit as st
Path='Telecom_Churn_Prediction/telecom_churn_prediction.pkl'
import joblib
model=joblib.load(open(Path,'rb'))
st.title('Telecom Churn Prediction')
st.write('------------------------------------------------')
gender=st.selectbox('Select Gender', ['Male', 'Female'])
sepal_w=st.number_input(label='Enter the Sepal Width')
petal_l=st.number_input(label='Enter the Petal Length')
petal_w=st.number_input(label='Enter the Petal Width')
pred=model.predict([[sepal_l,sepal_w,petal_l,petal_w]])
if st.button('Predict Result'):
    st.success(f'{pred}')
