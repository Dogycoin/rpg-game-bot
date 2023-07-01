import random

import telebot
import random as rn

tokean = 'tokean'  #Введите сюда токен
bot = telebot.TeleBot(tokean)
procent = 0
zona = 0


@bot.message_handler(commands=['start'])
def knopka_start(message):
    klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Да')
    btn2 = telebot.types.KeyboardButton('Нет')
    klaviatura.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Привет хочешь сыграть в РПГ - игру?', reply_markup=klaviatura)


@bot.message_handler(commands=['help'])
def knopka_help(message):
    bot.send_message(message.chat.id, text='Привет - это РПГ игра. Просто нажимай на все, что видишь')


@bot.message_handler(content_types=['text'])
def otveti_naknopki(message):
    global zona, procent, vibor
    if message.text == 'Нет':
        bot.send_message(message.chat.id, text='Знаешь чей это ответ?')
    elif message.text == 'Да':
        klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('Единая Россия')
        btn2 = telebot.types.KeyboardButton('КПРФ')
        btn3 = telebot.types.KeyboardButton('ЛДПР')
        btn4 = telebot.types.KeyboardButton('Яблоко')
        btn5 = telebot.types.KeyboardButton('Справедливая Россия')
        btn6 = telebot.types.KeyboardButton('Ксения Собчак')
        btn7 = telebot.types.KeyboardButton('Выйти в главное меню')
        btn8 = telebot.types.KeyboardButton('В путь')
        klaviatura.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text='Выбери партию(Если не выберешь Единую Россию, то тебя посадят).', reply_markup=klaviatura)
    elif message.text == 'Единая Россия':
        zona = 200
        procent = 1000000
        knopki_puti(message)
    elif message.text == 'КПРФ':
        zona = 60
        procent = 1000
        knopki_puti(message)
    elif message.text == 'ЛДПР':
        zona = 150
        procent = 1000
        knopki_puti(message)
    elif message.text == 'Яблоко':
        zona = 20
        procent = 500
        knopki_puti(message)
    elif message.text == 'Справедливая Россия':
        zona = 100
        procent = 1000
        knopki_puti(message)
    elif message.text == 'Ксения Собчак':
        zona = 10
        procent = 100
        knopki_puti(message)
    elif  message.text == 'Выйти в главное меню':
        klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('Да')
        btn2 = telebot.types.KeyboardButton('Нет')
        klaviatura.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Привет хочешь сыграть в РПГ - игру?', reply_markup=klaviatura)
    elif message.text == 'В путь':
        rand_chi = rn.randint(1, 2)
        if rand_chi == 1:
            bot.send_message(message.chat.id, text=variantu_vragov[rn.randint(0, len(variantu_vragov) - 1)])
            klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton('Помочь')
            btn2 = telebot.types.KeyboardButton('Убежать')
            klaviatura.add(btn1, btn2)
            bot.send_message(message.chat.id, text='У нас проблема. Что будем делать?', reply_markup=klaviatura)
        elif rand_chi == 2:
            klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton('В путь')
            btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
            klaviatura.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Вам никто не встретился', reply_markup=klaviatura)
    elif message.text == 'Убежать':
        rand_chis = rn.randint(1, 2)
        if rand_chis == 1:
            procent -= 200
            if procent > 0:
                klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = telebot.types.KeyboardButton('В путь')
                btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
                klaviatura.add(btn1, btn2)
                bot.send_message(message.chat.id, text=f'Вас выкинули. У вас осталось {procent}% выиграть выборы', reply_markup=klaviatura)
            else:
                klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
                klaviatura.add(btn2)
                bot.send_message(message.chat.id, text='Вы не настоящая Единая Россия. Вы подделка. Вы проиграли выборы', reply_markup=klaviatura)
        elif rand_chis == 2:
            klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton('В путь')
            btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
            klaviatura.add(btn1, btn2)
            bot.send_message(message.chat.id, text=f'Вам удалось  сбежать', reply_markup=klaviatura)
    elif message.text == 'Помочь':
        rand_chis = rn.randint(1, 2)
        if rand_chis == 1:
            procent += random.randint(0, 1000)
            klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton('В путь')
            btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
            klaviatura.add(btn1, btn2)
            bot.send_message(message.chat.id, text=f'Вы решили проблему. Шансы равны {procent}% выиграть выборы', reply_markup=klaviatura)
            bot.send_photo(message.chat.id, random.choice(list(varianti_oruzhiya.values())))
            zona += random.randint(0, 20)
            bot.send_message(message.chat.id, text=f'Вам выдали оружие. Теперь ваш урон {zona}')
        elif rand_chis == 2:
            procent -= random.randint(0, 1000)
            if procent > 0:
                klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = telebot.types.KeyboardButton('В путь')
                btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
                klaviatura.add(btn1, btn2)
                bot.send_message(message.chat.id, text=f'Вы не решили проблему. шансы понизились до {procent}% выиграть выборы', reply_markup=klaviatura)
            else:
                klaviatura = telebot.types.ReplyKeyboardMarkup()
                btn2 = telebot.types.KeyboardButton('Выйти в главное меню')
                klaviatura.add(btn2)
                bot.send_message(message.chat.id,
                                 text='Вы не настоящая Единая Россия. Вы подделка. Вы проиграли выборы',
                                 reply_markup=klaviatura)



global variantu_vragov
variantu_vragov = ['Владимир Жириновский умер. Скинетесь на похороны?', 'В стране опять начались митинги из - за Навального. Вызываем Омон?', 'В стране проблемы с экономикой. Повысим налоги?']
global varianti_oruzhiya
varianti_oruzhiya = {'Омон': 'https://avatars.mds.yandex.net/i?id=5e718d671099775280d3500eda8c24ede410e94d-6605560-images-thumbs&n=13',
                     'Полиция': 'https://avatars.mds.yandex.net/i?id=333bed53e88444ea1b08b65e1ba677cc91628f80-7547473-images-thumbs&n=13',
                     'Армия': 'https://avatars.mds.yandex.net/i?id=2d8f4dc166b7c83cc9ae2256c99b54abf2a1a4aa-7753204-images-thumbs&n=13'}


def knopki_puti(message):
    klaviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn7 = telebot.types.KeyboardButton('Выйти в главное меню')
    btn8 = telebot.types.KeyboardButton('В путь')
    klaviatura.add(btn7, btn8)
    if message.text == 'Единая Россия':
        bot.send_message(message.chat.id, text=f'Вы выбрали Единую Россию, вы молодец. Вы{procent}% выиграете выборы.', reply_markup=klaviatura)
    else:
        bot.send_message(message.chat.id, text='Вы не выиграете выборы', reply_markup=klaviatura)
    global vibor
    vibor = message.text









bot.polling(non_stop=True)  
