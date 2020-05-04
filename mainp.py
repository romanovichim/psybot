#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config 
import json
from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler
from pairans import psy_chat

bot = Bot(token=config.TOKEN)




def message_cb(bot, event):
    #получение ответа
    #исключим команды
    if((event.text).startswith("/")):
        #обработаем команды
        if(event.text=="/help"):
            bot.send_text(chat_id=event.from_chat, text = "Вот что я умею")
        elif(event.text=="/start"):
            bot.send_text(chat_id=event.from_chat, text = "Доброго времени суток! \n Отвечая на мои вопросы вы сможете точнее понять свое психологическое состояние и чувства.\n Скажите - как вы себя чувствуете? ")
        else:
            bot.send_text(chat_id=event.from_chat, text = "Я пока не знаю, такой команды, все команды можно узнать по команде /help")
    else:
        answer = psy_chat(event.text)
        bot.send_text(chat_id=event.from_chat, text = answer)
        



bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
