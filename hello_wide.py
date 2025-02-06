from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def hello():
    print("Hello world")

with DAG("hello_wide"):

    for i in range(5):
        PythonOperator(
            task_id=f"task_{i}",
            python_callable=hello,
        )
    