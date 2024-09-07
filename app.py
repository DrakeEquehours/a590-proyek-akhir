import streamlit as st
import pandas as pd
import joblib
import os

model = joblib.load('model/random_forest_model.joblib')
data = pd.read_csv('data.csv', sep=';')

features = [
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_grade',
]

st.sidebar.title("User Input")
user_inputs = {}
for feature in features:
    if data[feature].dtype == 'int64':
        user_inputs[feature] = st.sidebar.slider(f"Select {feature}", 
                                                 int(data[feature].min()), 
                                                 int(data[feature].max()), 
                                                 int(data[feature].median()))
    else:
        user_inputs[feature] = st.sidebar.slider(f"Select {feature}", 
                                                 float(data[feature].min()), 
                                                 float(data[feature].max()), 
                                                 float(data[feature].median()))

user_df = pd.DataFrame([user_inputs])

prediction = model.predict(user_df)

st.header("Student Dropout Prediction Apps")
st.write("Welcome to the apps, you can adjust your parameter in side box on your left to predict whether your student dropout or not")
st.subheader("Prediction Result:")
os.write(1,bytes(f'{prediction}\n', encoding='utf-8'))

if prediction[0] == 1:
    st.write(" With this parameter students will be GRADUATED :large_green_circle:")
else:
     st.write(" With this parameter students will be DROPOUT :large_orange_circle:")