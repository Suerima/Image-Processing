import streamlit as st
import numpy as np
import cv2 as cv
import joblib

st.set_page_config(page_title="Nhận diện khuôn mặt", page_icon="😊")

st.title("NHẬN DIỆN KHUÔN MẶT")
st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://img.freepik.com/premium-photo/travel-concept-headphones-camera-sketchbook-purse-pencil-keys-wooden-background-flat-lay-top-view-photo-with-copyspace-center_77211-1445.jpg?w=2000");
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}    
    </style>
    """,
    unsafe_allow_html=True
)

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


FRAME_WINDOW = st.image([])
cap = cv.VideoCapture(0)



svc = joblib.load('./FaceRecognition/svc.pkl')
mydict = ['BanThang', 'BanTot', 'ThayDuc']

def visualize(input, faces, fps, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            #print('Face {}, top-left coordinates: ({:.0f}, {:.0f}), box width: {:.0f}, box height {:.0f}, score: {:.2f}'.format(idx, face[0], face[1], face[2], face[3], face[-1]))

            coords = face[:-1].astype(np.int32)
            cv.rectangle(input, (coords[0], coords[1]), (coords[0]+coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)
    cv.putText(input, 'FPS: {:.2f}'.format(fps), (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


if __name__ == '__main__':
    detector = cv.FaceDetectorYN.create(
        './FaceRecognition/face_detection_yunet_2022mar.onnx',
        "",
        (320, 320),
        0.9,
        0.3,
        5000)
    
    recognizer = cv.FaceRecognizerSF.create(
    './FaceRecognition/face_recognition_sface_2021dec.onnx',"")

    tm = cv.TickMeter()

    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize([frameWidth, frameHeight])

    dem = 0
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        # Inference
        tm.start()
        faces = detector.detect(frame) # faces is a tuple
        tm.stop()
        
        if faces[1] is not None:
            face_align = recognizer.alignCrop(frame, faces[1][0])
            face_feature = recognizer.feature(face_align)
            test_predict = svc.predict(face_feature)
            result = mydict[test_predict[0]]
            cv.putText(frame,result,(1,50),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw results on the input image
        visualize(frame, faces, tm.getFPS())

        # Visualize results
        FRAME_WINDOW.image(frame, channels='BGR')
    cv.destroyAllWindows()
