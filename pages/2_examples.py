import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
from PIL import Image
##

## uploading a image
menu = ['Home', 'Dataset', 'Docs', 'About']
choice = st.sidebar.selectbox('Menu', menu)

def open_img(img_path : str):
    img = Image.open(img_path)
    return img

if choice == 'Home':
    st.subheader('Home')
    img_file = st.file_uploader("Upload a image", type=['jpg', 'png', 'jpeg'])
    if img_file is not None:
        st.image(img_file, caption='Uploaded image', use_container_width=True)
        # to se details
        st.write(type(img_file))
        st.write(dir(img_file))
        st.write(img_file.name)
        st.image(open_img(img_file)) # to display with PIL lib
elif choice == 'Dataset':
    st.subheader('Dataset')
    data_file = st.file_uploader('Upload a CSV file', type=['CSV'])
    if data_file is not None:
        st.write(type(data_file))
        if st.checkbox('Open dir'):
            st.write(dir(data_file))
        df = pd.read_csv(data_file)
        if st.checkbox('View Data'):
            st.dataframe(df)

    