# Airflow

# commands run step by step after creating virtual environment

*1 – Airflow Installation
pip install 'apache-airflow==2.3.4'  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.4/constraints-3.8.txt" 

*2 – First of all, Airflow needs a home directory where it stores all its settings, configurations. It is usually set to ~/airflow using the following command:
export AIRFLOW_HOME=~/airflow

*3 – Initializing the Airflow DB
airflow db init

*4 – Setup Admin User
airflow users create --username admin --firstname jeeshma --lastname g --role Admin --email admin@gmail.com

5 – Start Webserver
 airflow webserver --port 8080 -D



# Reference
https://github.com/apache/airflow
https://www.youtube.com/watch?v=K9AnJ9_ZAXE&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT