import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model=pickle.load(open('saved model/diabetes_model.sav','rb'))

heart_model=pickle.load(open('saved model/heart_model.sav','rb'))

parkinsons_model=pickle.load(open('saved model/parkinsons_model.sav','rb'))

#sidebar for navigation

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
#Diabetes Prediction System
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    #getting the input data from user
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('blood Pressure Level')
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin Value')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age value')
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is not Diabetic'
    st.success(diab_diagnosis)
    
        
        
    
    
    
#Heart Disease Prediction System
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.number_input('Age value')
    with col2:
        Sex=st.number_input('Gender value')
    with col3:
        CP=st.number_input('CP value')
    with col1:
        RBP=st.number_input('resting blood pressure')
    with col2:
        SC=st.number_input('serum cholestoral in mg/dl')
    with col3:
        FBS=st.number_input('fasting blood sugar > 120 mg/dl')
    with col1:
        RES=st.number_input('resting electrocardiographic results (values 0,1,2)')
    with col2:
        MHR=st.number_input('maximum heart rate achieved')
    with col3:
        EIA=st.number_input('exercise induced angina')
    with col1:
        OP=st.number_input('oldpeak = ST depression induced by exercise relative to rest')
    with col2:
        ST_segment=st.number_input('the slope of the peak exercise ST segment')
    with col3:
        MV=st.number_input('number of major vessels (0-3) colored by flourosopy')
    with col1:
        TNF=st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     #code for prediction
    heart_diag=''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_model.predict([[Age,Sex,CP,RBP,SC,FBS,RES,MHR,EIA,OP,ST_segment,MV,TNF]])
        
        if (heart_prediction[0]==1):
            heart_diag='The Person prone to heart disease'
        else:
            heart_diag='The Person is healthy'
    st.success(heart_diag)
    
        
        
    
    
        
        
        
    
    
#Parkinson's Prediction System
if (selected == 'Parkinsons Prediction'):
    st.title("Parkinson\'s Prediction using ML")
    MDVP=st.text_input('MDVP:Fo(Hz)')
    MDVPF=st.text_input('MDVP:Fhi(Hz)')
    MDVPFL=st.text_input('MDVP:Flo(Hz)')
    MDVPJ=st.text_input('MDVP:Jitter(%)')
    MDVPJ1=st.text_input('MDVP:Jitter(Abs)')
    MDVPR=st.text_input('MDVP:RAP')
    MDVPP=st.text_input('MDVP:PPQ')
    Jitter=st.text_input('Jitter:DDP')
    MDVPS=st.text_input('MDVP:Shimmer')
    MDVPSH=st.text_input('MDVP:Shimmer(dB)')
    Shimmer=st.text_input('Shimmer:APQ3')
    ShimmerA=st.text_input('Shimmer:APQ5')
    MDVPA=st.text_input('MDVP:APQ')
    ShimmerD=st.text_input('Shimmer:DDA')
    NHR=st.text_input('NHR')
    HNR=st.text_input('HNR')
    RPDE=st.text_input('RPDE')
    DFA=st.text_input('DFA')
    spread1=st.text_input('spread1')
    spread2=st.text_input('spread2')
    D2=st.text_input('D2')
    PPE=st.text_input('PPE')
    
    parkinsons_diag=''
     #creating a button for prediction
    if st.button('Parkinson\'s Disease Test Result'):
        parkinsons_prediction=parkinsons_model.predict([[MDVP,MDVPF,MDVPFL,MDVPJ,MDVPJ1,MDVPR,MDVPP,Jitter,MDVPS,MDVPSH,Shimmer,ShimmerA,MDVPA,ShimmerD,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (parkinsons_prediction[0]==1):
            parkinsons_diag='The Person prone to Parkinson\'s Disease'
        else:
            parkinsons_diag='The Person is healthy'
    st.success(parkinsons_diag)
    
    
