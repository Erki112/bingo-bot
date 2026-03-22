import os
from flask import Flask, render_template
from threading import Thread
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. Web Server for Render
# Bakka kanaan duraa kanaan bakka buusi
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Telegram Bot Logic
TOKEN = "8487920836:AAFe77nalADov0H7ufj4GWZb0gYiEq5xdBQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Linkii Render keetii asitti jijjiiruun baay'ee murteessaadha!
    # Erga 'Deploy' jettee booda linkii Render siif kennu as galchi.
    WEB_APP_URL = "https://bingo-bot-g7ua.onrender.com" 
    
    keyboard = [
        [InlineKeyboardButton("🎮 Join Professional Bingo", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "<b>Baga Nagaa Dhufte!</b>\n\nBingo Professional taphachuuf button gadii tuqi.",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

if __name__ == '__main__':
    keep_alive()
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    print("Botiin hojii jalqabeera...")
    bot_app.run_polling()
