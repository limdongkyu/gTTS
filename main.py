from gtts import gTTS
import streamlit as st

import os
import tempfile


def speak(text, lang='en'):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=text, lang=lang)
        tts.save(fp.name + '.mp3')
        try:
            # print(f"os.name - {os.name}")
            # raise Exception("test")
            
            # 운영체제에 따른 음성 파일 재생
            if os.name == 'nt':  # Windows
                os.system(f'start {fp.name}.mp3')
            elif os.name == 'posix':  # Linux/macOS
                os.system(f'afplay {fp.name}.mp3')  # macOS
                # Linux 사용자는 다음을 사용: os.system(f'mpg321 {fp.name}.mp3')
            else:
                raise Exception("auto play not supported.")
        except Exception as e:
            print(f"error: {e}")
            try:
                # streamlit에서 음성 파일 재생
                audio_file = open(f'{fp.name}.mp3', 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3', start_time=0)
            except Exception as e:
                st.error(e)

st.write("## Google Text-to-Speech)")


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
