# Fluxo de Processamento

1. **Extração de Tweets**:
   - Coletar tweets usando a API do Twitter.
   - Salvar dados brutos em formato JSON.

2. **Pré-processamento**:
   - Limpar e tokenizar os textos.
   - Salvar dados processados em formato Parquet.

3. **Análise de Sentimentos**:
   - Treinar um modelo de regressão logística.
   - Salvar o modelo treinado.

4. **Monitoramento**:
   - Registrar o modelo no MLflow.
   - Acompanhar métricas e versões do modelo.