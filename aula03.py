import os
os.system("cls")
os.system("color 2")

#ESTRUTURA CONDICIONAL IF ELSE (SE SENAO) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS: > >= < <= 1= -- AND OR

#ex01

# idade=int(input("Digite a sua idade:\n"))
# if idade >=18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

#ex02

# idade2=int(input("Digite a sua idade:\n"))
# if idade2 >0 and idade2<120:
#     print("Idade válida")
# else:
#     print("Idade inválida")

# idade=int(input("Digite a sua idade:\n"))
# if idade >0 and idade<120:
#     if idade >=18:
#         print("Você é maior de idade")
#     else:
#         print("Você é menor de idade")
# else:
#     print("Idade inválida")

#ex03

# login=input("Login: ")
# if login == "python@senai.com":
#     senha=input("Senha: ").lower()
#     if senha == "12345678":
#         print("\n---------USUÁRIO AUTENTICADO---------")
#     else:
#         print("SENHA INVÁLIDA")
# else:
#     print("USUÁRIO INVÁLIDO")

#ex04

# letra_minuscula=input("Digite uma letra: ")
# letra = letra_minuscula.upper()

# if letra == "A" or letra =="E" or letra =="I" or letra =="O" or letra =="U":
#     print(f"A letra {letra} é uma vogal.")
# else:
#     print(f"A letra {letra} é consoante.")

# letra=input("Digite uma letra: ").lower()
# if letra in "aeiou":
#     print("Vogal")
# else:
#     print("Consoante")

#ex05

# num1= float(input("Digite um numero: "))
# num2= float(input("Digite outro numero: "))

# if num1>num2:
#     print(f"O maior numero é {num1}")
#     print(f"O menor numero é {num2}")
# else:67
#     print(f"O maior numero é {num2}")
#     print(f"O menor numero é {num1}")

#ex06
maca= int(input("Quantas maçãs você deseja comprar: "))
if maca<12:
    print("-"*10, "TOTAL COMPRA", "-"*10)
    print(f"Maçã = R${0.3:.2f}")
    print(f"{maca} Maçãs = R${maca*0.3:.2f}")
else:
    print("-"*10, "TOTAL COMPRA", "-"*10)
    print(f"Maçã = R${0.25:.2f}")
    print(f"{maca} Maçãs = R${maca*0.25:.2f}")