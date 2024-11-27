from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="sleep",
    schedule=None,
):
    BashOperator(
        task_id="sleep",
        bash_command="date; sleep 30; date",
    )
