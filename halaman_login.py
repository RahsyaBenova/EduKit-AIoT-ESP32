import streamlit as st
from pymongo import MongoClient
import bcrypt

# 🔒 Koneksi ke MongoDB Atlas (Sesuaikan URI jika diperlukan)
MONGO_URI = "mongodb+srv://savaqua:12345@cluster0.duspxwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["auth_db"]
users_col = db["users"]

def hash_password(password):
    """Mengamankan password menggunakan hashing bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    """Memverifikasi password input dengan hash di database."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(name, username, password):
    """Menambahkan pengguna baru ke database."""
    if users_col.find_one({"username": username}):
        return False, "Username sudah digunakan, silakan pilih yang lain."
    
    hashed_pw = hash_password(password)
    # Secara default pendaftar baru memiliki role 'user'
    users_col.insert_one({
        "name": name,
        "username": username,
        "password": hashed_pw,
        "user_role": "user" 
    })
    return True, "Registrasi berhasil! Silakan pindah ke menu Login."

def login_user(username, password):
    """Memverifikasi kredensial login pengguna."""
    user = users_col.find_one({"username": username})
    if user and verify_password(password, user['password']):
        return True, user
    return False, None

def halaman_login():
    st.title("👤 Manajemen Akun")

    # Inisialisasi session state jika belum ada
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.user_data = {}

    if not st.session_state.is_logged_in:
        # Pilihan menu antara Login dan Register
        auth_mode = st.radio("Pilih Mode:", ["Login", "Register"], horizontal=True)

        if auth_mode == "Login":
            st.subheader("🔑 Masuk ke Akun")
            login_user_input = st.text_input("Username")
            login_pass_input = st.text_input("Password", type="password")
            
            if st.button("Masuk Sekarang"):
                success, data = login_user(login_user_input, login_pass_input)
                if success:
                    st.session_state.is_logged_in = True
                    st.session_state.user_data = data
                    st.success(f"Selamat datang, {data['name']}!")
                    st.rerun()
                else:
                    st.error("Username atau password salah.")

        elif auth_mode == "Register":
            st.subheader("📝 Daftar Akun Baru")
            reg_name = st.text_input("Nama Lengkap")
            reg_user = st.text_input("Pilih Username")
            reg_pass = st.text_input("Pilih Password", type="password")
            confirm_pass = st.text_input("Konfirmasi Password", type="password")

            if st.button("Daftar Sekarang"):
                if reg_name and reg_user and reg_pass:
                    if reg_pass == confirm_pass:
                        success, msg = register_user(reg_name, reg_user, reg_pass)
                        if success:
                            st.success(msg)
                            st.info("Silakan pilih menu 'Login' di atas untuk masuk.")
                        else:
                            st.error(msg)
                    else:
                        st.warning("Password dan Konfirmasi Password tidak cocok.")
                else:
                    st.warning("Mohon isi semua kolom registrasi.")

    else:
        # Tampilan jika sudah Login
        st.success(f"Anda masuk sebagai: **{st.session_state.user_data.get('name')}**")
        st.write(f"Peran Akun: `{st.session_state.user_data.get('user_role', 'user')}`")
        
        if st.button("Keluar dari Akun (Logout)"):
            st.session_state.is_logged_in = False
            st.session_state.user_data = {}
            st.rerun()
