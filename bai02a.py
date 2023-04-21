import streamlit as st
import cv2

st.subheader('Phát hiện khuôn mặt')
FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        break
cap.release()
