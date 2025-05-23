<h1 align="center">🌤️ Weather Data Pipeline with Airflow, Pandas & Apache Superset</h1>

  Проект собирает данные о погоде из <a href="https://openweathermap.org/api" target="_blank">OpenWeatherMap API</a>, обрабатывает их, сохраняет в БД через <strong>Airflow</strong> по расписанию (раз в день) и визуализирует в <strong>Apache Superset</strong>.


---

## 🧠 Описание проекта

Этот проект реализует полный ETL-пайплайн:

1. **Extract**: Получение данных о погоде из OpenWeatherMap API.
2. **Transform**: Обработка и преобразование данных с помощью <code>pandas</code>.
3. **Load**: Загрузка данных в PostgreSQL.
4. **Visualize**: Визуализация в Apache Superset.

---

## 🛠️ Используемые технологии

| Технология | Назначение |
|-----------|------------|
| Python | Основной язык программирования |
| OpenWeatherMap API | Источник данных о погоде |
| Pandas | Обработка и очистка данных |
| PostgreSQL | Хранение данных |
| Apache Airflow | Оркестрация ETL-процессов |
| Apache Superset | Визуализация данных |

---

## 📦 Архитектура проекта
<pre>[OpenWeatherMap API] → [Python Script + Pandas] → [PostgreSQL] → [Apache Superset] <br>
                        ↑
                        └── Управление через Apache Airflow (раз в день)</pre>

---

## 🧪 Возможности для улучшения<br>
✅ Добавить тесты (pytest)<br>
✅ Реализовать CI/CD через GitHub Actions<br>
✅ Расширить список городов или стран<br>
✅ Добавить обработку ошибок и логирование<br>
✅ Сохранять исторические данные за несколько лет<br>

---

## 📬 Связь
Если есть вопросы или идеи — пиши мне:<br>

📧 Email: klimеnkо161@gmаil.соm<br>
💼 LinkedIn: https://www.linkedin.com/in/selectbegemot/<br>

## ❤️ Спасибо за интерес к проекту!
Удачных экспериментов с данными о погоде! ☀️🌧️
