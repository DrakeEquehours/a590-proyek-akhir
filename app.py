import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model/random_forest_model.joblib')
data = pd.read_csv('data.csv', sep=';')

features = data.columns.tolist()
features.remove('Status')

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

st.sidebar.subheader("User Input:")
st.sidebar.write(user_df)

prediction = model.predict(user_df)

st.subheader("Prediction:")
if prediction[0] == 'Graduated':
    st.write(" With this parameter students will be GRADUATED :green_circle:")
else:
     st.write(" With this parameter students will be DROPOUT :red_circle:")