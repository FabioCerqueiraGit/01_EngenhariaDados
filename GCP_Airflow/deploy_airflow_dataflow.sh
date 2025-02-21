#!/bin/bash

# Definição de variáveis
PROJECT_ID="meu-projeto-gcp"
REGION="us-central1"
COMPOSER_ENV="meu-composer-env"
BUCKET_NAME="meu-bucket-de-dados"
DATAFLOW_JOB_NAME="transform-dataflow-job"

# Ativar o projeto no GCP
gcloud config set project $PROJECT_ID

# Criar ambiente do Cloud Composer (Airflow)
gcloud composer environments create $COMPOSER_ENV \
    --location $REGION \
    --airflow-version=2.5.1 \
    --image-version=composer-2-airflow-2.5.1 \
    --service-account=$(gcloud config get-value core/account)

echo "Cloud Composer (Airflow) criado com sucesso!"

# Obter o bucket gerenciado pelo Composer
COMPOSER_BUCKET=$(gcloud composer environments describe $COMPOSER_ENV \
    --location $REGION \
    --format="value(config.dagGcsPrefix)")

echo "Bucket do Composer: $COMPOSER_BUCKET"

# Copiar DAG para o bucket do Composer
gcloud storage cp etl_pipeline.py $COMPOSER_BUCKET/dags/

echo "DAG do Airflow copiada para o bucket do Composer!"

# Enviar o script de transformação para o Cloud Storage
gcloud storage cp transform.py gs://$BUCKET_NAME/scripts/

echo "Script de transformação enviado para o Cloud Storage!"

# Executar o job do Dataflow
gcloud dataflow jobs run $DATAFLOW_JOB_NAME \
    --gcs-location gs://dataflow-templates/latest/Word_Count \
    --region $REGION \
    --staging-location gs://$BUCKET_NAME/temp/ \
    --parameters inputFile=gs://$BUCKET_NAME/raw/sample_data_large.json,output=gs://$BUCKET_NAME/processed/sample_data_transformed.json

echo "Job do Dataflow iniciado com sucesso!"

echo "Deploy concluído com sucesso! 🚀"
