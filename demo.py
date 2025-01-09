from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="demo", schedule=None):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 45")
    hello = BashOperator(task_id="hello", bash_command="Hello version 2")

    sleep >> hello

