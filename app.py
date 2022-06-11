import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st
import base64
from PIL import Image

#app=Flask(__name__)
#Swagger(app)


pickle_in = open("crc.pkl","rb")
classifier=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_classifier(abd_tend_score, PR_score,age_group,code_D11_1st,code_D11_2nd,code_D12_1st,code_D12_2nd	,code_T08_1st,	code_T08_2nd,abdominal_pain_frequency,	code_D16_1st,code_D16_2nd,	Sex,	age_at_dendrite_date,	code_D01_1st,code_D01_2nd,code_D01_3rd,	code_D06_1st,code_D06_2nd,	code_D06_3rd,	code_D06_4th,	code_D06_5th,code_D11_3rd,code_D11_4th,code_D11_5th,code_D16_3rd,code_D63_1st,code_D63_2nd,	time_before_dendriteD01_1st	,time_before_dendriteD01_2nd,time_before_dendriteD01_3rd,	time_before_dendriteD06_1st,time_before_dendriteD06_2nd,time_before_dendriteD06_3rd,	time_before_dendriteD06_4th,time_before_dendriteD06_5th,time_before_dendriteD11_1st,	time_before_dendriteD11_2nd	,time_before_dendriteD11_3rd,	time_before_dendriteD11_4th,	time_before_dendriteD11_5th,	time_before_dendriteD12_1st,	time_before_dendriteD12_2nd,	time_before_dendriteD16_1st,	time_before_dendriteD16_2nd	,time_before_dendriteD16_3rd,	time_before_dendriteD63_1st,	time_before_dendriteD63_2nd	,time_before_dendriteT08_1st,	time_before_dendriteT08_2nd,	inv_PR_Ca_suspected,	inv_PR_abnormal,	inv_PR_normal_1st,	inv_PR_normal_2nd,	inv_FOB_positive,	invtime_PR_Ca_suspected,	invtime_PR_abnormal,	invtime_PR_normal_1st,	invtime_PR_normal_2nd	,invtime_FOB_positive,	haemoglobin1,	haemoglobin_time1,haemoglobin2,	haemoglobin_time2,	haemoglobin3,	haemoglobin_time3,	haemoglobin4,	haemoglobin_time4,	haemoglobin5,	haemoglobin_time5,	haemoglobin6,	haemoglobin_time6,	haemoglobin7,	haemoglobin_time7,	haemoglobin_low_figure_1st,	diabetic_control_poor	,code_D01_frequency,	code_D06_frequency,	code_D11_frequency,	code_D16_frequency,	invtime_PR_abnormal_any,	labelled_diabetic,	last_sugar	,time_last_sugar,	haematochezia,	time_haematochezia,	inv_PR_rectal_disease,	inv_PR_abnormal_any,	abdo_pain_score,	diarrhoea_score,	RB_score,	FOB_score	,constipation_score,	LOW_score,	anaemia_score,	sugar_score,	ham_score,score_caper1,abdo_pain_score1,diarrhoea_score1,LOW_score1,anaemia_score1,	constipation_score1,last_five_score,score_nofob,earliest_abdo_pain,abdo_pain_last_year,	earliest_loss_of_weight,loss_of_weight_last_year,	earliest_constipation,constipation_last_year,	earliest_diarrhoea,diarrhoea_last_year,earliest_rectal_bleeding,rectal_bleeding_last_year,	earliest_FOB,FOB_last_year):

    prediction=classifier.predict([[abd_tend_score,PR_score,age_group,code_D11_1st,code_D11_2nd,code_D12_1st,code_D12_2nd	,code_T08_1st,	code_T08_2nd,abdominal_pain_frequency,	code_D16_1st,code_D16_2nd,	Sex,	age_at_dendrite_date,	code_D01_1st,code_D01_2nd,code_D01_3rd,	code_D06_1st,code_D06_2nd,	code_D06_3rd,	code_D06_4th,	code_D06_5th,code_D11_3rd,code_D11_4th,code_D11_5th,code_D16_3rd,code_D63_1st,code_D63_2nd,	time_before_dendriteD01_1st	,time_before_dendriteD01_2nd,time_before_dendriteD01_3rd,	time_before_dendriteD06_1st,time_before_dendriteD06_2nd,time_before_dendriteD06_3rd,	time_before_dendriteD06_4th,time_before_dendriteD06_5th,time_before_dendriteD11_1st,	time_before_dendriteD11_2nd	,time_before_dendriteD11_3rd,	time_before_dendriteD11_4th,	time_before_dendriteD11_5th,	time_before_dendriteD12_1st,	time_before_dendriteD12_2nd,	time_before_dendriteD16_1st,	time_before_dendriteD16_2nd	,time_before_dendriteD16_3rd,	time_before_dendriteD63_1st,	time_before_dendriteD63_2nd	,time_before_dendriteT08_1st,	time_before_dendriteT08_2nd,	inv_PR_Ca_suspected,	inv_PR_abnormal,	inv_PR_normal_1st	,inv_PR_normal_2nd,	inv_FOB_positive,	invtime_PR_Ca_suspected,	invtime_PR_abnormal,	invtime_PR_normal_1st,	invtime_PR_normal_2nd	,invtime_FOB_positive,	haemoglobin1,	haemoglobin_time1,haemoglobin2,	haemoglobin_time2,	haemoglobin3,	haemoglobin_time3,	haemoglobin4,	haemoglobin_time4,	haemoglobin5,	haemoglobin_time5,	haemoglobin6,	haemoglobin_time6,	haemoglobin7,	haemoglobin_time7,	haemoglobin_low_figure_1st,	diabetic_control_poor	,code_D01_frequency,	code_D06_frequency,	code_D11_frequency,	code_D16_frequency,	invtime_PR_abnormal_any,	labelled_diabetic,	last_sugar,	time_last_sugar,	haematochezia,	time_haematochezia,	inv_PR_rectal_disease,	inv_PR_abnormal_any,	abdo_pain_score,	diarrhoea_score,	RB_score,	FOB_score,	constipation_score,	LOW_score	,anaemia_score,	sugar_score,	ham_score,score_caper1,abdo_pain_score1,diarrhoea_score1,LOW_score1,anaemia_score1,	constipation_score1,last_five_score,score_nofob,earliest_abdo_pain,abdo_pain_last_year,	earliest_loss_of_weight,loss_of_weight_last_year,	earliest_constipation,constipation_last_year,	earliest_diarrhoea,diarrhoea_last_year,earliest_rectal_bleeding,rectal_bleeding_last_year,	earliest_FOB,FOB_last_year]])
    print(prediction)
    return prediction


def main():
    main_bg = "radmo.jpg"
    main_bg_ext = "jpg"
    #image = Image.open('CRC.png')

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.cancercenter.com/-/media/ctca/images/feature-block-images/medical-illustrations/colon-cancer-illustrated-feature-dtm.png");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




#displaying the image on streamlit app

    #st.image(image, caption='Enter any caption here')
    side_bg = "ico.jpg"
    side_bg_ext = "jpg"
    st.title("Colorectal Cancer")
    html_temp = """

    <div style="background-color:tomato;padding:10px">
    <h2 style="color:black;text-align:center;">New ColorectalCancer Prediction</h2>

    </div>
    """
    #st.markdown(html_temp,unsafe_allow_html=True)


    abd_tend_score=0
    age_group=0
    code_D11_1st=st.number_input('code_D11_1st')
    code_D11_2nd=st.number_input('code_D11_2nd')
    code_D12_1st=st.number_input('code_D12_1st')
    code_D12_2nd=st.number_input('code_D12_2nd')
    code_T08_1st=st.number_input('code_T08_1st')
    code_T08_2nd=st.number_input('code_T08_2nd')
    code_D16_1st=st.number_input('code_D16_1st')
    code_D16_2nd=st.number_input('code_D16_2nd')
    Sex=st.number_input('Sex')
    age_at_dendrite_date=st.number_input('age_at_dendrite_date')
    if(age_at_dendrite_date>=70):
        age_group=2
    elif(age_at_dendrite_date<70):
        age_group=1
    code_D01_1st=st.number_input('code_D01_1st')
    code_D01_2nd=st.number_input('code_D01_2nd')
    code_D01_3rd=st.number_input('code_D01_3rd')
    code_D06_1st=st.number_input('code_D06_1st')
    code_D06_2nd=st.number_input('code_D06_2nd')
    code_D06_3rd=st.number_input('code_D06_3rd')
    code_D06_4th=st.number_input('code_D06_4th')
    code_D06_5th=st.number_input('code_D06_5th')
    code_D11_3rd=st.number_input('code_D11_3rd')
    code_D11_4th=st.number_input('code_D11_4th')
    code_D11_5th=st.number_input('code_D11_5th')
    code_D16_3rd=st.number_input('code_D16_3rd')
    code_D63_1st=st.number_input('code_D63_1st')
    code_D63_2nd=st.number_input('code_D63_2nd')
    time_before_dendriteD01_1st=st.number_input('time_before_dendriteD01_1st')
    time_before_dendriteD01_2nd=st.number_input('time_before_dendriteD01_2nd')
    time_before_dendriteD01_3rd=st.number_input('time_before_dendriteD01_3rd')
    time_before_dendriteD06_1st=st.number_input('time_before_dendriteD06_1st')
    time_before_dendriteD06_2nd=st.number_input('time_before_dendriteD06_2nd')
    time_before_dendriteD06_3rd=st.number_input('time_before_dendriteD06_3rd')
    time_before_dendriteD06_4th=st.number_input('time_before_dendriteD06_4th')
    time_before_dendriteD06_5th=st.number_input('time_before_dendriteD06_5th')
    time_before_dendriteD11_1st=st.number_input('time_before_dendriteD11_1st')
    time_before_dendriteD11_2nd=st.number_input('time_before_dendriteD11_2nd')
    time_before_dendriteD11_3rd=st.number_input('time_before_dendriteD11_3rd')
    time_before_dendriteD11_4th=st.number_input('time_before_dendriteD11_4th')
    time_before_dendriteD11_5th=st.number_input('time_before_dendriteD11_5th')
    time_before_dendriteD12_1st=st.number_input('time_before_dendriteD12_1st')
    time_before_dendriteD12_2nd=st.number_input('time_before_dendriteD12_2nd')
    time_before_dendriteD16_1st=st.number_input('time_before_dendriteD16_1st')
    time_before_dendriteD16_2nd=st.number_input('time_before_dendriteD16_2nd')
    time_before_dendriteD16_3rd=st.number_input('time_before_dendriteD16_3rd')
    time_before_dendriteD63_1st=st.number_input('time_before_dendriteD63_1st')
    time_before_dendriteD63_2nd=st.number_input('time_before_dendriteD63_2nd')
    time_before_dendriteT08_1st=st.number_input('time_before_dendriteT08_1st')
    time_before_dendriteT08_2nd=st.number_input('time_before_dendriteT08_2nd')
    inv_PR_Ca_suspected=st.number_input('inv_PR_Ca_suspected')
    inv_PR_abnormal=st.number_input('inv_PR_abnormal')
    inv_PR_normal_1st=st.number_input('inv_PR_normal_1st')
    inv_PR_normal_2nd=st.number_input('inv_PR_normal_2nd')
    inv_FOB_positive=st.number_input('inv_FOB_positive')
    invtime_PR_Ca_suspected=st.number_input('invtime_PR_Ca_suspected')
    invtime_PR_abnormal=st.number_input('invtime_PR_abnormal')
    invtime_PR_normal_1st=st.number_input('invtime_PR_normal_1st')
    invtime_PR_normal_2nd=st.number_input('invtime_PR_normal_2nd')
    invtime_FOB_positive=st.number_input('invtime_FOB_positive')
    haemoglobin1=st.number_input('haemoglobin1')
    haemoglobin_time1=st.number_input('haemoglobin_tim1')
    haemoglobin2=st.number_input('haemoglobin2')
    haemoglobin_time2=st.number_input('haemoglobin_time2')
    haemoglobin3=st.number_input('haemoglobin3')
    haemoglobin_time3=st.number_input('haemoglobin_time3')
    haemoglobin4=st.number_input('haemoglobin4')
    haemoglobin_time4=st.number_input('haemoglobin_time4')
    haemoglobin5=st.number_input('haemoglobin5')
    haemoglobin_time5=st.number_input('haemoglobin_time5')
    haemoglobin6=st.number_input('haemoglobin6')
    haemoglobin_time6=st.number_input('haemoglobin_time6')
    haemoglobin7=st.number_input('haemoglobin7')
    haemoglobin_time7=st.number_input('haemoglobin_time7')
    h_list=[haemoglobin1,haemoglobin2,haemoglobin3,haemoglobin4,haemoglobin5,haemoglobin6,haemoglobin7]
    haemoglobin_low_figure_1st=0
    for h in h_list:
        if h<13:
            haemoglobin_low_figure_1st=h
    diabetic_control_poor=st.number_input('diabetic_control_poor')
    code_D01_frequency=code_D01_1st+code_D01_2nd+code_D01_3rd
    code_D06_frequency=code_D06_1st+code_D06_2nd+code_D06_3rd+code_D06_4th+code_D06_5th
    code_D11_frequency=code_D11_1st+code_D11_2nd+code_D11_3rd+code_D11_4th+code_D11_5th
    code_D16_frequency=code_D16_1st+code_D16_2nd+code_D16_3rd
    labelled_diabetic=st.number_input('labelled_diabetic')
    last_sugar=st.number_input('last_sugar')
    time_last_sugar=st.number_input('time_last_sugar')
    haematochezia=st.number_input('haematochezia')
    time_haematochezia=st.number_input('time_haematochezia')
    inv_PR_rectal_disease=st.number_input('inv_PR_rectal_disease')
    inv_PR_abnormal_any=0
    invtime_PR_abnormal_any=0
    if(inv_PR_rectal_disease==1 or inv_PR_Ca_suspected==1 or inv_PR_abnormal==1):
        inv_PR_abnormal_any=1
        if(inv_PR_Ca_suspected==1):
            invtime_PR_abnormal_any=invtime_PR_Ca_suspected
        elif(inv_PR_abnormal==1):
            invtime_PR_abnormal_any=invtime_PR_abnormal
    PR_score=0
    if(inv_PR_rectal_disease==1 or inv_PR_Ca_suspected==1):
        PR_score=5
    abdominal_pain_frequency=code_D06_frequency+code_D01_frequency
    abdo_pain_score=0
    abdo_pain_score1=0
    if(abdominal_pain_frequency<3):
        abdo_pain_score=abdominal_pain_frequency
        abdo_pain_score1=abdominal_pain_frequency*15
    elif(abdominal_pain_frequency>=3):
        abdo_pain_score=3
        abdo_pain_score1=45
    diarrhoea_score=0
    diarrhoea_score1=0
    if(code_D11_frequency<4):
        diarrhoea_score=code_D11_frequency
        diarrhoea_score1=code_D11_frequency*10
    elif(code_D11_frequency>=4):
        diarrhoea_score=code_D11_frequency
        diarrhoea_score1=40
    RB_score=0
    if(code_D16_frequency>0 or haematochezia==1):
        RB_score=5
    FOB_score=0
    if(inv_FOB_positive==1):
        FOB_score=8
    constipation_score=0
    constipation_score1=0
    if(code_D12_1st+code_D12_2nd>0):
        constipation_score=1
        constipation_score1=25
    LOW_score=0
    LOW_score1=0
    if(code_T08_1st+code_T08_2nd>0):
        LOW_score=2
        LOW_score1=20
    anaemia_score=0
    anaemia_score1=0
    anaemia_score_list=list()
    anaemia_score1_list=list()
    for h in h_list:
        if(h>=13):
            anaemia_score_list.append(0)
            anaemia_score1_list.append(0)
        elif(h>=12 or h<=12.9):
            anaemia_score_list.append(2)
            anaemia_score1_list.append(20)
        elif(h>=10 or h<=11.9):
            anaemia_score_list.append(3)
            anaemia_score1_list.append(30)
        elif(h<10):
            anaemia_score_list.append(5)
            anaemia_score1_list.append(-1)
    anaemia_score=max(anaemia_score_list)
    anameia_score=max(anaemia_score1_list)
    sugar_score=0
    if(last_sugar>=10):
        sugar_score=1
    ham_score=abd_tend_score+PR_score+abdo_pain_score+diarrhoea_score+RB_score+FOB_score+constipation_score+LOW_score+anaemia_score+sugar_score
    score_caper1=st.number_input('score_caper1')
    last_five_score=abdo_pain_score1+diarrhoea_score1+LOW_score1+anaemia_score1+constipation_score1
    score_nofob=st.number_input('score_nofob')
    earliest_abdo_pain=min([time_before_dendriteD01_1st,time_before_dendriteD01_2nd, time_before_dendriteD01_3rd,time_before_dendriteD06_1st, time_before_dendriteD06_2nd,time_before_dendriteD06_3rd, time_before_dendriteD06_4th,time_before_dendriteD06_5th])
    abdo_pain_last_year=0
    if(earliest_abdo_pain!=-1 or earliest_abdo_pain!=0):
        abdo_pain_last_year=1
    earliest_loss_of_weight=min([time_before_dendriteT08_1st,time_before_dendriteT08_2nd])
    loss_of_weight_last_year=0
    if(earliest_loss_of_weight!=-1 or earliest_loss_of_weight!=0):
        loss_of_weight_last_year=1
    earliest_constipation=min([time_before_dendriteD12_1st,time_before_dendriteD12_2nd])
    constipation_last_year=0
    if(earliest_constipation!=-1 or earliest_constipation!=0):
        constipation_last_year=1
    earliest_diarrhoea= min([time_before_dendriteD11_1st,time_before_dendriteD11_2nd,time_before_dendriteD11_3rd,time_before_dendriteD11_4th,time_before_dendriteD11_5th])
    diarrhoea_last_year=0
    if(earliest_diarrhoea!=-1 or earliest_diarrhoea!=0):
        diarrhoea_last_year=1
    earliest_rectal_bleeding=min([time_before_dendriteD16_1st,time_before_dendriteD16_2nd,time_before_dendriteD16_3rd,time_haematochezia])
    rectal_bleeding_last_year=0
    if(earliest_rectal_bleeding!=-1 or earliest_rectal_bleeding!=0):
        rectal_bleeding_last_year=1
    earliest_FOB=invtime_FOB_positive
    FOB_last_year=0
    if(abs(inv_FOB_positive) <= 365.2422):
        FOB_last_year=1
    result=0
    result1=0
    result2=0

    choose_model = st.sidebar.selectbox("Choose the ML Model",["None","COLORECTAL CANCER"])
    if(choose_model == "COLORECTAL CANCER"):
        result= predict_classifier(abd_tend_score, PR_score,age_group,code_D11_1st,code_D11_2nd,code_D12_1st,code_D12_2nd	,code_T08_1st,	code_T08_2nd,abdominal_pain_frequency,	code_D16_1st,code_D16_2nd,	Sex,	age_at_dendrite_date,	code_D01_1st,code_D01_2nd,code_D01_3rd,	code_D06_1st,code_D06_2nd,	code_D06_3rd,	code_D06_4th,	code_D06_5th,code_D11_3rd,code_D11_4th,code_D11_5th,code_D16_3rd,code_D63_1st,code_D63_2nd,	time_before_dendriteD01_1st	,time_before_dendriteD01_2nd,time_before_dendriteD01_3rd,	time_before_dendriteD06_1st,time_before_dendriteD06_2nd,time_before_dendriteD06_3rd,	time_before_dendriteD06_4th,time_before_dendriteD06_5th,time_before_dendriteD11_1st,	time_before_dendriteD11_2nd	,time_before_dendriteD11_3rd,	time_before_dendriteD11_4th,	time_before_dendriteD11_5th,	time_before_dendriteD12_1st,	time_before_dendriteD12_2nd,	time_before_dendriteD16_1st,	time_before_dendriteD16_2nd	,time_before_dendriteD16_3rd,	time_before_dendriteD63_1st,	time_before_dendriteD63_2nd	,time_before_dendriteT08_1st,	time_before_dendriteT08_2nd,	inv_PR_Ca_suspected,	inv_PR_abnormal,	inv_PR_normal_1st,	inv_PR_normal_2nd,	inv_FOB_positive,	invtime_PR_Ca_suspected,	invtime_PR_abnormal,	invtime_PR_normal_1st,	invtime_PR_normal_2nd	,invtime_FOB_positive,	haemoglobin1,	haemoglobin_time1,haemoglobin2,	haemoglobin_time2,	haemoglobin3,	haemoglobin_time3,	haemoglobin4,	haemoglobin_time4,	haemoglobin5,	haemoglobin_time5,	haemoglobin6,	haemoglobin_time6,	haemoglobin7,	haemoglobin_time7,	haemoglobin_low_figure_1st,	diabetic_control_poor	,code_D01_frequency,	code_D06_frequency,	code_D11_frequency,	code_D16_frequency,	invtime_PR_abnormal_any,	labelled_diabetic,	last_sugar	,time_last_sugar,	haematochezia,	time_haematochezia,	inv_PR_rectal_disease,	inv_PR_abnormal_any,	abdo_pain_score,	diarrhoea_score,RB_score,	FOB_score,constipation_score,	LOW_score,	anaemia_score,	sugar_score,	ham_score,score_caper1,abdo_pain_score1,diarrhoea_score1,LOW_score1,anaemia_score1,constipation_score1,last_five_score,score_nofob,earliest_abdo_pain,abdo_pain_last_year,	earliest_loss_of_weight,loss_of_weight_last_year,	earliest_constipation,constipation_last_year,	earliest_diarrhoea,diarrhoea_last_year,earliest_rectal_bleeding,rectal_bleeding_last_year,	earliest_FOB,FOB_last_year)
    st.success('Colorectal Cancer Prediction{}'.format(result))




if __name__=='__main__':
    main()
    set_bg_hack_url()
