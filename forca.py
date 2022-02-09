def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("qual a letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("encontrei a letra {} na posição {}".format(letra, index+1))
            index = index+1

        print("jogando...")

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()