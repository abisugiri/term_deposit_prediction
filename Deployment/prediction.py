# Import Libraries
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pandas as pd
import numpy as np
import pickle
import json
import tensorflow as tf
import matplotlib.pyplot as plt



# Load all files

with open('list_num_cols.txt', 'r') as file_1:
  list_num_cols = json.load(file_1)

with open('list_cat_cols_1.txt', 'r') as file_2:
  list_cat_cols_1 = json.load(file_2)
  
with open('list_cat_cols_2.txt', 'r') as file_3:
  list_cat_cols_2 = json.load(file_3)
  
with open('model_scaler.pkl', 'rb') as file_4:
  scaler = pickle.load(file_4)

with open('model_encoder_1.pkl', 'rb') as file_5:
  ohe_1 = pickle.load(file_5)
  
with open('model_encoder_2.pkl', 'rb') as file_6:
  label_enc = pickle.load(file_6)

# Load Model

model = tf.keras.models.load_model('model_sequential_improvement.h5', compile=False)


def run():
    # Membuat Form
    with st.form(key='Client Info Form'):
        Age = st.number_input('Age of Client', min_value=18, max_value=90, value=25, step=1)
        Job = st.selectbox('job', ('management', 'technician', 'entrepreneur', 'blue-collar', 'unknown', 'retired', 'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student'), index=1)
        Marital = st.selectbox('marital', ('married', 'single', 'divorced'), index=1)
        Edu = st.selectbox('education', ('tertiary', 'secondary', 'unknown', 'primary'), index=1)
        st.markdown('---')
        
        Default = st.selectbox('default', ('no', 'yes'), index=1)
        Balance = st.number_input('Average yearly balance in Euros', min_value=-5000, max_value=100000, value=5000, step=1, help='in Euros')
        Housing = st.selectbox('housing', ('yes', 'no'), index=1)
        Loan = st.selectbox('loan', ('no', 'yes'), index=1)
        Contact = st.selectbox('contact', ('unknown', 'cellular', 'telephone'), index=1)
        st.markdown('---')

        Duration = st.slider('duration', 0, 4900, 2000)
        Campaign = st.slider('campaign', 1, 60, 30)
        Pdays = st.slider('pdays', -1, 850, 400)
        Previous = st.slider('previous', 0, 250, 100)
        Poutcome = st.selectbox('poutcome', ('unknown', 'failure', 'other', 'success'), index=1)

        submitted = st.form_submit_button('Predict')

        data_inf = {
        'age'               : Age,
        'job'               : Job,
        'marital'           : Marital,
        'education'         : Edu,
        'default'           : Default,
        'balance'           : Balance,
        'housing'           : Housing,
        'loan'              : Loan,
        'contact'           : Contact,
        'duration'          : Duration,
        'campaign'          : Campaign,
        'pdays'             : Pdays,
        'previous'          : Previous,
        'poutcome'          : Poutcome
    }
        
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        #Split between numerical columns and categorical columns
        
        data_inf_num   = data_inf[list_num_cols]
        data_inf_cat_1 = data_inf[list_cat_cols_1]
        data_inf_cat_2 = data_inf[list_cat_cols_2]

        #Feature scaling and feature encoding
        data_inf_num_scaled    = scaler.transform(data_inf_num)
        data_inf_cat_encoded_1 = ohe_1.transform(data_inf_cat_1)
        data_inf_cat_encoded_2 = data_inf_cat_2
        data_inf_cat_encoded_2['default'] = label_enc.transform(data_inf_cat_2['default'])
        data_inf_cat_encoded_2['housing'] = label_enc.transform(data_inf_cat_2['housing'])
        data_inf_cat_encoded_2['loan'] = label_enc.transform(data_inf_cat_2['loan'])
        
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded_1, data_inf_cat_encoded_2], axis = 1)
        
        

        #Predict ann
        
        y_pred_inf_model = pd.DataFrame(model.predict(data_inf_final))
        y_pred_inf_model = np.where(y_pred_inf_model >= 0.5, 'no', 'yes')
        
        st.dataframe(y_pred_inf_model)
        
if __name__ == '__main__':
    run()