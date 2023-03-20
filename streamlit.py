import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import time
import cv2
from streamlit_drawable_canvas import st_canvas
from PIL import Image


model = tf.keras.models.load_model("model.h5")

st.set_page_config(page_title='MNIST klassifikatsiya',layout='wide')
header1 = "Asosiy ko'rsatkichlar"
st.markdown("<h1 style='text-align: center;font-size: 20px;'>"+header1+"</h1>", unsafe_allow_html=True)
data_main = [["optimizer","Adam"],["loss funksiyasi","Categorical Cross Entropy"],
              ["epochs","5"],["train loss qiymati","0.0287"],
             ["train accuracy qiymati","0.9921"],
             ["evaluate loss qiymati","0.03769"],
             ["evaluate accuracy qiymati","0.9899"],
             ["parametrlar soni","2 238 122"]]

information = pd.DataFrame(data_main,columns=["Parametrlar","Qiymatlar"])
st.dataframe(information,width = 1000,height=315)

header2 = "Rasmni chizing va predict qiling"
st.markdown("<h1 style='text-align: center;font-size: 20px;'>"+header2+"</h1>", unsafe_allow_html=True)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 17)
stroke_color = st.sidebar.color_picker("Stroke color hex: ", "#fff")
bg_color = st.sidebar.color_picker("Background color hex: ", "#000")
realtime_update = st.sidebar.checkbox("Update in realtime", True)

col1,col2 = st.columns([1,1])
center_container = col1.container()

with center_container:
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=None,
        update_streamlit=realtime_update,
        height=400,
        width=400,
        drawing_mode="freedraw",
        point_display_radius=0,
        key="canvas"
    )

st.write(
    f"""
    <style>
        .reportview-container .main .block-container {{
            display: flex;
            justify-content: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
if canvas_result.image_data is not None:
    pil_image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGBA2GRAY)
    image = cv2.resize(image, (28, 28))
    c1,c2,c3 = col2.columns(3)
    if c2.button("Predict qilish"):
        image = np.array(image).reshape(1,28,28,1)
        image = image.astype('float32')/255
        one_hot_encoding_label = model.predict(image)
        result = np.argmax(one_hot_encoding_label)
        pb = one_hot_encoding_label[0][result]
        
        my_bar = col2.progress(0, text="Iltimos kuting...")
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text="Qiymat aniqlanmoqda.Iltimos kuting...")
        answer = [["Natija",result],["O'xshashlik",pb]]

        information = pd.DataFrame(answer,columns=["Parametrlar","Qiymatlar"])
        col2.dataframe(information,width=600,height=100)
            
