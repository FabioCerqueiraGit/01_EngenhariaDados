#!/bin/bash

# Definição de variáveis
AWS_REGION="us-east-1"
S3_BUCKET="meu-bucket-de-logs"
GLUE_JOB_NAME="etl-glue-job"
REDSHIFT_CLUSTER="meu-redshift-cluster"
REDSHIFT_DB="logs_db"
REDSHIFT_USER="admin"
REDSHIFT_PASSWORD="MinhaSenhaForte123"

# Criar um bucket no S3
aws s3 mb s3://$S3_BUCKET --region $AWS_REGION
echo "Bucket S3 criado: $S3_BUCKET"

# Criar o Glue Job
aws glue create-job --name $GLUE_JOB_NAME \
    --role "arn:aws:iam::123456789012:role/AWSGlueServiceRole" \
    --command "{\"Name\":\"glueetl\",\"ScriptLocation\":\"s3://$S3_BUCKET/scripts/etl_glue.py\"}" \
    --region $AWS_REGION

echo "Job AWS Glue criado: $GLUE_JOB_NAME"

# Criar cluster Redshift
aws redshift create-cluster \
    --cluster-identifier $REDSHIFT_CLUSTER \
    --node-type dc2.large \
    --master-username $REDSHIFT_USER \
    --master-user-password $REDSHIFT_PASSWORD \
    --cluster-type single-node \
    --region $AWS_REGION

echo "Cluster Redshift criado: $REDSHIFT_CLUSTER"

# Criar tabela no Redshift
SQL_STATEMENT="CREATE TABLE logs_processed (log_id INT IDENTITY(1,1), user_ip VARCHAR(50), url VARCHAR(500), response_code INT, event_time TIMESTAMP);"
aws redshift-data execute-statement --cluster-identifier $REDSHIFT_CLUSTER \
    --database $REDSHIFT_DB --db-user $REDSHIFT_USER --sql "$SQL_STATEMENT"

echo "Tabela logs_processed criada no Redshift"

echo "Setup concluído com sucesso! 🚀"
