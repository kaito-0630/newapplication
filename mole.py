import streamlit as st
import random

st.title("Whack-a-Mole")

mole_count = 0
score = 0

while mole_count < 10:
    mole_appeared = random.randint(0, 1)

    if mole_appeared:
        mole_count += 1
        button_label = "Whack the mole!"
        result = "Mole appeared!"
    else:
        button_label = "No mole here..."
        result = "No mole appeared."

    button_clicked = st.button(button_label)

    if button_clicked and mole_appeared:
        score += 1
        result = "You whacked the mole! Score: {}".format(score)
    elif button_clicked and not mole_appeared:
        result = "You missed! Score: {}".format(score)

    st.write(result)

st.write("Game over! Final score: {}".format(score))