import streamlit as st
import random

st.header("Let's pick what you want to eat 😋")

thai = ["noodle", "Pad Thai", "Papaya Salad", "Stickyrice"]
random_thai = random.choice(thai)

japan = ["sushi","ramen"]
random_japan = random.choice(japan)

korea = ["Bibimbub","Kimchi"]

stye = st.radio('What nation do you want',options = [f'Thai', f'Japan', f'Korea',f'Vietnam',f'China',f'What ever'],horizontal=True)

type = st.radio('What type do you want',options = ['Noodle', 'Snack', 'Vegan'],horizontal=True)

feel = st.radio('Today weather is too.....',options = ['Hot', 'Cold', 'Normal'],horizontal=True)


if stye == 'Thai':
    if type == 'Noodle':
        if feel == 'Hot':
            st.write(f"Do you want {random_thai}")

elif stye == 'Japan':
    if type == 'Noodle':
        if feel == 'Cold':
             st.write(f"Do you want {random_japan}")

else:
    st.write(f"try another choice")