import requests
import streamlit as st

def get_bot_response(user_input):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"sender": "user", "message": user_input}
    response = requests.post(url, json=payload)
    bot_response = response.json()[0]['text']
    return bot_response

def main():
    st.title("Sigortam Cepte FAQ")

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

    if 'chat_log' not in st.session_state:
        st.session_state.chat_log = []

    if 'enter_pressed' not in st.session_state:
        st.session_state.enter_pressed = False

    if 'enter_key_count' not in st.session_state:
        st.session_state.enter_key_count = 0

    user_input = st.text_input("User Input", value=st.session_state.user_input)

    if st.button("Send") or (st.session_state.enter_pressed and st.session_state.enter_key_count % 2 == 0):
        response = get_bot_response(user_input)
        st.session_state.chat_log.insert(0, ("Bot", response))
        st.session_state.chat_log.insert(0, ("User", user_input))
        st.session_state.user_input = ''
        st.session_state.enter_key_count += 1
        st.session_state.enter_pressed = False

    if st.session_state.enter_pressed:
        st.session_state.enter_key_count += 1
        st.session_state.enter_pressed = False

    for role, message in st.session_state.chat_log:
        st.write(f"{role}: {message}")

if __name__ == "__main__":
    main()
