-- Tabela de Produtos
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Preco DECIMAL(10, 2)
);

-- Tabela de Vendas
CREATE TABLE Vendas (
    VendaID INT PRIMARY KEY,
    ProdutoID INT,
    DataVenda DATE,
    Quantidade INT,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);