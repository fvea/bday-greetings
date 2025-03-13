import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pygame
import time
import threading

# Initialize pygame for music playback
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("happy_birthday.mp3")  # Add your music file here
    pygame.mixer.music.play(-1)  # Loop the music

# Start music in a separate thread
threading.Thread(target=play_music, daemon=True).start()

# Create a placeholder for dynamic text
placeholder = st.empty()

# Step 1: Display the initial greeting
with placeholder:
    st.title("🎉 Happy Birthday, Cherrylyn! 🎈")

# Trigger confetti and balloons
st.toast("🎉 Let the celebration begin! 🎉")
st.balloons()

# Wait before replacing the text
time.sleep(3)

# Step 2: Clear the initial greeting and show the final message
with placeholder:
    st.title("🎂 Wishing you a day filled with love, joy, and cake! 🍰")

# More animation
time.sleep(3)
st.toast("🎈🎈🎈 Balloons everywhere! 🎈🎈🎈")
st.balloons()

# Add some spacing for layout
add_vertical_space(2)

# Footer message
st.write("💖 Have an amazing year ahead, Cherrylyn! 💖")

# Stop music button
if st.button("Stop Music"):
    pygame.mixer.music.stop()
