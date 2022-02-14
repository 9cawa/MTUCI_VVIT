import requests

city = "Moscow,RU"
appid = "bb50fefd919363491695cea8da7152ca"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data=res.json()

print("Прогноз погоды на сегодня:")
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:",data['wind']['speed'])
print("Видимость",data['visibility'])
print()

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">", "> \r\nСкорость ветра <", i['wind']['speed'], \
          "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")