from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="demo"):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 30")
    hello = BashOperator(task_id="hello", bash_command="echo 'Hello version 3'")

    sleep >> hello

