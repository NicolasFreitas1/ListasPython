e1 = input("Digite o primeiro elemento: ")
e2 = input("Digite o segundo elemento: ")
e3 = input("Digite o terceiro elemento: ")

lista = [e1,e2,e3]
print(lista)

e = print("Qual elemento voce quer saber a posição da lista: ")

if e in lista:
    print("{} esta na posição: ".format(e), lista.index(e))
else:
    print("{} nao está na lista ".format(e))
