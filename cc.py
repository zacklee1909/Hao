import streamlit as st

# Tiêu đề của ứng dụng
st.title("Form Nhập Thông Tin (Chỉ Lập Trình Viên Thấy Kết Quả)")

# Form để người dùng nhập thông tin
with st.form(key='user_form'):
    # Nhập tên và email
    name = st.text_input("Nhập tên:")
    email = st.text_input("Nhập email:")
    
    # Nhập mật khẩu (ẩn thông tin nhập vào)
    password = st.text_input("Nhập mật khẩu:", type="password")
    
    # Nút Submit để gửi form
    submit_button = st.form_submit_button(label='Gửi')

# Xử lý khi người dùng nhấn nút gửi
if submit_button:
    # Lưu thông tin vào Session State (sẽ không được lưu vào file)
    st.session_state.name = name
    st.session_state.email = email
    st.session_state.password = password

    # Hiển thị thông báo thành công cho người dùng (chỉ thông báo thành công)
    st.success("Thông tin đã được gửi thành công!")

    # *** Lập trình viên có thể xem thông tin trong backend ***
    # In thông tin ra console (được lập trình viên thấy trong terminal)
    print(f"Thông tin người dùng (chỉ lập trình viên thấy):")
    print(f"Tên: {name}, Email: {email}, Mật khẩu: {password}")

# Tùy chọn cho lập trình viên: Xem thông tin đã được nhập trong Session State
if st.button('Xem thông tin người dùng'):
    if 'name' in st.session_state and 'email' in st.session_state and 'password' in st.session_state:
        st.write(f"Tên: {st.session_state.name}")
        st.write(f"Email: {st.session_state.email}")
        st.write(f"Mật khẩu: {st.session_state.password}")
    else:
        st.write("Không có dữ liệu để hiển thị.")
