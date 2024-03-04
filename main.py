from gtts import gTTS
import streamlit as st

import os
import tempfile


def speak(text, lang='en'):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=text, lang=lang)
        tts.save(fp.name + '.wav')
        
        
        print(f"os.name - {os.name}")
        print(f"fp.name - {fp.name}")
        # raise Exception("test")
        
        # 운영체제에 따른 음성 파일 재생
        status = 0
        if os.name == 'nt':  # Windows
            status = os.system(f'start {fp.name}.wav')
        elif os.name == 'posix':  # Linux/macOS
            status = os.system(f'afplay {fp.name}.wav')  # macOS
        else:
            status = 1
        
        if status != 0:
            # streamlit에서 음성 파일 재생
            audio_file = open(f'{fp.name}.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav', start_time=0)
        

st.write("## Google Text-to-Speech")


lang = st.radio(
    "Please select the language you want to enter.",
    [":rainbow[EN]", ":rainbow[KO]"],
    captions = ["English.", "korean"])

selct_lang = 'en' if lang == ':rainbow[EN]' else 'ko'

if lang == ':rainbow[EN]':
    st.write('You selected English.')
else:
    st.write("You selected korean")

text = st.text_input(
        "Text to talk about 👇",
    )

if st.button('start speaking.'):
    with st.spinner('Please wait a moment...'):
        speak(text, lang=selct_lang)
        st.success('The audio file has been created and played.')
        
        ko_fi_button_html = '''
            <a href='https://ko-fi.com/J3J2V8EYP' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
            '''
        st.markdown(ko_fi_button_html, unsafe_allow_html=True)
