import streamlit as st
import pickle
import os
import time
from app.home import home
from app.pilih_rekomendasi import pilih_rekomendasi
from app.daftar_rekomendasi import daftar_rekomendasi
from app.riwayat_rekomendasi import riwayat_rekomendasi
from app.edit_rekomendasi import edit_rekomendasi

# Fungsi utama
def main():
    st.set_page_config(
        page_title="My Streamlit App",
        layout="wide",  # Set layout to wide mode
        initial_sidebar_state="auto",  # Sidebar initial state
    )
    # Inisialisasi session_state
    if 'user' not in st.session_state:
        st.session_state.user = {'username': None}
    if 'login' not in st.session_state:
        st.session_state.login = False

    # Fungsi untuk memeriksa login berdasarkan username dan password
    def check_login(username, password):
        # Masukkan username dan password di sini
        credentials = {
            "aida": "aida123",
            "ilham": "ilham123"
        }
        if username in credentials and credentials[username] == password:
            return True
        else:
            return False

    # Tampilkan form login jika belum login
    if not st.session_state.login:
        with st.container():
            # Membuat dua kolom dengan rasio 3:2
            col1, col2 = st.columns([3, 2])
            with col1:
                st.header('Hai, Selamat Datang di NuansaDesain')
                st.subheader('Silahkan Login')
                username = st.text_input("Username:")
                password = st.text_input("Password:", type="password")
            with col2:
                st.image('data/warna/Warni.png')

            if st.button("Login"):
                # Periksa kecocokan username dan password
                if check_login(username, password):
                    st.session_state.user = {'username': username}
                    st.session_state.login = True

                    # Simpan email ke dalam file menggunakan pickle (opsional)
                    with open('user_email.pkl', 'wb') as file:
                        pickle.dump(username, file)

                    st.success("Login berhasil")
                    time.sleep(2)
                    st.experimental_rerun()
                else:
                    st.error("Login gagal. Silakan coba lagi.")

    # Jika sudah login, tampilkan halaman setelah login
    if st.session_state.login:
        username = st.session_state.user['username']
        st.sidebar.title(f'Hai, {username}!')
        opsi = st.sidebar.radio("Pilih Halaman", ['Beranda', 'Pilih Rekomendasi', 'Daftar Rekomendasi', 'Riwayat Rekomendasi', 'Edit Rekomendasi'])

        # Konten utama
        if opsi == "Beranda":
            home()
        elif opsi == "Pilih Rekomendasi":
            pilih_rekomendasi()
        elif opsi == 'Daftar Rekomendasi':
            daftar_rekomendasi()
        elif opsi == 'Riwayat Rekomendasi':
            riwayat_rekomendasi()
        elif opsi == 'Edit Rekomendasi':
            edit_rekomendasi()

        if st.sidebar.button("Logout"):
            # Hapus informasi pengguna dari sesi saat logout
            st.session_state.login = False
            st.success("Logout berhasil!")
            # Hapus file user_email.pkl saat logout (opsional)
            if os.path.exists("user_email.pkl"):
                os.remove("user_email.pkl")
            time.sleep(2)
            st.experimental_rerun()

if __name__ == '__main__':
    main()
