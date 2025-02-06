import os
import streamlit as st
import pandas as pd
from PIL import Image
import logging, base64, time
##

timestr = time.strftime("%Y%m%d-%H%M%S")
## download file with function method
def text_download():
    b64 = base64.b64encode(texto.encode()).decode()
    new_filename = f"new_text_file_{timestr}.txt"
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Download file</a>'

    st.markdown(href, unsafe_allow_html=True)
    
def csv_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    new_filename = f"new_csv_file_{timestr}.csv"
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Download file</a>'

    st.markdown(href, unsafe_allow_html=True)


## download with Classe method
class FileDownloader(object):
    def __init__(self, file, filename, file_type):
        self.file = file
        self.file_name = filename
        self.file_type = file_type
        
    def encode(self):
        if isinstance(self.file, pd.DataFrame):
            return self.file.to_csv(index=False).encode()
        elif isinstance(self.file, str):
            return self.file.encode()
        else:
            raise ValueError("Unsupported file type")

    def download(self):
        b64 = base64.b64encode(self.encode()).decode()
        new_filename = f"{self.file_name}{timestr}.{self.file_type}"
        href = f'<a href="data:file/{self.file_type};base64,{b64}" download="{new_filename}">Download file</a>'
        st.markdown(href, unsafe_allow_html=True)
    
##logging
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs_dir = os.path.join(BASE_DIR, 'logs')
os.makedirs(logs_dir, exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
    handlers=[
        logging.FileHandler(os.path.join(logs_dir, 'app.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
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
    logging.info('Home')
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
    logging.info('Dataset')
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
    logging.info('Docs')
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

else:
    tab1, tab2, tab3 = st.tabs(['download text file',
                                'download csv file',
                                'download xx file'])
    with tab1:
        st.image('https://www.streamlit.io/images/brand/streamlit-mark-color.png', width=100)
        logging.info('About')
        st.subheader('About')
        st.write('This is a Streamlit app for uploading files')
        st.write('Built with Streamlit and Python')
        st.write('By: Renann santos')
        st.write('Date: 2025-02-05')
    
        ## adding a file download option
        # def update_file(text: str):
        #     with open('C:/Windows/Temp/file.txt', 'w') as f:
        #         f.write(str(text))
        texto = st.text_area('Enter some text', placeholder='Type something')
        st.markdown('#### Download file')
        if st.button('Download file'):
            '''
            update_file(texto)
            texto = texto.encode('utf-8')
            b64 = base64.b64encode(texto).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="file.txt">Download file</a>'
            st.markdown(href, unsafe_allow_html=True)
            '''
            #text_download() - function method
            download_text = FileDownloader(texto, 'new_text_file', 'txt').download()
    with tab2:
        st.title('download a csv file')
        df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
        if st.checkbox('Show dataframe'):
            st.dataframe(df)
        if st.button('Download CSV file'):
            #download_csv = FileDownloader(df, 'new_csv_file', 'csv')
            #download_csv.download()
            download_csv = FileDownloader(df, 'new_csv_file', 'csv').download()
