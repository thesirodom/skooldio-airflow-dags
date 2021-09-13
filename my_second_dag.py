from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import logging

def _hello():
    return "Hello, Python"

def _print_log_messages():
    logging.info("This is an info message")

default_args = {
    "owner": "Skooldio",
}
with DAG(
    "my_second_dag",
    schedule_interval="*/30 * * * *",
    default_args=default_args,
    start_date=timezone.datetime(2021, 9, 1),
    catchup=False,
) as dag:

    start = DummyOperator(task_id="start")

    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo hello",
    )

    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=_hello,
    )

    run_this = PythonOperator(
        task_id="print_log_messages",
        python_callable=_print_log_messages,
    )

    end = DummyOperator(task_id="end")

    start >> [echo_hello, say_hello] >> run_this >> end
