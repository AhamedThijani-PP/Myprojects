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
seniorcitizen=st.selectbox('Are you Senior Citizen?(1 = Yes,0 = No)', ['1', '0'])
partner=st.selectbox('Are you single?(1 = Yes,0 = No)', ['1', '0'])
dependents=st.selectbox('Are you depended?(1 = Yes,0 = No)', ['1', '0'])
tenure=st.slider('Select a tenure', 0, 1300, 50)
phoneservice=st.selectbox('Select the Phone Service(1 = Yes,0 = No)', ['1', '0'])
multiplelines=st.selectbox('Select the Phone Service(1 = Yes,0 = No,2='No phone sevice)', ['1', '0','2'])
pred=model.predict([[sepal_l,sepal_w,petal_l,petal_w]])
if st.button('Predict Result'):
    st.success(f'{pred}')
