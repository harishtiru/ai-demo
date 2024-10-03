import streamlit as st
import random
import time
from langchain_cohere import ChatCohere


st.title("Test Case 4: Cohere Chat Bot - V2")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
llm = ChatCohere(model="command-r-plus",cohere_api_key="8hE4X6TIs359E7syTmVrEnAQQaIqfxDCE25W5TpJ",temperature=0)

# Accept user input
if prompt := st.chat_input("Enter your question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
       
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response=llm.invoke(prompt)
        
        st.write(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})