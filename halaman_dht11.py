import streamlit as st

def halaman_dht11():
    st.title("📊 Data Sensor DHT11 di ESP32")

    # Menambahkan gambar ilustrasi DHT11 dan ESP32
    st.image("https://kspelectronics-wordpress.s3.ap-south-2.amazonaws.com/wp-content/uploads/2023/12/10215130/20190601_125006_525x700_23a76fe5-0453-429c-a89f-cdd05e163ce9_500x.webp", caption="Sensor DHT11", use_container_width=True)

    st.markdown("""
    **Apa itu Sensor DHT11?**

    DHT11 adalah sensor yang digunakan untuk mengukur **suhu** dan **kelembaban** udara. Sensor ini sering digunakan dalam berbagai proyek elektronika, seperti di **ESP32**, untuk mengukur kondisi lingkungan sekitar.

    Sensor DHT11 memiliki beberapa kelebihan:
    - **Harga Terjangkau**: Salah satu sensor suhu dan kelembaban yang paling murah.
    - **Mudah Digunakan**: DHT11 dapat dengan mudah dihubungkan ke mikrokontroler seperti ESP32.
    - **Akurasi Terbatas**: DHT11 memiliki akurasi terbatas, tetapi cukup untuk banyak aplikasi dasar.

    ---
    
    ### **Cara kerja Sensor DHT11 di ESP32**

    Sensor DHT11 mengirimkan data suhu dan kelembaban melalui **sinya digital**. Untuk mengakses data ini di ESP32, kita dapat menggunakan **GPIO** dan kode MicroPython sebagai berikut:

    ```python
    from machine import Pin
    import dht
    import time

    # Inisialisasi sensor DHT11
    sensor = dht.DHT11(Pin(15))  # Menggunakan GPIO 15 untuk DHT11

    while True:
        try:
            sensor.measure()  # Mengambil data
            suhu = sensor.temperature()  # Mengambil suhu dalam Celcius
            kelembaban = sensor.humidity()  # Mengambil kelembaban

            print('Suhu: {} C'.format(suhu))
            print('Kelembaban: {}%'.format(kelembaban))
            
            time.sleep(2)  # Menunggu 2 detik sebelum mengambil data lagi
        except Exception as e:
            print('Error:', e)
    ```

    Penjelasan kode di atas:
    - **Pin(15)** digunakan untuk menghubungkan DHT11 ke ESP32.
    - `sensor.measure()` digunakan untuk mengaktifkan sensor dan mengambil data suhu dan kelembaban.
    - `sensor.temperature()` dan `sensor.humidity()` digunakan untuk membaca suhu dan kelembaban.

    ---
    
    **Catatan Penting:**
    - Pastikan **kabel dan pin** terhubung dengan benar ke **GPIO ESP32**.
    - Sensor DHT11 memiliki **waktu respon yang cukup lama**, jadi pastikan untuk memberikan waktu antar pembacaan.
    - Gunakan **resistor pull-up** untuk memastikan pembacaan data yang lebih akurat.

    ---
    
    **Kenapa DHT11 penting di ESP32?**

    Dengan sensor DHT11, kita dapat memonitor suhu dan kelembaban secara real-time. Ini berguna dalam berbagai aplikasi, seperti:
    - **Monitoring suhu ruangan**: Untuk kontrol suhu otomatis di ruangan.
    - **Proyek Cuaca**: Memantau suhu dan kelembaban di luar ruangan.
    - **Pengendalian Lingkungan**: Untuk proyek-proyek seperti akuarium otomatis atau sistem irigasi yang membutuhkan pengukuran kelembaban.

    --- 

    **Peringatan:**
    - DHT11 tidak cocok untuk penggunaan yang sangat presisi karena akurasi terbatasnya.
    - Untuk aplikasi yang membutuhkan akurasi lebih tinggi, pertimbangkan untuk menggunakan sensor lain seperti **DHT22**.

    😊 Semoga penjelasan ini bermanfaat! Jika ingin mencoba untuk **meng-upload kode** ke ESP32, silakan lanjut ke halaman upload.

    """)
