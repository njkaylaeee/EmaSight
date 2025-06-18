import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="EmaSight",
    page_icon="🥇",
    layout="wide"
)

# Judul aplikasi
st.title("🥇 EmaSight :blue[Navigasi Cerdas Investasi Emas Anda]")

# Deskripsi singkat
st.markdown("""
Selamat datang di **EmaSight**, sebuah dashboard pintar untuk memantau dan memprediksi harga emas dunia.  
Gunakan fitur-fitur di sebelah kiri untuk menavigasi ke:
- Hasil Pelatihan Model
- Visualisasi Dataset
- Formulir Prediksi Harga Emas
""")

# Muat data
df = pd.read_csv("Dataset/final_gold_data.csv")

# Konversi ke datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp', ascending=True)

# Tampilkan grafik harga 30 hari terakhir
st.subheader("📈 Harga Emas 30 Hari Terakhir")
df_last = df[['timestamp', 'close']].tail(30)
st.line_chart(data=df_last, x='timestamp', y='close')

# Footer
st.caption("© 2025 - EmaSight Dashboard")
