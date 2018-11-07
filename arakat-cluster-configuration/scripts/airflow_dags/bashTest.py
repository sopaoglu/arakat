from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG("testbash", default_args={"owner": "airflow", "start_date": datetime.strptime("01/01/2018", "%d/%m/%Y")}, schedule_interval="@once")

t2 = BashOperator(task_id='test',bash_command="sh /usr/local/shell_scripts/test.sh '/spark/bin/spark-submit --master spark://spark-master:7077 /usr/local/spark_code/MyFirstApp3_task1.py' 'MyFirstApp3_task1.py' ",dag=dag)


