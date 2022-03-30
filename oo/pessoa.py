class Pessoa:
    def __init__(self, nome=None, idade=29):
        #atalho alt + enter cria os atributos
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola{id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(id(p))
    print(Pessoa.cumprimentar(p))
    p.nome = 'vaguinaldo'
    print(p.nome)

