# Projetos de Engenharia de Dados 🚀

Este repositório contém quatro projetos de Engenharia de Dados utilizando diferentes tecnologias e provedores de nuvem. Cada projeto aborda um cenário real de pipeline de dados, desde a extração até a visualização e análise.

## Projetos

### 1. Pipeline de ETL com Apache Airflow no Google Cloud Platform (GCP)

**Objetivo:** Construir um pipeline de ETL para processamento de dados de vendas, utilizando Google Cloud Storage, Dataflow e BigQuery, com orquestração via Apache Airflow.

- **Tecnologias:** Apache Airflow, Google Cloud Storage, Apache Beam, Dataflow, BigQuery
- **Cenário:** Extração de dados de uma API de e-commerce, transformação com Apache Beam e carga no BigQuery para análise.
- **Destaques:** Automatiso e monitoramento com Airflow, escalabilidade no Dataflow, análise via SQL no BigQuery.

### 2. Pipeline de Logs com AWS Glue e Redshift

**Objetivo:** Criar um pipeline para ingestão e processamento de logs de acessos web na AWS, utilizando S3, AWS Glue e Redshift.

- **Tecnologias:** AWS S3, AWS Glue, AWS Lambda, Amazon Redshift
- **Cenário:** Coleta de logs de acesso, processamento e transformação no AWS Glue, carga no Redshift para consulta e relatórios.
- **Destaques:** Uso de AWS Glue para ETL serverless, armazenamento escalável no S3, otimização de consultas no Redshift.

### 3. Integração de Dados com Azure Data Factory (ADF)

**Objetivo:** Integrar múltiplas fontes de dados para um Data Warehouse no Azure.

- **Tecnologias:** Azure Data Factory, Azure SQL Database, Azure Blob Storage, Power BI
- **Cenário:** Coleta de dados de SQL Server e MySQL, armazenamento em Data Lake e carga para Data Warehouse no Azure SQL Database.
- **Destaques:** Orquestração com ADF, integração de dados heterogêneos, análise no Power BI.

### 4. Análise de Sentimentos com Databricks e Spark

**Objetivo:** Processar e analisar grandes volumes de dados de redes sociais utilizando Databricks e Apache Spark.

- **Tecnologias:** Databricks, Apache Spark, Delta Lake, MLflow
- **Cenário:** Extração de tweets, análise de sentimentos com Spark MLlib e armazenamento de dados processados no Delta Lake.
- **Destaques:** Processamento distribuído com Spark, modelagem de dados para IA, versão e monitoramento de modelos com MLflow.

## Como Executar os Projetos

Cada projeto possui um guia próprio na respectiva pasta do repositório, com instruções detalhadas sobre setup, dependências e execução.

Fique à vontade para explorar, contribuir e sugerir melhorias! 🚀
