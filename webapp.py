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
    smoking_status = st.selectbox('Are you a smoker? ',('Formerly smoked', 'Never smoked', 'I Smoke'))

def gender(gender):
        if gender=='Male':
            gender=0
        else:
            gender=1
            
        return gender


def hypertension(hypertension):
        if hypertension=='Yes':
            hypertension=1
        else:
            hypertension=0
            
        return hypertension

def heart_disease(heart_disease):
        if heart_disease=='No':
            heart_disease=0
        else:
            heart_disease=1
            
        return heart_disease

def ever_married(ever_married):
        if ever_married=='Yes':
            ever_married=0
        else:
            ever_married=1
            
        return ever_married

def work_type(work_type):
        if work_type=='Private':
            work_type=0
        elif work_type=='Self-employed':
            work_type=1
             elif work_type=='Governement job':
            work_type=2
      elif work_type=='Working with children':
            work_type=3
        else:
            work_type=4
            
        return work_type

def residence_type(residence_type):
        if residence_type=='Urban':
            residence_type=0
        else:
            residence_type=1
            
        return residence_type

def smoking_status(smoking_status):
        if smoking_status=='Formerly smoked':
            smoking_status=0
        elif smoking_status=='Never smoked':
            smoking_status=1
        elif smoking_status=='I Smoke':
            smoking_status=2 
        
        return smoking_status




    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict!'):
        diagnosis = diabetes_prediction([gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level,bmi,smoking_status])
        
        
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
