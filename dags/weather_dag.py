"""
DAG для получения данных о погоде и сохранения их в PostgreSQL.
Запускается ежедневно.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os
import sys

# Добавляем путь к основному каталогу проекта, чтобы можно было импортировать скрипты
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Импортируем функцию из нашего скрипта
from scripts.fetch_and_save_weather import main as fetch_weather

# === Параметры DAG ===
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# === Определение DAG ===
with DAG(
    dag_id='weather_data_pipeline',
    description='Получает данные о погоде из OpenWeatherMap и сохраняет в PostgreSQL',
    schedule_interval='0 * * * *',  # Запуск раз в час
    start_date=datetime(2025, 5, 5),
    catchup=False,
    default_args=default_args
) as dag:

    def run_weather_script(**kwargs):
        """
        Обертка для вызова функции fetch_weather
        """
        fetch_weather()

    # === Задача в DAG ===
    fetch_weather_task = PythonOperator(
        task_id='fetch_and_save_weather_data',
        python_callable=run_weather_script,
        provide_context=True
    )

    fetch_weather_task