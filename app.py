import streamlit as st
import google.generativeai as genai
from rembg import remove
from PIL import Image
import io

# 1. הגדרות תצוגה למובייל
st.set_page_config(page_title="AI Stylist", layout="centered")

# הסתרת תפריטים של סטרימליט למראה נקי
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. חיבור ל-API (משתמש ב-Secrets שהגדרת)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. פונקציה לעיבוד התמונה
def process_image(uploaded_file):
    image = Image.open(uploaded_file)
    # הסרת רקע
    with st.spinner("מנקה רקע..."):
        no_bg_img = remove(image)
    return no_bg_img

# 4. ממשק טאבים (כמו באפליקציה)
tab1, tab2, tab3 = st.tabs(["📸 צילום בגד", "🕺 המלביש", "📊 הסטייל שלי"])

with tab1:
    st.subheader("הוסף פריט לארון")
    uploaded_file = st.file_uploader("בחר תמונה של בגד", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        processed_img = process_image(uploaded_file)
        st.image(processed_img, caption="הבגד מוכן להלבשה", use_container_width=True)
        
        if st.button("שמור בארון"):
            # כאן בהמשך נוסיף את החיבור ל-Supabase
            st.success("הפריט נשמר!")

with tab2:
    st.subheader("הלבשת הדמות")
    # כאן נטען את דמות הבסיס שלך
    # ודא שהקובץ של הדמות נמצא בגיטהאב באותה תיקייה
    try:
        base_char = Image.open("character.png") # שנה לשם הקובץ שלך
        st.image(base_char, caption="הדוגמן שלך", use_container_width=True)
    except:
        st.info("העלה קובץ בשם character.png ל-GitHub כדי לראות את הדמות")

with tab3:
    st.subheader("ניתוח הסטייל שלך")
    st.write("כאן Gemini ינתח את כל הארון שלך ויתן לך תובנות.")
