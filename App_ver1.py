#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import streamlit as st
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


#image=Image.open(r'C:\Users\AnkAnalytics-Ananyo\Desktop\Ank_projects\eye-doc.jpg')
#st.image(image)
st.image('https://drscdn.500px.org/photo/1074121807/q%3D50_w%3D1000_of%3D1/v2?sig=8da04b764dde17f25bc233e7c84396f419d4986446da422cf1eed401200850d1')

# setting the app layout

# %%


st.write("The form provided below contain some statements regarding which you need to give your honest opinions.\n")


# %%


name=st.text_input(label='Enter your name')
mail=st.text_input(label="Enter your email address")


# %%


st.write("It is required to rate the statements on a scale of 1 to 7, where 1 indicates a statement that you strongly disagree and 7 indicates a statement that you strongle agree.")


# setting up the form

# %%


confidence=st.number_input(label="Enter your expected level of confidence (should be between 0 and 1)", min_value=0.0, max_value=1.0)
conf=float(confidence)


# %%


st.write("The statements are as follows:")


# %%


st.write("1. We have sufficient time to complete patient appointments:")
x1=st.radio(label = "1",options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x1=int(x1)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("2. There is pressure to achieve performance goals:")
x2=st.radio(label="2", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x2=int(x2)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("3. The number of Patients per day/week/month we see in our location is important:")
x3=st.radio(label="3", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x3=int(x3)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("4. The number of repeat patients we have for exams and eyewear is important:")
x4=st.radio(label="4", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x4=int(x4)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("5. We are comfortable/confident recommending photochromic lenses to patients:")
x5=st.radio(label="5", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x5=int(x5)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("6. We are comfortable/confident recommending a second pair of eyeglasses to patients:")
x6=st.radio(label="6", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x6=int(x6)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("7. At our practice, helping patients see clearly in all conditions is motivating:")
x7=st.radio(label="7", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x7=int(x7)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("8. We have a stronger emphasis on patient care over other business responsibilities and goals:")
x8=st.radio(label="8", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x8=int(x8)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("9. Everyone's work is valued and respected:")
x9=st.radio(label="9", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x9=int(x9)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# %%


st.write("10. It is important to the staff that they achieve regular salary or commission increases:")
x10=st.radio(label="10", options=['1','2','3','4','5','6','7'],label_visibility="collapsed")
x10=int(x10)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


# fitting the back end algorithm

# %%


def Response():
    sum1= math.exp(21.084+(-0.18312*x1)+(-0.6933*x2)+(-2.055024*x3)+(-0.94069*x4)+(1.2012*x5)+(1.34868*x6)+(-0.9822*x7)+(0.415055*x8)+(-0.468825*x9)+(-0.9594*x10))
    sum2= math.exp(7.51036+(0.733922*x1)+(-1.0524*x2)+(-1.9372*x3)+(-0.771995*x4)+(0.1684*x5)+(-0.193325*x6)+(0.1388*x7)+(1.8442*x8)+(0.28984*x9)+(-0.7406*x10))
    sum3= math.exp(0)
    
    prob1=sum1/(sum1+sum2+sum3)
    prob2=sum2/(sum1+sum2+sum3)
    prob3=sum3/(sum1+sum2+sum3)
    
    if(prob1>=conf):
        result="Passive Prescribers"
    elif(prob2>=conf):
        result="Passionate about Patients"
    elif(prob3>=conf):
        result="Business Champs"
    else:
        result="Not Classified"
    
    return result
        
#setting up the submit button and the result widget
if(st.button(label="Submit")):
    
    prog=st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        prog.progress(i+1)
        
    st.success(Response())

