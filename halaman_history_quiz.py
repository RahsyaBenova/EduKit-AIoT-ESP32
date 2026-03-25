# halaman_history_quiz.py

import streamlit as st
from pymongo import MongoClient

# Koneksi MongoDB
MONGO_URI = "mongodb+srv://savaqua:12345@cluster0.duspxwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["auth_db"]
quiz_collection = db["quiz_history"]
score_collection = db["quiz_scores"]  # Tambahan untuk skor

def halaman_history_quiz():
    st.title("📜 Riwayat Quiz")

    if "user_data" not in st.session_state or not st.session_state.get("is_logged_in"):
        st.warning("Silakan login untuk melihat riwayat quiz.")
        return

    user = st.session_state["user_data"]

    # Tombol untuk reset riwayat dan skor
    if st.button("🗑️ Reset Semua Riwayat dan Skor"):
        quiz_collection.delete_many({"username": user["username"]})
        score_collection.delete_one({"username": user["username"]})
        st.success("✅ Semua riwayat dan skor quiz berhasil direset.")

    # Tampilkan ringkasan skor
    score = score_collection.find_one({"username": user["username"]})
    if score:
        st.info(f"🎯 Skor Akumulasi: **{score.get('total_benar', 0)} benar** dari **{score.get('total_soal', 0)} soal**")
    else:
        st.info("Belum ada skor yang tercatat.")

    # Ambil riwayat quiz
    history = quiz_collection.find({"username": user["username"]}).sort("timestamp", -1)

    ada_riwayat = False
    for record in history:
        ada_riwayat = True
        st.markdown(f"""
        - 🕒 **Waktu**: {record['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
        - ❓ **Soal**: {record['soal']}
        - ✍️ **Jawaban Kamu**: {record['jawaban']}
        - ✅ **Hasil**: {record['hasil']}
        ---
        """)

    if not ada_riwayat:
        st.write("📭 Belum ada riwayat quiz yang tersedia.")
