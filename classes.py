class Escritor:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca) -> None:
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo!')


class MaquinaDeEscrever():
    def __init__(self) -> None:
        pass
    
    def escrever(self):
        print('Máquina está escrevendo!')
        