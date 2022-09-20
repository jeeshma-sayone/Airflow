from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello_new():
    print('new - * - Hello world from first Airflow DAG!')
    return 'Hello world from first Airflow DAG- new'


dag = DAG('hello_single_dag_pause', description='Hello World DAG',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2022, 9, 19), catchup=False,
          is_paused_upon_creation=True)
hello_operator = PythonOperator(task_id='hello_task_new',
                                python_callable=print_hello_new, dag=dag)