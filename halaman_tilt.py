import streamlit as st

def halaman_tilt():
    st.title("📐 Sensor Tilt Vibration dengan ESP32")

    st.image("assets/tilt.png", caption="Sensor Tilt Vibration", use_container_width=True)

    st.markdown("""
    **Apa itu Sensor Tilt Vibration?**

    Sensor **Tilt Vibration** digunakan untuk mendeteksi **kemiringan atau getaran**. Di dalamnya terdapat **bola logam kecil**. Ketika sensor dimiringkan atau terguncang, bola logam menyentuh terminal dan menyebabkan **hubungan singkat**, yang bisa dideteksi oleh mikrokontroler seperti **ESP32**.

    ---

    ### ⚙️ **Wiring dengan ESP32**
    - Sambungkan salah satu pin sensor ke **GND ESP32**
    - Pin lainnya dihubungkan ke:
      - **Resistor 10K**, lalu ke **3.3V**
      - **GPIO 23 ESP32** sebagai input digital

    > 📌 Gunakan **pull-up resistor** untuk memastikan sinyal stabil ketika sensor tidak aktif.

    ---

    ### 💻 **Contoh Program MicroPython**

    Berikut adalah contoh kode untuk membaca status dari sensor tilt:

    ```python
    from machine import Pin     # Pemanggilan MicroPython I/O
    from time import sleep      # Fungsi delay

    Vib = Pin(23, Pin.IN)       # Sensor Tilt terhubung ke GPIO 23

    while True:
        if Vib.value() == 1:    # Jika miring (sirkuit tertutup)
            print("Miring!")
        else:
            print("Lurus")
        
        sleep(0.5)              # Jeda 0.5 detik
    ```

    ---

    ### 📝 Penjelasan Kode:
    - `Pin(23, Pin.IN)` mengatur GPIO 23 sebagai input digital.
    - `Vib.value()` membaca status sensor:
      - `1`: Sensor miring atau terguncang.
      - `0`: Sensor dalam posisi normal/lurus.
    - `sleep(0.5)` memberikan jeda antar pembacaan.

    ---

    ### 💡 Tips:
    - Sensor ini cocok untuk sistem deteksi **pergerakan**, **kemiringan**, atau **getaran ringan**.
    - Letakkan sensor di posisi tetap dan hindari kabel longgar untuk menghindari false trigger.

    ---

    📌 *Sensor Tilt sederhana namun efektif untuk deteksi posisi dan keamanan proyek ESP32 kamu!*
    """)
