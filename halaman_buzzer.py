import streamlit as st

def halaman_buzzer():
    st.title("🔊 Penjelasan Buzzer di ESP32")

    st.image("https://i.ytimg.com/vi/GRL840Pisgs/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDQBeIRnaouPD2_vo4xPSD4pdobSg", caption="Buzzer Aktif", use_container_width=True)

    st.markdown("""
    **Apa itu Buzzer?**

    Buzzer adalah komponen elektronik yang digunakan untuk menghasilkan **suara**. Buzzer bisa digunakan untuk memberikan **notifikasi bunyi**, seperti alarm, pemberitahuan, atau efek suara pada sistem berbasis mikrokontroler seperti **ESP32**.

    Terdapat dua jenis buzzer:
    - **Buzzer Aktif**: Menghasilkan suara sendiri saat diberi tegangan.
    - **Buzzer Pasif**: Membutuhkan sinyal frekuensi (PWM) dari mikrokontroler untuk menghasilkan suara.

    ---

    ### **Cara Kerja Buzzer dengan ESP32**

    Untuk mengontrol buzzer dari ESP32, kita hanya perlu mengatur **GPIO pin** ke HIGH (nyala) atau LOW (mati). Untuk membuat suara berbunyi berkedip (beep-beep), kita bisa memberi delay.

    Berikut contoh kode MicroPython untuk mengontrol buzzer aktif di GPIO 26:

    ```python
    from machine import Pin
    import time

    buzzer = Pin(26, Pin.OUT)

    while True:
        buzzer.on()      # Buzzer berbunyi
        time.sleep(0.5)  # Tunggu 0.5 detik
        buzzer.off()     # Buzzer mati
        time.sleep(0.5)  # Tunggu 0.5 detik
    ```

    **Penjelasan kode:**
    - Pin **GPIO 26** digunakan sebagai output untuk mengontrol buzzer.
    - `buzzer.on()` menyalakan buzzer.
    - `buzzer.off()` mematikannya.
    - `sleep()` memberikan jeda agar buzzer berbunyi berkedip.

    ---

    ### **Tips Penggunaan Buzzer di ESP32**
    - Gunakan **resistor** kecil jika diperlukan untuk membatasi arus.
    - Pastikan buzzer terhubung dengan **polaritas yang benar** (khususnya buzzer aktif).
    - Jika menggunakan **buzzer pasif**, kamu bisa menggunakan sinyal PWM (Pulse Width Modulation) dari ESP32.

    ---

    ### **Aplikasi Buzzer**
    - Sistem **alarm pintu** atau **alarm kebakaran**.
    - Penanda **akhir waktu** pada sistem timer.
    - **Notifikasi suara** pada alat ukur atau sensor.

    ---

    💡 *Buzzer adalah cara sederhana tapi efektif untuk memberikan feedback suara pada proyek ESP32 kamu!*

    Jika ingin mencoba meng-upload kode buzzer ke ESP32, silakan buka halaman **Upload File ke ESP32** di menu samping.

    """)
