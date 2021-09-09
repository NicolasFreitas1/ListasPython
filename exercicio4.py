n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input("Digite o Segundo numero: "))
n3 = int(input("Digite o Terceiro numero: "))
n4 = int(input("Digite o Quarto numero: "))
n5 = int(input("Digite o Quinto numero: "))

lista_num = [n1,n2,n3,n4,n5]
print(lista_num)

soma = sum(lista_num)

print("A soma dos numeros anteriores é de: {}".format(soma))