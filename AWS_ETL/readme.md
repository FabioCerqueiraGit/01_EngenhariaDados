# Pipeline de Logs com AWS Glue e Redshift 🚀

## 📌 Descrição
Este projeto implementa um pipeline de ETL na AWS para processar logs de acessos web. O pipeline extrai, transforma e carrega (ETL) dados de logs armazenados no Amazon S3 para um cluster do Amazon Redshift, utilizando AWS Glue para processamento e transformação dos dados.

## 🏗️ Arquitetura
1. **Amazon S3**: Armazena os arquivos brutos de logs.
2. **AWS Glue**: Executa o job de ETL para processar e transformar os logs.
3. **Amazon Redshift**: Armazena os dados transformados para análises.
4. **AWS Lambda (Opcional)**: Pode ser usado para acionar o Glue quando novos logs forem adicionados ao S3.

## 🛠️ Tecnologias Utilizadas
- AWS S3
- AWS Glue
- AWS Lambda (Opcional)
- Amazon Redshift
- AWS IAM

## 📂 Estrutura do Projeto
```
aws-etl-project/
│── data/
│   ├── raw_logs/  # Logs brutos
│   ├── processed_logs/  # Logs transformados
│── scripts/
│   ├── etl_glue.py  # Script do job AWS Glue
│   ├── setup_aws.sh  # Script para criação da infraestrutura
│── README.md
```

## 🚀 Como Executar o Projeto
1. **Configurar a AWS CLI:**
   ```bash
   aws configure
   ```
2. **Executar o script de configuração:**
   ```bash
   ./setup_aws.sh
   ```
3. **Executar o job do AWS Glue:**
   ```bash
   aws glue start-job-run --job-name etl-glue-job
   ```
4. **Validar os dados no Redshift**
   ```sql
   SELECT * FROM logs_processed LIMIT 10;
   ```

## 📌 Próximos Passos
- Implementar monitoramento com AWS CloudWatch.
- Criar alertas para falhas no pipeline.
- Otimizar queries no Redshift para melhor performance.

---
📌 **Dúvidas ou sugestões? Fique à vontade para contribuir!** 🚀

