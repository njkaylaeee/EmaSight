import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page

# Cek login
if 'nama_pengguna' not in st.session_state or st.session_state.nama_pengguna == '':
    st.warning("⚠️ Silakan masukkan nama terlebih dahulu.")
    switch_page("app")

st.title("📊 Dataset & Visualisasi")
st.write(f"Halo, **{st.session_state.nama_pengguna}**!")

# Load dataset
df = pd.read_csv("dataset/gold_price.csv")

st.markdown("### Contoh Data Harga Emas")
st.dataframe(df.head())

# Visualisasi
st.markdown("### Tren Harga Emas Sejak Tahun 2000")

fig, ax = plt.subplots(figsize=(10,4))
sns.lineplot(data=df, x='Date', y='Close', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

if st.button("🔒 Logout"):
    st.session_state.nama_pengguna = ''
    switch_page("app")

