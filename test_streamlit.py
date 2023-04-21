import Chapter3 as c3
import Chapter4 as c4
import Chapter9 as c9
import cv2
import streamlit as st
import numpy as np
from PIL import Image


def negative_image(image, imgout):
    img_negative = c3.Negative(image, imgout)
    return img_negative


# def brighten_image(image, amount):
#     img_bright = cv2.convertScaleAbs(image, beta=amount)
#     return img_bright


# def blur_image(image, amount):
#     blur_img = cv2.GaussianBlur(image, (11, 11), amount)
#     return blur_img


# def enhance_details(img):
#     hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
#     return hdr


# def detect_faces(image):
#     face_cascade = cv2.CascadeClassifier(
#         cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     return image

st.title("Đồ án cuối kì Xử lý ảnh")
st.subheader("Choose an your image")
# st.text("We use OpenCV and Streamlit for this demo")

def main_loop():

 
    # blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    # brightness_amount = st.sidebar.slider(
    #     "Brightness", min_value=-50, max_value=50, value=0)
    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg', 'tif'])
    if not image_file:
        return None
    
    # imgin = cv2.imread(fl,cv2.IMREAD_GRAYSCALE)

    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    # imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # st.image(imgin, caption="", use_column_width=True)
    
    # original_image = np.array(imgin)

    
    options = ["Chapter 3", "Chapter 4", "Chapter 9"]
    selected_chapter = st.sidebar.selectbox("Select an option", options)

    if selected_chapter == "Chapter 3":
        selected = st.sidebar.radio("Options", ["Negative", "Logarit"])
        if selected == "Negative":
                imgout = np.zeros(imgin.shape, np.uint8)
                processed_image = negative_image(imgin, imgout)

                # processed_image = brighten_image(processed_image, brightness_amount)
        else:
                # processed_image = blur_image(original_image, blur_rate)
                return None
    elif selected_chapter == "Chapter 4":
         return None
    else:
         return None
    # apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')
    # detect_faces_option = st.sidebar.checkbox('Detect Faces')

    # if apply_enhancement_filter:
    #     processed_image = enhance_details(processed_image)

    # if detect_faces_option:
    #     processed_image = detect_faces(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([imgin, processed_image])
    # st.image(imgin, caption="", use_column_width=True)


if __name__ == '__main__':
    main_loop()
