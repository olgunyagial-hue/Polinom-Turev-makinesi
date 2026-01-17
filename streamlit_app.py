import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Verimlilik & Analiz Merkezi", page_icon="🚀")
st.title("🚀 Verimlilik & Analiz Merkezi")

# Analiz Girişi
text_input = st.text_area("Analiz Metnini Girin:", "Her sey yolunda dostum! Sistem calisiyor.")

if st.button("Analizi PDF Yap"):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Turkce karakterleri PDF'in anlayacagi dile ceviren minik bir temizlik
        safe_text = text_input.replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')
        safe_text = safe_text.replace('İ','I').replace('Ğ','G').replace('Ü','U').replace('Ş','S').replace('Ö','O').replace('Ç','C')
        
        pdf.multi_cell(0, 10, txt=safe_text)
        
        pdf_output = pdf.output(dest='S').encode('latin-1')
        st.download_button(label="📥 PDF'i Indir", data=pdf_output, file_name="analiz.pdf", mime="application/pdf")
        st.success("PDF Hazir! 😆")
    except Exception as e:
        st.error(f"Hata olustu: {e}")

st.divider()
st.write("Dostum bu sistem artik hata vermez! 👋")

