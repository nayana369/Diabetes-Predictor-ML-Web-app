import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("model_svc_pickle", "rb")
classifier = pickle.load(pickle_in)

df = pd.read_csv('diabetes.csv')
df_features = df.iloc[:,0:8]

def diabetes_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
  prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
  print(prediction)
  return prediction

def main():
  st.title('')
  html_temp = """
  <div style="background-color:#546beb; padding:10px">
  <h2 style="color:#93f50a;text-align:center;">Diabetes Predictor </h2>
  </div>
  """

  st.markdown(html_temp, unsafe_allow_html=True)
  #years = st.text_input("Years")  #years = st.text_input("Years","Type Here")
  #Pregnancies = st.text_input("Pregnancies")
  #Glucose = st.text_input("Glucose")
  #BloodPressure = st.text_input("BloodPressure")
  #SkinThickness = st.text_input("SkinThickness")
  #Insulin = st.text_input("Insulin")
  #BMI = st.text_input("BMI")
  #DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
  #Age = st.text_input("Age")

  Pregnancies = st.sidebar.slider('Pregnancies', 0, 20, 10)
  Glucose = st.sidebar.slider('Glucose', 0.0, 200.0, 50.0)
  BloodPressure  = st.sidebar.slider('Blood Pressure', 0.0,140.0, 98.0  )
  SkinThickness = st.sidebar.slider('Skin Thickness', 0.0, 100.0, 67.0)
  Insulin = st.sidebar.slider('Insulin', 0.0, 900.0, 150.0)
  BMI = st.sidebar.slider('BMI', 0.0, 70.0, 45.0)
  DiabetesPedigreeFunction = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 4.0, 0.125)
  Age = st.sidebar.slider('Age', 21, 100, 38 )

  # printing user inputs
  user_input = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
  col_head = list(df_features.columns.values)
  f = pd.DataFrame(user_input,columns = col_head)
  st.write('User Inputs')
  st.write(f)
  
  


  result = ""
  result1 = ""
  if st.button("Predict"):
    result1 = diabetes_prediction(float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age))
  
  if result1 == 0:
    result = "You don't have diabetes"
  else :
    result = "You have diabetes"
  st.success(result)
 
  
  


main()

