import pandas as pd
import streamlit as st
import numpy as np

st.title("Uber Pickups in New York City")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data(show_spinner="Loading the data... 🔥") # cache data is better for large data, dfs, tables, json, all data in general
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(nrows=20000)
data_load_state.text('Done! (using st.cache_data)')


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.divider()

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.divider()

st.subheader('Map of all pickups')
st.map(data)

st.divider()

st.subheader('Pickups by Hours') # 5 PM
# 5 PM dt can be used to get the date and time of the data in a column type datetime, and dt.hour can be used to get the hour of the data in a column type datetime
hour = st.slider('Hour to look at', 0, 23, 17, step=1) # 5 PM by defult but can change with slider
filtered_data = data[data[DATE_COLUMN].dt.hour == hour] 
st.map(filtered_data)

