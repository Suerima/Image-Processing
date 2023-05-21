import streamlit as st
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb
import Custome.custome as ct


ct.ChangeTheme("PHÁT HIỆN KHUÔN MẶT","😁")


options = ["Facebook", "Haarcascade"]
selected_chapter = st.sidebar.selectbox("Select an option", options)

if selected_chapter == "Facebook":
    fb.main_loop()
elif selected_chapter == "Haarcascade":
    ha.main_loop()

