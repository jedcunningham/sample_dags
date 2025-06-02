import sys
import pprint

from airflow.sdk import DAG, task

pprint.pprint(sys.path)

with DAG(dag_id="syspath"):

    @task
    def print_syspath():
        pprint.pprint(sys.path)



