import streamlit as st
import sys

sys.path.append('/home/geetheswar/Documents/projects/ChatMate/chatmate')
from streamlit_chat import message
from model import get_message

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Meet ChatMate")

def get_answer():
    question = st.session_state.input_text
    response = get_message(question)
    st.session_state.history.append({"message": question, "is_user": True})
    st.session_state.history.append({"message": response, "is_user": False})
    st.session_state.input_text = ''

for i, chat in enumerate(st.session_state.history):
    message(**chat, key=str(i))

st.text_input("Talk to Chikki", key="input_text", on_change=get_answer)
