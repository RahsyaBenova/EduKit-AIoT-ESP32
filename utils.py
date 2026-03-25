import subprocess

PORT = "COM5"  # Ganti dengan port kamu, misalnya COM3/COM5

def read_esp32_file(file_path: str) -> str:
    try:
        result = subprocess.run(
            ["mpremote", "connect", PORT, "fs", "cat", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def write_esp32_file(file_path: str, content: str) -> str:
    try:
        with open("temp_upload.py", "w", encoding="utf-8") as f:
            f.write(content)

        result = subprocess.run(
            ["mpremote", "connect", PORT, "fs", "cp", "temp_upload.py", f":{file_path}"],
            capture_output=True,
            text=True
        )
        return "✅ Sukses upload ke ESP32" if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
