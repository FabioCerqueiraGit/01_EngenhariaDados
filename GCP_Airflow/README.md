# Pipeline de ETL com Apache Airflow no Google Cloud Platform (GCP) 🚀

## Visão Geral
Este projeto implementa um pipeline de ETL utilizando o Apache Airflow para orquestração no Google Cloud Platform (GCP). O objetivo é extrair dados de uma API de e-commerce, processá-los com Apache Beam no Dataflow e armazená-los no BigQuery para análises futuras.

## Arquitetura do Pipeline
1. **Extração**: Coleta de dados de vendas de uma API REST e armazenamento temporário no Google Cloud Storage (GCS).
2. **Transformação**: Processamento dos dados utilizando Apache Beam e execução no Dataflow.
3. **Carga**: Armazenamento dos dados processados no BigQuery para análise.
4. **Orquestração**: O Apache Airflow gerencia todas as etapas do pipeline.

## Tecnologias Utilizadas
- **Google Cloud Platform (GCP)**
- **Apache Airflow** para orquestração
- **Google Cloud Storage (GCS)** para armazenamento de dados brutos
- **Apache Beam & Dataflow** para transformação de dados
- **BigQuery** para armazenamento e análise dos dados
- **Cloud Composer** para execução gerenciada do Airflow

## Configuração do Ambiente
### Pré-requisitos
1. Conta ativa no Google Cloud Platform (GCP)
2. Projeto configurado no GCP com faturamento habilitado
3. APIs do Cloud Storage, Dataflow, BigQuery e Cloud Composer ativadas
4. Ambiente do Cloud Composer configurado com Apache Airflow

### Passos de Configuração
1. Criar um bucket no Google Cloud Storage:
   ```sh
   gsutil mb gs://meu-bucket-de-dados
   ```
2. Criar um dataset no BigQuery:
   ```sql
   CREATE DATASET ecommerce_sales;
   ```
3. Configurar o ambiente do Cloud Composer pelo console do GCP.

## Estrutura do Repositório
```
📂 GCP_Airflow
 ┣ 📂 dags
 ┃ ┣ 📜 etl_pipeline.py  # DAG do Apache Airflow
 ┣ 📂 data
 ┃ ┣ 📜 sample_data.json  # Dados de exemplo
 ┣ 📂 scripts
 ┃ ┣ 📜 transform.py  # Código para Apache Beam
 ┣ 📜 README.md
```

## Execução do Pipeline
1. Subir a DAG do Airflow no Cloud Composer.
2. A DAG extrai os dados da API e os armazena no GCS.
3. O Apache Beam processa os dados e os salva no BigQuery.
4. O pipeline pode ser monitorado pelo Airflow.

## Próximos Passos
- Melhorar a eficiência do pipeline com otimizações no Dataflow.
- Implementar monitoramento detalhado com Stackdriver.
- Adicionar testes automatizados para validação de dados.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. 🚀

