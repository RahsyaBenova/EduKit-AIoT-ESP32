import streamlit as st

def halaman_motor_dc():
    st.title("🔄 Penjelasan Motor DC dengan ESP32")

    st.image("https://down-br.img.susercontent.com/file/2c9257e8d9bb9151b20d109ecad6f07f", caption="Kontrol Motor DC menggunakan ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu Motor DC?**

    Motor DC (Direct Current) adalah jenis motor listrik yang paling umum digunakan untuk mengubah energi listrik menjadi gerakan putar. Motor ini beroperasi dengan menggunakan **arus searah (DC)** dan dapat berputar **searah jarum jam (CW)** atau **berlawanan arah jarum jam (CCW)**.

    Untuk mengontrol kecepatan dan arah motor DC menggunakan ESP32, kita memerlukan **driver motor** seperti **L298N** atau **L9110S**.

    ---

    ### **Komponen yang Diperlukan**
    - Motor DC
    - ESP32
    - Driver Motor (misalnya L298N)
    - Kabel Jumper
    - Power Supply (baterai atau adaptor)

    ---

    ### **Diagram Koneksi (Contoh dengan L298N)**
    - IN1 -> GPIO 14 ESP32
    - IN2 -> GPIO 12 ESP32
    - ENA -> Aktif (untuk enable motor)
    - GND dan VCC dihubungkan sesuai kebutuhan

    ---

    ### **Contoh Kode MicroPython untuk Mengendalikan Motor DC**
    ```python
    from machine import Pin
    import time

    IN1 = Pin(14, Pin.OUT)
    IN2 = Pin(12, Pin.OUT)

    def motor_maju():
        IN1.value(1)
        IN2.value(0)

    def motor_mundur():
        IN1.value(0)
        IN2.value(1)

    def motor_berhenti():
        IN1.value(0)
        IN2.value(0)

    while True:
        print("Motor Maju")
        motor_maju()
        time.sleep(2)

        print("Motor Mundur")
        motor_mundur()
        time.sleep(2)

        print("Motor Berhenti")
        motor_berhenti()
        time.sleep(2)
    ```

    ---

    ### **Penjelasan Kode:**
    - GPIO 14 dan 12 digunakan untuk mengatur arah motor.
    - `motor_maju()` dan `motor_mundur()` mengatur kombinasi sinyal ke driver.
    - Fungsi `motor_berhenti()` mematikan kedua pin untuk menghentikan motor.

    ---

    ### **Tips Penggunaan Motor DC di ESP32**
    - Gunakan **driver motor** agar ESP32 tidak kelebihan beban.
    - Gunakan **power supply eksternal** untuk motor (jangan langsung dari ESP32).
    - Hindari membalik arah motor terlalu cepat untuk memperpanjang umur motor.

    ---

    ### **Aplikasi Motor DC**
    - Mobil robot sederhana (robot car)
    - Sistem conveyor belt mini
    - Kipas mini atau sistem pendingin
    - Proyek mekanik lainnya dengan kebutuhan gerakan satu arah atau bolak-balik

    ---

    🚗 *Motor DC adalah dasar dari banyak proyek robotika dan IoT yang bergerak. Dengan ESP32, kamu bisa mengontrol arah dan kecepatannya dengan mudah!*

    Jangan lupa lanjut ke halaman **Upload File ke ESP32** untuk mencoba kode motor DC kamu!

    """)
