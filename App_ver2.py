#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
from PIL import Image
import time


# setting the application name

# %%


st.set_page_config(page_title="Segment Classification App")


# setting the application title

# %%


st.title("Practitioner Segment Classification Tool")


# %%


image=Image.open(r'C:\Users\AnkAnalytics-Ananyo\Desktop\Ank_projects\eye-doc.jpg')
st.image(image)


# setting the app layout

# %%


st.write("The form provided below contain some statements regarding which you need to give your honest opinions.\n")


# %%


name=st.text_input(label='Enter your name')
mail=st.text_input(label="Enter your email address")


# setting up the form

# %%


confidence=st.number_input(label="Enter your expected level of confidence (should be between 0 and 1)", min_value=0.0, max_value=1.0)
conf=float(confidence)


# %%
st.write("Please upload csv file with ID, Responses in order.")
result = []
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Rows:",df.shape[0],"Columns:",df.shape[1])
    def show(df):
        st.write(df)    
    def calc(df):
            i=0 
            results = {
            'Passive Prescribers': 0,
            'Passionate About Patients':0,
            'Business Champs':0,
            'Not Classified':0
            }
            for i,row in df.iterrows():
                sum1= math.exp(21.084+(-0.18312*row['R1'])+(-0.6933*row['R2'])+(-2.055024*row['R3'])+(-0.94069*row['R4'])+(1.2012*row['R5'])+(1.34868*row['R6'])+(-0.9822*row['R7'])+(0.415055*row['R8'])+(-0.468825*row['R9'])+(-0.9594*row['R10']))
                sum2= math.exp(7.51036+(0.733922*row['R1'])+(-1.0524*row['R2'])+(-1.9372*row['R3'])+(-0.771995*row['R4'])+(0.1684*row['R5'])+(-0.193325*row['R6'])+(0.1388*row['R7'])+(1.8442*row['R8'])+(0.28984*row['R9'])+(-0.7406*row['R10']))
                sum3= math.exp(0)
                prob1=sum1/(sum1+sum2+sum3)
                prob2=sum2/(sum1+sum2+sum3)
                prob3=sum3/(sum1+sum2+sum3)
                if(prob1>=conf):
                    results['Passive Prescribers'] +=1
                elif(prob2>=conf):
                    results['Passionate About Patients'] +=1
                elif(prob3>=conf):
                    results['Business Champs'] +=1
                else:
                    results['Not Classified'] +=1
            result.append(results)
else :
    st.write('Empty File!')

# %%
try:
    if(st.button(label="Show")):
            prog=st.progress(0)
            for i in range(100):
                time.sleep(0.001)
                prog.progress(i+1)
            st.success(show(df))
    if(st.button(label="Submit")):
            prog=st.progress(0)
            for i in range(100):
                time.sleep(0.001)
                prog.progress(i+1)
            st.success(calc(df))     
            final_count = pd.DataFrame(result)
            st.write(final_count)
            st.write("   ------------------------------------------------------------------------------------------------    ")             
except:
    st.write("Please load a file to continue...")

