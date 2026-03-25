from machine import Pin, SoftI2C
import ssd1306
import time
import network
import socket
import os
import gc

# OLED setup
oled_width = 128
oled_height = 64
scl = Pin(22, Pin.OUT, Pin.PULL_UP)
sda = Pin(21, Pin.OUT, Pin.PULL_UP)
i2c = SoftI2C(scl=scl, sda=sda, freq=400000)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text("Hello, Troynics!", 0, 0)
oled.text("MicroPython-ESP32", 0, 16)
oled.text("OLED Test", 0, 32)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

# WiFi config
SSID = 'test'
PASSWORD = '12345678'

def show_ip_on_oled(ip):
    oled.fill(0)
    oled.text("WiFi Terkoneksi", 0, 0)
    oled.text("IP Address:", 0, 16)
    oled.text(ip, 0, 32)
    oled.show()

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('🔌 Menghubungkan ke WiFi...')
        oled.text("Menghubungkan...", 0, 48)
        oled.show()
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(0.1)
    ip = wlan.ifconfig()[0]
    print('📶 Terkoneksi! IP:', ip)
    show_ip_on_oled(ip)

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('🌐 Web server berjalan di port 8080')

    while True:
        cl, addr = s.accept()
        print('📥 Koneksi dari', addr)
        try:
            cl_file = cl.makefile('rwb', 0)
            request_line = cl_file.readline()
            print("➡️", request_line)

            if b'POST /upload' in request_line:
                # Skip headers
                while True:
                    line = cl_file.readline()
                    if line == b'\r\n' or line == b'':
                        break

                # Terima body
                body = b''
                while True:
                    chunk = cl.recv(1024)
                    if not chunk:
                        break
                    body += chunk

                # Simpan file
                with open("uploaded.py", "w") as f:
                    f.write(body.decode("utf-8"))
                print("✅ File berhasil disimpan")

                # OLED update
                oled.fill(0)
                oled.text("Upload sukses!", 0, 0)
                oled.text("Menjalankan...", 0, 16)
                oled.show()

                # Jalankan uploaded.py
                try:
                    import uploaded
                    import sys
                    if 'uploaded' in sys.modules:
                        del sys.modules['uploaded']
                    import uploaded
                    cl.send(b'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\nUpload dan eksekusi berhasil!')
                    oled.text("✅ Sukses!", 0, 40)
                    oled.show()
                except Exception as e:
                    cl.send(b'HTTP/1.0 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nGagal menjalankan file.\n')
                    cl.send(str(e).encode())
                    oled.text("❌ Gagal run!", 0, 40)
                    oled.show()

            else:
                cl.send(b'HTTP/1.0 404 Not Found\r\n\r\n')
        except Exception as e:
            print('❌ Error:', e)
        finally:
            cl.close()
            gc.collect()

# Run program
connect_wifi(SSID, PASSWORD)
start_server()