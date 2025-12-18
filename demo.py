from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

def on_success(**kwargs):
    print("Hi, I'm in on_success_callback")




with DAG(dag_id="demo"):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 10")
    hello = BashOperator(task_id="hello_new", bash_command="echo 'Hello world!'")

    sleep >> hello
