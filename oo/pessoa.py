class Pessoa:
    def __init__(self,*filhos, nome = None, idade=35):
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
    print(luciano.__dict__)  #atributos de instancia fica aqui
    print(mauricio.__dict__)



