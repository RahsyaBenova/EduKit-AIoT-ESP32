import streamlit as st

def halaman_tm1637():
    st.title("⏱️ Penjelasan Modul TM1637 dengan ESP32")

    st.image("https://www.ardutech.com/wp-content/uploads/2019/10/17.-TM1637-pin.jpg", caption="Koneksi TM1637 ke ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu TM1637?**

    TM1637 adalah **driver LED** yang umum digunakan untuk mengendalikan **display 7-segment 4-digit**. Modul ini memungkinkan tampilan angka, teks pendek, atau waktu dengan hanya menggunakan **2 pin data** (CLK dan DIO), sehingga sangat efisien untuk proyek berbasis ESP32.

    ---

    ### 🧰 Komponen yang Diperlukan
    - ESP32
    - Modul TM1637 (4-digit 7-segment display)
    - Kabel jumper

    ---

    ### 🔌 Koneksi TM1637 ke ESP32

    | TM1637 Pin | ESP32 Pin |
    |------------|-----------|
    | VCC        | 3.3V      |
    | GND        | GND       |
    | CLK        | GPIO 22   |
    | DIO        | GPIO 21   |

    ---

    ### 🧪 Contoh Kode MicroPython

    ```python
    from machine import Pin
    import tm1637
    import time

    # Inisialisasi TM1637
    display = tm1637.TM1637(clk=Pin(22), dio=Pin(21))

    # Tampilkan angka
    display.numbers(12, 34)  # Menampilkan '12:34'

    # Tampilkan teks
    display.show('AbCd')     # Menampilkan 'AbCd'

    # Tampilkan angka heksadesimal
    display.hex(0x1A2B)      # Menampilkan '1A2B'

    # Tampilkan angka desimal
    display.number(1234)     # Menampilkan '1234'

    # Tampilkan suhu
    display.temperature(25)  # Menampilkan '25°C'
    ```

    **Catatan:**
    - Pastikan Anda telah mengunggah file `tm1637.py` ke ESP32 Anda. Anda dapat menemukan pustaka ini di [GitHub](https://github.com/mcauser/micropython-tm1637) atau menggunakan perintah `mpremote mip install github:mcauser/micropython-tm1637`.

    ---

    ### 💡 Tips Penggunaan
    - Gunakan `display.scroll("Pesan")` untuk menampilkan teks yang lebih panjang dengan efek scroll.
    - Gunakan `display.brightness(0-7)` untuk mengatur tingkat kecerahan display.
    - Modul ini ideal untuk menampilkan waktu, suhu, atau nilai sensor lainnya.

    ---

    ### 📌 Aplikasi TM1637
    - Jam digital
    - Stopwatch atau timer
    - Tampilan suhu atau kelembaban
    - Indikator status sistem

    ---

    ⏲️ *TM1637 adalah solusi hemat pin dan efisien untuk menampilkan informasi numerik pada proyek ESP32 Anda.*

    Untuk mencoba kode ini pada ESP32 Anda, silakan kunjungi halaman **Upload File ke ESP32**.
    """)
