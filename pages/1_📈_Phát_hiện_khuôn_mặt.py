import streamlit as st
import time
import numpy as np
import cv2 as cv
import object_detection as od
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb
from PIL import Image

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="📈")

st.markdown("# Phát hiện khuôn mặt")

options = ["Facebook", "Haarcascade"]
selected_chapter = st.sidebar.selectbox("Select an option", options)

if selected_chapter == "Facebook":
    fb.main_loop()
elif selected_chapter == "Haarcascade":
    camera_device = 0
    cap = cv.VideoCapture(camera_device)
    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        if frame is None:
            st.error('No captured frame')
            break
        frame = ha.detectAndDisplay(frame)
        stframe.image(frame, channels="BGR")


st.button("Re-run")
