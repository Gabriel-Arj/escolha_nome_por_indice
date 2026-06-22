def num_nom():
    print("Olá " + nome[nom_num])
nome = ["Gabriel", "João", "Helena", "Maria"]
nom_num = int(input("Escolha um numero de 0 a 3: "))
while nom_num not in range(len(nome)):
    print("Esse numero não esta correto, tente novamente")
    nom_num = int(input("Escolha um numero de 0 a 3: "))

num_nom()
