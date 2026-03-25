# contoh kode yang diupload via streamlit
import machine
import network
import ujson
import urequests
import time
import dht

# WiFi Credentials
SSID = "OrangGantengPekanbaru"
PASSWORD = "12345678"

# Ubidots API Configuration
UBIDOTS_API_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/piresp32"
API_TOKEN = "BBUS-kwzj88JMWqOV9H76HlKno1KsdvVBNH"

# Hardware Setup
led = machine.Pin(4, machine.Pin.OUT)
buzzer = machine.Pin(18, machine.Pin.OUT)
dht_sensor = dht.DHT11(machine.Pin(23))

# Connect ke WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    print("Menghubungkan ke WiFi...")
    while not wlan.isconnected():
        pass
    print("Terhubung! IP:", wlan.ifconfig()[0])

# Baca data DHT11
def read_dht11():
    try:
        dht_sensor.measure()
        suhu = dht_sensor.temperature()
        kelembapan = dht_sensor.humidity()
        return suhu, kelembapan
    except Exception as e:
        print("Gagal membaca DHT11:", e)
        return None, None

# Kirim data ke Ubidots
def kirim_ke_ubidots(pir, suhu, hum):
    payload = {
        "temperature": {"value": suhu},
        "humidity": {"value": hum}
    }
    headers = {
        "X-Auth-Token": API_TOKEN,
        "Content-Type": "application/json"
    }
    try:
        response = urequests.post(UBIDOTS_API_URL, json=payload, headers=headers)
        print("Data terkirim ke Ubidots! Status:", response.status_code)
        response.close()
    except Exception as e:
        print("Gagal mengirim data ke Ubidots:", e)

# ===================
# MAIN PROGRAM
# ===================

connect_wifi()

while True:
    pir_value = pir_sensor.value()
    suhu, hum = read_dht11()

    if suhu is not None and hum is not None:
        print("Suhu:", suhu, "°C | Kelembapan:", hum, "% | PIR:", pir_value)
        kirim_ke_ubidots(pir_value, suhu, hum)
    
    time.sleep(2)
