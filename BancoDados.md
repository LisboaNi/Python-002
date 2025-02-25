## 📂 Estrutura Completa do Banco de Dados  

### 1️⃣ **Tabela Empresa** (Nova)  
| Campo           | Tipo         | Descri\u00e7\u00e3o                                       |
|----------------|-------------|------------------------------------------------|
| id             | INT (PK)    | Identificador \u00fanico da empresa                 |
| nome           | VARCHAR     | Nome da empresa                                |
| email          | VARCHAR     | E-mail de contato                              |
| telefone       | VARCHAR     | Telefone ou WhatsApp                           |
| logo           | VARCHAR     | Caminho ou URL da logo                        |
| cor_tema       | VARCHAR(7)  | Cor principal do site (ex: `#FF5733`)         |
| imagem_destaque | VARCHAR   | Caminho ou URL da imagem principal            |
| descricao      | TEXT        | Descri\u00e7\u00e3o sobre a empresa                     |

---

### 2️⃣ **Tabela Produto**  
| Campo      | Tipo         | Descri\u00e7\u00e3o                         |
|------------|-------------|----------------------------------|
| id         | INT (PK)    | Identificador \u00fanico do produto  |
| nome       | VARCHAR     | Nome do produto                 |
| preco      | DECIMAL     | Pre\u00e7o do produto                |
| descricao  | TEXT        | Descri\u00e7\u00e3o detalhada             |
| tamanho    | VARCHAR     | Tamanho (P, M, G, etc.)         |
| cor        | VARCHAR     | Cor do produto                  |
| estoque    | INT         | Quantidade dispon\u00edvel           |
| imagem     | VARCHAR     | Caminho do arquivo da imagem    |

---

### 3️⃣ **Tabela Cliente**  
| Campo    | Tipo         | Descri\u00e7\u00e3o                         |
|----------|-------------|----------------------------------|
| id       | INT (PK)    | Identificador \u00fanico do cliente  |
| nome     | VARCHAR     | Nome completo                   |
| cpf      | VARCHAR(11) | CPF do cliente                  |
| contato  | VARCHAR     | Telefone ou WhatsApp            |
| email    | VARCHAR     | E-mail do cliente               |

---

### 4️⃣ **Tabela Carrinho**  
| Campo       | Tipo      | Descri\u00e7\u00e3o                         |
|------------|----------|----------------------------------|
| id         | INT (PK) | Identificador do carrinho       |
| cliente_id | INT (FK) | Cliente que possui o carrinho   |
| produto_id | INT (FK) | Produto adicionado ao carrinho  |
| quantidade | INT      | Quantidade do produto           |
| total      | DECIMAL  | Valor total do item no carrinho |

---

### 5️⃣ **Tabela Pedido**  
| Campo       | Tipo         | Descri\u00e7\u00e3o                          |
|------------|-------------|-----------------------------------|
| id         | INT (PK)    | Identificador \u00fanico do pedido   |
| cliente_id | INT (FK)    | Cliente que fez o pedido        |
| data       | TIMESTAMP   | Data da compra                  |
| total      | DECIMAL     | Valor total do pedido           |
| status     | ENUM        | Status do pedido (pendente, aprovado, enviado, cancelado) |

---

### 6️⃣ **Tabela Pedido_Produto (Relacionamento N:N)**  
| Campo       | Tipo      | Descri\u00e7\u00e3o                          |
|------------|----------|-----------------------------------|
| id         | INT (PK) | Identificador \u00fanico               |
| pedido_id  | INT (FK) | Refer\u00eancia ao pedido              |
| produto_id | INT (FK) | Produto comprado                  |
| quantidade | INT      | Quantidade do produto no pedido  |

---

### 7️⃣ **Tabela Pagamento**  
| Campo       | Tipo         | Descri\u00e7\u00e3o                          |
|------------|-------------|-----------------------------------|
| id         | INT (PK)    | Identificador do pagamento       |
| pedido_id  | INT (FK)    | Pedido associado ao pagamento   |
| metodo     | VARCHAR     | M\u00e9todo de pagamento (Pix, Cart\u00e3o, Boleto) |
| valor      | DECIMAL     | Valor pago                       |
| status     | ENUM        | Status do pagamento (pendente, aprovado, recusado) |
| data       | TIMESTAMP   | Data e hora do pagamento         |

---

### 🔗 **Relacionamentos Importantes**  
- **Pedido** ligado a **Cliente** (cada cliente pode ter vários pedidos).
- **Pedido_Produto** faz o relacionamento entre **Pedido** e **Produto**.  
- **Carrinho** pertence a um **Cliente** e pode ter **Produtos**.  
- **Pagamento** associado a um **Pedido**.  
- **Empresa** contém informações da loja e personalização do site.

---