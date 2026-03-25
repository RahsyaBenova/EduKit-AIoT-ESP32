import streamlit as st

def halaman_ds18s20():
    st.title("🌡️ Sensor Suhu DS18S20 dengan ESP32")

    st.image("assets/ds18s20.png", caption="Sensor DS18S20", use_container_width=True)

    st.markdown("""
    **Apa itu DS18S20?**

    DS18S20 adalah sensor suhu **digital** yang menggunakan **protokol komunikasi 1-Wire**, sehingga hanya memerlukan satu pin data untuk komunikasi. Sensor ini sangat cocok untuk sistem monitoring suhu pada **ruangan, akuarium, lemari pendingin**, hingga sistem **IoT**.

    ---

    ### 📊 Spesifikasi Sensor

    | Spesifikasi           | Keterangan                         |
    |-----------------------|-------------------------------------|
    | Tegangan Operasi      | 3V - 5.5V                          |
    | Rentang Suhu          | -55°C hingga +125°C               |
    | Akurasi               | ±0.5°C (antara -10°C s.d. +85°C)  |
    | Resolusi Data         | 9-bit                             |
    | Protokol Komunikasi   | 1-Wire                            |
    | Tipe Output           | Digital                           |
    | Waktu Konversi        | 750 ms                            |

    ---

    ### 🔌 Wiring ke ESP32

    - **Pin 1 (GND)**: ke GND ESP32
    - **Pin 2 (DATA)**: ke **GPIO 4**, **resistor 10K**, lalu ke **3.3V**
    - **Pin 3 (VCC)**: ke 3.3V ESP32

    > 📌 **Catatan**: Resistor 10K antara data dan VCC diperlukan sebagai **pull-up resistor** untuk stabilitas sinyal.

    ---

    ### 💻 Contoh Kode MicroPython

    ```python
    import machine, onewire, ds18x20, time

    # Inisialisasi OneWire dan DS18B20
    ow = onewire.OneWire(machine.Pin(4))
    ds = ds18x20.DS18X20(ow)

    roms = ds.scan()  # Scan sensor yang terhubung
    print("Sensor DS18B20 ditemukan:", roms)

    while True:
        ds.convert_temp()       # Mulai konversi suhu
        time.sleep_ms(750)      # Tunggu konversi selesai

        for rom in roms:
            print("Suhu:", ds.read_temp(rom), "°C")

        time.sleep(2)           # Ambil data suhu setiap 2 detik
    ```

    ---

    ### 📝 Penjelasan Kode:
    - `onewire.OneWire()` dan `ds18x20.DS18X20()` adalah library MicroPython untuk membaca sensor.
    - `scan()` mendeteksi sensor DS18S20 yang terhubung.
    - `convert_temp()` memulai proses pengukuran suhu.
    - `read_temp(rom)` membaca hasil suhu dalam derajat Celsius.
    - Sensor dapat **daisy-chain** beberapa unit dalam satu jalur data.

    ---

    ✅ *DS18S20 memberikan solusi pengukuran suhu yang presisi, efisien, dan mudah diintegrasikan dengan ESP32!*
    """)
