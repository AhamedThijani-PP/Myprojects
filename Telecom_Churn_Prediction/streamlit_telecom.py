from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split as tts
import pandas as pd
import streamlit as st
import joblib
def main():
    page = st.sidebar.selectbox('Select a page', ['Home', 'About', 'Contact'])
    if page == 'Home':
        render_home()
    elif page == 'About':
        render_about()
    elif page == 'Contact':
        render_contact()
def render_home():
    st.header('Home Page')
    st.write('Welcome to the home page!')
    Path='Telecom_Churn_Prediction/telecom_churn_prediction.pkl'
    model=joblib.load(open(Path,'rb'))
    st.title('Telecom Churn Prediction')
    st.write('------------------------------------------------')
    gender=st.selectbox('Select Gender(1=Male,0=Female)', ['1', '0'])
    seniorcitizen=st.selectbox('Are you Senior Citizen?(1 = Yes,0 = No)', ['1', '0'])
    partner=st.selectbox('Are you single?(1 = Yes,0 = No)', ['1', '0'])
    dependents=st.selectbox('Are you depended?(1 = Yes,0 = No)', ['1', '0'])
    tenure=st.slider('Select a tenure', 0, 1300, 50)
    phoneservice=st.selectbox('Select the Phone Service(1 = Yes,0 = No)', ['1', '0'])
    multiplelines=st.selectbox('Select the Phone Service(1 = Yes,0 = No,2=No phone sevice)', ['1', '0','2'])
    internetservice=st.selectbox('Select the Internet Service(1 = Fibre,0 = No,2=DSL)', ['1', '0','2'])
    onlinesecurity=st.selectbox('Select the Online Security(1 = Yes,0 = No,2=No Internet Service)', ['1', '0','2'])
    onlinebackup=st.selectbox('Select the Online Backup(1 = Yes,0 = No,2=No Internet sevice)', ['1', '0','2'])
    deviceprotection=st.selectbox('Select the Device Protection(1 = Yes,0 = No,2=No Internet service)', ['1', '0','2'])
    techsupport=st.selectbox('Select the Tech Support(1 = Yes,0 = No,2=No Internet sevice)', ['1', '0','2'])
    streamingtv=st.selectbox('Select the StreamingTV(1 = Yes,0 = No,2=No Internet sevice)', ['1', '0','2'])
    streamingmovies=st.selectbox('Select the StreamingMovies(1 = Yes,0 = No,2=No Internet sevice)', ['1', '0','2'])
    contract=st.selectbox('Select the contract(1 = One Year,2= Two Year,3=Month to Month)', ['1', '2','3'])
    paperless=st.selectbox('Is it Paperless Billing?(1 = Yes,0 = No)', ['1', '0'])
    paymentmethod=st.selectbox('Select the Payment Method(1 = Mailed check,0 = Electronic check,2=Bank Transfer(Automatic),3=credit card', ['1', '0','2'])
    monthlycharges=st.number_input(label='Enter the monthly Charge')
    totalcharges=st.number_input(label='Enter the Total Charge')
    pred=model.predict([[gender,seniorcitizen,partner,dependents,tenure,phoneservice,multiplelines,internetservice,onlinesecurity,onlinebackup,deviceprotection,techsupport,streamingtv,streamingmovies,contract,paperless,paymentmethod,monthlycharges,totalcharges]])
    if pred=='1':
        pred='People are likely to churn'
    else:
        pred='People are not likely to churn'
    if st.button('Predict Result'):
        st.success(pred)
def render_about():
    st.header('About Page')
    st.write('It is an experimental prototype created by second year BCA Robotics students of Yenepoya. This model has good performance.It is still in the experimental phase.')

def render_contact():
    st.header('Contact Page')
    st.write("If you have any concern, don't hesitate to contact us ahamedthijanipp@gmail.com")

if __name__ == "__main__":
    main()
