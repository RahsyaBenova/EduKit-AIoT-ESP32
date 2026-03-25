import streamlit as st

def halaman_oled():
    st.title("🖥️ Penjelasan OLED Display (SSD1306) dengan ESP32")

    st.image("https://images.tokopedia.net/img/cache/700/hDjmkQ/2022/12/14/2064ce1f-a6e3-4c5e-abae-67a9fc379aed.jpg", caption="Koneksi OLED SSD1306 ke ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu OLED Display?**

    OLED (Organic Light Emitting Diode) adalah layar kecil yang dapat menampilkan teks, grafik, atau data sensor. Modul yang umum digunakan adalah **SSD1306** dengan ukuran 0.96 inci dan resolusi **128x64 piksel**, menggunakan komunikasi **I2C**.

    ---

    ### 🧰 Komponen yang Diperlukan
    - ESP32
    - OLED SSD1306 (I2C)
    - Breadboard & Kabel Jumper

    ---

    ### 🔌 Koneksi I2C OLED ke ESP32

    | OLED Pin | ESP32 Pin |
    |----------|-----------|
    | VCC      | 3.3V      |
    | GND      | GND       |
    | SCL      | GPIO 22   |
    | SDA      | GPIO 21   |

    ---

    ### 🧪 Contoh Kode MicroPython

    ```python
    from machine import Pin, I2C
    import ssd1306

    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    oled.fill(0)  # Bersihkan layar
    oled.text('Halo, ESP32!', 0, 0)
    oled.text('OLED Siap!', 0, 10)
    oled.show()
    ```

    **Penjelasan:**
    - `i2c = I2C(0, scl=Pin(22), sda=Pin(21))`: Menginisialisasi komunikasi I2C pada GPIO 22 dan 21.
    - `oled = ssd1306.SSD1306_I2C(128, 64, i2c)`: Menginisialisasi objek OLED dengan resolusi 128x64.
    - `oled.fill(0)`: Membersihkan layar.
    - `oled.text('...', x, y)`: Menampilkan teks pada posisi (x, y).
    - `oled.show()`: Menampilkan konten di layar.

    ---

    ### 💡 Tips Penggunaan
    - Gunakan **font kecil** untuk menampilkan lebih banyak informasi.
    - Pastikan alamat I2C OLED adalah **0x3C** (default).
    - Untuk tampilan grafis lebih kompleks, pertimbangkan menggunakan library tambahan seperti `framebuf`.

    ---

    ### 📌 Aplikasi OLED Display
    - Menampilkan data sensor (suhu, kelembaban, dsb.)
    - Jam digital atau stopwatch
    - Menu navigasi pada perangkat IoT
    - Tampilan status sistem

    ---

    📺 *Dengan OLED display, Anda dapat menambahkan antarmuka visual yang menarik dan informatif pada proyek ESP32 Anda!*

    Untuk mencoba kode ini pada ESP32 Anda, silakan kunjungi halaman **Upload File ke ESP32**.
    """)
