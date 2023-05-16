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
    ha.main_loop()


st.button("Re-run")
