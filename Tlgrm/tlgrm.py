'''
Created on 28 мая 2019 г.

@author: m.elagina
'''
import telebot
from telebot import apihelper

bot = telebot.TeleBot("731755687:AAHZ1i5BIdAb5X9987jHEBW8d0fDwonthgU")

apihelper.proxy = {'https':'socks5://user_155418644:SVQKrPpwINvM@9169c2.fckrknbot.club:443'}
# apihelper.proxy = {'http':'http://10.10.1.10:3128'}

@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id(), message.text)
bot.polling(none_stop = True)


# tg://socks?server=ftfkr.teletype.live&port=1080&user=telegram&pass=telegram    

# https://t.me/socks?server=9169c2.fckrknbot.club&port=443&user=user_155418644&pass=SVQKrPpwINvM