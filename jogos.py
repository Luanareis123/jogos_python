import forca
import ADIVINHACAO

def escolher_jogo():

    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int (input("Digite qual o jogo você quer jogar:"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        ADIVINHACAO.jogar()

if(__name__=="__main__"):
    escolher_jogo()
