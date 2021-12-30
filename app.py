import streamlit as st
import joblib
filename = 'finalized_model.sav'
st.title(' IOT Device Classification App')

model = joblib.load(filename)

u1 = st.number_input('packet_inter_arrivel_A_stdev')
u2 = st.number_input('packet_inter_arrivel_stdev')
u3 = st.number_input('packet_inter_arrivel_A_avg')

u4 = st.number_input('packet_inter_arrivel_avg')
u5 = st.number_input('packet_inter_arrivel_A_max')
u6 = st.number_input('packet_inter_arrivel_max')

u7 = st.number_input('reset_B')
u8 = st.number_input('duration')
u9 = st.number_input('packet_inter_arrivel_B_median')
u10 = st.number_input('packet_inter_arrivel_A_var')

topred = [[u1, u2, u3, u4, u5, u6, u7,  u8, u9, u10]]



option = st.button('Predict' )


if option is True :
    pred = model.predict(topred)
    val = int(pred[0])
    # print(val)
    # print(type(val))

    if val == 0:
        st.subheader('Predicted - DEVICE | TV')
    elif val == 1 :
        st.subheader('Predicted - DEVICE | baby_monitor')
    elif val == 2 :
        st.subheader('Predicted - DEVICE | lights')
    elif val == 3 :
        st.subheader('Predicted - DEVICE | motion_sensor')
    elif val == 4 :
        st.subheader('Predicted - DEVICE | security_camera')
    elif val == 5 :
        st.subheader('Predicted - DEVICE | smoke_detector')
    elif val == 6 :
        st.subheader('Predicted - DEVICE | socket')   
    elif val == 7 :
        st.subheader('Predicted - DEVICE | thermostat') 
    elif val == 8 :
        st.subheader('Predicted - DEVICE | watch') 
