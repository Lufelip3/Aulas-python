import os
os.system("cls")
os.system("color 2")

#ESTRUTURA DE REPETIÇÃO WHILE

#break -> QUEBRA CONDIÇÃO
# i=0
# while i<11:
#      print(i)
#      i+=1 #-> i++ -> i = i +1

#ex 01
# i=0
# while i<20:
#     print(i)
#     i+=1

# #ex 02
# i=25
# while i<=50:
#     print(i)
#     i+=1

#ex 03

# print("1 - Cadastra o nome | 2 - Cadastra o cpf | 3 - Cadastra a idade | 4 - Sai do programa")
# i=0
# while i<4:
#     i = int(input("\nDigite a opção desejada: "))
#     if i==1:
#         nome=input("Digite o nome: ")
#     elif i==2:
#         cpf=input("Digite o CPF: ")
#     elif i==3:
#         idade=int(input("Digite a idade: "))
# else:
#     print("\nNome:",nome)
#     print("CPF:",cpf)
#     print("Idade:",idade)

import random

numero = -2
num = -1
while num!=numero:
    numero = random.randint(0,5)
    num = int(input("Tente acertar o numero que a maquina pensou: "))
    if num!=numero:
        print(f"""\nVocê errou :(
A máquina pensou {numero}
Você digitou {num}""")
else:
    print("\nPARABÉNS, VOCÊ ACERTOU :)")