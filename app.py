import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは、Streamlitの世界へようこそ！")

# 入力フォーム
name = st.text_input("あなたの名前を入力してください")
if name:
    st.write(f"{name}さん、ようこそ！")

# グラフを書いてみる
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    '年': [2020, 2021, 2022, 2023],
    '売上': [100, 130, 160, 190]
})
st.line_chart(df.set_index('年'))

# csv ファイルをアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロード")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# 文字の大きさを変えてみる
import streamlit as st

st.markdown("# これはタイトルサイズの文字（H1）")
st.markdown("## これはサブタイトルサイズ（H2）")
st.markdown("### これは中見出しサイズ（H3）")

import streamlit as st

# import streamlit as st

# 「st.markdown("")」はタイトルサイズの文字（H1）を表示する簡易関数
# 「st.markdown("")」はMarkdown形式で柔軟な表現が可能（文字サイズ・太字・色など）

st.markdown("<h1 style='color:red;'>赤いタイトル</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='color:blue;'>青いタイトル</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='color:green;'>緑のタイトル</h1>", unsafe_allow_html=True)


