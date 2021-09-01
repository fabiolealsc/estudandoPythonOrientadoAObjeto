#Programa para aprender Classe e metodo

class Pessoa:
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo!')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando!')
            return

        print(f'{self.nome} está falando sobre {assunto}!')
        self.falando = True
    

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        
        print(f'{self.nome} parou de falar!')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja está comendo')
            return
        
        if self.falando:
            print(f'{self.nome} está falando e não pode comer!')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return
        
        print(f'{self.nome} parou de comer!')
        self.comendo = False