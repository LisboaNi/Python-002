// loja/static/js/scripts.js

// Função para filtrar pedidos pelo campo de pesquisa
function searchPedidos() {
    let searchInput = document.getElementById("search-box").value.toLowerCase();
    let pedidos = document.querySelectorAll(".pedido-item");

    pedidos.forEach(pedido => {
        let pedidoText = pedido.textContent.toLowerCase();
        if (pedidoText.includes(searchInput)) {
            pedido.style.display = "block";
        } else {
            pedido.style.display = "none";
        }
    });
}
