import streamlit as st
import pandas as pd
st.title("Python project")
with st.form("Điền vào chỗ cần điền"):
    name = st.text_input("Họ và tên")
    age = st.text_input("Tuổi")
    work = st.text_input("Nghề nghiệp")
    favor = st.text_input("Sở thích")
    sdt = st.text_input("SĐT")
    gift = st.text_input("Gửi lời cho người làm code")
    send = st.form_submit_button("Send")
if send:
    st.session_state.name = name
    st.session_state.age = age
    st.session_state.work = work
    st.session_state.favor = favor
    st.session_state.sdt = sdt
    st.session_state.gift = gift
    print(f"Thông tin người dùng:")
    print(f"{name},{age},{work},{favor},{sdt},{gift}")
    st.success(f"Cảm ơn {name} rất nhiều.")
if st.button('Xem thông tin người dùng'):
    if 'name' in st.session_state and 'age' in st.session_state and 'work' in st.session_state and 'favor' in st.session_state and 'sdt' in st.session_state and 'gift' in st.session_state:
        st.write(f"Họ và tên : {st.session_state.name}") 
        st.write(f"Tuổi : {st.session_state.age}")
        st.write(f"Nghề nghiệp : {st.session_state.work}")
        st.write(f"Sở thích : {st.session_state.sdt}")
        st.write(f"Gift : {st.session_state.gift}")
    else:
        st.write("Không có dữ liệu để hiển thị.")
