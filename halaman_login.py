# halaman_login.py

import streamlit as st
from pymongo import MongoClient
import bcrypt

# 🔒 Koneksi MongoDB Atlas
MONGO_URI = "mongodb+srv://savaqua:12345@cluster0.duspxwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["auth_db"]
users = db["users"]

# 🔐 Fungsi hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# 🔐 Fungsi verifikasi password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# 📝 Fungsi registrasi
def register_user(name, username, password):
    if users.find_one({"username": username}):
        return False, "Username sudah terdaftar."
    hashed_pw = hash_password(password)
    users.insert_one({"name": name, "username": username, "password": hashed_pw})
    return True, "Berhasil registrasi!"

# 🔓 Fungsi login
def login_user(username, password):
    user = users.find_one({"username": username})
    if user and verify_password(password, user['password']):
        return True, user
    return False, None

# 🎯 Halaman login & register
def halaman_login():
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.user_data = {}

    menu = st.radio("Login/Register", ["Login", "Register"])

    if not st.session_state.is_logged_in:
        if menu == "Login":
            st.subheader("🔐 Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                success, user_data = login_user(username, password)
                if success:
                    st.session_state.is_logged_in = True
                    st.session_state.user_data = user_data
                    st.success("Login berhasil!")
                    st.rerun()
                else:
                    st.error("Username atau password salah.")

        elif menu == "Register":
            st.subheader("📝 Registrasi")
            name = st.text_input("Nama Lengkap")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Register"):
                success, msg = register_user(name, username, password)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
    else:
        st.success(f"Halo, {st.session_state.user_data['name']} 👋")
        if st.button("Logout"):
            st.session_state.is_logged_in = False
            st.session_state.user_data = {}
            st.success("Berhasil logout.")
            st.rerun()
