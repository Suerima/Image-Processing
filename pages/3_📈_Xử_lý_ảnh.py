import streamlit as st
import time
import numpy as np
import ImageProcessing.Chapter3 as c3
import ImageProcessing.Chapter4 as c4
import ImageProcessing.Chapter9 as c9
import cv2
import object_detection as od
from PIL import Image

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="📈")

st.markdown("# Xử lý ảnh")
st.write()

image_file = st.sidebar.file_uploader("Upload Your Image", type=[
                                  'jpg', 'png', 'jpeg', 'tif'])
global imgin
if image_file is not None:
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE) 

    options = ["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"]
    selected_chapter = st.sidebar.selectbox("Select an option", options)


    if selected_chapter == "Chapter 3":
        selected = st.sidebar.radio("Options", ["Negative", "Logarit", "Power", "PiecewiseLinear", "Histogram", "HistogramEqualization",
                                                    "LocalHistogram", "HistogramStatistics", "MySmoothing", "Smoothing", "SmoothingGauss",
                                                    "MedianFilter", "MySharpen", "Sharpen", "UnSharpMasking", "MyGradient", "Gradient"])
            

        if selected == "Negative":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Negative(imgin, imgout)
        elif selected == "Logarit":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Logarit(imgin, imgout)
        elif selected == "Power":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Power(imgin, imgout)
        elif selected == "PiecewiseLinear":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.PiecewiseLinear(imgin, imgout)
        elif selected == "Histogram":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Histogram(imgin, imgout)
        elif selected == "HistogramEqualization":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.HistogramEqualization(imgin, imgout)
        elif selected == "LocalHistogram":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.LocalHistogram(imgin, imgout)
        elif selected == "HistogramStatistics":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.HistogramStatistics(imgin, imgout)
        elif selected == "MySmoothing":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.MySmoothing(imgin, imgout)
        elif selected == "Smoothing":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Smoothing(imgin)
        elif selected == "SmoothingGauss":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.SmoothingGauss(imgin)
        elif selected == "MedianFilter":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.MedianFilter(imgin, imgout)
        elif selected == "MySharpen":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.MySharpen(imgin, imgout)
        elif selected == "Sharpen":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Sharpen(imgin)
        elif selected == "UnSharpMasking":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.UnSharpMasking(imgin)
        elif selected == "MyGradient":
            imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.MyGradient(imgin, imgout)
        elif selected == "Gradient":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c3.Gradient(imgin)
            
    elif selected_chapter == "Chapter 4":
        selected = st.sidebar.radio("Options", ["Spectrum", "FrequencyFilter", "DrawFilter", "RemoveMoire"])
            
        if selected == "Spectrum":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c4.Spectrum(imgin)
        elif selected == "FrequencyFilter":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c4.FrequencyFilter(imgin)
        elif selected == "DrawFilter":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c4.DrawFilter(imgin)
        elif selected == "RemoveMoire":
            # imgout = np.zeros(imgin.shape, np.uint8)
            processed_image = c4.RemoveMoire(imgin)
    # elif selected_chapter == "Chapter 5":
    #     selected = st.sidebar.radio("Options", ["CreateMotionfilter", "CreateMotionNoise", "CreateInverseMotionfilter", "DenoiseMotion"])
    #     if selected == "Spectrum":
    #         # imgout = np.zeros(imgin.shape, np.uint8)
    #         processed_image = c5.Spectrum(imgin)
    #     elif selected == "FrequencyFilter":
    #         # imgout = np.zeros(imgin.shape, np.uint8)
    #         processed_image = c5.FrequencyFilter(imgin)
    #     elif selected == "DrawFilter":
    #         # imgout = np.zeros(imgin.shape, np.uint8)
    #         processed_image = c5.DrawFilter(imgin)
    #     elif selected == "RemoveMoire":
    #         # imgout = np.zeros(imgin.shape, np.uint8)
    #         processed_image = c5.RemoveMoire(imgin)
    elif selected_chapter == "Chapter 9":
        selected = st.sidebar.radio("Options", ["ConnectedComponent", "CountRice"])
        if selected == "ConnectedComponent":
            processed_image = c9.ConnectedComponent(imgin)    
        elif selected == "CountRice":
            processed_image = c9.CountRice(imgin)
    

    st.subheader("Original Image and Processed Image")
    st.image([imgin, processed_image], width = 350)
st.button("Re-run")
