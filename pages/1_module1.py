#core pkgs
import streamlit as st 
import os, getpass
#additional pkgs
import pandas as pd 
from PIL import Image

###########
user = getpass.getuser()
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Workd with texts', 'Work with data', 'Work with widgets', 'Work with Media Files', 'Get inputs from user'])
df1 = pd.read_csv(f'C:/Users/{user}/Downloads/LearnStreamlit/Module01/iris.csv')


def main():
    with tab1:
        st.title("Module 1: Displaying Text data") # title
        st.text('Hello World') # text
        st.markdown('### This is a Markdown') # markdown
        
        ##header 
        st.header('This is a header')
        st.subheader('This is a subheader')
        
        st.divider() # horizontal line
        
        #displaying colorful text like booststrap/text Alert 
        st.success('successful') # green
        st.info('Info') # blue
        st.warning('Warning') # yellow
        st.error('Error') # red
        st.exception('Exception') # red
        
        st.divider() # horizontal line
        
        # Superfunctions 
        st.write('## This is a write function')
        st.write(range(10))
        st.write(list(range(10)))
        st.write(pd.DataFrame({
            'column1': range(10),
            'column2': range(10)
        }))
        st.write({'key': 'value'})
        st.write('sum of range(10):', sum(range(10)))
        #####
        
        st.divider() # horizontal line
        
        st.write(dir(st)) # list of all functions in streamlit
        #st.write(help(st)) # documentation of streamlit
    
    
    with tab2:
        # Displaying data
        st.title('Displaying data')
        st.write('#### _a simple dataframe example 1_')
        ####
        st.dataframe(df1.style.highlight_max(axis=0)) ## example 1 
        st.divider()
        st.write('#### _a simple dataframe example 2_')
        st.write(df1) ## example 2
        st.divider()
        st.write('#### _a simple dataframe example 3_')
        st.write('##### _using st.table static df_')
        if st.checkbox('Show dataframe', key='1'):
            st.table(df1) ## static table
        else:
            st.write('Dataframe is hidden')
        ####
        st.divider()
        ## Using superfunctions st.write to display data
        st.write('#### _a simple dataframe example 4_')
        st.write(df1.head())
        if st.checkbox('Show dataframe', key='2'):
            st.write(df1.to_json())
        else:
            st.write('Json is hidden')
        ####
        st.divider()
        mycode = '''
        def myfunc():
            return 'Hello World'
        '''
        st.code(mycode, language='python')

    with tab3:
        st.title('Workging with widgets')
        # buttons/checkboxes/radio/selectbox
        
        st.text('we gonna work with widgets, like buttons, checkboxes, radio, selectbox')
            
        st.write('#### _a simple button example_')
        text = 'text activated by clicking the button'
        if st.button('Submit'):
            st.write(text)
        
        st.write('#### _radio button example_')
        radio = st.radio('Select a number', [1, 2, 3, 4, 5])
        if st.button('Show selected number', key='show_numeric'):
            st.write(radio)
            if radio == 1:
                st.write('You selected 1')
        status = st.radio('Select a status', ['active', 'inactive'])
        if status == 'active':
            st.success('Active')
        elif status == 'inactive':
            st.warning('Inactive')
            
        st.write('#### _checkbox example_')
        if st.checkbox('Show/Hide'):
            st.write('Checkbox is activated')
        else:
            st.write('Checkbox is desactivated')
            
        st.write('#### expander')
        
    with st.expander(label='Features', expanded=False, icon='🔥'):
        st.write('This is a expander content')
        
    ## selectbox
    st.write('#### _selectbox example_')
    games = ['WOW', 'The joy of programing', 'POE', 'Valorant', 'Runescape 3']
    selected_game = st.selectbox('Select a game', games, placeholder='Select a game')
    spoken_lang = ['English', 'French', 'Spanish', 'German', 'Italian']
    selected_lang = st.multiselect('What languages do you speak?', spoken_lang, default=None)
    
    
    ## slider
    #int / float / date
    age = st.slider('Select your age', min_value=0, max_value=100, value=23, step=1)

    # Any Datatype select slider
    st.write('#### _slider example_')
    color = st.select_slider('select a color', options=['red', 'green', 'blue', 'yellow', 'black', 'white'])
        
    with tab4:
        st.title('Work with Media Files')
        image = Image.open('D:/projects/streamlit_learning/data/image_02.jpg')
        st.image(image, caption='Car running', use_container_width=True) # use_column_width=True to fit the image in the column width
        st.write('#### _image example_')                        # caption to add a title to the image

        st.write('#### _streamlit can display images from the web to_')
        url = "https://images.hdqwalls.com/wallpapers/solo-leveling-vx.jpg"
        st.image(url, caption='Solo Leveling', use_container_width=True)
        
        # displaying video
        st.write('#### _video example_')
        video_file = open('D:/projects/streamlit_learning/data/secret_of_success.mp4', 'rb').read()
        st.video(video_file, start_time=0, format='video/mp4')
        
        # displaying audio
        st.write('#### _audio example_')
        audio_file = open('D:/projects/streamlit_learning/data/song.mp3', mode='rb').read()
        st.audio(audio_file, format='audio/mp3')
            
    with tab5:
        st.title('Get inputs from user')
        ipt_name = st.text_input('Enter your name', placeholder='Type here...', max_chars=10)
        ipt_pass = st.text_input('Enter a password', type='password')
        ##
        st.write(f'#### --> this is your name: {ipt_name}')
        st.write(f'#### --> this is your password: {ipt_pass}')
        ##
        ipt_msg = st.text_area(label='Enter your message', placeholder='Type here...', height=100)
        ##
        st.write(f'#### --> this is your message: {ipt_msg}')
        ##
        ipt_date = st.date_input('Enter a date') ## input a date 
        ipt_number = st.number_input('Enter a number', min_value=0, max_value=100, value=0, step=1) ## input a number, can be change to float
        ipt_time = st.time_input('Enter a time') ## input a time 
        ##
        st.color_picker('pick a color')
            
if __name__ == '__main__':
    main()  