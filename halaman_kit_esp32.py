import streamlit as st

def halaman_kit_esp32():
    st.title("🧰 Edukit - AIoT Kit ESP32")
    st.image("assets/kit.png", use_container_width=True)

    st.markdown("## 📘 Penjelasan Komponen")
    tab1, tab2, tab3 = st.tabs(["🧩 Bagian Atas", "🔧 Bagian Bawah", "📑 Panel Output"])

    with tab1:
        st.markdown("""
        **1. Max7219 7 Segment:** Modul tampilan angka 8 digit, cocok untuk menampilkan waktu, angka, dan lainnya.
        
        **2. OLED 64x128:** Layar kecil untuk menampilkan teks atau grafik dengan resolusi tinggi.
        
        **3. Buzzer Aktif:** Menghasilkan bunyi saat diberi tegangan. Digunakan untuk alarm/sinyal.
        
        **4. Buzzer Pasif:** Harus dikontrol frekuensinya untuk menghasilkan bunyi.
        
        **5. Display LED dan Tombol:** Terdiri dari 4 LED dan 4 tombol untuk input dan output visual sederhana.
        
        **6. Motor DC:** Motor sederhana untuk eksperimen rotasi.
        
        **7. Motor Servo:** Digunakan untuk menggerakkan objek secara presisi.
        """)

    with tab2:
        st.markdown("""
        **1. Push Button:** Tombol tekan untuk input manual.

        **2. NTC (Negative Temperature Coefficient):** Sensor suhu analog, resistansinya menurun saat suhu naik.

        **3. LDR (Light Dependent Resistor):** Sensor cahaya, resistansinya menurun saat cahaya bertambah.

        **4. Sensor Getaran (Vibration):** Mendeteksi getaran fisik atau guncangan.

        **5. DS18B20:** Sensor suhu digital dengan presisi tinggi.

        **6. IR Receiver:** Menerima sinyal dari remote infra merah.

        **7. TCRT5000:** Sensor infrared jarak dekat, sering digunakan untuk deteksi garis.

        **8. Trimmer Potensiometer:** Potensiometer untuk input analog yang bisa disesuaikan.

        **9. DHT11:** Sensor suhu dan kelembaban digital.

        **10. Breadboard:** Tempat eksperimen rangkaian elektronik tanpa soldering.
        """)

    with tab3:
        st.markdown("## 🔌 Terminal Panel Output")
        st.markdown("""
        ### a. Terminal Plus (+) dan Minus (-)
        Digunakan sebagai input tegangan modul output, untuk sumber daya ke modul. 
        Terminal Plus (+) terhubung ke VCC (3.3V atau 5V), sedangkan terminal Minus (-) ke GND (Ground).
        """)
        st.image("assets/terminal_output.png", caption="Gambar Terminal Output")

        st.markdown("""
        ### b. Seven Segment - Max7219
        Modul tampilan angka 8 digit dengan protokol SPI (Serial Peripheral Interface). 
        Chipset yang digunakan adalah **Max7219**, cocok untuk menampilkan angka dan simbol. 
        Pin yang digunakan: VCC, GND, DIN, CS, dan CLK.
        """)
        st.image("assets/max7219.png", caption="Gambar Seven Segment Max7219")

        st.markdown("""
        ### c. OLED Display 64x128
        OLED adalah layar kecil yang dapat menampilkan teks atau gambar, menggunakan protokol I2C (SCL, SDA). 
        Resolusi umum adalah 64 x 128 piksel. Sangat cocok untuk menampilkan informasi ringkas dari mikrokontroler.
        """)
        st.image("assets/oled.png", caption="Gambar OLED Display")
        
        st.markdown("Pin: VCC, GND, SCL, SDA")

        st.markdown("""
        ### d. Buzzer Aktif
        Buzzer aktif adalah jenis buzzer yang dapat mengeluarkan suara secara langsung ketika diberi tegangan DC tertentu, 
        tanpa membutuhkan rangkaian tambahan seperti oscillator eksternal.
        """)
        st.image("assets/buzzer_aktif.png", caption="Gambar Buzzer Aktif")

        st.markdown("""
        ### e. Buzzer Pasif
        Buzzer pasif adalah jenis buzzer yang tidak memiliki sirkuit penghasil suara internal. 
        Untuk menghasilkan suara, buzzer pasif memerlukan sinyal eksternal berupa frekuensi (biasanya antara 2 kHz hingga 5 kHz).
        """)
        st.image("assets/buzzer_pasif.png", caption="Gambar Buzzer Pasif")

        st.markdown("""
        ### f. LED (Light Emitting Diode)
        LED adalah komponen semikonduktor yang memancarkan cahaya saat dialiri arus listrik. 
        Warna cahaya tergantung pada bahan semikonduktor yang digunakan. 
        LED banyak digunakan sebagai indikator status.
        """)
        st.image("assets/led.png", caption="Gambar LED")

        st.markdown("""
        ### g. Motor DC (Direct Current Motor)
        Motor DC bekerja dengan arus searah dan berfungsi mengubah energi listrik menjadi energi mekanik (gerakan rotasi). 
        Umumnya digunakan dalam perangkat bergerak seperti kipas, mainan, dan robot.
        """)
        st.image("assets/motor_dc.png", caption="Gambar Motor DC")

        st.markdown("""
        ### h. Motor Servo
        Motor servo merupakan motor listrik yang dirancang untuk kontrol presisi terhadap posisi dan sudut. 
        Digunakan dalam bidang robotika, mekanisme gerak, serta sistem otomatisasi yang memerlukan presisi.
        """)
        st.image("assets/motor_servo.png", caption="Gambar Motor Servo")


    st.markdown("### 🔌 Terminal:")    
    st.markdown("""
    - **3V3:** Sumber daya 3.3V
    - **GND:** Ground
    - **5V:** Sumber daya 5V
    """)
