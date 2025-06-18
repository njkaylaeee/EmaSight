import streamlit as st
import numpy as np
import joblib
from streamlit_extras.switch_page_button import switch_page

# Cek login
if 'nama_pengguna' not in st.session_state or st.session_state.nama_pengguna == '':
    st.warning("⚠️ Silakan masukkan nama terlebih dahulu.")
    switch_page("app")

st.title("🔮 Formulir Prediksi Harga Emas")
st.write(f"Halo, **{st.session_state.nama_pengguna}**!")

# Input fitur
st.markdown("### Masukkan Nilai Fitur")
usd_index = st.slider("US Dollar Index", 80, 120, 100)
inflasi = st.slider("Tingkat Inflasi (%)", 0.0, 10.0, 2.5)
suku_bunga = st.slider("Suku Bunga Acuan (%)", 0.0, 10.0, 3.5)

# Prediksi
if st.button("Prediksi Harga Emas"):
  from tensorflow.keras.models import load_model
import joblib

model = load_model("model/gold_price_model.keras")
scaler = joblib.load("model/scaler.save")
fitur = scaler.transform([[usd_index, inflasi, suku_bunga]])
prediksi = model.predict(fitur)[0][0]

    fitur = np.array([[usd_index, inflasi, suku_bunga]])
    prediksi = model.predict(fitur)[0]
    st.success(f"💰 Prediksi Harga Emas: ${prediksi:,.2f}")

if st.button("🔒 Logout"):
    st.session_state.nama_pengguna = ''
    switch_page("app")

