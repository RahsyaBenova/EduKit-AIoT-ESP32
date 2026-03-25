import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import random
# Koneksi MongoDB
MONGO_URI = "mongodb+srv://savaqua:12345@cluster0.duspxwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["auth_db"]
quiz_collection = db["quiz_history"]
score_collection = db["quiz_scores"]

# Soal Quiz Lengkap dari berbagai topik
quiz_bank = [
    {
        "soal": "Apa fungsi resistor saat menggunakan LED pada ESP32?",
        "opsi": [
            "Untuk membuat LED lebih terang",
            "Mengubah warna LED",
            "Membatasi arus agar LED tidak rusak",
            "Mengisi daya ke LED"
        ],
        "jawaban_benar": "Membatasi arus agar LED tidak rusak"
    },
    {
        "soal": "Apa kegunaan sensor DHT11 pada proyek ESP32?",
        "opsi": [
            "Mengukur jarak",
            "Mengukur suhu dan kelembaban",
            "Mendeteksi cahaya",
            "Mengendalikan motor"
        ],
        "jawaban_benar": "Mengukur suhu dan kelembaban"
    },
    {
        "soal": "Buzzer digunakan untuk?",
        "opsi": [
            "Menampilkan data suhu",
            "Memberikan sinyal suara",
            "Menyimpan data",
            "Mengukur kelembaban"
        ],
        "jawaban_benar": "Memberikan sinyal suara"
    },
    {
        "soal": "Apa fungsi dari potensiometer trim dalam rangkaian?",
        "opsi": [
            "Menyesuaikan tegangan atau arus",
            "Menyimpan data sensor",
            "Menambah kapasitas arus",
            "Memperkuat sinyal WiFi"
        ],
        "jawaban_benar": "Menyesuaikan tegangan atau arus"
    },
    {
        "soal": "Apa tujuan menggunakan sensor LDR?",
        "opsi": [
            "Mendeteksi suhu",
            "Mendeteksi kelembaban",
            "Mendeteksi cahaya",
            "Mengontrol motor"
        ],
        "jawaban_benar": "Mendeteksi cahaya"
    },
    {
        "soal": "Apa peran OLED display pada proyek ESP32?",
        "opsi": [
            "Mengukur suhu",
            "Menampilkan informasi secara visual",
            "Menyimpan data proyek",
            "Mengeluarkan suara"
        ],
        "jawaban_benar": "Menampilkan informasi secara visual"
    },
    {
        "soal": "TM1637 digunakan untuk apa?",
        "opsi": [
            "Menampilkan angka pada 7-segment display",
            "Mendeteksi suhu",
            "Mengontrol LED",
            "Mengendalikan motor"
        ],
        "jawaban_benar": "Menampilkan angka pada 7-segment display"
    },
    {
        "soal": "Apa fungsi dari motor DC pada proyek ESP32?",
        "opsi": [
            "Mendeteksi suhu",
            "Menampilkan teks",
            "Menggerakkan benda secara rotasi",
            "Mengukur kelembaban"
        ],
        "jawaban_benar": "Menggerakkan benda secara rotasi"
    },
    {
        "soal": "Apa fungsi dari sensor push button?",
        "opsi": [
            "Mendeteksi suhu",
            "Sebagai input tekanan (manual)",
            "Menampilkan angka",
            "Mengontrol kelembaban"
        ],
        "jawaban_benar": "Sebagai input tekanan (manual)"
    },
    {
        "soal": "Apa fungsi sensor NTC dalam proyek ESP32?",
        "opsi": [
            "Mengukur suhu berdasarkan resistansi",
            "Mengukur kelembaban",
            "Menyimpan data",
            "Mengeluarkan suara"
        ],
        "jawaban_benar": "Mengukur suhu berdasarkan resistansi"
    },
    {
        "soal": "Apa fungsi dari tilt sensor?",
        "opsi": [
            "Mendeteksi kemiringan atau orientasi",
            "Mengontrol LED",
            "Mengukur kelembaban",
            "Menyimpan data"
        ],
        "jawaban_benar": "Mendeteksi kemiringan atau orientasi"
    },
    {
        "soal": "DS18S20 digunakan untuk apa?",
        "opsi": [
            "Sensor suhu digital",
            "Sensor cahaya",
            "Sensor gerak",
            "Sensor suara"
        ],
        "jawaban_benar": "Sensor suhu digital"
    },
    {
        "soal": "Apa fungsi sensor TSOP1838?",
        "opsi": [
            "Penerima sinyal infrared",
            "Sensor suhu",
            "Sensor cahaya",
            "Pengendali suara"
        ],
        "jawaban_benar": "Penerima sinyal infrared"
    },
    {
        "soal": "TCR5000 digunakan untuk mendeteksi?",
        "opsi": [
            "Garis hitam/putih",
            "Cahaya warna merah",
            "Panas dari tubuh manusia",
            "Sinyal WiFi"
        ],
        "jawaban_benar": "Garis hitam/putih"
    },
    {
        "soal": "Apa fungsi dari object detection sensor?",
        "opsi": [
            "Mendeteksi kehadiran benda",
            "Mengukur suhu",
            "Menyalakan motor",
            "Menampilkan angka"
        ],
        "jawaban_benar": "Mendeteksi kehadiran benda"
    },
    {
        "soal": "Apa kegunaan servo motor?",
        "opsi": [
            "Menggerakkan objek secara presisi sesuai sudut",
            "Mendeteksi suhu",
            "Menyimpan data proyek",
            "Menampilkan suara"
        ],
        "jawaban_benar": "Menggerakkan objek secara presisi sesuai sudut"
    },
    {
        "soal": "Bagaimana cara meng-upload file ke ESP32?",
        "opsi": [
            "Menggunakan kabel USB dan software seperti Thonny atau Arduino IDE",
            "Menekan tombol reset secara terus menerus",
            "Menyambungkan ke speaker",
            "Mengirimkan file lewat email"
        ],
        "jawaban_benar": "Menggunakan kabel USB dan software seperti Thonny atau Arduino IDE"
    },
    {
        "soal": "Apa kegunaan chatbot dalam proyek ESP32 berbasis edukasi?",
        "opsi": [
            "Memberikan bantuan interaktif atau informasi kepada pengguna",
            "Mengontrol motor",
            "Mendeteksi suhu",
            "Menampilkan grafik data"
        ],
        "jawaban_benar": "Memberikan bantuan interaktif atau informasi kepada pengguna"
    }
]

def halaman_quiz():
    st.title("🧠 Quiz Challenge")
    st.markdown("Uji pengetahuanmu tentang komponen ESP32! Jawab 10 soal berikut:")

    # Cek login
    if "user_data" not in st.session_state or not st.session_state.get("is_logged_in"):
        st.warning("Silakan login terlebih dahulu untuk mengikuti kuis.")
        return

    user = st.session_state["user_data"]

    # Simpan soal ke session_state jika belum ada
    if "soal_acak" not in st.session_state:
        st.session_state["soal_acak"] = random.sample(quiz_bank, 10)

    soal_acak = st.session_state["soal_acak"]
    jawaban_user = {}

    # Tampilkan soal
    for idx, soal_data in enumerate(soal_acak):
        st.subheader(f"Soal {idx + 1}")
        jawaban = st.radio(
            soal_data["soal"],
            soal_data["opsi"],
            key=f"quiz_soal_{idx}"
        )
        jawaban_user[idx] = {
            "soal_data": soal_data,
            "jawaban": jawaban
        }

    # Proses ketika tombol diklik
    if st.button("✅ Kirim Semua Jawaban"):
        total_benar = 0
        now = datetime.now()

        for item in jawaban_user.values():
            soal_data = item["soal_data"]
            jawaban = item["jawaban"]
            benar = jawaban == soal_data["jawaban_benar"]
            hasil = "Benar" if benar else "Salah"

            if benar:
                total_benar += 1

            # Simpan ke DB
            quiz_collection.insert_one({
                "user_id": user["_id"],
                "username": user["username"],
                "soal": soal_data["soal"],
                "jawaban": jawaban,
                "hasil": hasil,
                "timestamp": now
            })

        # Update skor
        score_collection.update_one(
            {"username": user["username"]},
            {
                "$inc": {
                    "total_soal": len(jawaban_user),
                    "total_benar": total_benar
                },
                "$set": {
                    "last_updated": now
                }
            },
            upsert=True
        )

        st.success(f"🎉 Kamu menjawab dengan benar {total_benar} dari {len(jawaban_user)} soal.")

        # Reset soal_acak agar user bisa mulai ulang jika ingin
        del st.session_state["soal_acak"]
