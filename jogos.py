import forca
import adivinhacao
def escolhe_jogo():
    print("*********************************")
    print("BEscolha seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adiivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo==1:
        print ("jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()