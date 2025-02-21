# Análise de Sentimentos com Databricks e Spark

## Objetivo
Processar e analisar grandes volumes de dados de redes sociais utilizando Databricks e Apache Spark.

## Tecnologias
- Databricks
- Apache Spark
- Delta Lake
- MLflow

## Cenário
1. Extração de tweets.
2. Análise de sentimentos com Spark MLlib.
3. Armazenamento de dados processados no Delta Lake.

## Destaques
- Processamento distribuído com Spark.
- Modelagem de dados para IA.
- Versionamento e monitoramento de modelos com MLflow.

## Como Executar
1. Clone este repositório.
2. Siga as instruções em `docs/arquitetura.md` para configurar o ambiente.
3. Execute os notebooks na ordem numérica.

## Dúvidas frequentes sobre este projeto:

1. Usou aprendizado supervisionado, não-supervisionado ou por reforço?
Resposta: Aprendizado Supervisionado.

Justificativa: O projeto envolve a análise de sentimentos, onde o modelo é treinado com um conjunto de dados rotulado (tweets classificados como positivos, negativos ou neutros). O objetivo é prever o sentimento de novos tweets com base nesses rótulos.

2. Usou uma tarefa de classificação, de regressão (múltipla, univariada ou multivariada) ou outra coisa?
Resposta: Classificação.

Justificativa: A tarefa consiste em classificar os tweets em categorias discretas (positivo, negativo, neutro). Portanto, é um problema de classificação multiclasse (com três classes possíveis).

3. Você usou técnicas de aprendizado em batch ou online?
Resposta: Aprendizado em Batch.

Justificativa: O projeto utiliza um conjunto de dados estático (tweets coletados previamente) para treinar o modelo. Além disso, o Apache Spark é otimizado para processamento em batch, onde os dados são processados em grandes lotes. O aprendizado online seria mais adequado para cenários onde os dados chegam em fluxo contínuo e o modelo precisa ser atualizado em tempo real.

4. Qual foi a medida de desempenho? RMSE ou MAE?
Resposta: Nenhuma das duas.

Justificativa: Como se trata de um problema de classificação, as métricas mais comuns são:

Acurácia: Proporção de previsões corretas em relação ao total.

Precisão: Proporção de previsões positivas corretas.

Recall: Proporção de casos positivos corretamente identificados.

F1-Score: Média harmônica entre precisão e recall.

Matriz de Confusão: Para visualizar o desempenho do modelo em cada classe.

RMSE (Root Mean Squared Error) e MAE (Mean Absolute Error) são métricas típicas de problemas de regressão, onde o objetivo é prever valores contínuos, e não classificações.

