from django.shortcuts import render
from .forms import PostForm
from telegram import Bot
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


class SenderMessages:
    TELEGRAM_TOKEN = TELEGRAM_TOKEN
    CHAT_ID = CHAT_ID
    bot = Bot(token=TELEGRAM_TOKEN)

    def sended_message(message):
        send = SenderMessages
        send.bot.send_message(chat_id=send.CHAT_ID, text=message)

def index(request, gera_dev_cook=None):
    SenderMessages.sended_message('_X_')
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            SenderMessages.sended_message(text)
            return render(request, 'index.html', {'ok': ok})

    ok = False
    return render(request, "index.html", {'form': form, 'ok': ok})
