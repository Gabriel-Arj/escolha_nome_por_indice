def num_nom():
    print("Ohayo " + nome[nom_num])
def drgn():
    drgn_inpt = input("O que você achou GPT?")
nome = ["Gabriel", "Talita", "Edivaldo", "Graça"]
nom_num = int(input("Escolha um numero de 0 a 3: "))
while nom_num not in range(len(nome)):
    print("Esse numero não esta corrento, tente novamente")
    nom_num = int(input("Escolha um numero de 0 a 3: "))

num_nom()
drgn()