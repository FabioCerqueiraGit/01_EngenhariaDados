# Fluxo de Integração de Dados

## Passo a Passo

1. **Coleta de Dados**:
   - Utilizar o Azure Data Factory para coletar dados de:
     - SQL Server: Tabelas `Clientes` e `Pedidos`.
     - MySQL: Tabelas `Produtos` e `Vendas`.

2. **Armazenamento Temporário**:
   - Salvar os dados brutos no Azure Blob Storage (`data/raw/`).

3. **Transformação de Dados**:
   - Aplicar transformações como limpeza, filtragem e enriquecimento.
   - Salvar os dados processados no Azure Blob Storage (`data/processed/`).

4. **Carga no Data Warehouse**:
   - Carregar os dados processados no Azure SQL Database.

5. **Análise no Power BI**:
   - Conectar o Power BI ao Azure SQL Database.
   - Criar dashboards para análise de dados.

## Pipeline no ADF
- **Atividade 1**: Copiar dados do SQL Server para o Blob Storage.
- **Atividade 2**: Transformar dados usando Data Flow.
- **Atividade 3**: Carregar dados no Azure SQL Database.