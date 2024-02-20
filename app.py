import streamlit as st
import random


st.header("Let's pick what you want to eat 😋")

stye = st.radio('What nation do you want',options = ['Thai', 'Japan', 'Korea','Vietnm','China'],horizontal=True)

thai = ["noodle", "Pad Thai", "Papaya Salad", "Stickyrice"]
random_thai = random.choice(thai)

type = st.radio(
     "Stye o you want",
     ('Noodle', 'rice', 'fast food'))

if stye == 'Thai':
    if type == 'Noodle':
        st.write(f"Do you want {random_thai}")


else:
    st.write(f"try another choice")