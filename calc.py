import streamlit as st
st.title('Calculator App')
st.write('------------------------------------------------')
n1=st.number_input(label='Enter the first number')
n2=st.number_input(label='Enter the second number')
op=st.radio('Select an operation to perform',('Add','Subtract','Multiply','Divide'))
ans=0
def calculate():
    if op=='Add':
        ans=n1+n2
    elif op=='Subtract':
        ans=n1-n2
    elif op=='Multiply':
        ans=n1*n2
    elif op=='Divide':
        ans=n1/n2
    else:
        ans='Not defined'
    st.success(f'Answer={ans}')
if st.button('Calculate Result'):
    calculate()