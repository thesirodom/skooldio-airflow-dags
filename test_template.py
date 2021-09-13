from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def hello(dag):
    print(dag)


default_args = {
    "owner": "Skooldio",
}
with DAG(
    "test_template",
    schedule_interval="@daily",
    default_args=default_args,
    start_date=timezone.datetime(2021, 9, 1),
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start")

    print_today = BashOperator(
        task_id="print_today",
        bash_command="echo {{ ds }}"
    )

    hello = PythonOperator(
        task_id="hello",
        python_callable=hello,
    )

    end = DummyOperator(task_id="end")

    start >> print_today >> hello >> end