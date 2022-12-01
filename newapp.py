# %%writefile newapp.py

import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope):   

    # Pre-processing user input    
    Age = Age

    if Sex == 'M':
        Sex = 0
    elif Sex == 'F':
        Sex = 1

    if ChestPainType == 'ATA':
        ChestPainType = 0
    elif ChestPainType == 'NAP':
        ChestPainType = 1
    elif ChestPainType == 'ASY':
        ChestPainType = 2
    elif ChestPainType == 'TA':
        ChestPainType = 3

    RestingBP = RestingBP

    Cholesterol = Cholesterol

    FastingBS = FastingBS

    if RestingECG == 'Normal':
        RestingECG = 0
    elif RestingECG == 'ST':
        RestingECG = 1
    elif RestingECG == 'LVH':
        RestingECG = 2
    
    MaxHR = MaxHR

    if ExerciseAngina == 'N':
        ExerciseAngina = 0
    elif ExerciseAngina == 'Y':
        ExerciseAngina = 1
    
    Oldpeak = Oldpeak

    if ST_Slope == 'Up':
        ST_Slope = 0
    elif ST_Slope == 'Flat':
        ST_Slope = 1
    elif ST_Slope == 'Down':
        ST_Slope = 2



    # Making predictions 
    prediction = classifier.predict( 
        [[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])

    if prediction == 0:
        pred = 'No Heart Disease'
    else:
        pred = 'Heart Disease'
    return pred


# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    Age = st.number_input("Input your Age")
    Sex = st.selectbox('Sex',("M","F"))
    ChestPainType = st.selectbox("Chest Pain Type",('ATA', 'NAP', 'ASY', 'TA'))
    RestingBP = st.number_input("Resting Blood Pressure")
    Cholesterol = st.number_input('Serum cholestoral in mg/dl: ')
    FastingBS = st.selectbox('Fasting blood sugar',(0,1))
    RestingECG = st.selectbox('Resting electrocardiographic results',('Normal', 'ST', 'LVH'))
    MaxHR = st.number_input('Maximum heart rate achieved: ')
    ExerciseAngina = st.selectbox('Exercise induced angina N = No, Y = Yes: ',('N','Y'))
    Oldpeak = st.number_input('oldpeak ')
    ST_Slope = st.selectbox('The slope of the peak exercise ST segmen', ('Up', 'Flat', 'Down'))
    result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope) 
        st.success('Your Heart Disease Prediction is {}'.format(result))

if __name__=='__main__': 
    main()