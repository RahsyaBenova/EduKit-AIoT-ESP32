import streamlit as st

def halaman_ldr():
    st.title("🔆 Penjelasan Sensor LDR dengan ESP32")

    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDZ-6isMwsE2_ko10nkaa1CpQWCPWKCs-ZODvyiJugNIhrBYj3IPDjoMYxpmHqQ5JgblHZz6W7e-ucoBlm2q5fDtPeAXevKq76pv5s-lyOUoYoLstlUc46JNpVvW7EYHNRwAmbza5QeC4/s1600/ldr-sensor-500x500.jpg", caption="Koneksi Sensor LDR ke ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu Sensor LDR?**

    LDR (Light Dependent Resistor) adalah sensor yang mengubah resistansinya berdasarkan intensitas cahaya. Semakin terang cahaya yang diterima, semakin rendah resistansinya. Sensor ini sering digunakan untuk mendeteksi tingkat pencahayaan di lingkungan sekitar.

    ---

    ### 🧰 Komponen yang Diperlukan
    - ESP32
    - Sensor LDR
    - Resistor 10 kΩ
    - Breadboard & Kabel Jumper

    ---

    ### 🔌 Koneksi LDR ke ESP32

    Untuk membaca nilai cahaya secara analog, kita dapat menggunakan konfigurasi pembagi tegangan:

    - **LDR** dihubungkan antara **3.3V** dan **pin ADC** (misalnya GPIO36).
    - **Resistor 10 kΩ** dihubungkan antara **pin ADC** dan **GND**.

    Dengan konfigurasi ini, tegangan pada pin ADC akan bervariasi sesuai dengan intensitas cahaya yang diterima oleh LDR.

    ---

    ### 🧪 Contoh Kode MicroPython

    ```python
    from machine import ADC, Pin
    import time

    # Inisialisasi ADC pada GPIO36
    ldr = ADC(Pin(36))
    ldr.atten(ADC.ATTN_11DB)  # Rentang input hingga ~3.3V
    ldr.width(ADC.WIDTH_12BIT)  # Resolusi 12-bit (0-4095)

    while True:
        nilai = ldr.read()
        print("Nilai ADC:", nilai)
        time.sleep(1)
    ```

    **Penjelasan:**
    - `ADC.ATTN_11DB`: Mengatur attenuasi untuk memungkinkan pembacaan tegangan hingga ~3.3V.
    - `ADC.WIDTH_12BIT`: Mengatur resolusi ADC menjadi 12-bit, menghasilkan nilai antara 0 hingga 4095.
    - `ldr.read()`: Membaca nilai tegangan analog yang dikonversi menjadi nilai digital.

    ---

    ### 💡 Tips Penggunaan
    - Nilai ADC yang lebih tinggi menunjukkan intensitas cahaya yang lebih tinggi.
    - Anda dapat menetapkan ambang batas untuk mendeteksi kondisi terang atau gelap.
    - Sensor LDR dapat digunakan dalam berbagai aplikasi seperti:
        - Sistem pencahayaan otomatis
        - Pengukur intensitas cahaya
        - Proyek IoT yang memerlukan deteksi cahaya

    ---

    🌞 *Dengan sensor LDR, Anda dapat membuat perangkat yang responsif terhadap perubahan cahaya di lingkungan sekitar.*

    Untuk mencoba kode ini pada ESP32 Anda, silakan kunjungi halaman **Upload File ke ESP32**.
    """)
