import streamlit as st
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="😁")

st.title("PHÁT HIỆN KHUÔN MẶT")

st.sidebar.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("https://img.freepik.com/premium-photo/top-view-photo-piggy-bank-calculator-center-plane-car-models-camera-map-magnifier-compass-notebook-passport-cover-plant-isolated-wooden-table-background_352249-4634.jpg?w=2000");
        background-size: 90%;
        # background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://wallpaperaccess.com/full/962592.jpg");
        background-size: 105%;
        background-position: right;
        background-repeat: no-repeat;
        background-attachment: local;
    }}    
    </style>
    """,
    unsafe_allow_html=True
)


options = ["Facebook", "Haarcascade"]
selected_chapter = st.sidebar.selectbox("Select an option", options)

if selected_chapter == "Facebook":
    fb.main_loop()
elif selected_chapter == "Haarcascade":
    ha.main_loop()


st.button("Re-run")
