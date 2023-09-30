import openai
import streamlit as st
from streamlit_stream import openai_st

st.set_page_config(page_title='St_Stream', page_icon=':robot_face: ')
st.title('LLM Streaming with streamlit!')
input = st.chat_input("Say something")
if input:
    with st.chat_message("user"):
        st.write(f"Human: {input}")
    prompt = {'role': 'user', 'content': input}
    message = st.chat_message("assistant")
    with message:
        box = st.empty()
        openai_stream.stream_openai(model='gpt-3.5-turbo', prompt=prompt, box=box)