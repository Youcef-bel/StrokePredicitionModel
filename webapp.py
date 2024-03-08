import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('clf.sav', 'rb'))

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'You have a Low Risk of having a stroke'
    else:
        return 'You have a High Risk of having a stroke'

def main():
    # giving a title
    st.markdown(
        """
        <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 200px; /* Adjust the height as needed */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center"><img src="https://tse2.mm.bing.net/th/id/OIG4.gHRNynXqDtnxOHJr8Nlj?pid=ImgGn" alt="Logo" width=200 height=200></div>', unsafe_allow_html=True)
    st.title('Stroke Prediction Web App')

    # getting the input data from the user
    gender = st.selectbox('Gender', ('Male', 'Female'))
    age = st.text_input('Age')
    hypertension_input = st.selectbox('Do you have hypertension ', ('Yes', 'No'))
    heart_disease_input = st.selectbox('Do you have a Heart disease ', ('Yes', 'No'))
    ever_married_input = st.selectbox('Are you married? ', ('Yes', 'No'))
    work_type_input = st.selectbox('Your work type?', ('Private', 'Self-employed', 'Government job', 'Working with children', 'Never worked'))
    residence_type_input = st.selectbox('Residence type ', ('Urban', 'Rural'))
    avg_glucose_level = st.text_input('Average glucose level')
    bmi = st.text_input('BMI')
    smoking_status_input = st.selectbox('Are you a smoker? ', ('Formerly smoked', 'Never smoked', 'I Smoke'))

    gender_numeric = convert_gender(gender)
    hypertension_numeric = convert_hypertension(hypertension_input)
    heart_disease_numeric = convert_heart_disease(heart_disease_input)
    ever_married_numeric = convert_ever_married(ever_married_input)
    work_type_numeric = convert_work_type(work_type_input)
    residence_type_numeric = convert_residence_type(residence_type_input)
    smoking_status_numeric = convert_smoking_status(smoking_status_input)

    # Create a list of inputs for the prediction function
    input_data = [gender_numeric, age, hypertension_numeric, heart_disease_numeric, ever_married_numeric, work_type_numeric, residence_type_numeric, avg_glucose_level, bmi, smoking_status_numeric]

    diagnosis = ''

    # creating a button for Prediction
    if st.button('Predict!'):
        diagnosis = diabetes_prediction(input_data)
    st.success(diagnosis)



    st.markdown("---")
    st.markdown("<h3 style='text-align: left; color: white;'>Introduction</h3>", unsafe_allow_html=True)
    st.write("Our Stroke Prediction Model is an advanced machine learning algorithm designed to assess an individual's likelihood of experiencing a stroke in the future. Stroke, a critical medical condition, requires early detection and preventive measures to minimize the associated health risks.")
    st.markdown("---")
    st.markdown("Developed by Youcef Belmokhtar")
    st.markdown("LinkedIn profile: https://www.linkedin.com/in/youcefbelmokhtar/")

def convert_gender(gender):
    if gender == 'Male':
        return 0
    else:
        return 1

def convert_hypertension(hypertension):
    if hypertension == 'Yes':
        return 1
    else:
        return 0

def convert_heart_disease(heart_disease):
    if heart_disease == 'No':
        return 0
    else:
        return 1

def convert_ever_married(ever_married):
    if ever_married == 'Yes':
        return 0
    else:
        return 1

def convert_work_type(work_type):
    if work_type == 'Private':
        return 0
    elif work_type == 'Self-employed':
        return 1
    elif work_type == 'Government job':
        return 2
    elif work_type == 'Working with children':
        return 3
    else:
        return 4

def convert_residence_type(residence_type):
    if residence_type == 'Urban':
        return 0
    else:
        return 1

def convert_smoking_status(smoking_status):
    if smoking_status == 'Formerly smoked':
        return 0
    elif smoking_status == 'Never smoked':
        return 1
    elif smoking_status == 'I Smoke':
        return 2


if __name__ == '__main__':
    main()
