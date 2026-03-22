import os
from flask import Flask, render_template
from threading import Thread
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "Server is Running!"

@app.route('/bingo')
def bingo():
    return render_template('index.html')

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# ASITTI TOKEN KALLAATTIIDHAAN HIN GALCHINU
# Render 'Environment' irraa akka dubbisu goona
TOKEN = os.environ.get('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    WEB_APP_URL = "https://bingo-bot-g7ua.onrender.com/bingo" 
    keyboard = [[InlineKeyboardButton("🎮 Join Professional Bingo", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("<b>Baga Nagaa Dhufte!</b>\nBingo taphachuuf button gadii tuqi.", reply_markup=reply_markup, parse_mode='HTML')

if __name__ == '__main__':
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
    if TOKEN:
        print(f"Botiin Token kanaan hojii jalqabeera: {TOKEN[:10]}...")
        bot_app = ApplicationBuilder().token(TOKEN).build()
        bot_app.add_handler(CommandHandler("start", start))
        bot_app.run_polling()
    else:
        print("ERROR: TOKEN hin argamne! Environment Variables Render irratti mirkaneessi.")
