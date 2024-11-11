import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
def plot_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color="red", lw=2)
    ax.fill(x, y, color="red", alpha=0.3)
    ax.text(0, 0, "Anh yêu em nhiều vãi lồn <3", color="black", fontsize=18, ha='center', va='center')
    ax.set_aspect('equal')
    ax.axis('off')  
    return fig
st.title("Gửi em!")
st.write("xin lỗi anh nhát nhưng mà anh biết code")
fig = plot_heart()
st.pyplot(fig)
