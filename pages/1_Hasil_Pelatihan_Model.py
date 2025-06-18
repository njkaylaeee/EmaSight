import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Cek apakah user sudah login (mengisi nama)
if 'nama_pengguna' not in st.session_state or st.session_state.nama_pengguna == '':
    st.warning("⚠️ Silakan masukkan nama terlebih dahulu.")
    switch_page("app")  # Redirect ke halaman utama

# Konten halaman dashboard
st.title("📈 Hasil Pelatihan Model")
st.write(f"Halo, **{st.session_state.nama_pengguna}**! Ini hasil pelatihan model prediksi harga emas.")

# Contoh isi halaman...
st.success("Model GRU mencapai akurasi 95% terhadap data historis!")

# Tombol logout
if st.button("🔒 Logout"):
    st.session_state.nama_pengguna = ''
    switch_page("app")

