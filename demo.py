from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

# hi

with DAG(dag_id="demo"):
    # Second run
    sleep = BashOperator(task_id="sleep", bash_command="sleep 1")
    hello = BashOperator(task_id="hello", bash_command="echo 'Hello Astronomer22!!'")

    sleep >> hello

