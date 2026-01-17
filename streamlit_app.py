import streamlit as st
from fpdf import FPDF
import io

# Sayfa Ayarları
st.set_page_config(page_title="Verimlilik Laboratuvarı", page_icon="🚀")

st.title("🤖 Verimlilik & Analiz Merkezi")
st.write("Dostum hoş geldin! Sesini veya el yazısı notunu yükle, PDF'ini al.")

# 1. Dosya Yükleme Alanı
uploaded_file = st.file_uploader("Dosya Seç (Ses veya Resim)", type=['png', 'jpg', 'jpeg', 'mp3', 'wav'])

if uploaded_file is not None:
    st.success("Dosya başarıyla yüklendi dostum! Analiz başlıyor...")
    
    # Burada normalde OpenAI/Whisper çalışır ama şu an arayüzü kuruyoruz
    text_result = "Analiz Edilen Not: Dostum bu bir test çıktısıdır. Sistem tıkır tıkır çalışıyor! 😆"
    
    st.text_area("Analiz Sonucu:", text_result, height=150)

    # 2. PDF Oluşturma Butonu
    if st.button("PDF Olarak İndir ✨"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="YZ Verimlilik Raporu", ln=1, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=text_result)
        
        # PDF'i belleğe yazma
        pdf_output = pdf.output(dest='S').encode('latin-1')
        st.download_button(label="📥 Dosyayı Kaydet", data=pdf_output, file_name="analiz_raporu.pdf", mime="application/pdf")

st.info("Dış Açıortay Metaforu ile güçlendirilmiştir. 👋")
