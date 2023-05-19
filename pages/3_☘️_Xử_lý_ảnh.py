import streamlit as st
import numpy as np
import ImageProcessing.Chapter3 as c3
import ImageProcessing.Chapter4 as c4
import ImageProcessing.Chapter5 as c5
import ImageProcessing.Chapter9 as c9
import cv2
import object_detection as od
from PIL import Image

st.set_page_config(page_title="Xử lý ảnh", page_icon="📷")

st.title("XỬ LÝ ẢNH")
st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://www.wallpapertip.com/wmimgs/24-249670_high-resolution-wooden-background-hd.jpg");
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
        background-size: 105%;
        # background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

image_file = st.sidebar.file_uploader("Upload Your Image", type=[
                                  'jpg', 'png', 'jpeg', 'tif'])


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
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Negative(imgin)
        elif selected == "Logarit":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Logarit(imgin)
        elif selected == "Power":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Power(imgin)
        elif selected == "PiecewiseLinear":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.PiecewiseLinear(imgin)
        elif selected == "Histogram":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Histogram(imgin)
        elif selected == "HistogramEqualization":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.HistEqual(imgin)
        elif selected == "HistogramEqualizationColor":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            processed_image = c3.HistEqualColor(imgin)
        elif selected == "LocalHistogram":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.LocalHist(imgin)
        elif selected == "HistogramStatistics":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.HistStat(imgin)
        elif selected == "BoxFilter":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.BoxFilter(imgin)
        elif selected == "GaussFilter":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.GaussFilter(imgin)
        elif selected == "Threshold":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Threshold(imgin)
        elif selected == "MedianFilter":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.MedianFilter(imgin)
        elif selected == "Sharpen":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Sharpen(imgin)
        elif selected == "Gradient":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c3.Gradient(imgin)           
    elif selected_chapter == "Chapter 4":
        selected = st.sidebar.radio("Options", ["Spectrum", "FrequencyFilter", "DrawFilter", "RemoveMoire"])
        if selected == "Spectrum":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c4.Spectrum(imgin)
        elif selected == "FrequencyFilter":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c4.FrequencyFilter(imgin)
        elif selected == "DrawFilter":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            hex_color = '#0E1117'
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
            imgin = Image.new('RGB', (1, 1),  rgb_color)
            processed_image = c4.DrawNotchRejectFilter()
        elif selected == "RemoveMoire":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c4.RemoveMoire(imgin)

    elif selected_chapter == "Chapter 5":
        selected = st.sidebar.radio("Options", ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"])
        if selected == "CreateMotionNoise":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c5.CreateMotionNoise(imgin)
        elif selected == "DenoiseMotion":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c5.DenoiseMotion(imgin)
        elif selected == "DenoisestMotion":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            temp = cv2.medianBlur(imgin, 7)
            processed_image = c5.DenoiseMotion(temp)        
    elif selected_chapter == "Chapter 9":
        selected = st.sidebar.radio("Options", ["ConnectedComponent", "CountRice"])
        if selected == "ConnectedComponent":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c9.ConnectedComponent(imgin)    
        elif selected == "CountRice":
            st.markdown("<p style='color: #DFEFFF; font-size: 22px;'> <strong>→ Negative: Hàm làm ám ảnh. Kết quả: trắng thành đen, đen thành trắng.</strong></p>", unsafe_allow_html=True)
            processed_image = c9.CountRice(imgin)
    

    # st.subheader("Ảnh trước khi được xử lý")
    # st.image(imgin, width = 350)

    # st.subheader("Ảnh sau khi được xử lý")
    # st.image(processed_image, width = 350)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p style='color: #803619; font-size: 28px;'> <strong>Ảnh trước khi được xử lý</strong></p>", unsafe_allow_html=True)
        st.image(imgin, width=350)

    with col2:
        st.markdown("<p style='color: #803619; font-size: 28px;'> <strong>Ảnh sau khi được xử lý</strong></p>", unsafe_allow_html=True)
        st.image(processed_image, width=350)