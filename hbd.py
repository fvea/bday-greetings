import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pygame
import time
import threading

# Initialize pygame for music playback
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("happy_birthday.mp3")
    pygame.mixer.music.play(-1)

# Set page config
st.set_page_config(
    page_title="Happy Birthday!",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# State to track if lights are on
if "lights_on" not in st.session_state:
    st.session_state.lights_on = False

# Decorated function for theme control using st.fragment()
@st.fragment
def theme_switcher():
    dark_mode = st.toggle("💡 Turn on Lights", value=st.session_state.lights_on)
    if dark_mode:
        st._config.set_option('theme.base', "dark")
        st.session_state.lights_on = True
    else:
        st._config.set_option('theme.base', "light")
        st.session_state.lights_on = False
    st.rerun(scope="fragment")

# Display the theme switcher (this will update independently)
theme_switcher()

# Start the greeting only when the lights are turned on
if st.session_state.lights_on:
    # Start music in a separate thread
    threading.Thread(target=play_music, daemon=True).start()

    # Create a placeholder for dynamic text
    placeholder = st.empty()

    # Step 1: Display the initial greeting
    with placeholder:
        st.title("🎉 Happy Birthday, Cherrylyn! 🎈")

    # Trigger confetti and balloons
    st.toast("🎉 Let the celebration begin! 🎉")
    st.snow()

    # Wait before replacing the text
    time.sleep(3)

    # Step 2: Clear the initial greeting and show the final message
    with placeholder:
        st.title("🎂 Wishing you a day filled with love, joy, and cake! 🍰")

    # More animation
    time.sleep(1)
    st.toast("🎈🎈🎈 Balloons everywhere! 🎈🎈🎈")
    st.snow()

    # Add some spacing for layout
    add_vertical_space(2)

    # Footer message
    st.write("💖 Have an amazing year ahead, Cherrylyn! 💖")
