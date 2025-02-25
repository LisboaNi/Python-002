from django.db import models

# Modelo Empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    cor_tema = models.CharField(max_length=7, blank=True, null=True)  # Exemplo: #FF5733
    imagem_destaque = models.ImageField(upload_to="destaques/", blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo Produto
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    tamanho = models.CharField(max_length=10, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    contato = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

# Modelo Carrinho
class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"

# Modelo Pedido
class Pedido(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("enviado", "Enviado"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

# Modelo Pedido_Produto (Relacionamento N:N)
class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no Pedido {self.pedido.id}"

# Modelo Pagamento
class Pagamento(models.Model):
    METODO_CHOICES = [
        ("pix", "PIX"),
        ("cartao", "Cartão de Crédito"),
        ("boleto", "Boleto Bancário"),
    ]
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("recusado", "Recusado"),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=10, choices=METODO_CHOICES, default="pix")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento {self.id} - {self.pedido.cliente.nome}"
