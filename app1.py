import streamlit as st
import matplotlib.pyplot as plt
def plot_square():
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color="blue", lw=3) 
    ax.fill(x, y, color="lightblue", alpha=0.5)  
    ax.text(0.5, 0.5, "CHO XIN 50K", color="darkblue", fontsize=20, ha='center', va='center')  
    ax.set_aspect('equal')
    ax.axis('off') 
    return fig
st.title("Gửi anh em")
st.write("mb bank 0376394887")
fig = plot_square()
st.pyplot(fig)
