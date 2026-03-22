import os
from flask import Flask, render_template
from threading import Thread
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. Flask setup
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "Server is Running!"

# KAN ATI JETTE: User ID akka fudhatu taasifameera
@app.route('/bingo/<int:user_id>')
def bingo(user_id):
    return render_template('index.html', user_id=user_id)

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# 2. TOKEN KEE (ISA @BotFather IRRAA FIDDE)
TOKEN = "8487920836:AAF-Ij4fkDMxrBA1xUmfSjJMwPybHjWV4Ps"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # URL irratti User ID ni dabalama (fakkeenya: /bingo/12345)
    WEB_APP_URL = f"https://bingo-bot-g7ua.onrender.com/bingo/{user_id}" 
    
    keyboard = [[InlineKeyboardButton("🎮 Tapha Qaroo Bingo Jalqabi", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"<b>Baga Nagaa Dhufte!</b>\n\nID kee: <code>{user_id}</code>\n\nQaroo Bingo taphachuuf button gadii tuqi.",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

if __name__ == '__main__':
    # Flask Server jalqabsiisuu
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
    # Telegram Bot jalqabsiisuu
    print("Botiin hojii jalqabeera...")
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.run_polling()
