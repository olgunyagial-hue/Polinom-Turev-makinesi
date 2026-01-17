import streamlit as st
from fpdf import FPDF
from PIL import Image
import io

st.set_page_config(page_title="Elle Yazı -> PDF", page_icon="📝")

# Claude'un stilini Streamlit'e uygulayalım
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .stButton>button { width: 100%; border-radius: 15px; height: 3em; background-color: #8b5cf6; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Elle Yazı → PDF Dönüştürücü")
st.write("Notlarınızı fotoğraflayın, profesyonel PDF yapın!")

# Claude'un istediği girişler
uploaded_files = st.file_uploader("📸 Fotoğraf Çek veya Galeriden Seç", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if uploaded_files:
    st.subheader(f"✅ {len(uploaded_files)} Sayfa Eklendi")
    
    if st.button("📥 PDF OLUŞTUR VE İNDİR"):
        pdf = FPDF()
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            # PDF formatına uygun hale getir
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            
            pdf.add_page()
            # Resmi sayfaya tam oturt
            pdf.image(img_byte_arr, 0, 0, 210, 297) 
        
        pdf_output = pdf.output(dest='S')
        st.download_button(label="🚀 PDF Hazır! Buraya Tıkla İndir", data=pdf_output, file_name="notlarim.pdf", mime="application/pdf")

st.info("Dostum, Claude'un tasarımını Python motoruna bağladım. Şimdi tıkır tıkır çalışacak! 😆")



