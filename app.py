import streamlit as st
from supabase import create_client, Client
# ... (שאר ה-imports הקודמים)

# חיבור ל-Supabase
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# פונקציה לשמירת פריט בבסיס הנתונים
def save_item_to_db(item_type, color, style):
    data = {
        "item_type": item_type,
        "color": color,
        "style_tags": [style]
    }
    try:
        supabase.table("clothes").insert(data).execute()
        st.success("הפריט נשמר בהצלחה במסד הנתונים!")
    except Exception as e:
        st.error(f"שגיאה בשמירה: {e}")

# בתוך tab1 (איפה שהעלאת הבגד):
if st.button("שמור בארון"):
    # כאן אנחנו שולחים ל-Gemini שיגיד לנו מה זה הבגד
    # נניח ש-analysis מכיל את המידע
    save_item_to_db("shirt", "blue", "casual")
