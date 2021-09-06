from classes import Caneta, Escritor, MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
#print(escritor.nome)
#print(caneta.marca)
#maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
del escritor
#print(escritor)
print(caneta.marca)
maquina.escrever()