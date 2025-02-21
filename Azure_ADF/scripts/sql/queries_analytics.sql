-- Consulta combinando Clientes (SQL Server) e Vendas (MySQL)
SELECT c.Nome AS Cliente, p.Nome AS Produto, v.Quantidade, v.DataVenda
FROM Clientes c
JOIN Pedidos pd ON c.ClienteID = pd.ClienteID
JOIN Vendas v ON pd.PedidoID = v.VendaID
JOIN Produtos p ON v.ProdutoID = p.ProdutoID;