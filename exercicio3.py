nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

lista_notas = [nota1,nota2,nota3,nota4]

mean = sum(lista_notas)/len(lista_notas)

print("Sua média é: {}".format(mean))