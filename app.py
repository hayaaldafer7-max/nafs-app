import streamlit as st
import pdfplumber
import random

# إعدادات الصفحة
st.set_page_config(page_title="منصة مبادرة نافس التفاعلية", page_icon="📚", layout="wide")

# تهيئة ذاكرة الجلسة
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'scores' not in st.session_state:
    st.session_state.scores = {}

# العبارات التحفيزية
praise_messages = [
    "أحسنتِ يا بطلة! إجابة صحيحة ومتميزة 🌟",
    "رائعة جداً! استمري في هذا التفوق 👏",
    "إجابة دقيقة ودليل على فهمك المتميز! ✨",
    "عظيم جداً! ذكاء وتركيز عالٍ 🎯"
]

encouraging_messages = [
    "محاولة جيدة! ركزي أكثر في السؤال القادم 💪",
    "لا بأس، التعلم يأتي من المحاولة والتكرار 📖",
    "اقرئي السؤال بتمعن أكثر في المرة القادمة 💡",
    "استمري في المحاولة، أنتِ قادرة على التميز! 🌈"
]

# ترويسة المنصة والمعلومات الرسمية
st.title("📚 منصة مبادرة نافس التفاعلية")
st.caption("مبادرة تعليمية لإعداد وتأهيل الطالبات لاختبارات نافس الوطنية بنجاح وتميز")

st.info("""
🏫 **بيانات المبادرة والاعتماد:**
* **المبادرة مقدمة لـ:** المدرسة الابتدائية الأولى بالخالدية  
* **الجهة المنفذة / المدرسة:** ثانويه البديع  
* **إعداد وتنفيذ الأستاذة:** هياء مسفر آل ظافر  
""")

st.divider()

# عن المبادرة
with st.expander("✨ عن المبادرة وأهدافها (ماذا تستفيد الطالبة؟)", expanded=False):
    col_about1, col_about2 = st.columns(2)
    with col_about1:
        st.markdown("### 🎯 هدف المبادرة")
        st.write("تحويل النماذج الورقية لاختبارات 'نافس' إلى بيئة رقمية تفاعلية تمكن الطالبات من قياس الأداء وتنمية مهارات التفكير العليا.")
    with col_about2:
        st.markdown("### 💡 فوائد المنصة للطالبة")
        st.markdown("- التهيؤ النفسي والمعرفي للاختبارات الوطنية[span_7](start_span)[span_7](end_span).\n- التقييم الفوري مع عبارات تحفيزية.\n- متابعة مستمرة للتقدم.")

st.divider()

# الشريط الجانبي
with st.sidebar:
    st.header("👤 بيانات الطالبة")
    student_name = st.text_input("ادخلي اسم الطالبة الثلاثي:", value=st.session_state.student_name)
    if student_name:
        st.session_state.student_name = student_name
        st.success(f"مرحباً بكِ: {student_name} ✨")
    
    st.divider()
    st.header("👩‍🏫 لوحة متابعة المعلمة")
    if st.session_state.scores:
        for name, score_info in st.session_state.scores.items():
            st.metric(label=f"الطالبة: {name}", value=f"{score_info['score']} / {score_info['total']}", delta=f"{score_info['percentage']}%")
    else:
        st.info("لم يتم تسجيل نتائج بعد.")

# رفع الملف
uploaded_file = st.file_uploader("اختر ملف اختبار نافس (PDF)", type=["pdf"])

if uploaded_file is not None:
    if not st.session_state.student_name:
        st.warning("⚠️ يُرجى كتابة اسم الطالبة في القائمة الجانبية قبل البدء بالإجابة.")
    
    with pdfplumber.open(uploaded_file) as pdf:
        total_pages = len(pdf.pages)

    st.subheader("📊 تحليل ملف الاختبار")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("إجمالي صفحات المستند", f"{total_pages} صفحات")
    with col2:
        st.metric("حالة النظام", "جاهز للاختبار التفاعلي ✅")

    st.divider()
    st.subheader("📝 أسئلة اختبار نافس الحقيقية (الصف السادس - رياضيات)")

    # الأسئلة المستخرجة مباشرة من ملف نافس المرفق
    nafs_questions = [
        {
            "id": 1,
            "category": "الكسور الاعتيادية والأعداد الكسرية",
            "question": "ما مجموع الطلاب الذين اجتازوا مادتي الرياضيات والعلوم إذا كان مجموع طلاب الصف السادس اجتازوا الاختبار بنجاح؟[span_8](start_span)[span_8](end_span)",
            "options": ["19 من 10", "7 من 10", "4 من 10", "1 من 70"],
            "answer": "19 من 10"
        },
        {
            "id": 2,
            "category": "الحجم والمساحة السطحية",
            "question": "حجم المنشور الرباعي الذي طوله 8 م، وعرضه 8 م، وارتفاعه 5 م بالمتر المكعب يساوي:[span_9](start_span)[span_9](end_span)",
            "options": ["64", "80", "240", "320"],
            "answer": "320"
        },
        {
            "id": 3,
            "category": "العوامل والمضاعفات",
            "question": "أي من الأعداد الآتية هو القاسم المشترك الأكبر بين العددين 24 و 36؟[span_10](start_span)[span_10](end_span)",
            "options": ["2", "6", "12", "24"],
            "answer": "12"
        },
        {
            "id": 4,
            "category": "المستوى الإحداثي",
            "question": "حدد سعد نقطة على بعد 5 وحدات يمين نقطة الأصل، و3 وحدات أعلى نقطة الأصل، لذا يكون إحداثي النقطة هو:[span_11](start_span)[span_11](end_span)",
            "options": ["(3, 4)", "(5, 3)", "(3, 5)", "(2, 5)"],
            "answer": "(5, 3)"
        }
    ]

    user_answers = {}
    
    with st.form("nafs_actual_quiz"):
        for q in nafs_questions:
            st.markdown(f"**سؤال ({q['id']}) - [{q['category']}]:** {q['question']}")
            user_answers[q['id']] = st.radio(
                "اختر الإجابة الصحيحة:", 
                q['options'], 
                key=f"q_{q['id']}"
            )
            st.divider()
            
        submit_btn = st.form_submit_button("إرسال الإجابات والتقييم 🚀")

    if submit_btn:
        if not st.session_state.student_name:
            st.error("يرجى إدخال اسم الطالبة في القائمة الجانبية أولاً!")
        else:
            correct_count = 0
            total_q = len(nafs_questions)
            
            st.subheader("🏁 نتيجة التقييم والتحفيز")
            
            for q in nafs_questions:
                ans = user_answers[q['id']]
                if ans == q['answer']:
                    correct_count += 1
                    st.success(f"السؤال {q['id']}: إجابة صحيحة! ({ans}) — {random.choice(praise_messages)}")
                else:
                    st.error(f"السؤال {q['id']}: إجابة تحتاج مراجعة. إجابتك: ({ans}) | الإجابة الصحيحة: ({q['answer']}) — {random.choice(encouraging_messages)}")

            percentage = round((correct_count / total_q) * 100, 1)
            
            st.session_state.scores[st.session_state.student_name] = {
                "score": correct_count,
                "total": total_q,
                "percentage": percentage
            }
            
            st.balloons()
            st.info(f"✨ النتيجة النهائية للطالبة ({st.session_state.student_name}): {correct_count} من {total_q} (النسبة: {percentage}%)")
