import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('https://github.com/Youcef-bel/StrokePredicitionModel/blob/main/clf.sav', 'rb'))

def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

ef main():
    
    
    # giving a title
    st.title('Stroke Prediction Web App')
    
    
    # getting the input data from the user
    
    
    gender = st.text_input('Gender')
    age = st.text_input('Age')
    hypertension = st.text_input('Do you have a hypertension?')
    heart_disease = st.text_input('Do you have a heart disease')
    ever_married = st.text_input('Are you merried?')
    work_type = st.text_input('Work type')
    residence_type = st.text_input('Residence type')
    avg_glucose_level = st.text_input('Average glucose level')
    bmi = st.text_input('BMI')
    smoking_status = st.text_input('Are you a smoker?')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict!'):
        diagnosis = diabetes_prediction([gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level,bmi,smoking_status])
        
        
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
