import streamlit as st
import time
import numpy as np
import ImageProcessing.Chapter3 as c3
import ImageProcessing.Chapter4 as c4
import ImageProcessing.Chapter5 as c5
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
                                                "HistogramEqualizationColor", "LocalHistogram", "HistogramStatistics", 
                                                "BoxFilter", "GaussFilter","Threshold", "MedianFilter", "Sharpen", "Gradient"])
            
        if selected == "Negative":
            processed_image = c3.Negative(imgin)
        elif selected == "Logarit":
            processed_image = c3.Logarit(imgin)
        elif selected == "Power":
            processed_image = c3.Power(imgin)
        elif selected == "PiecewiseLinear":
            processed_image = c3.PiecewiseLinear(imgin)
        elif selected == "Histogram":
            processed_image = c3.Histogram(imgin)
        elif selected == "HistogramEqualization":
            processed_image = c3.HistEqual(imgin)
        elif selected == "HistogramEqualizationColor":
            imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            processed_image = c3.HistEqualColor(imgin)
        elif selected == "LocalHistogram":
            processed_image = c3.LocalHist(imgin)
        elif selected == "HistogramStatistics":
            processed_image = c3.HistStat(imgin)
        elif selected == "BoxFilter":
            processed_image = c3.BoxFilter(imgin)
        elif selected == "GaussFilter":
            processed_image = c3.GaussFilter(imgin)
        elif selected == "Threshold":
            processed_image = c3.Threshold(imgin)
        elif selected == "MedianFilter":
            processed_image = c3.MedianFilter(imgin)
        elif selected == "Sharpen":
            processed_image = c3.Sharpen(imgin)
        elif selected == "Gradient":
            processed_image = c3.Gradient(imgin)           
    elif selected_chapter == "Chapter 4":
        selected = st.sidebar.radio("Options", ["Spectrum", "FrequencyFilter", "DrawFilter", "RemoveMoire"])
        if selected == "Spectrum":
            processed_image = c4.Spectrum(imgin)
        elif selected == "FrequencyFilter":
            processed_image = c4.FrequencyFilter(imgin)
        elif selected == "DrawFilter":
            imgin = Image.new('RGB', (5, 5),  st.get_option("theme.backgroundColor"))
            processed_image = c4.DrawNotchRejectFilter()
        elif selected == "RemoveMoire":
            processed_image = c4.RemoveMoire(imgin)

    elif selected_chapter == "Chapter 5":
        selected = st.sidebar.radio("Options", ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"])
        if selected == "CreateMotionNoise":
            processed_image = c5.CreateMotionNoise(imgin)
        elif selected == "DenoiseMotion":
            processed_image = c5.DenoiseMotion(imgin)
        elif selected == "DenoisestMotion":
            temp = cv2.medianBlur(imgin, 7)
            processed_image = c5.DenoiseMotion(temp)        
    elif selected_chapter == "Chapter 9":
        selected = st.sidebar.radio("Options", ["ConnectedComponent", "CountRice"])
        if selected == "ConnectedComponent":
            processed_image = c9.ConnectedComponent(imgin)    
        elif selected == "CountRice":
            processed_image = c9.CountRice(imgin)
    

    st.subheader("Original Image and Processed Image")
    st.image([imgin, processed_image], width = 350)
st.button("Re-run")
