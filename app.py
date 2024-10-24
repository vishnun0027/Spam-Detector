import streamlit as st
from spamdetector import Detection


# Page Config
st.set_page_config("Spam Detector", page_icon="📩")
# tittle
st.title("Spam Detector 🚨📩")
st.sidebar.info("""The app detects whether a message is spam or not. Users input a message,
           wait for a moment while it's analyzed, and then receive the result: either
         "spam" or "not spam.""")


message = st.text_area("Enter your message/mail here",height=200)
if st.button("Predict"):
    if message:
        with st.spinner("Detecting..."):
            result = Detection(message)
        if result == "SPAM":
            st.error("Spam", icon="🚨") 
        if result == "NOT SPAM":
            st.success("Not Spam",icon="✅")   
    else:
        st.warning("Please enter a message.")
