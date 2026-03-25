import streamlit as st

def halaman_led():
    st.title("💡 Penjelasan LED di ESP32")
    
    # Menambahkan gambar ilustrasi LED dan ESP32
    st.image("https://www.ledyilighting.com/wp-content/uploads/2023/03/Light-Emitting-Diodes.jpg", caption="Light Emitting Diode (LED)", use_container_width=True)

    st.markdown("""
    **Apa itu LED?**

    LED (Light Emitting Diode) adalah komponen elektronik yang memancarkan cahaya saat diberi arus listrik. Dalam dunia mikrokontroler seperti ESP32, LED sering digunakan untuk:

    - **Indikator status**: Menunjukkan apakah perangkat hidup atau mati.
    - **Notifikasi (nyala/mati)**: Memberikan pemberitahuan dengan perubahan status.
    - **Uji koneksi board**: Memastikan board ESP32 berfungsi dengan baik.

    ---
    
    ### **Cara kerja LED di ESP32**

    LED dapat dikendalikan dengan menggunakan **GPIO pins** pada ESP32. Pin ini bisa di-set untuk mengeluarkan sinyal listrik, menghidupkan dan mematikan LED. Sebagai contoh:

    ```python
    from machine import Pin
    import time

    led = Pin(2, Pin.OUT)  # GPIO2 biasanya terhubung ke LED bawaan

    while True:
        led.value(1)  # LED ON
        time.sleep(1)
        led.value(0)  # LED OFF
        time.sleep(1)
    ```

    Penjelasan kode di atas:
    - **GPIO2** (biasanya pin untuk LED internal pada ESP32) digunakan untuk menyalakan dan mematikan LED.
    - `led.value(1)` menyalakan LED dan `led.value(0)` mematikan LED.
    - Fungsi `time.sleep(1)` memberikan jeda 1 detik antara perubahan status LED.

    ---
    
    **Catatan Penting:**
    - Pastikan **menggunakan resistor pembatas** (biasanya 220–330 ohm) untuk menghindari kerusakan pada LED dan pin ESP32.
    - Jika menggunakan LED eksternal, pastikan Anda mengetahui **pin GPIO yang digunakan**.

    ---
    
    **Kenapa LED penting di ESP32?**

    LED sering digunakan untuk menampilkan status board, apakah board ESP32 sedang **menunggu koneksi Wi-Fi** atau sudah **terhubung ke jaringan**. Penggunaan LED juga sangat berguna untuk debugging dan pengujian aplikasi sederhana.

    ---
    
    Semoga penjelasan ini bermanfaat! 😊 Jika ingin mencoba untuk **meng-upload kode** ke ESP32, silakan lanjut ke halaman upload.

    """)
