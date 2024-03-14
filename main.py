import telebot

class CityBot:
    def __init__(self):
        self.city_attractions = {
            "Париж": "Эйфелева башня",
            "Лондон": "Лондонский Тауэр",
            "Рим": "Колизей",
            "Нью-Йорк": "Статуя Свободы",
            "Токио": "Буддийский храм Сэнсо-дзи"
        }

    def get_attraction(self, city):
        if city in self.city_attractions:
            return self.city_attractions[city]
        else:
            return "Извините, достопримечательность для данного города не найдена."

    def get_city(self, attraction):
        for city, attr in self.city_attractions.items():
            if attr == attraction:
                return city
        return "Извините, город для данной достопримечательности не найден."

bot = telebot.TeleBot("7144744223:AAEcxX39NLZ8c-ioEIHUhkpYrT8X3hfUnZE")
city_bot = CityBot()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот-путеводитель. Напиши мне город, и я подскажу тебе его достопримечательность.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text
    response = None

    if user_input in city_bot.city_attractions:
        response = f"Для города {user_input} рекомендуется посетить: {city_bot.get_attraction(user_input)}"
    else:
        response = f"Для достопримечательности {user_input} рекомендуется посетить город: {city_bot.get_city(user_input)}"

    bot.send_message(message.chat.id, response)

bot.polling()
