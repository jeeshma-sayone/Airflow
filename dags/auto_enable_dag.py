from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello_test_new():
    print('test - * - Hello world from first Airflow DAG new!')
    return 'Hello world from first Airflow DAG- test auto enable'


dag = DAG('hello_auto_start', description='Hello World DAG-Test new , single dag auto enable.',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2022, 9, 19), catchup=False)
hello_operator = PythonOperator(task_id='hello_task_test_new',
                                python_callable=print_hello_test_new, dag=dag)
