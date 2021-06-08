from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from private.sub import HELLO

args = {
    "owner": HELLO,
}

with DAG(
    dag_id="sleep",
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(2),
) as dag:
    BashOperator(
        task_id="sleep",
        bash_command="date; sleep 30; date",
    )
