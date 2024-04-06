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
    gender = st.selectbox('Select Gender', ['Male', 'Female'])
    gender = '1' if gender == 'Male' else 0
    seniorcitizen=st.selectbox('Are you Senior Citizen?', ['Yes','No'])
    seniorcitizen= '1' if seniorcitizen == 'Yes' else 0
    partner=st.selectbox('Are you single?', ['Yes','No'])
    partner='1' if partner == 'Yes' else 0
    dependents=st.selectbox('Are you depended?', ['Yes','No'])
    dependents='1' if dependents == 'Yes' else 0
    tenure=st.slider('Select a tenure', 0, 1300, 50)
    phoneservice=st.selectbox('Select the Phone Service', ['Yes','No'])
    phoneservice='1' if phoneservice == 'Yes' else 0
    multiplelines=st.selectbox('Select the Phone Service', ['Yes','No','No PhoneService'])
    if multiplelines == 'Yes':
        multiplelines = '1'
    elif multiplelines == 'No':
        multiplelines = '0'
    else:
        multiplelines = '2'
    internetservice=st.selectbox('Select the Internet Service', ['No','Fiber','DSL'])
    if internetservice == 'Fiber':
        internetservice = '1'
    elif internetservice == 'No':
        internetservice = '0'
    else:
        internetservice = '2'
    onlinesecurity=st.selectbox('Select the Online Security', ['Yes','No','No InternetService'])
    if onlinesecurity == 'Yes':
        onlinesecurity = '1'
    elif onlinesecurity == 'No':
        onlinesecurity = '0'
    else:
        onlinesecurity = '2'
    onlinebackup=st.selectbox('Select the Online Backup', ['Yes','No','No InternetService'])
    if onlinebackup == 'Yes':
        onlinebackup = '1'
    elif onlinebackup == 'No':
        onlinebackup = '0'
    else:
        onlinebackup= '2'
    deviceprotection=st.selectbox('Select the Device Protection', ['Yes','No','No PhoneService'])
    if deviceprotection == 'Yes':
        deviceprotection = '1'
    elif deviceprotection == 'No':
        deviceprotection = '0'
    else:
        deviceprotection= '2'
    techsupport=st.selectbox('Select the Tech Support', ['Yes','No','No InternetService'])
    if techsupport == 'Yes':
        techsupport = '1'
    elif techsupport == 'No':
        techsupport = '0'
    else:
        techsupport= '2'
    streamingtv=st.selectbox('Select the StreamingTV', ['Yes','No','No InternetService'])
    if streamingtv == 'Yes':
        streamingtv = '1'
    elif streamingtv == 'No':
        streamingtv = '0'
    else:
        streamingtv= '2'
    streamingmovies=st.selectbox('Select the StreamingMovies', ['Yes','No','No InternetService'])
    if streamingmovies == 'Yes':
        streamingmovies = '1'
    elif streamingmovies == 'No':
        streamingmovies = '0'
    else:
        streamingmovies= '2'
    contract=st.selectbox('Select the contract',['One Year','Two Year','Month to Month'])
    if contract == 'One Year':
        contract = '1'
    elif contract == 'Two Year':
        contract = '2'
    else:
        contract='3'
    paperless=st.selectbox('Is it Paperless Billing?', ['Yes','No'])
    partner='1' if partner == 'Yes' else 0
    paymentmethod=st.selectbox('Select the Payment Method', ['Electronic check','Mailed check','Bank Transfer(Automatic)','credit card'])
    if paymentmethod == 'One Year':
        paymentmethod = '1'
    elif paymentmethod == 'Two Year':
        paymentmethod = '2'
    elif paymentmethod='Bank Transfer(Automatic)':
        paymentmethod='3'
    else:
        paymentmethod='4'
    monthlycharges=st.number_input(label='Enter the monthly Charge')
    totalcharges=st.number_input(label='Enter the Total Charge')
    pred=model.predict([[gender,seniorcitizen,partner,dependents,tenure,phoneservice,multiplelines,internetservice,onlinesecurity,onlinebackup,deviceprotection,techsupport,streamingtv,streamingmovies,contract,paperless,paymentmethod,monthlycharges,totalcharges]])
    if pred==0:
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
