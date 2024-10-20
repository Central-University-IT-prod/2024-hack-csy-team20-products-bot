import telebot
import requests
from telebot import types

bot = telebot.TeleBot('{{sensitive data}}')


@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='вход<3', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти лучшее приложение в мире:)", reply_markup = markup)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Название продукта:)");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    elif message.text == 'Получить продукты':
        url = "http://product/products/all"
        response = requests.get(url)
        bot.send_message(message.from_user.id, response);
    elif message.text in 'Получить продукт':
        message.text.split()[2]
        lalala = message.text.split()[2]
        url = "http://product/products/"+lalala
        response = requests.get(url)
        bot.send_message(message.from_user.id, response);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем тип продукта
    global name ;
    name= message.text;
    bot.send_message(message.from_user.id, ' Тип продукта<3');
    bot.register_next_step_handler(message, get_type );

def get_type(message):
    global type;
    type = message.text;
    bot.send_message(message.from_user.id, 'Срок годности');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global expiration;
    expiration = message.text;
    try:
        data = int(message.text) #проверяем, что cрок годности введен корректно
    except Exception:
         bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Продукт: срок годности - ' + str(expiration ) + ', название - '+name+', тип - '+type)
    url = "http://product/products?name="+name+"&type="+type+"&expiration_date="+expiration
    requests.post(url)

def get_expiration(message):
    global type;
    type = message.text;
    bot.send_message(message.from_user.id,'Всё вместе');
    bot.register_next_step_handler(message,get_age,get_type,get_name);
bot.polling(none_stop=True, interval=0)
