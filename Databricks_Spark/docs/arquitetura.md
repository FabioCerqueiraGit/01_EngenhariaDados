# Arquitetura do Projeto

## Visão Geral
Este projeto utiliza Databricks e Apache Spark para processar e analisar grandes volumes de dados de redes sociais, com foco em análise de sentimentos.

## Componentes Principais
1. **Extração de Tweets**: Coleta de dados brutos da API do Twitter.
2. **Pré-processamento**: Limpeza e preparação dos dados.
3. **Análise de Sentimentos**: Treinamento de um modelo de machine learning.
4. **Armazenamento**: Dados processados são salvos no Delta Lake.
5. **Monitoramento**: Versionamento e monitoramento de modelos com MLflow.