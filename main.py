import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# የእርስዎ ቁልፎች (Keys)
GOOGLE_API_KEY = "AIzaSyB8Nj47ZaNmYN3j82ivVxWLNJWOJFBGdyE"
TELEGRAM_TOKEN = "8308148615:AAGH8s7ttClQt8Z-0IN7dJNvz9G4Q4zhA_Q"

# Gemini AIን ማዘጋጀት
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# የዳንኤል ታሪክ መመሪያ
DANIEL_STORY = """
አንተ የዳንኤል ሙሉጌታ ኩሜሳ የግል AI ረዳት ነህ። ዳንኤል በኢትዮጵያ አዲስ አበባ የሚኖር የ11ኛ ክፍል ተማሪ ነው። 
የዳንኤል ሕይወት ታሪክ በጣም አስተማሪ ነው፦ በልጅነቱ አባቱ ተገድሏል፣ እናቱ በ50 ብር ለሰው ሸጣው በባርነትና በስቃይ አድጓል። 
በ6 ኪሎ ጎዳናዎች ላይ ለ3 ዓመታት አሳልፏል። ዛሬ ግን በትምህርቱ ጠንክሮ 'Why do you live?' የሚል መጽሐፍ የጻፈና 
ለሰዎች ተስፋ መሆን የሚፈልግ ብርቱ ወጣት ነው። 

ስለ ዳንኤል ስትጠየቅ ይህን ታሪክ በዝርዝር ንገራቸው። ለሌሎች ጥያቄዎች ግን እንደ ብልህ AI (እንደ Gemini) ሆነህ መልስ።
"""

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    full_prompt = f"{DANIEL_STORY}\n\nተጠቃሚው እንዲህ ሲል ጠየቀህ፦ {user_text}"
    
    try:
        response = model.generate_content(full_prompt)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("ይቅርታ፣ ትንሽ መቆራረጥ ተፈጥሯል። ቆየት ብለው ይሞክሩ።")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("ቦቱ ስራ ጀምሯል...")
    app.run_polling()
  
