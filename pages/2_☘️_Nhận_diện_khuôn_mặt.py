import streamlit as st
import numpy as np
import cv2 as cv
import joblib
import Custome.custome as ct
import FaceRecognition.get_face as gf
import FaceRecognition.training as tn
import FaceRecognition.predict as pr

ct.ChangeTheme("NHẬN DIỆN KHUÔN MẶT","😊")


options = ["Get face", "Training", "Predict"]

selected_chapter = st.sidebar.radio("Select an option", options)

if selected_chapter == "Get face":
    gf.main()
elif selected_chapter == "Training":
    tn.main()
elif selected_chapter == "Predict":
    pr.main()