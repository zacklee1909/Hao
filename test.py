import streamlit as st
import pandas as pd
st.title("Python project")
with st.form("Điền vào chỗ cần điền"):
    name = st.text_input("Họ và tên")
    age = st.text_input("Tuổi")
    work = st.text_input("Nghề nghiệp")
    favor = st.text_input("Sở thích")
    gift = st.text_input("Gửi lời cho người làm code")
    send = st.form_submit_button(Label='Gửi')
if send:
    data = {
        "Name": [name],
        "Age": [age],
        "Work": [work],
        "Favorite": [favor],
        "Gift": [gift]
    }
    df = pd.DataFrame(data)
    print(f"Thông tin người dùng:")
    print(f"{name},{age},{work},{favor},{gift}")
    df.to_csv("form_data.csv",mode='a',header=False,index=False)
    st.success(f"Cảm ơn {name} rất nhiều.")
