# import cv2
# import streamlit as st
# import numpy as np
# from PIL import Image


# def brighten_image(image, amount):
#     img_bright = cv2.convertScaleAbs(image, beta=amount)
#     return img_bright


# def blur_image(image, amount):
#     blur_img = cv2.GaussianBlur(image, (11, 11), amount)
#     return blur_img


# def enhance_details(img):
#     hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
#     return hdr


# def main_loop():
#     st.title("OpenCV Demo App")
#     st.subheader("This app allows you to play with Image filters!")
#     st.text("We use OpenCV and Streamlit for this demo")

#     blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
#     brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
#     apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')

#     image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
#     if not image_file:
#         return None

#     original_image = Image.open(image_file)
#     original_image = np.array(original_image)

#     processed_image = blur_image(original_image, blur_rate)
#     processed_image = brighten_image(processed_image, brightness_amount)

#     if apply_enhancement_filter:
#         processed_image = enhance_details(processed_image)

#     st.text("Original Image vs Processed Image")
#     st.image([original_image, processed_image])


# if __name__ == '__main__':
#     main_loop()


# #%%
import Chapter3 as c3
import Chapter4 as c3
import Chapter9 as c9
import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image


def main_loop():
    st.title("OpenCV Demo App")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")
    
    st.sidebar.radio("Test", ["Home", "Company"])
    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')
    detect_faces_option = st.sidebar.checkbox('Detect Faces')

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)

    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    if detect_faces_option:
        processed_image = detect_faces(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image])


if __name__ == '__main__':
    main_loop()
