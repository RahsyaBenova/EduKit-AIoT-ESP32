import streamlit as st
import requests

def halaman_upload_file():
    st.title("📤 Upload File Python ke ESP32 (MicroPython)")

    # Input IP Address ESP32
    esp_ip = st.text_input("🔌 Masukkan IP Address ESP32", placeholder="Contoh: 192.168.1.100")

    # Fungsi untuk mengecek IP ESP32
    def get_esp_ip():
        try:
            response = requests.get(f"http://{esp_ip}:8080/getip", timeout=5)
            if response.status_code == 200:
                return f"📡 IP dari ESP32: `{response.text}`"
            else:
                return f"⚠️ Gagal mendapatkan IP. Status Code: {response.status_code}"
        except requests.exceptions.ConnectionError:
            return "❌ Gagal terhubung ke ESP32."
        except Exception as e:
            return f"❌ Terjadi error: {e}"

    if st.button("🔍 Cek Koneksi & IP dari ESP32"):
        if esp_ip:
            ip_response = get_esp_ip()
            st.info(ip_response)
        else:
            st.warning("⚠️ Masukkan IP ESP32 terlebih dahulu.")

    st.markdown("---")

    # Kolom untuk meng-upload file Python
    uploaded_file = st.file_uploader("📄 Pilih file Python (.py)", type=["py"])

    # Kolom untuk menulis atau mengedit kode langsung
    st.subheader("✏️ Edit Kode Python Secara Langsung:")
    direct_code = st.text_area("Tuliskan kode Python di sini:", height=300, placeholder="Contoh kode Python...")

    if uploaded_file:
        try:
            file_content = uploaded_file.read().decode("utf-8")
            filename = uploaded_file.name

            st.markdown(f"📝 Edit isi file: `{filename}`")
            edited_content = st.text_area("Edit sebelum upload", value=file_content, height=300)

            if st.button("🚀 Upload dan Jalankan ke ESP32 (Dari File)"):
                try:
                    upload_response = requests.post(
                        f"http://{esp_ip}:8080/upload",
                        data=edited_content,
                        headers={"Content-Type": "text/plain"},
                        timeout=5
                    )

                    if upload_response.status_code == 200:
                        st.success("✅ File berhasil diupload ke ESP32!")
                        st.code(upload_response.text, language="text")
                    else:
                        st.error(f"⚠️ Upload gagal. Status Code: {upload_response.status_code}")
                        st.text(upload_response.text)

                except requests.exceptions.ConnectionError:
                    st.error("❌ Tidak bisa terhubung ke ESP32.")
                except requests.exceptions.Timeout:
                    st.error("⌛ Timeout dari ESP32.")
                except Exception as e:
                    st.error(f"❌ Terjadi error: {e}")

        except Exception as e:
            st.error(f"❌ Gagal membaca file: {e}")

    # Jika tidak ada file yang di-upload, user bisa mengedit kode langsung
    if direct_code:
        if st.button("🚀 Upload dan Jalankan ke ESP32 (Dari Editor)"):
            try:
                upload_response = requests.post(
                    f"http://{esp_ip}:8080/upload",
                    data=direct_code,
                    headers={"Content-Type": "text/plain"},
                    timeout=5
                )

                if upload_response.status_code == 200:
                    st.success("✅ Kode berhasil diupload dan dijalankan di ESP32!")
                    st.code(upload_response.text, language="text")
                else:
                    st.error(f"⚠️ Upload gagal. Status Code: {upload_response.status_code}")
                    st.text(upload_response.text)

            except requests.exceptions.ConnectionError:
                st.error("")
            except requests.exceptions.Timeout:
                st.error("")
            except Exception as e:
                st.error(f"")
