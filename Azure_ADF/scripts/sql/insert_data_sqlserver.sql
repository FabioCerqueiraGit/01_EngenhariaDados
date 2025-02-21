-- Inserir dados na tabela Clientes
INSERT INTO Clientes (ClienteID, Nome, Email) VALUES
(1, 'João Silva', 'joao.silva@example.com'),
(2, 'Maria Oliveira', 'maria.oliveira@example.com');

-- Inserir dados na tabela Pedidos
INSERT INTO Pedidos (PedidoID, ClienteID, DataPedido, Valor) VALUES
(1, 1, '2023-01-15', 150.00),
(2, 2, '2023-01-20', 200.00);