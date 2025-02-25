from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Produto, Carrinho, Pedido, PedidoProduto, Cliente, Pagamento, Empresa
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ClienteForm
from django.contrib.auth import login, authenticate

#  Listar todos os produtos
def listar_produtos(request):
    nome = request.GET.get("nome")
    if nome:
        produtos = Produto.objects.filter(nome__icontains=nome)
    else:
        produtos = Produto.objects.all()   
    
    empresa = Empresa.objects.first()

    return render(request, "Store/produtos.html", {"produtos": produtos, 'empresa': empresa})

#  Detalhar um produto específico
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, "Store/detalhe_produto.html", {"produto": produto})

# Cadastrar um cliente
def cadastrar_cliente(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            login(request, user)
            return redirect('listar_produtos')
    else:
        user_form = UserForm()
        cliente_form = ClienteForm()
    return render(request, 'Store/cadastrar_cliente.html', {'user_form': user_form, 'cliente_form': cliente_form})





#  Adicionar produto ao carrinho
@login_required
def listar_pedidos(request):
    cliente = Cliente.objects.get(user=request.user)
    pedidos = Pedido.objects.filter(cliente=cliente)
    return render(request, 'Store/pedidos_cliente.html', {'pedidos': pedidos})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    cliente = Cliente.objects.get(user=request.user)

    # Verifica se o produto já está no carrinho do cliente
    item, created = Carrinho.objects.get_or_create(cliente=cliente, produto=produto)
    if not created:
        item.quantidade += 1
    item.total = item.quantidade * produto.preco
    item.save()

    return redirect('ver_carrinho')

#  Ver carrinho
@login_required
def ver_carrinho(request):
    cliente = Cliente.objects.get(email=request.user.email)
    carrinho = Carrinho.objects.filter(cliente=cliente)
    total_carrinho = sum(item.total for item in carrinho)

    return render(request, "Store/carrinho.html", {"carrinho": carrinho, "total": total_carrinho})

#  Criar um pedido a partir do carrinho
@login_required
def finalizar_pedido(request):
    cliente = Cliente.objects.get(email=request.user.email)
    carrinho = Carrinho.objects.filter(cliente=cliente)

    if not carrinho.exists():
        return redirect("ver_carrinho")

    # Criar pedido
    pedido = Pedido.objects.create(cliente=cliente, data=now(), total=sum(item.total for item in carrinho))

    # Adicionar produtos ao pedido
    for item in carrinho:
        PedidoProduto.objects.create(pedido=pedido, produto=item.produto, quantidade=item.quantidade)
        item.produto.estoque -= item.quantidade  # Reduz estoque
        item.produto.save()

    # Limpar carrinho
    carrinho.delete()

    return redirect("pagina_pagamento", pedido_id=pedido.id)

#  Página de pagamento
@login_required
def pagina_pagamento(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente__email=request.user.email)
    return render(request, "Store/pagamento.html", {"pedido": pedido})

#  Processar pagamento (simulação)
@login_required
def processar_pagamento(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente__email=request.user.email)

    # Simulação: aprovar pagamento
    pagamento = Pagamento.objects.create(
        pedido=pedido,
        metodo="pix",
        valor=pedido.total,
        status="aprovado",
        data=now(),
    )

    pedido.status = "aprovado"
    pedido.save()

    return redirect("pedidos_cliente")

#  Listar pedidos do cliente
@login_required
def pedidos_cliente(request):
    cliente = Cliente.objects.get(email=request.user.email)
    pedidos = Pedido.objects.filter(cliente=cliente)
#     empresa = Empresa.objects.first()

#     return render(request, "Store/pedidos.html", {"pedidos": pedidos, 'empresa': empresa})
