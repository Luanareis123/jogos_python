
# Laços de repetição = While ou for variavel in range (numero de repetição)
# {:f}.format (1.50) serve para formatar um numero float. Sendo f float e dentro disso colocamos quantas casas
    #decimais queremos etc.. se for um numero inteiro colocamos {:d}
# random: ele gera numeros aleatorios. O random precisa ser importado / import = random.random()
# abs é um numero absoluto ( não importa o que eu coloque (-10;10;10.0) fica sempre o numero inteiro.
import random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    random.seed(100)
    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print ("Qual nível de dificuldade?")
    print ("(1) Fácil (2) Médio (3) Dificil")
    nivel = int(input("Digite o nível do jogo que você deseja: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 6
    else:
        total_tentativas = 3

    for  rodada in range (1, total_tentativas + 1):
        print ("Tentativa {} de {}".format(rodada, total_tentativas))

        numero_usuario = int(input("Digite um numero entre 1 e 100: "))
        print ("Você digitou ", numero_usuario)

        if(numero_usuario < 1 or numero_usuario > 100):
            print ("Você deve digitar um numero entre 1 e 100!")


        acertou = numero_secreto == numero_usuario
        numero_maior = numero_usuario > numero_secreto
        numero_menor = numero_usuario < numero_secreto

        if (acertou):
            print ("Você acertou e fez {} pontos. Parabéns!" .format(pontos))
            break
        else:
            if (numero_maior):
                print ("Você errou! o seu numero foi maior do que o numero secreto")
            elif (numero_menor):
                print ("Você errou! O seu numero foi menor do que o numero secreto.")
                pontos_perdidos = abs (numero_secreto - numero_usuario)
                pontos = pontos - pontos_perdidos


    print ("Fim do jogo!")

if(__name__=="__main__"):
    jogar()