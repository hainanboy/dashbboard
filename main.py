import streamlit as st
import pandas as pd



header = st.container()
dataset = st.container()
feactures = st.container()
modelTrainiing = st.container()

with header:
    st.title('Welcome to my project')
    st.text('This project show the transactions of taxis in NYC')

with dataset:
    st.title('Most intelligent dogs dataset')
    st.text('Data from Kagle')

    #dog_data=pd.read_csv('dog_intelligence.csv')
    dog_data=pd.read_csv('topSubscribed.csv')
    st.write(dog_data.head())

    st.subheader('Subtitle for my graph')
    pulocation_dist=pd.DataFrame(dog_data['Subscribers'].value_counts().head(50))
    st.bar_chart(pulocation_dist)

with feactures:
    st.title('The feactures for my project')

    st.markdown('* **first feature** I created this feature because....')
    st.markdown('* **secounud feature** I created this feature because....')
    st.markdown('* **third feature** I created this feature because....')

with modelTrainiing:
    st.title('Area for train the model')
    st.text('Here we choose the parameters')

    sel_col, disp_col= st.columns(2)

    max_depth=sel_col.slider('What should be the max_depth of the model?',min_value=10, max_value=100, value=20, step=10)

    n_estimators=sel_col.selectbox('How many trees should be?', options=[100,200,300,'No limit'],index=0)

    input_feature=sel_col.text_input('Which feature shold be used as the input feature','Subscribers')