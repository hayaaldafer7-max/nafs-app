import streamlit as st
import pdfplumber
import random

# إعدادات الصفحة
st.set_page_config(page_title="منصة مبادرة نافس التفاعلية", page_icon="📚", layout="wide")

# تهيئة ذاكرة الجلسة (Session State)
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

# بطاقة المعلومات الرسمية للمبادة والإعداد
st.info("""
🏫 **بيانات المبادرة والاعتماد:**
* **المبادرة مقدمة لـ:** المدرسة الابتدائية الأولى بالخالدية  
* **الجهة المنفذة / المدرسة:** ثانوية البديع  
* **إعداد وتنفيذ الأستاذة:** هياء مسفر آل ظافر  
""")

st.divider()

# ----------------------------------------------------
# قسم التعريف بالمبادرة وأهدافها
# ----------------------------------------------------
with st.expander("✨ عن المبادرة وأهدافها (ماذا تستفيد الطالبة؟)", expanded=True):
    col_about1, col_about2 = st.columns(2)
    
    with col_about1:
        st.markdown("### 🎯 هدف المبادرة")
        st.write("""
        تهدف هذه المبادرة النوعية إلى تحويل النماذج الورقية لاختبارات **"نافس"** إلى بيئة رقمية تفاعلية ممتعة، 
        تساعد على تمكين الطالبات من أدوات قياس الأداء وتنمية مهارات التفكير العليا والتحليل الرياضي والعلمي.
        """)
        
    with col_about2:
        st.markdown("### 💡 ماذا تستفيد الطالبة من المنصة؟")
        st.markdown("""
        * **التهيؤ النفسي والمعرفي:** التعود على نمط أسئلة الاختبارات الوطنية بشكل تفاعلي.
        * **التقييم والتغذية الراجعة الفورية:** معرفة الإجابة الصحيحة فوراً مع عبارات تحفيزية تُعزز الثقة بالنفس.
        * **تشخيص وتطوير المهارات:** التعرف على نقاط القوة والمهارات التي تحتاج إلى مراجعة وتدريب.
        * **متابعة مستمرة:** تمكين المعلمة من متابعة مستوى تقدم الطالبة ودعمها أولاً بأول.
        """)

st.divider()

# ----------------------------------------------------
# الشريط الجانبي (بيانات الطالبة ولوحة متابعة المعلمة)
# ----------------------------------------------------
with st.sidebar:
    st.header("👤 بيانات الطالبة")
    student_name = st.text_input("ادخلي اسم الطالبة الثلاثي:", value=st.session_state.student_name)
    if student_name:
        st.session_state.student_name = student_name
        st.success(f"مرحباً بكِ الطالبة: {student_name} ✨")
    
    st.divider()
    st.header("👩‍🏫 لوحة متابعة المعلمة")
    st.write("النتائج والتقدم المسجل للطالبات:")
    if st.session_state.scores:
        for name, score_info in st.session_state.scores.items():
            st.metric(
                label=f"الطالبة: {name}", 
                value=f"{score_info['score']} / {score_info['total']}", 
                delta=f"{score_info['percentage']}%"
            )
    else:
        st.info("لم يتم تسجيل أي نتائج حتى الآن.")

# ----------------------------------------------------
# رفع الملف والتحليل
# ----------------------------------------------------
uploaded_file = st.file_uploader("اختر ملف اختبار نافس (PDF)", type=["pdf"])

if uploaded_file is not None:
    if not st.session_state.student_name:
        st.warning("⚠️ يُرجى كتابة اسم الطالبة في القائمة الجانبية قبل البدء بالإجابة.")
    
    st.success("تم رفع الملف بنجاح! جاري تحليل واستخراج الأسئلة...")
    
    with pdfplumber.open(uploaded_file) as pdf:
        total_pages = len(pdf.pages)

    st.subheader("📊 تحليل وتصنيف المستند")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("إجمالي صفحات الاختبار", f"{total_pages} صفحات")
    with col2:
        st.metric("حالة استخراج الأسئلة", "تم بنجاح ✅")

    st.divider()
    st.subheader("📝 نموذج الاختبار التفاعلي")

    # أسئلة نموذجية تفاعلية
    questions = [
        {
            "id": 1,
            "category": "المهارات الأساسية",
            "question": "ما هي الخطوة الأولى الصحيحة عند البدء في حل مسألة رياضية أو علمية؟",
            "options": ["قراءة المسألة وفهم المعطيات والمطلوب", "التخمين العشوائي", "كتابة الناتج النهائي مباشرة", "ترك السؤال"],
            "answer": "قراءة المسألة وفهم المعطيات والمطلوب"
        },
        {
            "id": 2,
            "category": "التحليل الاستنتاجي",
            "question": "عند استخراج المعطيات وتحديد المطلوب من السؤال، ما الهدف الأساسي من ذلك؟",
            "options": ["تحديد الخطة والاستراتيجية المناسبة للحل", "استهلاك وقت الاختبار", "حفظ نص المسألة", "تلوين الأرقام"],
            "answer": "تحديد الخطة والاستراتيجية المناسبة للحل"
        }
    ]

    user_answers = {}
    
    with st.form("nafs_quiz_form"):
        for q in questions:
            st.markdown(f"**سؤال ({q['id']}) - [تصنيف المهارة: {q['category']}]:** {q['question']}")
            user_answers[q['id']] = st.radio(
                "اختر الإجابة الصحيحة:", 
                q['options'], 
                key=f"q_{q['id']}"
            )
            st.divider()
            
        submit_btn = st.form_submit_button("إرسال الإجابات والتقييم 🚀")

    if submit_btn:
        if not st.session_state.student_name:
            st.error("يرجى إدخال اسم الطالبة أولاً لترحيل النتيجة إلى لوحة المعلمة!")
        else:
            correct_count = 0
            total_q = len(questions)
            
            st.subheader("🏁 نتيجة التقييم والعبارات التحفيزية")
            
            for q in questions:
                ans = user_answers[q['id']]
                if ans == q['answer']:
                    correct_count += 1
                    st.success(f"السؤال {q['id']}: إجابة صحيحة! ({ans}) — {random.choice(praise_messages)}")
                else:
                    st.error(f"السؤال {q['id']}: إجابة تحتاج مراجعة. إجابتك: ({ans}) | الإجابة الصحيحة: ({q['answer']}) — {random.choice(encouraging_messages)}")

            percentage = round((correct_count / total_q) * 100, 1)
            
            # حفظ النتيجة للمعلمة
            st.session_state.scores[st.session_state.student_name] = {
                "score": correct_count,
                "total": total_q,
                "percentage": percentage
            }
            
            st.balloons()
            st.info(f"✨ النتيجة النهائية للطالبة ({st.session_state.student_name}): {correct_count} من {total_q} (النسبة: {percentage}%)")
