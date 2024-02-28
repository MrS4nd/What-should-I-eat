import streamlit as st
import random

# Define cuisines and their dishes
cuisines = {
    'Italian': ['Pizza', 'Pasta Carbonara', 'Tiramisu'],
    'Indian': ['Butter Chicken', 'Paneer Tikka', 'Gulab Jamun'],
    'Japanese': ['Sushi', 'Ramen', 'Matcha Ice Cream']
    # Add more cuisines and dishes here
}

def generate_random_food(selected_cuisines):
    if not selected_cuisines:
        st.warning("Please select at least one cuisine.")
        return

    random_cuisine = random.choice(selected_cuisines)
    random_dish = random.choice(cuisines[random_cuisine])

    st.success(f"Your random dish: {random_dish}")

def main():
    st.title("Random Food Generator")
    st.write("Choose your favorite cuisines:")

    selected_cuisines = st.multiselect("Select cuisines", list(cuisines.keys()))
    generate_random_food(selected_cuisines)

if __name__ == "__main__":
    main()
