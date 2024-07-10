import streamlit as st
import pandas as pd
import io

st.title("CSV 轉換為 XLSX")


uploaded_file = st.file_uploader("上傳 CSV 文件", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("您上傳的 CSV 文件內容：")
    st.dataframe(df)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    processed_data = output.getvalue()

    st.download_button(
        label="下載 XLSX 文件",
        data=processed_data,
        file_name="converted.xlsx",
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )

st.title("XLSX 轉換為 CSV")

uploaded_file_2 = st.file_uploader("上傳 XLSX 文件", type="xlsx")

if uploaded_file_2 is not None:
    df = pd.read_excel(uploaded_file_2)
    st.write("您上傳的 XLSX 文件內容：")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="下載 CSV 文件",
        data=csv,
        file_name="converted.csv",
        mime='text/csv',
    )
