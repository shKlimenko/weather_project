import requests
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

# Загружаем переменные окружения из .env
load_dotenv()

# === 1. Конфигурация ===
API_KEY = os.getenv("API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# === 2. Функция получения данных с OpenWeatherMap ===
def get_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=ru"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при запросе к API: {response.status_code}, {response.text}")

# === 3. Функция извлечения данных из JSON ===
def extract_weather_info(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    cloudiness = data["clouds"]["all"]
    weather_description = data["weather"][0]["description"]
    dt = datetime.fromtimestamp(data["dt"])

    return (
        dt, city, country, temp, feels_like,
        pressure, humidity, wind_speed, cloudiness, weather_description
    )

# === 4. Функция сохранения в PostgreSQL ===
def save_to_postgres(data):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO weather_data (
        timestamp, city, country, temperature, feels_like, pressure,
        humidity, wind_speed, cloudiness, description
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, data)
    conn.commit()

    cursor.close()
    conn.close()

# === 5. Основная функция запуска ===
def main():
    print("Получаем данные о погоде...")
    data = get_weather_data()
    
    print("Извлекаем информацию...")
    weather_info = extract_weather_info(data)
    
    print("Сохраняем в базу данных...")
    #save_to_postgres(weather_info)
    
    print("✅ Данные успешно получены и сохранены!")

    '''print(f'Город {weather_info[1]} Температура {weather_info[3]} ощущается как {weather_info[4]}')
    print(f'Давление {weather_info[5]} скорость ветра {weather_info[7]} облачность {weather_info[8]}')
    print(f'{weather_info[9]}')
    print(f'{extract_weather_info(weather_info)}')'''

    try:
        print("Дата и время:", weather_info[0])
        print("Город:", weather_info[1])
        print("Страна:", weather_info[2])
        print("Температура:", weather_info[3])
        print("Ощущается как:", weather_info[4])
        print("Давление:", weather_info[5])
        print("Влажность:", weather_info[6])
        print("Скорость ветра:", weather_info[7])
        print("Облачность:", weather_info[8])
        print("Описание погоды:", weather_info[9])
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ {e} в данных о погоде.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()