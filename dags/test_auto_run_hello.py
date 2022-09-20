from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_hello_test():
    print('test - * - Hello world from first Airflow DAG!')
    return 'Hello world from first Airflow DAG- test'


dag = DAG('hello_world_test', description='Hello World DAG-Test',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2022, 9, 19), catchup=False)
hello_operator = PythonOperator(task_id='hello_task_test',
                                python_callable=print_hello_test, dag=dag)
