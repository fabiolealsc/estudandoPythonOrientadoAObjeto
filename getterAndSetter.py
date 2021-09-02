
class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    
    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
        

p1 = Produto('CAMISA', 50)
p1.desconto(10)
print(p1.preco, p1.nome)


p2 = Produto('CANECA', 'R$30')
p2.desconto(10)
print(p2.preco, p2.nome)