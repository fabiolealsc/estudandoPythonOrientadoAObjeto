"""
public, protected, private
_ protect
__ private
"""

class BaseDeDados:
    def __init__(self) -> None:
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listaClientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1, 'Otávio')
bd.inserir_clientes(2, 'Luiza')
bd.inserir_clientes(3, 'Maria')
bd.__dados = 'Outra Coisa'
bd.listaClientes()