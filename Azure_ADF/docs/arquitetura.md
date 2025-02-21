# Arquitetura do Projeto

## Visão Geral
Este projeto tem como objetivo integrar dados de múltiplas fontes (SQL Server e MySQL) em um Data Warehouse no Azure, utilizando o Azure Data Factory (ADF) para orquestração e o Power BI para análise.

## Componentes Principais
1. **Fontes de Dados**:
   - SQL Server: Dados de clientes e pedidos.
   - MySQL: Dados de produtos e vendas.

2. **Azure Data Factory (ADF)**:
   - Pipeline de integração para coletar, transformar e carregar dados.

3. **Azure Blob Storage**:
   - Armazenamento temporário para dados brutos e processados.

4. **Azure SQL Database**:
   - Data Warehouse para armazenar dados consolidados.

5. **Power BI**:
   - Dashboard para análise e visualização dos dados.

## Fluxo de Dados
1. Coleta de dados brutos das fontes (SQL Server e MySQL).
2. Armazenamento temporário no Azure Blob Storage.
3. Transformação e enriquecimento dos dados.
4. Carga dos dados processados no Azure SQL Database.
5. Análise e visualização no Power BI.