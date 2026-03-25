import streamlit as st

def halaman_tcrt5000():
    st.title("🔦 Sensor Refleksi Inframerah TCRT5000")

    st.image("assets/tcrt5000.png", caption="Gambar Sensor TCRT5000", use_container_width=True)

    st.markdown("""
    **Apa itu TCRT5000?**

    TCRT5000 adalah **sensor refleksi inframerah** yang terdiri dari **LED inframerah (IR LED)** sebagai pemancar cahaya, dan **phototransistor** sebagai penerima cahaya. Sensor ini digunakan untuk mendeteksi **objek berdekatan** atau **garis hitam/putih** pada robot line follower.

    ---

    ### 🛠️ Wiring TCRT5000 ke ESP32

    - **Anoda IR LED** → ke **3.3V** melalui resistor **330Ω**
    - **Katoda IR LED** → ke **GND**
    - **Emitor Phototransistor** → ke **GND**
    - **Kolektor Phototransistor** → ke **GPIO 34** dan ke **3.3V** melalui resistor **6.8kΩ**

    ---

    ### 💡 Cara Kerja

    - IR LED memancarkan cahaya ke permukaan.
    - Jika permukaan **cerah (misalnya putih)**, cahaya dipantulkan dan diterima phototransistor → nilai ADC lebih **tinggi**.
    - Jika permukaan **gelap (misalnya hitam)**, sedikit cahaya dipantulkan → nilai ADC lebih **rendah**.

    ---

    ### 🔧 Contoh Program MicroPython

    ```python
    from machine import Pin, ADC   # Pemanggilan MicroPython I/O
    from time import sleep        # Pemanggilan delay

    sensor = ADC(Pin(34))  # Input analog pada GPIO 34
    sensor.atten(ADC.ATTN_11DB)  # Atur rentang tegangan 0-3.3V

    while True:
        Nilai = sensor.read()  # Baca nilai ADC (0-4095)
        print("Nilai Sensor :", Nilai)
        sleep(0.5)  # Delay 0.5 detik
    ```

    ---

    ### 📝 Penjelasan Program
    - `ADC(Pin(34))`: Mengatur GPIO 34 sebagai input analog.
    - `atten(ADC.ATTN_11DB)`: Mengatur pembacaan ADC agar mampu membaca rentang 0-3.3V.
    - `sensor.read()`: Mengambil nilai analog dari phototransistor.
    - Output bisa digunakan untuk membedakan **objek terang dan gelap**, atau **jeda antar benda**.

    ---

    ### 🚀 Aplikasi TCRT5000
    - Robot **Line Follower**
    - **Deteksi benda** atau permukaan dekat
    - Sensor **counter objek**
    - Pemicu otomatis (misalnya pada dispenser atau tempat sampah otomatis)

    ---

    ⚙️ *Sensor TCRT5000 sangat berguna untuk deteksi permukaan atau objek jarak dekat dengan sistem inframerah reflektif.*
    """)

