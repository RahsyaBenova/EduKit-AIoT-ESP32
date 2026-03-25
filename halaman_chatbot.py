import streamlit as st
import google.generativeai as genai

def halaman_chatbot():
    st.title("🤖 Chatbot Kode ESP32 dengan Gemini")
    st.markdown("Gunakan model **Gemini 2.5 Flash** untuk membuat atau menjelaskan kode ESP32 (MicroPython).")

    # Input API Key
    api_key = st.text_input("🔐 Masukkan API Key Gemini Anda:", type="password")

    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")

            # Input Prompt
            default_prompt = "Make a complete code of example turning on a LED using ESP32 with MicroPython code, just write as a text, without ```python"
            prompt = st.text_area("💬 Masukkan prompt untuk chatbot:", value=default_prompt, height=150)

            if st.button("🚀 Generate Kode"):
                with st.spinner("Sedang menghubungi Gemini..."):
                    response = model.generate_content(prompt)
                    st.subheader("📄 Kode yang Dihasilkan:")
                    st.code(response.text, language='python')
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
    else:
        st.warning("Masukkan API Key terlebih dahulu untuk mulai menggunakan chatbot.")
