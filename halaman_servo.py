import streamlit as st

def halaman_servo():
    st.title("⚙️ Penjelasan Motor Servo dengan ESP32")

    st.image("https://fit.labs.telkomuniversity.ac.id/wp-content/uploads/sites/37/2017/08/servo.jpg", caption="Kontrol Servo Motor dengan ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu Motor Servo?**

    Servo motor adalah aktuator kecil yang sangat presisi dan dapat diputar pada sudut tertentu, biasanya antara **0° hingga 180°**. Motor servo banyak digunakan dalam robotika, sistem kendali pintu otomatis, dan berbagai proyek IoT lainnya.

    Servo memiliki 3 kabel:
    - **VCC (Merah)**: Tegangan (biasanya 5V)
    - **GND (Coklat/Hitam)**: Ground
    - **Signal (Kuning/Putih)**: Menerima sinyal kontrol (PWM) dari ESP32

    ---

    ### **Cara Kerja Servo Motor di ESP32**

    ESP32 mengendalikan posisi servo dengan mengirimkan sinyal PWM (Pulse Width Modulation). Semakin lebar pulsa yang dikirim, semakin besar sudut yang dicapai servo.

    Berikut contoh kode **MicroPython** untuk mengendalikan motor servo menggunakan GPIO 13:

    ```python
    from machine import Pin, PWM
    import time

    servo = PWM(Pin(13), freq=50)

    def set_angle(angle):
        duty = int((angle / 180) * 102 + 26)  # Konversi sudut ke nilai duty PWM
        servo.duty(duty)

    while True:
        for angle in range(0, 181, 30):
            set_angle(angle)
            print("Sudut:", angle)
            time.sleep(1)
    ```

    **Penjelasan kode:**
    - **PWM** digunakan pada GPIO 13 dengan frekuensi 50Hz (standar untuk servo).
    - Fungsi `set_angle()` mengubah sudut ke bentuk sinyal PWM (duty cycle).
    - Loop `for` akan memutar servo dari 0° hingga 180° secara bertahap.

    ---

    ### **Tips Penggunaan Servo dengan ESP32**
    - Gunakan **power supply terpisah** jika servo lebih dari satu atau beban cukup berat.
    - Jangan memberi beban berlebihan ke lengan servo.
    - Pastikan servo yang digunakan adalah **SG90** atau jenis yang kompatibel dengan PWM standar.

    ---

    ### **Aplikasi Motor Servo**
    - **Lengan robot** dan proyek mekanik kecil.
    - **Pintu otomatis** atau pengatur ventilasi.
    - **Kamera pan-tilt** untuk pengawasan.
    - **Kendali sudut** pada sistem IoT berbasis posisi.

    ---

    🎯 *Dengan motor servo, kamu bisa menciptakan gerakan mekanik yang presisi dan terkontrol langsung dari ESP32!*

    Jika ingin mengupload kode servo ke ESP32, jangan lupa kunjungi halaman **Upload File ke ESP32** ya!

    """)
