import os
os.system("cls")#limpa a tela
os.system("color 2") #troca de cor no terminal
#aula 02 -> variaveis, tipos e input
#tipos de dados -> texto(string), n inteiro(int) n quebrado(float)

#declarações de variaveis
# escola="SENAI"
# #mostrando o valor da variavel no print
# #separando por parametro
# print("Eu estudo no", escola)
# #concatenando texto
# print("Eu estudo no "+ escola)
# #f string {} -> mostra o valor na variavel dentro das aspas
# print(f"Eu estudo no {escola}")

# #exemplo de variavel int e float
# numerointeiro = 100
# numeroquebrado = 12.5
# soma = numerointeiro+numeroquebrado
# print(f"A soma de {numerointeiro} + {numeroquebrado} = {soma}")

#ex01

# nome = "Luis Felipe"
# cpf = "123.456.789-00"
# idade = 18
# print(f"Meu nome é {nome}, eu tenho {idade} anos e meu CPF é {cpf}.")
# #print("Nome:", nome, "\nIdade:", idade, "\nCPF:", cpf)

#input("") -> pergunta algo para o usuario e armazena em uma variavel
#obrgatoriamente antes do input deve existir uma variavel!

#lembrando que print() NÃO armazena valor


# nome = input("Digite seu nome: ")
# print(f"Seu nome é {nome}")

#ex02
# nome = input("Qual o seu nome: ")
# cpf = input("Qual o seu CPF: ")
# rg = input("Qual a seu RG: ")
# print(f"Meu nome é {nome}, meu RG é {rg} e meu CPF é {cpf}.")

#conversão de dados
#input() -> sempre armazena os valores em string
#int() -> converte para numero inteiro
#float() -> converte para numero inteiro ou quebrado


# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite outro numero: "))
# print(f"Soma de {n1} + {n2} = {n1+n2}")

# n1 = int(input("Digite um numero: "))
# print(f"O antecessor de {n1} é {n1-1} e o sucessor é {n1+1}")

# idade = int(input("\nDigite o seu ano de nascimento: "))
# print(f"Você provavelmente tem {2025-idade} anos")

#porcentagem
# print("25% de 100 = ", 0.25*100)
# print("4% de 400 = ", 0.04*400)
# print("99% de 1525 = ", 0.99*1525)

# desconto = 150*0.15
# print(f"O preço final do produto é R${150-desconto}")

print("="*15,"SUPERMERCADO","="*15)
produto1= input("Digite o nome do produto: ")
valorProduto1= float(input("Digite o valor do produto R$"))
produto2= input("\nDigite o nome do produto: ")
valorProduto2= float(input("Digite o valor do produto R$"))
print(f"\n", "="*15, "CAIXA","="*15)
print(f"{produto1} R${valorProduto1:.2f} com 10% de desconto: R${valorProduto1*0.1:.2f}")
print(f"{produto2} R${valorProduto2:.2f} com 25% de desconto: R${valorProduto2*0.25:.2f}")
print("-"*40)
print(f"Valor final: R${(valorProduto1-(valorProduto1*0.1))+(valorProduto2-(valorProduto2*0.25)):.2f}")