import streamlit as st
import voice_assistant
from streamlit_chat import message
import time

st.set_page_config(layout="wide", page_title="AI Voice Assistant", page_icon='🎙️')
st.title("Test the App")

listen_btn = st.button("Record")
if listen_btn:
    go = 1
    while go:
        with st.spinner("Recording User Voice ..."):
            voice_data = voice_assistant.record_audio("Recording")

        # use a unique key for each message to avoid duplicate component ID
        unique_key = f"user_msg_{int(time.time()*1000)}"
        message(voice_data, is_user=True, key=unique_key)

        go = voice_assistant.respond(voice_data)
