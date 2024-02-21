import streamlit as st
import random

st.header("Let's pick what you want to eat 😋")

thai = ["noodle", "Pad Thai", "Papaya Salad", "Stickyrice"]
random_thai = random.choice(thai)

japan = ["sushi","ramen"]
random_japan = random.choice(japan)

korea = ["Bibimbub","Kimchi"]

allergy = st.multiselect('Allergies',['Milk 🥛','Eggs 🥚','Vegetables 🥗','Fish 🐟','Crustacean shellfish 🦐','Tree nuts 🌰','Peanuts 🥜','Wheat 🌾','Soybeans 🫘','Sesame 𓇢']) 

style = st.radio('What type do you want',options = ['Noodle', 'Snack', 'Vegan'],horizontal=True)

typ = st.radio('Today weather is too.....',options = ['Hot', 'Cold', 'Normal'],horizontal=True)


st.button("Try again")


if style == 'Thai':
    if type == 'Noodle':
        st.write(f"Do you want {random_thai}")

elif style == 'Japan':
    if type == 'Noodle':
       st.write(f"Do you want {random_japan}")

else:
    st.write(f"try another choice")