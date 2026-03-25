import streamlit as st

def halaman_tsop1838():
    st.title("📡 Sensor Inframerah TSOP1838 dengan ESP32")

    st.image("assets/tsop1838.png", caption="Sensor TSOP1838", use_container_width=True)

    st.markdown("""
    **Apa itu TSOP1838?**

    TSOP1838 adalah **sensor penerima inframerah (IR)** yang mampu menerima sinyal dari remote control dengan **frekuensi standar 38 kHz**. Sensor ini banyak digunakan dalam berbagai aplikasi seperti **kendali jarak jauh**, **otomatisasi rumah**, hingga **sistem kontrol sederhana** menggunakan remote TV.

    ---

    ### 🛠️ Wiring ke ESP32

    - **Pin 1** (OUT): ke **GPIO 14** melalui resistor **100 ohm**
    - **Pin 2** (GND): ke **GND ESP32**
    - **Pin 3** (VCC): ke **3.3V ESP32**

    ---

    ### 💡 Fitur TSOP1838
    - Dapat menyaring sinyal **noise** atau gangguan dari cahaya sekitar.
    - Kompatibel dengan protokol **NEC**, yang umum digunakan pada remote TV.
    - Cocok untuk kontrol berbasis remote dalam proyek ESP32.

    ---

    ### 🔧 Contoh Program 1 (Basic Print)

    ```python
    from machine import Pin
    from ir_rx import NEC_16

    def callback(data, addr, ctrl):
        if data > 0:  # Jika data dikirim
            print(data)

    ir = NEC_16(Pin(14, Pin.IN), callback)
    ```

    ---

    ### 🛠️ Contoh Program 2 (Mengontrol LED dengan Remote)

    ```python
    from machine import Pin
    from ir_rx import NEC_16

    def ir_callback(data, addr, ctrl):
        global ir_data
        if data > 0:
            ir_data = data
            print('Kode :', data)      

    ir = NEC_16(Pin(14, Pin.IN), ir_callback)
    led = Pin(2, Pin.OUT)

    ir_data = 0

    while True:
        if ir_data > 0:
            if ir_data == 15:   # Tombol 0 pada remote
                led.value(0)
            elif ir_data == 16: # Tombol 1 pada remote
                led.value(1)
            ir_data = 0
    ```

    ---

    ### 📝 Penjelasan Kode:
    - `NEC_16()` adalah class dari library `ir_rx` untuk membaca protokol NEC (sering digunakan di remote TV).
    - Callback dijalankan saat sinyal IR diterima.
    - `ir_data` menyimpan kode tombol terakhir yang diterima dari remote.
    - LED dikendalikan berdasarkan tombol remote yang ditekan.

    ---

    ✅ *Dengan TSOP1838 dan ESP32, kamu bisa membuat proyek keren seperti kontrol TV buatan sendiri, sistem otomatisasi, atau game IR sederhana!*
    """)

