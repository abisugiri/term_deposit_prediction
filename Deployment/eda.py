import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


st.set_page_config(
    page_title= 'Term Deposit Subscription',
    layout='wide',
    initial_sidebar_state = 'expanded'
    )

def run ():
    # Membuat Title
    st.title('Term Deposit Subscription Prediction')

    # Membuat Sub Header
    st.subheader('Exploratory Data Analysis')

    # Menambah Gambar
    image = Image.open('deposit.jpg')
    st.image(image, caption ='Term Deposit')

    # Menambahkan deskripsi

    st.write('Page ini dibuat oleh **Abi Sugiri**')
    

    # Membuat Garis Lurus
    st.markdown('----')

    # Show DataFrame
    data = pd.read_csv('data.csv')
    st.dataframe(data)

    # Barplot
    st.write('#### Means of Customers Contact')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='contact', data=data)
    st.pyplot(fig)

    # Barplot
    st.write('#### Customers with Housing Loan')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='housing', data=data)
    st.pyplot(fig)

    # Barplot
    st.write('#### Customer Occupations')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='job', data=data)
    st.pyplot(fig)

    # Barplot
    st.write('#### Customers With Credit in Default')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='default', data=data)
    st.pyplot(fig)

    # Barplot
    st.write('#### Customers With Personal Loan')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='loan', data=data)
    st.pyplot(fig)


    # Membuat Histogram berdasarkan input User
    st.write('#### Histogram Based on Input from User')
    pilihan = st.selectbox('Select a Column : ', ('age', 'balance', 'duration', 'campaign'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)
    

if __name__ == '__main__':
    run()