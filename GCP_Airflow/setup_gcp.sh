#!/bin/bash

# Definição de variáveis
PROJECT_ID="meu-projeto-gcp"
BUCKET_NAME="meu-bucket-de-dados"
DATASET_NAME="ecommerce_sales"
TABLE_NAME="orders"
REGION="us-central1"

# Ativar o projeto no GCP
gcloud config set project $PROJECT_ID

# Criar o bucket no Cloud Storage
gcloud storage buckets create gs://$BUCKET_NAME --location=$REGION

echo "Bucket $BUCKET_NAME criado com sucesso!"

# Criar um dataset no BigQuery
gcloud bigquery datasets create $DATASET_NAME --location=$REGION

echo "Dataset $DATASET_NAME criado com sucesso!"

# Criar uma tabela no BigQuery
gcloud bigquery tables create $DATASET_NAME.$TABLE_NAME \
    --schema="order_id:INTEGER,customer_id:INTEGER,product:STRING,category:STRING,price:FLOAT,quantity:INTEGER,order_date:TIMESTAMP,total_price:FLOAT" \
    --location=$REGION

echo "Tabela $TABLE_NAME criada com sucesso no dataset $DATASET_NAME!"

# Definir permissões para que o Airflow e Dataflow possam acessar os recursos
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$(gcloud config get-value core/account)" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$(gcloud config get-value core/account)" \
    --role="roles/bigquery.admin"

echo "Permissões configuradas!"

echo "Setup concluído com sucesso! 🚀"
