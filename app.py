import streamlit as st
import joblib
import pandas as pd
import json

model = joblib.load('model.pkl')

with open('job_map.json') as f:
    job_map = json.load(f)
with open('res_map.json') as f:
    res_map = json.load(f)
with open('loc_map.json') as f:
    loc_map = json.load(f)

st.title('Data Science Salary Predictor')
st.write('Estimate your salary based on role, experience, and location.')

experience = st.selectbox('Experience level', ['EN', 'MI', 'SE', 'EX'])
employment = st.selectbox('Employment type', ['FT', 'PT', 'CT', 'FL'])
job_title = st.selectbox('Job title', sorted(job_map.keys()))
residence = st.selectbox('Your country of residence', sorted(res_map.keys()))
company_loc = st.selectbox('Company location', sorted(loc_map.keys()))
remote = st.selectbox('Remote ratio', [0, 50, 100])
company_size = st.selectbox('Company size', ['S', 'M', 'L'])
work_year = st.slider('Work year', 2020, 2023, 2023)

exp_map = {'EN': 0, 'MI': 2, 'SE': 3, 'EX': 1}
emp_map = {'CT': 0, 'FL': 1, 'FT': 2, 'PT': 3}
size_map = {'L': 0, 'M': 1, 'S': 2}

input_data = pd.DataFrame([{
    'work_year': work_year,
    'experience_level': exp_map[experience],
    'employment_type': emp_map[employment],
    'job_title': job_map[job_title],
    'employee_residence': res_map[residence],
    'remote_ratio': remote,
    'company_location': loc_map[company_loc],
    'company_size': size_map[company_size]
}])

if st.button('Predict salary'):
    prediction = model.predict(input_data)[0]
    st.metric('Estimated salary (USD)', f"${prediction:,.0f}")
    st.write(f'Role: {job_title} | Experience: {experience} | Location: {residence}')