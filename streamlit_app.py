import streamlit as st
from fpdf import FPDF

def main():
    st.set_page_config(page_title="Polinom Analiz Merkezi", page_icon="📈")
    
    st.title("📈 Polinom Analiz ve Türev Merkezi")
    
    # --- YENİ MENÜLER ---
    st.subheader("📸 Girdi Seçenekleri")
    picture = st.camera_input("Soru Fotoğrafı Çek")
    audio_data = st.audio_input("Soruyu Sesli Anlat")
    
    st.divider()

    # --- HESAPLAMA BÖLÜMÜ ---
    st.subheader("✍️ Polinom Girişi")
    polinom_input = st.text_input("Polinomu yazın (Örn: 3x^2 + 2x + 5):", "2x^2 + 3x + 1")

    if st.button("Türev Al ve Analiz Et"):
        st.success(f"Girdi: {polinom_input}")
        st.info("Türev Sonucu: (Örnek Hesaplama) 4x + 3")
        
        # PDF OLUŞTURMA
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Polinom Analiz Raporu", ln=1, align='C')
        pdf.cell(200, 10, txt=f"Girdi: {polinom_input}", ln=2, align='L')
        pdf.cell(200, 10, txt="Turev: 4x + 3", ln=3, align='L')

        # HATASIZ PDF ÇIKTISI (encode silindi!)
        pdf_output = pdf.output(dest='S')
        
        st.download_button(
            label="📥 PDF Raporu İndir",
            data=pdf_output,
            file_name="analiz_raporu.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()


