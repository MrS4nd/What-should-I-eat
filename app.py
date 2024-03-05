import streamlit as st
import random
import itertools

st.header("Let's random what you want to eat 😋")

drinks = 'drinks.txt'

th = 'thai.txt'
viet = 'viet.txt'
jap = 'japan.txt'
ko = 'korea.txt'
ch = 'ch.txt'


def drink_menu(drinks):
    with open(drinks,'r') as d:
        d_lines = d.readlines()
        drinks_lines = random.choice(d_lines) 
    return drinks_lines.strip() 

def thai_menu(th):
    with open(th,'r') as t:
        t_lines = t.readlines()
        thai_lines = random.choice(t_lines)
    return thai_lines.strip()

def Viet_menu(viet):
    with open(viet,'r') as v:
        v_lines = v.readlines()
        viet_lines = random.choice(v_lines)
    return viet_lines.strip()
    
def Japan_menu(jap):
    with open(jap,'r') as j:
        j_lines = j.readlines()
        japan_lines = random.choice(j_lines)
    return japan_lines.strip()
    
def Korea_menu(ko):
    with open(ko,'r') as k:
        k_lines = k.readlines()
        korea_lines = random.choice(k_lines)
    return korea_lines.strip()   

def China_menu(ch):
    with open(ch,'r') as c:
        c_lines = c.readlines()
        china_lines = random.choice(c_lines)
    return china_lines.strip()

user = st.radio('Do you have any preferred foods that you\'d like?',options = ['Yes', 'No'],horizontal=True)
if user == 'Yes': 
    user_input = st.text_input("Your food option: ")
    food_op = [option.strip() for option in user_input.split(",")]
    random_user = random.choice(food_op)

al = st.radio('Are there any foods that you allergies for?',options = ['Yes', 'No',],horizontal=True)
if al == 'Yes':
    allergy = st.multiselect('What types of food are you allergic to?',['Dairy products 🥛','Eggs 🥚','Vegetables 🥗','Fish 🐟','Crustacean shellfish 🦐',
                            'Tree nuts 🌰','Peanuts 🥜','Wheat 🌾','Soybeans 🫘','Sesame 𓇢'])

pick = st.radio('Are there any foods that you don\'t eat?',options = ['Yes', 'No',],horizontal=True)
if pick == 'Yes':
    choose = st.multiselect('Are there any foods that you don\'t eat?',['Pork 🐖','Beef 🐄','Chicken 🐓','Spicy 🌶️','Seafood 🦪'])

nation = st.multiselect('Which cuisine\'s dishes do you prefer?',['Thailand 🛕','Vietnam 🪷','Japan ⛩️','Korea 🫰','China 🧧'])

drink = st.radio('Would you like a drink with that?',options = ['Yes','No'],horizontal=True)

if st.button('Start Random') or nation:
    if user == 'Yes':
        st.write("You should eat :", random_user)

    if nation == True:

        st.write("")

        if 'Thailand 🛕' in nation:
            st.write("For Thai dishes :", thai_menu(th))    
        
        if 'Korea 🫰' in nation:
            st.write("For Korea dishes :",Korea_menu(ko))
    
        if 'Vietnam 🪷' in nation:
            st.write("For Vietnam dishes :",Viet_menu(viet))
    
        if 'Japan ⛩️' in nation:
            st.write("For Japan dishes :",Japan_menu(jap))

        if 'China 🧧' in nation:
            st.write("For Chinese dishes :",China_menu(ch))

        if drink == 'Yes':
                st.write("For drinks :", drink_menu(drinks))
        elif nation == False:

            st.write("Please slect \"Cuisines\" or \"Enter your food options\"")

else:
    st.write('Please select \"Cuisines\" or \"Enter your food options\" and then press \"Start Random\" 🥺')