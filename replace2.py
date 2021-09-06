from classes2 import CarrinhoDeComprar, Produto

carrinho = CarrinhoDeComprar()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserirProduto(p1)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)
carrinho.inserirProduto(p1)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)

carrinho.listaProdutos()
print(carrinho.somaTotal())