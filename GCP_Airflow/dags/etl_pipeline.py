from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator, GCSToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.apache.beam.operators.beam import BeamRunPythonPipelineOperator
from airflow.utils.dates import days_ago

BUCKET_NAME = "meu-bucket-de-dados"
DATASET_NAME = "ecommerce_sales"
TABLE_NAME = "orders"

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'gcp_airflow_etl',
    default_args=DEFAULT_ARGS,
    description='Pipeline ETL com Airflow, Dataflow e BigQuery',
    schedule_interval='@daily',
)

create_gcs_bucket = GCSCreateBucketOperator(
    task_id='create_gcs_bucket',
    bucket_name=BUCKET_NAME,
    storage_class='STANDARD',
    location='US',
    dag=dag,
)

upload_to_gcs = GCSToGCSOperator(
    task_id='upload_to_gcs',
    source_bucket=BUCKET_NAME,
    source_object='raw/sample_data_large.json',
    destination_bucket=BUCKET_NAME,
    destination_object='processed/sample_data.json',
    move_object=False,
    dag=dag,
)

run_dataflow_job = BeamRunPythonPipelineOperator(
    task_id='run_dataflow_job',
    runner='DataflowRunner',
    py_file='gs://meu-bucket-de-dados/scripts/transform.py',
    pipeline_options={
        'tempLocation': f'gs://{BUCKET_NAME}/temp/',
        'stagingLocation': f'gs://{BUCKET_NAME}/staging/',
    },
    dag=dag,
)

load_to_bigquery = BigQueryInsertJobOperator(
    task_id='load_to_bigquery',
    configuration={
        "query": {
            "query": f"""
                LOAD DATA INTO `{DATASET_NAME}.{TABLE_NAME}`
                FROM FILES (format='JSON', uris=['gs://{BUCKET_NAME}/processed/sample_data.json']);
            """,
            "useLegacySql": False,
        }
    },
    dag=dag,
)

create_gcs_bucket >> upload_to_gcs >> run_dataflow_job >> load_to_bigquery
