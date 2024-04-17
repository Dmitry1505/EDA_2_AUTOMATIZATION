# import numpy as np
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport

# Web App Title
st.markdown('''
# **Сервис для создания автоматических отчетов на основе разведочного анализа данных**

Добавьте файл в форматах xlsx,xls или csv и отчет будет сгенерирован автоматически

**Рекомендовано** исследование не более пяти параметров

---
''')

# Upload Excel data
with st.sidebar.header('**Добавить файлы**'):
    uploaded_file_xls = st.sidebar.file_uploader("***Добавить файл в формате xlsx,xls***", type=["xlsx", "xls"])
    uploaded_file_csv = st.sidebar.file_uploader("***Добавить файл в формате csv***", type=["csv"])


# Pandas Profiling Report
if uploaded_file_xls is not None:
    @st.cache_data
    def load_excel():
        excel = pd.read_excel(uploaded_file_xls)
        return excel
    df = load_excel()
    pr = ProfileReport(df, explorative=True)
    st.header('**Загруженные данные**')
    st.write(df)
    st.write('---')
    st.header('**Отчет разведочного анализа данных**')
    st_profile_report(pr)
elif uploaded_file_csv is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file_csv)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Загруженные данные**')
    st.write(df)
    st.write('---')
    st.header('**Отчет разведочного анализа данных**')
    st_profile_report(pr)
else:
    st.info('Ожидается загрузка')

#start:
# streamlit run "C:\Python_project\Streamlit_experience\EDA\eda-app-main\app2.py"
# visions==0.7.4

# pandas==2.2.2
# streamlit==1.32.2
# ydata_profiling==4.7.0
# streamlit_pandas_profiling==0.1.3