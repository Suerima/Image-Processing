import streamlit as st
import numpy as np
import cv2
import object_detection as od
from PIL import Image

import Custome.custome as cs
import ImageProcessing.Chapter3 as c3
import ImageProcessing.Chapter4 as c4
import ImageProcessing.Chapter5 as c5
import ImageProcessing.Chapter9 as c9

cs.ChangeTheme("XỬ LÝ ẢNH","📷")

image_file = st.sidebar.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg', 'tif'])

if image_file is not None:
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    options = {
        "Chapter 3": [
            "Negative", "Logarit", "Power", "PiecewiseLinear", "Histogram",
            "HistogramEqualization", "HistogramEqualizationColor", "LocalHistogram",
            "HistogramStatistics", "BoxFilter", "GaussFilter", "Threshold",
            "MedianFilter", "Sharpen", "Gradient"
        ],
        "Chapter 4": [
            "Spectrum", "FrequencyFilter", "DrawNotchRejectFilter", "RemoveMoire"
        ],
        "Chapter 5": [
            "CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"
        ],
        "Chapter 9": [
            "ConnectedComponent", "CountRice"
        ]
    }

    selected_chapter = st.sidebar.selectbox("Select an option", options.keys())

    selected_option = st.sidebar.radio("Options", options[selected_chapter])

    if selected_chapter == "Chapter 3":
        st.markdown("<p style='color: #CBDEED; font-size: 25px;'> <strong>🔘{}</strong></p>".format(selected_option), unsafe_allow_html=True)
        if selected_option == "HistogramEqualizationColor":
            imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        processed_image = getattr(c3, selected_option)(imgin)

    elif selected_chapter == "Chapter 4":
        st.markdown("<p style='color: #CBDEED; font-size: 25px;'> <strong>{}</strong></p>".format(selected_option), unsafe_allow_html=True)
        if selected_option == "DrawNotchRejectFilter":
            hex_color = '#0E1117'
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
            imgin = Image.new('RGB', (1, 1),  rgb_color)
        processed_image = getattr(c4, selected_option)(imgin)

    elif selected_chapter == "Chapter 5":
        st.markdown("<p style='color: #CBDEED; font-size: 25px;'> <strong>{}</strong></p>".format(selected_option), unsafe_allow_html=True)
        if selected_option == "DenoisestMotion":
            temp = cv2.medianBlur(imgin, 7)
            processed_image = getattr(c5, "DenoiseMotion")(temp)
        else:
            processed_image = getattr(c5, selected_option)(imgin)

    elif selected_chapter == "Chapter 9":
        st.markdown("<p style='color: #CBDEED; font-size: 25px;'> <strong>{}</strong></p>".format(selected_option), unsafe_allow_html=True)
        processed_image = getattr(c9, selected_option)(imgin)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p style='color: #BA4F24; font-size: 28px;'> <strong>Ảnh trước khi được xử lý</strong></p>", unsafe_allow_html=True)
        st.image(imgin, width=350)

    with col2:
        st.markdown("<p style='color: #BA4F24; font-size: 28px;'> <strong>Ảnh sau khi được xử lý</strong></p>", unsafe_allow_html=True)
        st.image(processed_image, width=350)
