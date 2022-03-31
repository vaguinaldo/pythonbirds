class Pessoa:
    #atributo de classe
    olhos=2
    def __init__(self, *filhos, nome=None, idade=29):
        #atalho alt + enter cria os atributos
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola meu nome é {self.nome}'

    #Decorators
    @staticmethod
    def metodo_estatico():
        return 42

    #Decorators
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'olhos {cls.olhos} '


class Homen(Pessoa):
    def cumprimentar(self):
        #cumprimentar_da_class_pai = Pessoa.cumprimentar(self)
        cumprimentar_da_class_pai = super().cumprimentar()
        return f'{cumprimentar_da_class_pai}. Aperto de mão'


class Mutante(Pessoa):
    # sobrescrita de atributos
    olhos = 3



if __name__ == '__main__':
    vagui = Homen(nome='vaguinaldo')
    pedro = Pessoa(nome='pedro')
    maria = Pessoa(nome='maria')
    acir = Pessoa(nome='acir')

    joao = Mutante(vagui,pedro,maria,acir, nome='joao')
    print(vagui.idade)
    print(joao.filhos)
    print(joao.olhos)
    for filho in joao.filhos:
        print(filho.nome)

    vagui.sobrenome='pereira'
    #para deleter uma atriburo de um objeto --> del
    # del vaguinaldo.sobrenome

    print(vagui.__dict__)
    print(id(vagui.olhos))
    print(Pessoa.metodo_estatico(), vagui.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), vagui.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homen))
    print(isinstance(vagui, Pessoa))
    print(isinstance(vagui, Homen))
    print(vagui.olhos)
    print(joao.olhos)
    print(joao.cumprimentar())
    print(vagui.cumprimentar())


