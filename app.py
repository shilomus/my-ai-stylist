import streamlit as st
import google.generativeai as genai
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="AI Stylist", layout="centered", initial_sidebar_state="collapsed")

tab1, tab2, tab3 = st.tabs(["👕 הארון שלי", "✨ המלצה יומית", "🧐 דירוג סטייל"])

with tab1:
    st.header("העלאת בגדים")
    # כאן נשים את הקוד של העלאת התמונה

with tab2:
    st.header("מה נלבש היום?")
    # כאן נשים את הלוגיקה של הלבשת הדמות

with tab3:
    st.header("ביקורת אופנה")
    # כאן ה-AI ידרג את הלוק

# הגדרת ה-API של גוגל
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

def process_clothing_item(uploaded_file):
    # 1. הסרת רקע (הופך את התמונה לשקופה)
    input_image = Image.open(uploaded_file)
    output_image = remove(input_image)
    
    # 2. ניתוח באמצעות Gemini
    prompt = """
    Analyze this clothing item and return ONLY a JSON with:
    'type': (shirt/pants/shoes/accessory),
    'color': (main color),
    'style': (e.g., casual, formal, vintage)
    """
    response = model.generate_content([prompt, input_image])
    
    return output_image, response.text

# ממשק משתמש פשוט
st.title("הסטייליסט האישי שלי 0$")
uploaded_file = st.file_uploader("צלם או העלה פריט לבוש", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with st.spinner("ה-AI מנתח ומנקה את הבגד..."):
        transparent_img, analysis = process_clothing_item(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(transparent_img, caption="הבגד המעובד (ללא רקע)")
        with col2:
            st.write("ניתוח סטייל:")
            st.code(analysis)
