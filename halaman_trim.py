import streamlit as st

def halaman_trim():
    st.title("🎚️ Penjelasan Potensiometer Trim dengan ESP32")

    st.image("https://images.tokopedia.net/img/cache/250-square/product-1/2016/7/21/679813/679813_2b8360f7-ca35-457e-81d2-354fff452dc6.jpg", caption="Koneksi Potensiometer ke ESP32", use_container_width=True)

    st.markdown("""
    **Apa itu Potensiometer Trim?**

    Potensiometer trim, atau trimpot, adalah resistor variabel kecil yang digunakan untuk menyesuaikan dan mengkalibrasi sirkuit elektronik. Dengan memutar sekrup kecil pada trimpot, Anda dapat mengubah resistansi, yang pada gilirannya mengubah tegangan outputnya. Ini sangat berguna dalam proyek-proyek yang memerlukan penyesuaian presisi, seperti pengaturan sensitivitas sensor atau kalibrasi tegangan referensi.

    ---

    ### 🧰 Komponen yang Diperlukan
    - ESP32
    - Potensiometer trim (misalnya 10 kΩ)
    - Breadboard & Kabel Jumper

    ---

    ### 🔌 Koneksi Potensiometer Trim ke ESP32

    Potensiometer trim memiliki tiga pin:
    - **VCC**: Terhubung ke 3.3V pada ESP32
    - **GND**: Terhubung ke GND pada ESP32
    - **Output**: Terhubung ke pin ADC pada ESP32 (misalnya GPIO36)

    Konfigurasi ini membentuk pembagi tegangan, di mana tegangan pada pin output akan bervariasi tergantung pada posisi trimpot.

    ---

    ### 🧪 Contoh Kode MicroPython

    ```python
    from machine import ADC, Pin
    import time

    # Inisialisasi ADC pada GPIO36
    pot = ADC(Pin(36))
    pot.atten(ADC.ATTN_11DB)  # Rentang input hingga ~3.3V
    pot.width(ADC.WIDTH_12BIT)  # Resolusi 12-bit (0-4095)

    while True:
        nilai = pot.read()
        print("Nilai ADC:", nilai)
        time.sleep(1)
    ```

    **Penjelasan:**
    - `ADC.ATTN_11DB`: Mengatur attenuasi untuk memungkinkan pembacaan tegangan hingga ~3.3V.
    - `ADC.WIDTH_12BIT`: Mengatur resolusi ADC menjadi 12-bit, menghasilkan nilai antara 0 hingga 4095.
    - `pot.read()`: Membaca nilai tegangan analog yang dikonversi menjadi nilai digital.

    ---

    ### 💡 Tips Penggunaan
    - Gunakan trimpot untuk mengatur ambang batas sensor, seperti sensitivitas LDR atau sensor suhu.
    - Trimpot dapat digunakan untuk mengkalibrasi tegangan referensi dalam sirkuit analog.
    - Pastikan untuk menggunakan trimpot dengan nilai resistansi yang sesuai dengan kebutuhan sirkuit Anda.

    ---

    🔧 *Potensiometer trim adalah komponen kecil namun sangat berguna untuk penyesuaian presisi dalam proyek ESP32 Anda.*

    Untuk mencoba kode ini pada ESP32 Anda, silakan kunjungi halaman **Upload File ke ESP32**.
    """)
