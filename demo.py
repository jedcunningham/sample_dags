from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

from airflow.models.connection import Connection


conn = Connection.get_connection_from_secrets("my_git_conn")

def on_success(**kwargs):
    print("Hi, I'm in on_success_callback")




with DAG(dag_id="demo", on_success_callback=on_success):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 10")
    hello = BashOperator(task_id="hello_new", bash_command="echo 'Hello world!'")

    sleep >> hello
