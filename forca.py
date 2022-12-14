def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Forca!")
    print("*********************************")
#for verifica se algo esta em outro algo
#palavra.find("n").... find verifica se determinada letra esta na palavra.

    palavra_secreta ="Banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False

    print (letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


    print ("Fim do jogo!")

if(__name__=="__main__"):
    jogar()

