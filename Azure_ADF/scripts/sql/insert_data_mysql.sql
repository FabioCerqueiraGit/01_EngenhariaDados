-- Inserir dados na tabela Produtos
INSERT INTO Produtos (ProdutoID, Nome, Preco) VALUES
(1, 'Notebook', 3500.00),
(2, 'Smartphone', 1500.00);

-- Inserir dados na tabela Vendas
INSERT INTO Vendas (VendaID, ProdutoID, DataVenda, Quantidade) VALUES
(1, 1, '2023-01-10', 2),
(2, 2, '2023-01-12', 5);