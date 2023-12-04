#Importing Libraries
import pandas as pd
from PIL import Image
import streamlit as st


#1. Display Title
st.title('CadioVasculasr Syndrome Prediction')

# Subheader
st.subheader("Using Genetic Algorithm")

st.text("Hello Welcome Justytech Prediction...Helping you get better")

#2. Image selection
image=Image.open(r'C:\Users\hp\Documents\SCHOOL PROJECT\heart.jpg')
st.image(image, caption='CadioVasculasr Syndrome Prediction using Esemble Learning and Genetic Algorithm', use_column_width=True)
st.image(image, width=200)

columns =['age', 'sex', 'cp', 'chol', 'fbs', 'restecg', 'exang', 'slope', 'ca','thal']
#4. Set a subheader
st.subheader('Data Information:')


#7. Feature input from user
def get_user_input():
    
    age = st.slider('age', 0, 150, 150)
    
    sex = st.radio("Select Gender: ", ('Male', 'Female'))
    if (sex == 'Male'):
        sex  = 1
        st.success("Male")
    else:
        sex = 0
        st.success("Female")
    
    cp = st.slider('chest pain type', 120, 210, 175)
    
    trestbps = st.selectbox("resting blood pressure: ",['typical angina','atypical angina', 'non-anginal pain', 'asymptomatic'])
    if (trestbps == 'typical angina'):
        trestbps  = 1
        st.success('typical angina')
    elif (trestbps == 'atypical angina'):
        trestbps = 2
        st.success("atypical angina")
    elif (trestbps ==  'non-anginal pain'):
        trestbps = 3
        st.success("non-anginal pain")
    else:
        trestbps = 4
        st.success("asymptomatic")
        
    chol = st.slider('serum cholestoral in mg/dl', 50,500)
        
    fbs = st.number_input("fasting blood sugar > 120 mg/dl")
 
    restecg = st.slider("resting electrocardiographic results", 0, 2)
    st.text('Selected: {}'.format(restecg))
    
        
    thalach = st.number_input("fmaximum heart rate achieved",0,350)
    
    exang = st.slider("exercise induced angina:--No:0 --Yes:1", 0, 1)
    
    oldpeak = st.number_input("ST depression induced by exercise relative to rest")
    
    slope = st.number_input("the slope of the peak exercise ST segment")
    
    ca = st.slider("number of major vessels (0-3) colored by flourosopy", 0, 3)

    thal = st.slider(" 0 = normal; 1 = fixed defect;  = reversable defec", 0, 3)


    #Store a dictionary into a variable
    user_data = {
        'age':age,
        'sex':sex,
        'cp':cp,
        'trestbps':trestbps,
        'chol':chol,
        'fbs':fbs,
        'restecg':restecg,
        'thalach':thalach,
        'exang':exang,
        'oldpeak':oldpeak,
        'slope':slope,
        'ca':ca,
        'thal':thal}

    #Retransforming into dataframe
    features = pd.DataFrame(user_data, index = [0])
    return features[columns]

#8. Store user input into a variable
user_input = get_user_input()

#9. Set a subheader and display the users input
st.subheader('User Input:')
st.write(user_input)


import joblib
model =  joblib.load('cardiovascular syndrome algorithm')

#12. Store the models predictions in a variable
prediction1 = model.predict(user_input)

#13. Set a subheader and display
st.subheader('Classification: ')
if prediction1 == 0:
    st.success("you are free of cadiovascular syndrome")  
else:
    st.error("you are free of cadiovascular syndrome") 
    