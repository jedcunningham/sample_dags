from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="bundle_version_demo"):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 60")
    hello = BashOperator(task_id="hello_v2", bash_command="echo 'Hello world!'")
    sleep >> hello

