"""
## App: Bank Market Campaigns Prediction with Streamlit 
Author: [Jayashankar Chaluvaraj)](https://github.com/jshankarc))\n
Description: 
This is built with Streamlit Framework, an awesome framework for building interactive model.
"""
import streamlit as st
import numpy as np
import pandas as pd


st.title('Bank Market Campaigns Prediction')

st.write('Now Let\'s fill a form Campaign Parameters')

df = pd.read_csv('Bank-Market-UCI/dataset/bank.csv', ';')

# Age range 
age = st.slider('Age', df['age'].min(), df['age'].max())
st.write('Age:', age)

#Jobs
job = st.selectbox('Job Categories', (df['job'].unique()))
st.write('Job Category: ', job)

#martial status
martial = st.selectbox('Martial Status', (df['marital'].unique()))
st.write('Martial Status: ', martial)

#Eduction
education = st.selectbox('Eduction', (df['education'].unique()))
st.write('Eduction Status: ', education)

#Default
default = st.checkbox("Has credit in Default?")
st.write('Default: ', default)

#Housing Loan
housing = st.checkbox("Has Housing Loan?")
st.write('Housing Loan: ', housing)

#Personal Loan
personal = st.checkbox("Has Personal Loan?")
st.write('Personal Loan: ', personal)

#Contact Communication Type
education = st.selectbox('Contact Communication Type', (df['contact'].unique()))
st.write('Contact Communication Type: ', education)

months_map = {'January' : 'jan', 'February' : 'feb', 'March' : 'mar', 'April' : 'apr', 'May' : 'may', 'June' : 'jun', 'July' : 'jul',
          'August' : 'aug', 'September' : 'sep', 'October' : 'oct', 'November' : 'nov', 'December' : 'dec'}

#Eduction
education = st.selectbox('Last Contact Month', (list({*months_map.keys()})))
education_value = months_map.get(education)
st.write('Eduction Status: ', education)

#last contact call duration in second
duration = st.slider('Last Contact Call duration in seconds', df['duration'].min(), df['duration'].max())
st.write('Duration:', duration)

#campaign - number of contacts performed during the campaign
campaign = st.slider('Total number of contacts performed during the campaign', df['campaign'].min(), df['campaign'].max())
st.write('campaign:', campaign)

#pdays - last contacted in days
pdays = st.slider('Last contacted information in days', df['pdays'].min(), df['pdays'].max())
st.write('campaign:', pdays)

#previous - number of times contacted before the campaign
previous = st.slider('Total number of contacts performed in the previous campaign', df['previous'].min(), df['previous'].max())
st.write('campaign:', previous)

#poutcome - last campaign result
poutcome = st.selectbox('Last campaign result', (df['poutcome'].unique()))
st.write('Last campaign result: ', poutcome)
