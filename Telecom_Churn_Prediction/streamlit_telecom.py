import streamlit as st
import joblib

def about_section():
    st.title('About Telecom Churn Prediction')

    st.markdown("""
    This web application aims to predict telecom customer churn, which refers to when customers leave a telecom service provider for another provider or discontinue using telecom services altogether.

    **Features**:
    - Data exploration: Visualize and explore the telecom dataset.
    - Data preprocessing: Clean and preprocess the dataset for modeling.
    - Model training: Train a machine learning model to predict churn.
    - Model evaluation: Evaluate the performance of the trained model.
    - Prediction: Make predictions on new data.

    **Dataset**:
    The application uses a publicly available telecom customer churn dataset. It contains various features such as customer demographics, usage patterns, and service subscription details.

    **Prediction Model**:
    The prediction model is built using machine learning algorithms such as logistic regression, random forest, or gradient boosting. It utilizes features from the dataset to predict the likelihood of customer churn.

    **Note**:
    This application is for demonstration purposes only and may not reflect real-world scenarios. The predictions generated should not be used for making critical business decisions without proper validation and verification.

    For more information, refer to the [GitHub repository](https://github.com/your-username/telecom-churn-prediction).
    """)

def main():
    st.set_page_config(page_title="Telecom Churn Prediction", page_icon=None, layout="wide", initial_sidebar_state="auto", watermark=False)
    
    st.title('Telecom Churn Prediction')
    st.write('Welcome to the Telecom Churn Prediction app!')
    st.write('------------------------------------------------')

    Path='Telecom_Churn_Prediction/telecom_churn_prediction.pkl'
    model=joblib.load(open(Path,'rb'))

    st.subheader('Customer Information')
    gender = st.selectbox('Select Gender', ['Male', 'Female'])
    gender = 1 if gender == 'Male' else 0

    senior_citizen = st.radio('Are you a Senior Citizen?', ['Yes','No'])
    senior_citizen = 1 if senior_citizen == 'Yes' else 0

    partner = st.radio('Are you single?', ['Yes','No'])
    partner = 1 if partner == 'Yes' else 0

    dependents = st.radio('Do you have dependents?', ['Yes','No'])
    dependents = 1 if dependents == 'Yes' else 0

    tenure = st.slider('Select a tenure', 0, 1300, 5)

    phone_service = st.radio('Do you have Phone Service?', ['Yes','No'])
    phone_service = 1 if phone_service == 'Yes' else 0

    multiple_lines = st.selectbox('Select the Multiple Lines', ['Yes','No','No PhoneService'])
    multiple_lines = 1 if multiple_lines == 'Yes' else 0 if multiple_lines == 'No' else 2

    internet_service = st.selectbox('Select the Internet Service', ['No','Fiber','DSL'])
    internet_service = 1 if internet_service == 'Fiber' else 0 if internet_service == 'No' else 2

    online_security = st.selectbox('Select the Online Security', ['Yes','No','No InternetService'])
    online_security = 1 if online_security == 'Yes' else 0 if online_security == 'No' else 2

    online_backup = st.selectbox('Select the Online Backup', ['Yes','No','No InternetService'])
    online_backup = 1 if online_backup == 'Yes' else 0 if online_backup == 'No' else 2

    device_protection = st.selectbox('Select the Device Protection', ['Yes','No','No PhoneService'])
    device_protection = 1 if device_protection == 'Yes' else 0 if device_protection == 'No' else 2

    tech_support = st.selectbox('Select the Tech Support', ['Yes','No','No InternetService'])
    tech_support = 1 if tech_support == 'Yes' else 0 if tech_support == 'No' else 2

    streaming_tv = st.selectbox('Select the Streaming TV', ['Yes','No','No InternetService'])
    streaming_tv = 1 if streaming_tv == 'Yes' else 0 if streaming_tv == 'No' else 2

    streaming_movies = st.selectbox('Select the Streaming Movies', ['Yes','No','No InternetService'])
    streaming_movies = 1 if streaming_movies == 'Yes' else 0 if streaming_movies == 'No' else 2

    contract = st.selectbox('Select the contract', ['One Year','Two Year','Month to Month'])
    contract = 1 if contract == 'One Year' else 2 if contract == 'Two Year' else 3

    paperless_billing = st.radio('Is it Paperless Billing?', ['Yes','No'])
    paperless_billing = 1 if paperless_billing == 'Yes' else 0

    payment_method = st.selectbox('Select the Payment Method', ['Electronic check','Mailed check','Bank Transfer(Automatic)','Credit card'])
    payment_method = 1 if payment_method == 'Electronic check' else 2 if payment_method == 'Mailed check' else 3 if payment_method == 'Bank Transfer(Automatic)' else 4

    monthly_charges = st.number_input('Enter the Monthly Charge')
    total_charges = st.number_input('Enter the Total Charge')

    if st.button('Predict Result'):
        pred = model.predict([[gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges]])
        
        if pred == 0:
            result = 'People are likely to churn'
        else:
            result = 'People are not likely to churn'

        st.success(result)

if __name__ == "__main__":
    main()
