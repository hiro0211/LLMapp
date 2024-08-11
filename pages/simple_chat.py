import streamlit as st
import openai
import requests

st.title("simple chat")

user_message = st.text_input(label="どうしましたか")

if user_message:
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    st.write(completion)

    # ai_message = "こんにちは！"
    # st.write(ai_message)
