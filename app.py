import streamlit as st
from auth import signup_user, login_user
from chatbot import generate_response
from database import store_chat, get_chat_history, store_feedback
from rl_logic import adjust_prompt

# Set Streamlit page config
st.set_page_config(page_title="Affiliate Marketing Chatbot")

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Title
st.title("🤖 Affiliate Marketing Chatbot")
st.subheader("Learn why creatives are crucial!")

# --- Login/Signup Section ---
if not st.session_state.logged_in:
    with st.sidebar:
        st.header("Login / Signup")
        option = st.radio("Choose", ["Login", "Signup"])
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Submit"):
            if option == "Signup":
                if signup_user(user, pwd):
                    st.success("Signup successful! Now login.")
                else:
                    st.error("User already exists.")
            elif option == "Login":
                if login_user(user, pwd):
                    st.session_state.logged_in = True
                    st.session_state.username = user
                    st.success("Logged in successfully!")
                    st.experimental_rerun()  # 👈 this line is the fix
                else:
                    st.error("Invalid credentials")


# --- Main Chat Interface ---
else:
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))

    # User asks a question
    prompt = st.text_input("Ask your question:")
    
    if st.button("Get Answer") and prompt:
        # RL simulation: Adjust prompt if needed
        final_prompt = adjust_prompt(prompt)
        
        # Generate response via LLM
        response = generate_response(final_prompt)
        st.markdown(f"🤖 **Bot:** {response}")

        # Store chat and feedback
        store_chat(st.session_state.username, prompt, response)
        
        rating = st.radio("Was this helpful?", ["👍", "👎"])
        store_feedback(st.session_state.username, prompt, 1 if rating == "👍" else 0)

    # Show last 10 chats
    if st.checkbox("Show Chat History"):
        history = get_chat_history(st.session_state.username)
        for chat in history:
            st.markdown(f"🗨️ **You:** {chat.prompt}")
            st.markdown(f"🤖 **Bot:** {chat.response}")
            st.caption(str(chat.timestamp))
