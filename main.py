import telebot

from telebot import types
bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('ТОП 10\U0001F525')
    item2 = types.KeyboardButton('Жанры\U0001F60E')
    #item3 = types.KeyboardButton('Что нибудь добавить')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,'Привет\U0001F590, {0.first_name}!' .format(message.from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "ТОП 10\U0001F525"):
        bot.send_message(message.chat.id,"Наруто\nХвост феи\nВолейбо\nВанпачмен\nКод Гиас\nВрата Штейна\nАтака Титанов\nМастера меча онлайн")
    elif (message.text == "Жанры\U0001F60E"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("\U0001F4ABФэнези")
        btn2 = types.KeyboardButton("\U0001F921Комедия")
        btn3 = types.KeyboardButton("\U0001F3D0Спорт")
        btn4 = types.KeyboardButton("\U0001F929Приключения")
        btn5 = types.KeyboardButton("\U0001F575Детиктив")
        btn6 = types.KeyboardButton("\U0001F480Ужасы")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Жанры\U0001F60E", reply_markup=markup)

    elif (message.text == "\U0001F4ABФэнези"):
        bot.send_photo(message.chat.id, 'https://kinofilmpro.ru/wp-content/uploads/2022/07/1-8.jpeg', 'Хвост Феи\nГоды выпуска: 2009, 2014, 2018.\nОригинальное название: Fairy Tail\nСерия:328')

    elif message.text == "\U0001F921Комедия":
        bot.send_photo(message.chat.id, 'https://www.anibox.org/_nw/79/29896803.jpg', 'Намбака\nГод выпуска: 2016.\nОригинальное название: Nanbaka\nСерия:26')

    elif message.text == "\U0001F3D0Спорт":
        bot.send_photo(message.chat.id,'https://kinofilmpro.ru/wp-content/uploads/2022/05/4-2.jpeg', 'Волейбол\nГоды выпуска: 2014, 2015, 2016, 2020.Оригинальное название: Haikyuu!!\nСерия:98')

    elif message.text == "\U0001F929Приключения":
        bot.send_photo(message.chat.id,'https://i.pinimg.com/originals/ce/52/82/ce5282ce32ad5afba76354a6f7c359e2.jpg', 'Хантер х Хантер\nГод выпуска: 2011.\nОригинальное название: Hunter x Hunter\nСерия:148')

    elif message.text == "\U0001F575Детиктив":
        bot.send_photo(message.chat.id,'https://suzzy.ru/wp-content/uploads/2021/01/20501e5a3e135e8667bb4b70c4d3377677674a3br1-1200-800v2_uhq.jpg', 'Бродячие псы\nГоды выпуска: 2016, 2019.\nОригинальное название: Bungou Stray Dogs\nСерия:36')

    elif message.text == "\U0001F480Ужасы":
        bot.send_photo(message.chat.id,'https://kartinkin.net/uploads/posts/2021-07/1626733033_22-kartinkin-com-p-anime-obeshchannii-neverlend-emma-vzroslay-23.jpg', 'Обещанный Неверленд\nГоды выпуска: 2019, 2021.\nОригинальное название: Yakusoku no Neverland\nСерия:23')

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("ТОП 10\U0001F525")
        item2 = types.KeyboardButton("Жанры\U0001F60E")

        markup.add(item1, item2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)



