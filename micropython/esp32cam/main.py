import network
import socket
import camera
import time

# Ganti dengan WiFi Anda
SSID = "test"
PASSWORD = "12345678"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to WiFi...")
    for _ in range(15):
        if wlan.isconnected():
            ip = wlan.ifconfig()[0]
            print("Connected to WiFi. IP Address:", ip)
            return ip
        time.sleep(1)

    print("Failed to connect to WiFi.")
    return None

def init_camera():
    try:
        camera.deinit()  # reset terlebih dahulu jika sebelumnya sudah aktif
    except:
        pass

    try:
        camera.init(0, format=camera.JPEG)
        camera.framesize(camera.FRAME_QVGA)  # 320x240 (QVGA)
        camera.quality(12)  # 10-63 (semakin rendah semakin bagus)
        print("Camera initialized successfully.")
    except Exception as e:
        print("Camera initialization failed:", e)

def start_http_server(ip):
    addr = (ip, 8080)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    print("Server started at http://{}:8080".format(ip))

    while True:
        try:
            conn, client_addr = s.accept()
            print("Client connected from:", client_addr)

            request = conn.recv(1024)  # Terima HTTP GET request
            print("Request:", request)

            if b"GET" in request:
                frame = camera.capture()
                if frame:
                    response = b"""HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: """ + str(len(frame)).encode() + b"""\r\n\r\n""" + frame
                    conn.sendall(response)
                    print("Image sent to client.")
                else:
                    conn.sendall(b"HTTP/1.1 500 Internal Server Error\r\n\r\nFailed to capture image.")
            conn.close()
        except Exception as e:
            print("Error handling request:", e)
            try:
                conn.close()
            except:
                pass

# Main Execution
ip = connect_wifi()
if ip:
    init_camera()
    start_http_server(ip)
else:
    print("WiFi connection failed. Cannot start server.")

