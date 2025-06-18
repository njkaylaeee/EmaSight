import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Inisialisasi session
if 'nama_pengguna' not in st.session_state:
    st.session_state.nama_pengguna = ''

# Cek apakah nama sudah dimasukkan
if st.session_state.nama_pengguna == '':
    with st.modal("🎉 Selamat Datang!"):
        st.write("Silakan masukkan nama kamu terlebih dahulu!")
        nama = st.text_input("Nama Anda", key="input_nama")
        if st.button("Masuk"):
            if nama.strip() != "":
                st.session_state.nama_pengguna = nama
                st.rerun()
            else:
                st.warning("Nama tidak boleh kosong!")
else:
    # Tampilkan halaman utama
    st.image("https://i.ibb.co/x3ppHzn/emas-banner.png", use_column_width=True)
    st.markdown(f"""
    ## GoldSight **Navigasi Cerdas Investasi Emas Anda**
    ### Prediksi Harga Emas Berbasis Deep Learning

    **GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data di tengah volatilitas pasar global.
    """, unsafe_allow_html=True)

    if st.button("🚀 Go to Dashboard"):
        switch_page("1_Hasil_Pelatihan_Model")
