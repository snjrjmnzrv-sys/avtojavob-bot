import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message

# MY.TELEGRAM.ORG MA'LUMOTLARI
API_ID = 6019016968       
API_HASH = "41b66ab6019016968a6866293ab93fa1"  

app = Client("render_session", api_id=API_ID, api_hash=API_HASH)

LOVE_WORDS = [
    "sizni sevaman", "sizni yaxshi koʻraman", "sizni yaxshi koraman",
    "asalim", "shakarim", "jonim", "sizsiz yashay olmayman", 
    "hayotimsiz", "i love you", "я тебя люблю"
]

BAD_WORDS = [
    "sikay", "sikaman", "dalbayop", "dalbayob", "gandon", 
    "qoʻtoq", "qotoq", "jalap", "am", "yiban", "qanchiq"
]

@app.on_message(filters.private & ~filters.me)
async def auto_responder(client: Client, message: Message):
    if not message.text:
        return
        
    text = message.text.lower()
    current_hour = datetime.now().hour

    if any(word in text for word in BAD_WORDS):
        await message.reply_text("Sökinmang odobli bölaylik")
        return

    if any(word in text for word in LOVE_WORDS):
        await message.reply_text("Men ham ")
        return

    if "karta" in text or "card" in text:
        await message.reply_text("5614 6821 1410 9384")
        return

    if current_hour >= 23 or current_hour < 6:
        await asyncio.sleep(5)
        await message.reply_text("Men dam olyapman sizga ham xayrli tun")
    else:
        await asyncio.sleep(300)
        async for last_msg in client.get_chat_history(message.chat.id, limit=1):
            if last_msg.from_user and last_msg.from_user.is_self:
                return
        await message.reply_text("Men avtojavob beradigan botman. Sanjar online bölganda sizga javob beradi")

print("Userbot Render'da muvaffaqiyatli ishga tushdi...")
app.run()
