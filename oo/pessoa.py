class Pessoa:
    def __init__(self, *filhos, nome=None, idade=29):
        #atalho alt + enter cria os atributos
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola{id(self)}'


if __name__ == '__main__':
    vagui = Pessoa(nome='vaguinaldo')
    joao = Pessoa(vagui, nome='joao')
    print(vagui.idade)
    print(joao.filhos)
    for filho in joao.filhos:
        print(filho.nome)
