from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG("hello", schedule=None):
    EmptyOperator(task_id="hello")
