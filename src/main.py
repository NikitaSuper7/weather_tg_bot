import requests
import telebot

bot = telebot.TeleBot('6999037028:AAHcWLBmmJXieYUJWA0hcxd9kaRKqIlxJrg')
api_2 = '85adfcffe34017f4c547e305de05e169'
# city = 'niznevartovsk'

if __name__ == '__main__':
    with open('new_key.txt', 'r') as file:
        api_key = file.read()
    # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # result = requests.get(url)
    # data = result.json()
    # print(result.status_code)


    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Привет, рад тебя видеть. Введи название города.')


    @bot.message_handler(content_types=['text'])
    def get_weather(message):
        city = message.text.strip().lower()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        result = requests.get(url)
        if result.status_code == 200:
            data = result.json()
            temp = data['main']['temp']
            weather = data['weather'][0]['main']
            # image = 'ex_1.png'
            # image = 'sunn.png' if temp > 5.0 else 'cold.png'
            # with open('./' + image, 'rb') as picture:
            #     pict = picture.read()
            bot.reply_to(message, f"Сейчас погода - {temp}, {weather}")
            if weather == 'Clear':
                bot.send_message(message.chat.id, '☀')
            elif weather == 'Clouds':
                bot.send_message(message.chat.id, '🌥')
            elif weather == 'Thunderstorm':
                bot.send_message(message.chat.id, '⛈')
        else:
            bot.reply_to(message, "Город не найден")
        # bot.send_photo(message.chat.id, pict)


    bot.polling(none_stop=True)
