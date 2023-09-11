import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilihan Halaman : ', ('EDA', 'Predict Client Term Deposit Subscription'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()