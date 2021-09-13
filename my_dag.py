from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "Skooldio",
}

with DAG(
    "my_dag",
    schedule_interval="*/5 * * * *",
    default_args=default_args,
    start_date=timezone.datetime(2021, 9, 1),
    catchup=False,
) as dag:
    t1 = DummyOperator(task_id="my_1st_dummy_task")

    t2 = DummyOperator(task_id="my_2nd_dummy_task")

    # Define the dependency
    t1 >> t2