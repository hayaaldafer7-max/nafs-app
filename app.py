import streamlit as st
import pdfplumber

st.set_page_config(page_title="منصة أسئلة نافس التفاعلية", page_icon="📚", layout="centered")

st.title("📚 منصة أسئلة اختبارات نافس التفاعلية")
st.write("أهلاً بكِ أستاذة هياء. قومي برفع ملف الـ PDF الخاص باختبار نافس لتحويله إلى اختبار تفاعلي للطلاب.")

uploaded_file = st.file_uploader("اختر ملف اختبار نافس (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("تم رفع الملف بنجاح! جاري قراءة الأسئلة...")
    with pdfplumber.open(uploaded_file) as pdf:
        total_pages = len(pdf.pages)
        st.info(f"عدد صفحات المستند: {total_pages}")
        
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
                
        if full_text.strip():
            st.write("### معاينة نص الأسئلة المستخرجة:")
            st.text_area("النص:", full_text[:1000] + "...", height=200)
        else:
            st.warning("لم يتم العثور على نصوص واضحة داخل الملف.")

