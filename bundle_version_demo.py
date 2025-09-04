from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="bundle_version_demo"):
    sleep = BashOperator(task_id="sleep", bash_command="sleep 45")
    hello = BashOperator(task_id="hello", bash_command="echo 'Hello world!'")
    sleep >> hello

