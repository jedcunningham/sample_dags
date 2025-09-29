from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="demo"):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 10")
    hello = BashOperator(task_id="hello_new", bash_command="echo 'Hello Seattle!'")

    sleep >> hello
