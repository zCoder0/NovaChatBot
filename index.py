import streamlit as st
import time
from MyModel import MyModel
from Translate import Translation
# Initialize the model
model = MyModel()
trans = Translation()
# Title and chatbot description
st.title("🤖 Nova Assistant")
st.markdown("Im here to help you. Feel free to ask anything!")

# CSS for styling chat bubbles with right and left alignment and fitted borders
st.markdown("""
    <style>
        /* Container for chat bubbles */
        .chat-container {
            max-width: 700px;
            margin: auto;
            display: flex;
            flex-direction: column;
        }
        
        /* User message styling - aligned to the right with border */
        .user-bubble {
            background-color: rgba(240, 240, 240, 0.8); /* Light white background */
            color: black;
            padding: 5px 10px;
            margin-top:10px;
            border-radius: 20px;
            text-align: right;
            float: right;
            clear:both;
            with : fit-content;
             border: none;
       
        }
        
        /* Bot message styling - aligned to the left with border */
        .bot-bubble {
            background-color: transparent; /* Transparent background */
            color: black;
             padding: 10px 10px;
            border-radius: 20px;
            text-align: left;
            margin-top:15px;
            float: left;
            clear: both;
            max-width: 100%;
            width: fit-content;
          
        }

        /* Typing indicator */
        .typing {
            font-style: italic;
            color: grey;
        }
    </style>
""", unsafe_allow_html=True)

# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Custom function for the gradual typing effect with emoji
def gradual_typing(response_text, delay=0.05):
    response = "🤖 "  # Add emoji before the bot's response
    typing_area = st.empty()
    for char in response_text:
        response += char
        typing_area.markdown(f"<div class='bot-bubble'>{response}▮</div>", unsafe_allow_html=True)
        time.sleep(delay)
    typing_area.markdown(f"<div class='bot-bubble'>{response}</div>", unsafe_allow_html=True)

# Input from user
user_message = st.chat_input("Type your message here...")


if user_message:
    # Add user message to history
    st.session_state.history.append({"message": user_message, "is_user": True})
    
    # Get bot response with typing effect
    
    user_message ,ln = trans.translate(user_message)
    bot_response = model.predict(user_message.lower())
    bot_response ,lng= trans.translate(bot_response,ln)
    # Append bot response to history
    st.session_state.history.append({"message": bot_response, "is_user": False})

# Display chat history with typing effect for the latest bot message
for i, chat in enumerate(st.session_state.history):
    if chat["is_user"]:
        # Display user message aligned to the right with fitted border
        st.markdown(f"""
            <div class="chat-container">
                <div class="user-bubble">{chat["message"]}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Apply gradual typing effect to only the latest bot message with emoji
        if i == len(st.session_state.history) - 1:
            gradual_typing(chat["message"])
        else:
            # Display bot message aligned to the left with emoji
            st.markdown(f"""
                <div class="chat-container">
                    <div class="bot-bubble">🤖 {chat["message"]}</div>
                </div>
            """, unsafe_allow_html=True)
