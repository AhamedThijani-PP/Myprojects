import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('IRIS.csv')
x=df.iloc[:,0:4].values
y=df.iloc[:,4].values
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
model=LogisticRegression()
model.fit(x_train,y_train)
st.title('Iris Prediction Model')
st.write('------------------------------------------------')
sepal_l=st.number_input(label='Enter the Sepal Length')
sepal_w=st.number_input(label='Enter the Sepal Width')
petal_l=st.number_input(label='Enter the Petal Length')
petal_w=st.number_input(label='Enter the Petal Width')
pred=model.predict([[sepal_l,sepal_w,petal_l,petal_w]])
if st.button('Predict Result'):
    st.success(f'{pred}')