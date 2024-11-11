import streamlit as st
import pandas as pd
st.title("Python project")
with st.form(key='user_form'):
    name = st.text_input("Họ và tên")
    age = st.text_input("Tuổi")
    work = st.text_input("Nghề nghiệp")
    favor = st.text_input("Sở thích")
    sdt = st.text_input("SĐT")
    gift = st.text_input("Gửi lời cho người làm code")
    send = st.form_submit_button("Send")
if send:
    st.write(f"{name},{age},{work},{favor},{sdt},{gift}")
    st.success(f"Cảm ơn rất nhiều.")
    
