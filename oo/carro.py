"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1 - Motor
2 - Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1 - Atributo de dado velocidade
2 - Método acelerar, que deverá incremetar a velocidade de uma unidade.
3 - Método frear que deverá decrementar a velocidade em duas unidades.

A Direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:

1 - Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar_a_direita
3 - Método girar_a_esquerda

    N
o       l
    S
"""

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0

        return self.velocidade


class Direcao:
    def __init__(self, direcao='Norte'):
        self.direcao = direcao

    def girar_a_direita(self):
        if self.direcao =='Norte':
            self.direcao = 'Leste'
        elif self.direcao =='Leste':
            self.direcao ='Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'
    
        return self.direcao

    def girar_a_esquerda(self):
        if self.direcao =='Norte':
            self.direcao = 'Oeste'
        elif self.direcao =='Oeste':
            self.direcao ='Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'

        return self.direcao


class Carro():
    def __init__(self, motor, direcao):
        self.direcao = direcao
        self.motor = motor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.direcao

    def frear(self):
        return self.motor.frear()

    def acelerar(self):
        return self.motor.acelerar()

    def calcular_velocidade(self):
        return self.motor.velocidade

if __name__ == '__main__':
    #teste motor
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    # Testando Direcao
    direcao = Direcao()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)

    carro = Carro(motor, direcao)
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.calcular_direcao())
    print(carro.girar_a_esquerda())
   # print(carro.calcular_direcao())
















