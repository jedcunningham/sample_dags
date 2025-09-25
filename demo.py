from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="demo"):
    # First run
    sleep = BashOperator(task_id="sleep", bash_command="sleep 60")
    hello = BashOperator(task_id="hello2", bash_command="echo 'Hello Airflow Summit!'")

    sleep >> hello

