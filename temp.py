# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numphy as np
import streamlit as st

loaded_model = pickle.load(open(r'C:\Users\Shounak\Downloads\TD ML-Project\Heart disease\heart_disease_trained_model.sav','rb'))

def heart_disease_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data)
    
    input_data_reshape = input_data_as_np_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
    if(prediction[0] == 0):
        return 'The person does not have a heart disease'
    else:
        return 'The person has a heart disease'

def main():
    
    st.title('Heart disease Prediction Web App')
    
    
    Age = st.text_input('Age')
    Sex = st.text_input('Sex (1->Male, 0->Female)')
    Cp = st.text_input('Chest Pain Type(0,1,2,3)')
    trestbps = st.text_input('Resting Blood Pressure (in mm Hg on admission to the hospital)')
    chol = st.text_input('Serum Cholestral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar (1->True, 0->False)')
    restecg = st.text_input('Resting Electrocardiographic Results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('The Slope of the peak exercise ST segment')
    ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    thal = st.text_input('1 = Normal; 2 = Fixed defect; 3 = Reversable defect')

    #variable for Prediction
    diagnosis = ''
    
    if st.button('Test Result :'):
        diagnosis = heart_disease_prediction([Age,Sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.sucess(diagnosis)
    
if __name_ == "__main__":
    main()

    