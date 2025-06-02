import sys
import pprint

from airflow.sdk import DAG, task

pprint.pprint(sys.path)

from foo import HI


with DAG(dag_id="syspath"):

    @task
    def print_syspath():
        pprint.pprint(sys.path)

    print_syspath()



