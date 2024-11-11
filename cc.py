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
    # *** Lập trình viên chỉ thấy thông tin, không hiển thị cho người dùng ***
    # In thông tin vào console (chỉ lập trình viên thấy trong terminal)
    print(f"Thông tin người dùng (chỉ lập trình viên thấy):")
    print(f"Tên: {name}, Email: {email}, Mật khẩu: {password}")

    # *** Chỉ hiển thị cho người dùng thông báo thành công ***
    st.success("Thông tin đã được gửi thành công!")
    
    # Ẩn tất cả thông tin người dùng (không hiển thị trên giao diện)
    st.empty()  # Dòng này sẽ giúp ẩn mọi thông tin trên giao diện
