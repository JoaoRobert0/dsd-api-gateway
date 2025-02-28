const express = require('express');
const app = express();

// Middleware para interpretar o corpo das requisições em JSON
app.use(express.json());

// Armazenamento em memória para produtos (simulando um banco de dados)
let produtos = [
  { id: 1, nome: 'Produto A', preco: 10 },
  { id: 2, nome: 'Produto B', preco: 20 }
];

// Rota para criar um novo produto
app.post('/produtos', (req, res) => {
  const { nome, preco } = req.body;

  if (!nome || !preco) {
    return res.status(400).json({ error: 'Nome e preço são obrigatórios' });
  }

  const novoProduto = {
    id: produtos.length + 1,
    nome,
    preco
  };

  produtos.push(novoProduto);
  res.status(201).json(novoProduto);
});

// Rota para listar todos os produtos
app.get('/produtos', (req, res) => {
  res.status(200).json(produtos);
});

// Rota para listar um produto específico
app.get('/produtos/:id', (req, res) => {
  const produto = produtos.find(p => p.id === parseInt(req.params.id));

  if (!produto) {
    return res.status(404).json({ error: 'Produto não encontrado' });
  }

  res.status(200).json(produto);
});

// Rota para atualizar um produto
app.put('/produtos/:id', (req, res) => {
  const produto = produtos.find(p => p.id === parseInt(req.params.id));

  if (!produto) {
    return res.status(404).json({ error: 'Produto não encontrado' });
  }

  const { nome, preco } = req.body;

  if (nome) produto.nome = nome;
  if (preco) produto.preco = preco;

  res.status(200).json(produto);
});

// Rota para deletar um produto
app.delete('/produtos/:id', (req, res) => {
  const index = produtos.findIndex(p => p.id === parseInt(req.params.id));

  if (index === -1) {
    return res.status(404).json({ error: 'Produto não encontrado' });
  }

  produtos.splice(index, 1);
  res.status(200).json({ message: 'Produto deletado com sucesso' });
});

// Iniciar o servidor
const port = 3000;
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
