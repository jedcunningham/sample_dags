from airflow.sdk import DAG, task

with DAG(dag_id="anotherdemo"):

    @task
    def hi():
        print("hello22")

