import streamlit as st
import requests
import cv2
import numpy as np
import json
from inference_sdk import InferenceHTTPClient
from gtts import gTTS
import pygame
import os
import uuid

# Inisialisasi pygame untuk pemutaran suara diaktifkan hanya ketika untuk local 
# pygame.mixer.init()

def halaman_deteksi_sensor_dan_penjelasan():
    # st.set_page_config(page_title="Deteksi Sensor ESP32 + Gemini", layout="centered")
    st.title("🔍 Deteksi Sensor dari ESP32 dan Penjelasan Otomatis")

    with st.form("config_form"):
        esp32_ip = st.text_input("🌐 Alamat IP ESP32:", value="http://192.168.137.51:8080")
        api_key = st.text_input("🔐 API Key Gemini:", type="password")
        submitted = st.form_submit_button("🚀 Jalankan Deteksi dan Penjelasan")

    if submitted and api_key and esp32_ip:
        # Ambil gambar dari ESP32
        st.info("📷 Mengambil gambar dari ESP32...")
        resp = requests.get(esp32_ip)

        if resp.status_code != 200:
            st.error("❌ Gagal mengambil gambar dari ESP32.")
            return

        img_bytes = resp.content
        st.success("✅ Gambar berhasil diambil dari ESP32!")

        with open("esp32_cam.jpg", "wb") as f:
            f.write(img_bytes)

        # Kirim ke Roboflow
        st.info("🧠 Mengirim gambar ke Roboflow untuk deteksi objek...")
        client = InferenceHTTPClient(
            api_url="https://detect.roboflow.com",
            api_key="SVW2JOYR76zYVxQJ33nt"
        )

        result = client.run_workflow(
            workspace_name="cobza",
            workflow_id="custom-workflow",
            images={"image": "esp32_cam.jpg"},
            use_cache=True
        )

        results_list = result  
        predictions = results_list[0].get('predictions', {}).get('predictions', []) if results_list else []

        # Tampilkan gambar asli
        img_np = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), -1)
        st.image(img_np, caption="Gambar Asli dari ESP32", use_column_width=True)

        if not predictions:
            st.warning("🤷 Tidak ada objek yang terdeteksi.")
            return

        # Penjelasan menggunakan Gemini
        st.subheader("📚 Penjelasan Sensor yang Terdeteksi")
        headers = {"Content-Type": "application/json"}
        gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        for pred in predictions:
            class_name = pred.get('class', 'Unknown')
            prompt = f"Jelaskan secara singkat tentang sensor {class_name}. Apa definisinya, fungsinya, dan contoh penerapannya dalam kehidupan sehari-hari? JANGAN TAMBAHKAN TULISAN TEBAL ATAU SIMBOL BINTANG AGAR TIDAK TERBACA SAAT DI TEXT TO SPEECH"
            data = {"contents": [{"parts": [{"text": prompt}]}]}

            st.markdown(f"### 🔎 Sensor: {class_name}")
            gemini_resp = requests.post(gemini_url, headers=headers, data=json.dumps(data))

            if gemini_resp.status_code == 200:
                gemini_result = gemini_resp.json()
                explanation = gemini_result["candidates"][0]["content"]["parts"][0]["text"]
                st.write(explanation)

                # TTS
                tts_text = f"Penjelasan tentang sensor {class_name}. {explanation}"
                tts = gTTS(text=tts_text, lang='id')
                audio_file = f"tts_{uuid.uuid4()}.mp3"
                tts.save(audio_file)

                # Hapus Komentar untuk Memutar audio dengan pygame ketika local run webnya
                # pygame.mixer.music.load(audio_file)
                # pygame.mixer.music.play()
                # while pygame.mixer.music.get_busy():
                #     pygame.time.Clock().tick(10)

                os.remove(audio_file)
            else:
                st.error(f"❌ Gagal mendapatkan penjelasan dari Gemini untuk {class_name}")
    elif submitted:
        st.warning("⚠️ Mohon masukkan IP ESP32 dan API Key Gemini.")
