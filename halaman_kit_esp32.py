import streamlit as st

def halaman_kit_esp32():
    st.title("🎒 Edukit - AIoT Kit ESP32")
    
    # Bagian Pembuka & Tujuan
    st.info("""
    **Pembuka:** Selamat datang di modul interaktif EduKit! Di sini, Anda akan belajar bagaimana komponen elektronik bekerja sama untuk menciptakan sistem cerdas.
    
    **Tujuan Pembelajaran:**
    - Memahami fungsi setiap komponen pada *kit* ESP32.
    - Mengetahui cara penyambungan terminal *input* dan *output*.
    """)

    
    st.image("assets/kit.png", use_container_width=True)

    st.markdown("## 🛠️ Penjelasan Komponen")
    tab1, tab2, tab3 = st.tabs(["🧩 Bagian Atas", "🧬 Bagian Bawah", "📟 Panel Output"])

    with tab1:
        st.markdown("""
        1. **Max7219 7 Segment:** *Modul* tampilan angka 8 digit, cocok untuk menampilkan waktu dan angka.
        2. **OLED 64x128:** Layar kecil untuk menampilkan teks atau grafik dengan resolusi tinggi.
        3. **Buzzer Aktif:** Menghasilkan bunyi saat diberi tegangan; digunakan untuk alarm.
        4. **Buzzer Pasif:** Harus dikontrol frekuensinya (*frequency*) untuk menghasilkan nada tertentu.
        5. **Display LED dan Tombol:** Terdiri dari 4 LED dan 4 tombol untuk *input* dan *output* visual sederhana.
        6. **Motor DC:** Motor sederhana untuk eksperimen rotasi (*rotation*).
        7. **Motor Servo:** Digunakan untuk menggerakkan objek secara presisi sesuai sudut.
        """)

    with tab2:
        st.markdown("""
        1. **Push Button:** Tombol tekan untuk *input* manual.
        2. **NTC (*Negative Temperature Coefficient*):** Sensor suhu analog; resistansinya menurun saat suhu naik.
        3. **LDR (*Light Dependent Resistor*):** Sensor cahaya; resistansinya menurun saat cahaya bertambah.
        4. **Sensor Getaran (*Vibration*):** Mendeteksi getaran fisik atau guncangan.
        5. **DS18B20:** Sensor suhu *digital* dengan presisi tinggi.
        6. **IR Receiver:** Menerima sinyal dari *remote* inframerah.
        7. **TCRT5000:** Sensor *infrared* jarak dekat, sering digunakan untuk deteksi garis (*line follower*).
        8. **Trimmer Potensiometer:** Potensiometer untuk *input* analog yang bisa disesuaikan nilainya.
        9. **DHT11:** Sensor suhu dan kelembaban *digital*.
        10. **Breadboard:** Tempat eksperimen rangkaian elektronik tanpa perlu penyolderan (*soldering*).
        """)

    with tab3:
        st.markdown("## 📟 Terminal Panel Output")
        st.markdown("""
        ### a. Terminal Plus (+) dan Minus (-)
        Digunakan sebagai *input* tegangan *modul output*. Terminal Plus (+) terhubung ke VCC (3.3V atau 5V), sedangkan terminal Minus (-) ke GND (*Ground*).
        """)
        
        st.image("assets/oled.png", caption="Gambar OLED Display menggunakan protokol I2C")
        st.markdown("**Pin:** VCC, GND, SCL, SDA")

    st.markdown("### 🔌 Pedoman Terminal:")    
    st.markdown("""
    - **3V3:** Sumber daya 3.3 *Volt*.
    - **GND:** *Ground* (Titik nol volt).
    - **5V:** Sumber daya 5 *Volt*.
    """)
