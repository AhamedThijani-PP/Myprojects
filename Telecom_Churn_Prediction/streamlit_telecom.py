import streamlit as st

def main():
    st.set_page_config(page_title="Telecom Churn Prediction", page_icon=None, layout="wide", initial_sidebar_state="auto")

    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'About', 'Contact'])

    if page == 'Home':
        render_home()
    elif page == 'About':
        render_about()
    elif page == 'Contact':
        render_contact()

def render_home():
    st.title('Telecom Churn Prediction')
    st.write('Welcome to the Telecom Churn Prediction app!')

    # Load the trained model
    model = load_model()

    # Display input fields for user interaction
    with st.form("churn_prediction_form"):
        st.header('Input Parameters')
        
        gender = st.selectbox('Select Gender', ['Male', 'Female'])
        gender = '1' if gender == 'Male' else 0

        senior_citizen = st.radio('Are you Senior Citizen?', ['Yes', 'No'], index=1)
        senior_citizen = '1' if senior_citizen == 'Yes' else 0

        partner = st.radio('Are you single?', ['Yes', 'No'], index=1)
        partner = '1' if partner == 'Yes' else 0

        dependents = st.radio('Are you depended?', ['Yes', 'No'], index=1)
        dependents = '1' if dependents == 'Yes' else 0

        tenure = st.slider('Select tenure', 0, 1300, 5)

        # Add more input fields here...

        submit_button = st.form_submit_button(label='Predict Churn')

    if submit_button:
        # Predict churn based on user input
        prediction = predict_churn(model, gender, senior_citizen, partner, dependents, tenure)
        
        # Display prediction result
        st.success(f'Churn prediction: {prediction}')

def render_about():
    st.title('About Page')
    st.write('This app is designed for predicting telecom customer churn. It uses machine learning techniques to analyze customer data and predict whether a customer is likely to churn or not.')

def render_contact():
    st.title('Contact Page')
    st.write('If you have any questions or suggestions, please feel free to contact us at ahamedthijanipp@gmail.com')

if __name__ == "__main__":
    main()
