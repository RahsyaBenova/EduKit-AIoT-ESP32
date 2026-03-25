import streamlit as st

def halaman_button():
    st.title("🔘 Penjelasan Tombol (Push Button) dengan ESP32")

    st.image("https://images.tokopedia.net/img/cache/700/hDjmkQ/2020/9/18/8ef2e23d-efa0-4702-9932-911e2109d23e.jpg", caption="Koneksi Push Button ke ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu Push Button?**

    Push button adalah saklar sederhana yang menghubungkan atau memutuskan sirkuit saat ditekan. Dalam proyek ESP32, push button digunakan untuk memberikan input digital, seperti menyalakan atau mematikan LED, mengubah mode operasi, atau memicu aksi tertentu.

    ---

    ### 🧰 Komponen yang Diperlukan
    - ESP32
    - Push button
    - Resistor 10 kΩ (untuk pull-down)
    - Breadboard & Kabel Jumper

    ---

    ### 🔌 Koneksi Push Button ke ESP32

    Terdapat dua metode umum untuk menghubungkan push button ke ESP32:

    1. **Menggunakan Pull-down Resistor:**
       - Satu pin push button terhubung ke **3.3V**.
       - Pin lainnya terhubung ke **GPIO ESP32** dan juga ke **GND** melalui resistor 10 kΩ.
       - Saat tombol ditekan, GPIO membaca **HIGH**; saat tidak ditekan, membaca **LOW**.

    2. **Menggunakan Pull-up Resistor:**
       - Satu pin push button terhubung ke **GND**.
       - Pin lainnya terhubung ke **GPIO ESP32** dan juga ke **3.3V** melalui resistor 10 kΩ.
       - Saat tombol ditekan, GPIO membaca **LOW**; saat tidak ditekan, membaca **HIGH**.

    **Catatan:** Menggunakan resistor pull-up atau pull-down mencegah kondisi input "melayang" (floating) yang dapat menyebabkan pembacaan tidak stabil.

    ---

    ### 🧪 Contoh Kode MicroPython

    Berikut contoh kode untuk membaca status push button menggunakan pull-down resistor:

    ```python
    from machine import Pin
    import time

    # Inisialisasi pin GPIO sebagai input dengan pull-down resistor
    tombol = Pin(15, Pin.IN, Pin.PULL_DOWN)

    while True:
        if tombol.value() == 1:
            print("Tombol ditekan")
        else:
            print("Tombol tidak ditekan")
        time.sleep(0.5)
    ```

    **Penjelasan:**
    - `Pin(15, Pin.IN, Pin.PULL_DOWN)`: Mengatur GPIO15 sebagai input dengan resistor pull-down internal.
    - `tombol.value()`: Membaca status tombol; `1` jika ditekan, `0` jika tidak.

    ---

    ### 💡 Tips Penggunaan
    - Gunakan debounce (penundaan singkat) untuk menghindari pembacaan ganda saat tombol ditekan.
    - Push button dapat digunakan untuk:
        - Mengendalikan LED atau perangkat lain.
        - Mengubah mode operasi perangkat.
        - Memicu aksi tertentu dalam program.

    ---

    🔘 *Dengan memahami cara kerja push button, Anda dapat menambahkan interaksi pengguna ke proyek ESP32 Anda.*

    Untuk mencoba kode ini pada ESP32 Anda, silakan kunjungi halaman **Upload File ke ESP32**.
    """)
