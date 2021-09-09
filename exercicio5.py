
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o primeiro nome: ")
nome3 = input("Digite o primeiro nome: ")

lista_nomes = [nome1, nome2, nome3]

nome = input("Qual nome voce quer saber se existe na lista? ")
if nome in lista_nomes:
    print("{} esta na lista!".format(nome))
else:
    print("{} nao esta na lista :(".format(nome))    