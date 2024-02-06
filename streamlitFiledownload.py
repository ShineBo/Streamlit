import os
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
import cv2

import streamlit as st
from PIL import Image
import cv2 
import numpy as np


st.title("Image Download App")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    convert_btn=st.button("Convert Color to Gray")
    status=st.radio("Select Option:",('No Convert','Color to Gray','Color to HSV'),index=0)
    bytes_data = uploaded_file.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    if status =='Color to Gray':
        #image.save("image/img.jpg",format="jpeg")
        #cv2_img = cv2.imread("image/img.jpg")

        cv_img_gray=cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY)
        st.image(cv_img_gray)

        cv2.imwrite("image/edited.jpg",cv_img_gray)
    if status =='Color to HSV':
        #image.save("image/img.jpg",format="jpeg")
        #cv2_img = cv2.imread("image/img.jpg")
        
        cv_img_hsv=cv2.cvtColor(cv2_img,cv2.COLOR_BGR2HSV)
        st.image(cv_img_hsv)

        cv2.imwrite("image/edited.jpg",cv_img_hsv)
    if status =="No Convert":
        cv2.imwrite("image/edited.jpg",cv2_img)
        
        # Download Button
    with open("image/edited.jpg", "rb") as file:
        btn = st.download_button(
                  label="Download image",
                  data=file,
                  file_name="download.png",
                  mime="image/png"
    )