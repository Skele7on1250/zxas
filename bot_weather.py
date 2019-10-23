import telebot
import pyowm
bot = telebot.TeleBot("713393027:AAHwcfUsUx_nOvfzMLrgI0-D2JYopONSwKY")
owm = pyowm.OWM('API', language = "ru")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здраствуй, я великая  Бабушка Маланья, я могу определить погоду в любом городе. Напиши мне название города и сами убедитесь")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
    

        answer = "На данный момент в " + message.text +" " + w.get_detailed_status() + "\n"
        answer += "Температура сейчас в районе " + str(temp) + " градусов" + "\n\n"
        if temp < -20:
            answer += "Одевайся как танк!!!!!"

        elif temp < 0:
            answer += "Сейчас холодно мой дружок пирожок, одевайся тепло"
        elif temp < 10:
            answer += "Советую одеться потеплее" + "\n\n"
        elif temp < 20:
            answer += "Хмм, я думаю тебе стоит накинуть кофту, легкую куртку и тд."
        else:
            answer += "Сейчас тепло и я бы порекомендовала бы сосредоточится на погоде" + " так как сейчас " + w.get_detailed_status() 
        

        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id,'Что-что? Я вас не поняла, напишите еще раз')
if __name__ == '__main__':
    bot.polling( none_stop = True )    

                     
