#TIPOS DE ATRIBUTO
#atributos de instancia criados normalmente dentro do __init__
#atributos de instancia criados dinamicamente e removidos com a palavra reservada del
#atributos de instancia criados na CLASSE , o valor sendo o mesmo para todos os objetos.


class Pessoa:

    olhos = 2  # atributos de classe criado fora do dander init cria somente um atributo na memoria sem duplica-lo
    def __init__(self,*filhos, nome = None, idade=35):
       #cria atributos na memoria
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):    #Método
        return f'Olá {id(self)}'
if __name__ == '__main__':
    mauricio = Pessoa(nome='Mauricio')
    luciano = Pessoa(mauricio,nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = "Denari" # criando atributo dinamico
    del luciano.filhos #remove o atributos dinamicamente - usar atributos dinamicos qdo uma data para uso um formato diferente só apresentação web.
    luciano.olhos = 1
    del luciano.olhos # aqui apaga o atributo do objeto luciano e não da classe, voltando ao buscar o valor do objeto na classe
    print(luciano.__dict__)  # dander dict atributos de instancia fica aqui
    print(mauricio.__dict__) # não vao aparecer os atributos classe, apenas os atributos de instancia criados no __init__
    Pessoa.olhos = 3  #mudando o atributo de classe olhos para 3, mas o objeto olhos no
    print(Pessoa.olhos)
    print(mauricio.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(mauricio.olhos), id(luciano.olhos)) ##o valor eh o mesmo pois o atributo foi criado fora dander  __init__



