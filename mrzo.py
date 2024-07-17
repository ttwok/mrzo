import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

st.title('종목 차트 검색')

with st.sidebar:
    date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2022, 1, 1)
    )

    code = st.text_input(
        '종목코드(ex : aapl)', 
        value='',
        placeholder='종목코드를 입력해 주세요'
    )

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']

    tab1, tab2 = st.tabs(['차트', '데이터'])

    with tab1:    
        st.line_chart(data)

    with tab2:
        st.dataframe(df.sort_index(ascending=False))

    with st.expander('컬럼 설명'):
        st.markdown('''
        - Open: 시가
        - High: 고가
        - Low: 저가
        - Close: 종가
        - Adj Close: 수정 종가
        - Volumn: 거래량
        ''')


# 특정 경로에 있는 이미지 파일 읽기
image_path_n = 'normal.png'  # 지정된 이미지 파일 경로
image_n = Image.open(image_path_n)

# 특정 경로에 있는 이미지 파일 읽기
image_path_z = 'zoker.png'  # 지정된 이미지 파일 경로
image_z = Image.open(image_path_z)

# 특정 경로에 있는 이미지 파일 읽기
image_path = 'up.jpg'  # 지정된 이미지 파일 경로
image = Image.open(image_path)


# 라디오 선택 버튼
mbti = st.radio(
    'zoker의 상태는 어떤가요?',
    ('기본', '흑화', 'yellow'),
    index=2)

if mbti == '기본':
    st.write(':blue[give me mandoo]')
    st.image(image_n, caption='Uploaded Image.', use_column_width=True)
elif mbti == '흑화':
    st.write(' :green[short all in]')
    st.image(image_z, caption='Uploaded Image.', use_column_width=True)
else:
    st.write(":red[hellow mr zo]:grey_exclamation:")


st.title('hellow mr zo')


# 특정 경로에 있는 이미지 파일 읽기
image_path_n = 'normal.png'  # 지정된 이미지 파일 경로
image_n = Image.open(image_path_n)

# 특정 경로에 있는 이미지 파일 읽기
image_path_z = 'zoker.png'  # 지정된 이미지 파일 경로
image_z = Image.open(image_path_z)

# 특정 경로에 있는 이미지 파일 읽기
image_path = 'up.jpg'  # 지정된 이미지 파일 경로
image = Image.open(image_path)

st.image(image, caption='Uploaded Image.', use_column_width=True)

