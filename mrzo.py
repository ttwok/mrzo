import streamlit as st
import base64

# 비디오 파일을 읽기


st.write('**:red[hey,] mr zo where?**')
st.map()
'''
---
'''
with st.expander('hellow CH.1'):
    st.image('zoker.png',width=200)

with st.sidebar:
    st.write('''---''')
    st.title('hellow mr zo')
    st.write('''---''')
    x = st.selectbox('what are you doing mr zo', ['','sad','stop','heaven'])
    if x == 'sad':
        st.image('pic/sad.jpg')
    elif x == 'stop':
        st.image('pic/stop.jpg')
    elif x == 'heaven':
        st.image('pic/heaven.jpg')
    y = st.selectbox('where are you going mr zo', ['','water','boom','teach'])
    if y == 'water':
        st.image('pic/water.jpg')
    elif y == 'boom':
        st.image('pic/boom.jpg')
    elif y == 'teach':
        st.image('pic/teach.jpg')

with st.expander('hellow CH.2'):
    tab1, tab2, tab3,tab4 = st.tabs(['RUN', 'zo movie','zo picture','b meal'])
    with tab1:
        st.title('I GAP NI DA')
        st.image('pic/run.jpg')
    with tab2:
        ':sunglasses:'
        col1, cols2 = st.columns(2)
        with col1:
            with open('media/talking.mp4','rb') as f:
                video_data_0 = f.read()
            st.header('sing')
            st.video(video_data_0)
        with cols2:
            with open('media/surprise.mp4','rb') as f:
                video_data_1 = f.read()
            st.header('hellow')
            st.video(video_data_1)
        cols3, cols4 = st.columns(2)
        with cols3:
            with open('media/dadara.mp4', 'rb') as f:
                video_data_2 = f.read()
            st.header('zo tank')
            st.video(video_data_2)
        with cols4:
            with open('media/golf.mp4', 'rb') as f:
                video_data_3 = f.read()
            st.header('zolf')
            st.video(video_data_3)            
    with tab3:
        t3_col1,t3_col2,t3_col3 = st.columns([1.5,2,2.65])
        t3_col1.image('pic/1.jpg')
        t3_col2.image('pic/2.jpg')
        t3_col3.image('pic/3.jpg')
        t3_col4,t3_col5,t3_col6 = st.columns([1,1,1.31])
        t3_col4.image('pic/4.jpg')
        t3_col5.image('pic/5.jpg')
        t3_col6.image('pic/6.jpg')
        t3_col7,t3_col8,t3_col9 = st.columns([0.9,1,2.1])
        t3_col7.image('pic/7.jpg')
        t3_col8.image('pic/8.jpg')
        t3_col9.image('pic/9.jpg')
        t3_col10,t3_col11,t3_col12 = st.columns([1,0.54,1])
        t3_col10.image('pic/10.jpg')
        t3_col11.image('pic/11.jpg')
        t3_col12.image('pic/12.jpg')     
        t3_col13,t3_col14,t3_col15 = st.columns([1.2,1,1.25])
        t3_col13.image('pic/13.jpg')
        t3_col14.image('pic/14.jpg')
        t3_col15.image('pic/15.jpg')                  
    with tab4:
        st.write('my gun')
        st.image('pic/b_meal.jpg')
