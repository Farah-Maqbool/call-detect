import streamlit as st
from stt import speech_to_text
from classify import classify_text
from action import send_email_alert

st.title('Call Detect')
uploaded_file = st.file_uploader('Upload Call Recording (mp3/wav)',type=['mp3','wav'])

if uploaded_file:

    audio_path = f'temp_audio.{uploaded_file.name.split('.')[-1]}'
    with open(audio_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.audio(audio_path, format='audio/mp3')

    st.write("Processing audio...")
    text = speech_to_text(audio_path)
    st.write("Transcribed Text:", text)


    result = classify_text(text)
    st.write("Threat Detected?", result)

    
    if result == "YES":
        send_email_alert(text)
        st.success("Alert sent to security team!")
    else:
        st.info("No threat detected.")
