import streamlit as st

st.set_page_config(page_title="Đồ án môn xử lý ảnh", page_icon="👋",)

st.title("Đồ án cuối kỳ nhóm môn Xử lý ảnh")
st.markdown("<p style='color: white; font-size: 28px;'> <strong>Giảng viên hướng dẫn: ThS. Trần Tiến Đức</strong></p>", unsafe_allow_html=True)
st.markdown("<p style='color: white; font-size: 28px;'> <strong>Thành viên nhóm:</strong></p>", unsafe_allow_html=True)
st.markdown("<p style='color: white; font-size: 28px;'> <strong>👉 20133098 - Nguyễn Văn Trường Tốt</strong></p>", unsafe_allow_html=True)
st.markdown("<p style='color: white; font-size: 28px;'> <strong>👉20133091 - Nguyễn Quốc Thắng </strong></p>", unsafe_allow_html=True)

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


st.sidebar.success("Select a demo above.")
