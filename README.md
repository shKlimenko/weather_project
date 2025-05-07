🌤️ Weather Data Pipeline with Airflow, Pandas & Apache Superset
Проект собирает данные о погоде из OpenWeatherMap API , обрабатывает их с помощью Pandas , сохраняет в БД через Apache Airflow по расписанию (раз в день) и визуализирует в Apache Superset . 

🧠 Описание проекта
Этот проект реализует полный ETL-пайплайн:
<ul>
<li>Extract : Получение данных о погоде из OpenWeatherMap API.
<li>Transform : Обработка и преобразование данных с помощью pandas.
<li>Load : Загрузка данных в PostgreSQL.
<li>Visualize : Визуализация в Apache Superset.
</ul>
🛠️ Используемые технологии
Python
Основной язык программирования
OpenWeatherMap API
Источник данных о погоде
Pandas
Обработка и очистка данных
PostgreSQL
Хранение данных
Apache Airflow
Оркестрация ETL-процессов
Apache Superset
Визуализация данных

📦 Архитектура проекта


1
2
3
[OpenWeatherMap API] → [Python Script + Pandas] → [PostgreSQL] → [Apache Superset]
                        ↑
                        └── Управление через Apache Airflow (раз в день)
🚀 Как запустить проект локально
1. Клонируй репозиторий
bash


1
2
git clone https://github.com/yourusername/weather-data-pipeline.git
cd weather-data-pipeline
2. Создай .env файл
Создай файл .env в корне проекта со следующим содержанием:

env


1
2
3
4
5
6
OPENWEATHER_API_KEY=your_api_key_here
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=weather_data
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
Не забудь заменить your_api_key_here на реальный ключ из OpenWeatherMap. 

3. Установи зависимости
bash


1
pip install -r requirements.txt
4. Подними инфраструктуру через Docker
bash


1
docker-compose up -d
Это запустит: 

PostgreSQL
Apache Airflow
Apache Superset
5. Настрой Airflow
Открой интерфейс Airflow: http://localhost:8080
Логин: airflow
Пароль: airflow

Добавь подключение к PostgreSQL:

Type: Postgres
Host: postgres
Schema: weather_data
User: airflow
Password: airflow
Port: 5432
Активируй DAG weather_pipeline.

📊 Визуализация в Apache Superset
Открой: http://localhost:8088
Авторизуйся:
Логин: admin
Пароль: admin
Добавь PostgreSQL как источник данных.
Создай дашборд и добавь графики (температура, давление, скорость ветра и т.д.).
📁 Структура проекта


1
2
3
4
5
6
7
8
9
10
weather-data-pipeline/
│
├── dags/                   # Airflow DAGs
│   └── weather_pipeline.py
├── scripts/                # Скрипты сборки и обработки данных
│   └── fetch_weather_data.py
├── docker-compose.yml      # Оркестрация контейнеров
├── requirements.txt        # Зависимости Python
├── .env                    # Переменные окружения
└── README.md               # Документация
🧪 Возможности для улучшения
✅ Добавить тесты (pytest)
✅ Реализовать CI/CD через GitHub Actions
✅ Расширить список городов или стран
✅ Добавить обработку ошибок и логирование
✅ Сохранять исторические данные за несколько лет
✅ Интеграция с AWS S3 или GCP для хранения бэкапов
📬 Связь
Если есть вопросы или идеи — пиши мне:

📧 Email: your_email@example.com
💼 LinkedIn: linkedin.com/in/yourprofile
❤️ Спасибо за интерес к проекту!
Удачных экспериментов с данными о погоде! ☀️🌧️
Если понравилось — поставь ⭐ звезду на GitHub.