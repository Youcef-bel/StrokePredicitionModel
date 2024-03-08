import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('clf.sav', 'rb'))

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

def main():
    
    
    # giving a title
    st.title('Stroke Prediction Web App')
    
    
    # getting the input data from the user
    
    
    gender = st.selectbox('Gender',('Male','Female'))
    age = st.text_input('Age')
    hypertension = st.selectbox('Do you have a hypertension ',('Yes','No'))
    heart_disease = st.selectbox('Do you have a Heart disease ',('Yes','No'))
    ever_married = st.selectbox('Are you merried? ',('Yes','No'))
    work_type = st.selectbox('Your work type?',('Private', 'Self-employed', 'Governement job', 'Working with children', 'Never worked'))
    residence_type = st.selectbox('Residence type ',('Urban','Rural'))
    avg_glucose_level = st.text_input('Average glucose level')
    bmi = st.text_input('BMI')
    smoking_status = st.selectbox('Are you a smoker? ',('Yes','No'))
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict!'):
        diagnosis = diabetes_prediction([gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level,bmi,smoking_status])
        
        
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
