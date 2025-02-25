from django.urls import path
from . import views


urlpatterns = [
    path("", views.listar_produtos, name="listar_produtos"),
    path("produto/<int:produto_id>/", views.detalhe_produto, name="detalhe_produto"),
    path("carrinho/", views.ver_carrinho, name="ver_carrinho"),
    path("carrinho/adicionar/<int:produto_id>/", views.adicionar_ao_carrinho, name="adicionar_ao_carrinho"),
    path("pedido/finalizar/", views.finalizar_pedido, name="finalizar_pedido"),
    path("pedido/pagamento/<int:pedido_id>/", views.pagina_pagamento, name="pagina_pagamento"),
    path("pedido/pagar/<int:pedido_id>/", views.processar_pagamento, name="processar_pagamento"),
    path("pedidos/", views.pedidos_cliente, name="pedidos_cliente"),
]
