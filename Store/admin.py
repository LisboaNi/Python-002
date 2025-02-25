from django.contrib import admin

from .models import Empresa, Produto, Cliente, Carrinho, Pedido, PedidoProduto, Pagamento

admin.site.register(Empresa)
admin.site.register(Produto)
admin.site.register(Pedido)

# admin.site.register(Cliente)
# admin.site.register(Carrinho)
# admin.site.register(PedidoProduto)
# admin.site.register(Pagamento)



