from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np




def predict(model, input_df):
    predictions_data = predict_model(estimator = model, data = input_df)
    return predictions_data['Label'][0]
    
model = load_model('LR-model')
 

def run():
    
    
    
    st.title("Smartphone Pricing Classification App")
    
    if True:

        battery_power = st.number_input("How many mAh (up to 6000)", 0, 6000)
        
        if st.checkbox('Does it have bluetooth?'):
            blue = 'yes'
        else:
            blue = 'no'
        
        clock_speed = st.number_input("Clockspeed (up to 3.2 GHz)", 0.0, 3.2, .1)
        
        if st.checkbox('Dual SIM?'):
            dual_sim = 'yes'
        else:
            dual_sim = 'no'
        
        fc = st.number_input("Front Camera mega pixels (up to 19 MP)", 0, 19)
        
        if st.checkbox('Does it offer 4G?'):
            four_g = 'yes'
        else:
            four_g = 'no'
        
        int_memory = st.number_input("How much internal memory or storage (up to 512 GB)?", 2, 512)
        
        m_dep = st.number_input("Smartphone Depth (up to 1 cm.)", 0.1, 1.0, .1)
        
        mobile_wt = st.number_input("Weight of Smartphone (up to 200 g.)", 80, 200)
        
        n_cores = st.number_input("Number of Cores in Processor (up to 8 cores)", 1, 8)
        
        pc = st.number_input("Selfie Camera Mega pixels (up to 20 MP)", 0, 20)
        
        px_height = st.number_input("Pixel Resolution (up to 1900 pixels in Height)", 0, 1900)
        
        px_width = st.number_input("Pixel Resolution (up to 2600 pixels in Width)", 601, 2600)
        
        ram = st.number_input("How much ram (up to 6 Giga bytes)", 0, 6)
        
        sc_h = st.number_input("Smartphone Height (up to 190 mm)", 50, 190)
        
        sc_w = st.number_input("Smartphone Width (up to 180 mm)", 0, 180)
        
        talk_time = st.number_input("Battery Life (up to 18 hours)", 0, 18)
        
        if st.checkbox('Does it offer 3G?'):
            three_g = 'yes'
        else:
            three_g = 'no'
        
        if st.checkbox('Is your smartphone touch screen?'):
            touch_screen = 'yes'
        else:
            touch_screen = 'no'
        
        if st.checkbox('Does the phone offer wifi?'):
            wifi = 'yes'
        else:
            wifi = 'no'
        
        features = {'battery_power': battery_power, 'blue': blue, 'clock_speed': clock_speed, 'dual_sim': dual_sim, 'fc': fc, 'four_g': four_g, 'int_memory': int_memory, 'm_dep': m_dep, 'mobile_wt': mobile_wt, 'n_cores': n_cores, 'pc': pc, 'px_height': px_height, 'px_width': px_width, 'ram': ram, 'sc_h': sc_h, 'sc_w': sc_w, 'talk_time': talk_time, 'three_g': three_g, 'touch_screen': touch_screen, 'wifi': wifi}
        
        features_df = pd.DataFrame([features])    
        
        st.table(features_df)
        
        if st.button("Predict"):
            output = predict(model, features_df)
        
            st.write("The phone price is within the " + str(output) + ' category!')
    
if __name__ == '__main__':
    run()