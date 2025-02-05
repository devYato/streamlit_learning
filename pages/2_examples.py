import os
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

def save_uploaded_file(uploaded_file):
    with open(os.path.join("C:/Windows/Temp", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())# can use read() too
        return st.success(f"Saved File:{uploaded_file.name} to C:/Windows/Temp")

if choice == 'Home':
    st.subheader('Home')
    img_file = st.file_uploader("Upload a image", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True) # when accept multiple files, the return is a list
    if img_file is not None:
        # to se details and download
        for i in img_file: # or len(img_file)
            #how to put a path to save the image using os
            if st.button('Save image', key=i.name):
                save_uploaded_file(i)
                # with open (os.path.join('C:/Windows/Temp', img_file.name), 'wb') as f:
                #     # f.write(img_file.read()) # works
                #     f.write(img_file.getbuffer()) # works too
            # st.image(open_img(img_file)) # to display with PIL lib
            st.image(i, caption=i.name, use_container_width=True)
            st.write(type(i))
            st.write(dir(i))
            st.write(i.name)
        
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
            
elif choice == 'Docs':
    st.subheader('Docs')
    st.write('Here is the documentation of your archive')
    doc = st.file_uploader('Upload a PDF, TXT or DOCX file', type=['PDF', 'TXT', 'DOCX'])
    if doc is not None:
        st.write(type(doc))
        ## i can work with the type of file, and show the contents depending on type
        details = {"type": doc.type, "name": doc.name, "size": doc.size}
        if st.button('Show details', key='details'):
            st.write(details)
        if doc.type == 'text/plain':
            st.write('text file')
            #st.write(doc.read()) ## work but in bytes 
            raw_text = str(doc.read(), 'utf-8', errors='ignore')
            st.write(raw_text)
        elif doc.type == 'application/pdf':
            st.write('pdf file')
            print(type(doc))
            print(doc)
