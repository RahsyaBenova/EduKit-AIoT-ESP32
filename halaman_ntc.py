import streamlit as st

def halaman_ntc():
    st.title("🌡️ Sensor Suhu NTC dengan ESP32")

    st.image("assets/ntc.png", caption="Penggunaan NTC dan Contoh Program", use_container_width=True)

    st.markdown("""
    **Apa itu NTC?**

    NTC (**Negative Temperature Coefficient**) adalah jenis **termistor** (resistor peka suhu) yang resistansinya **menurun** saat suhu meningkat. Sensor ini banyak digunakan untuk:
    - Pengukuran suhu
    - Proteksi rangkaian elektronik
    - Pengontrolan suhu dalam sistem tertanam

    ---

    ### ⚙️ **Wiring dengan ESP32**
    - Satu pin NTC dihubungkan ke **3.3V ESP32**
    - Pin NTC lainnya dihubungkan dengan resistor 10K, kemudian ke **GND**
    - Titik tengah (antara NTC dan resistor) dihubungkan ke pin **GPIO 34 ESP32 (ADC)**

    ---

    ### 💻 **Contoh Program MicroPython**
    Berikut adalah contoh program untuk membaca suhu dari NTC menggunakan ESP32:

    ```python
    from machine import Pin, ADC
    from time import sleep
    import math

    NTC = ADC(Pin(34))        # NTC terhubung ke GPIO 34
    NTC.atten(ADC.ATTN_11DB)  # Rentang pembacaan hingga 3.3V

    led = Pin(2, Pin.OUT)     # LED indikator di GPIO 2

    # Konstanta NTC (bisa berbeda tergantung spesifikasi)
    BETA = 3950               # B constant dari datasheet NTC
    R0 = 10000                # Resistor Pull-Down 10K
    T0 = 298.15               # Suhu referensi (25°C dalam Kelvin)

    while True:
        V = NTC.read() / 4095 * 3.3
        R = R0 * (3.3 / V - 1)
        suhu = 1 / (1 / T0 + (1 / BETA) * math.log(R / R0)) - 273.15

        print("Suhu: {:.2f} °C".format(suhu))

        if suhu > 30:
            led.on()   # LED nyala jika suhu > 30°C
        else:
            led.off()  # LED mati

        sleep(2)
    ```

    ---

    ### 📝 Penjelasan Kode:
    - `NTC.read()` membaca tegangan analog.
    - Menggunakan **persamaan Steinhart-Hart** untuk konversi ke suhu.
    - LED akan menyala jika suhu melebihi 30°C sebagai indikator.

    ---

    ### 💡 Tips:
    - Gunakan NTC sesuai datasheet untuk hasil akurat.
    - Bisa disesuaikan nilai resistor pull-down (umumnya 10K).
    - Tambahkan filtering (moving average) jika data terbaca tidak stabil.

    ---

    🔍 *Sensor NTC sangat berguna dalam sistem kendali suhu atau monitoring lingkungan menggunakan ESP32!*
    """)

