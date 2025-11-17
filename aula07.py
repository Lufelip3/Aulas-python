import os
os.system("cls")
os.system("color 2")

# FUNÇÕES
# organizar o codigo e evita duplicidade
# def NomeFuncao():
# A funcao só será executada ao ser chamada pelo Nome
# NomeFuncao()

# FUNCAO SEM PARAMETRO E FUNCAO SEM RETORNO
# def Conteudo():
#     print("Aula de funções")
#     print("Estudando os tipos de funções")

# # Chamando a funcao pelo nome para se executada:
# Conteudo()

# FUNCAO SEM PARAMETRO E COM RETORNO
# def RetornaNumero():
#     return 100

# FUNCAO COM PARAMETRO E SEM RETORNO
# def ExecutaSoma(num1,num2):
#     print(num1+num2)

# #TODA FUNCAO COM PARAMETRO AO SER CHAMADA É OBRIGATÓRIO PASSAR OS PARAMETROS ENTRE PARENTESES()
# ExecutaSoma(30,20)

# FUNCAO COM PARAMETRO E COM RETORNO
# def RetornaSoma(n1,n2):
#     return n1+n2

# print(RetornaSoma(100,200))

#ESCOPO DE FUNCAO
# x= 10

# def Escopo():
#     global x
#     x=15

# Escopo()

# print(x)

#ex01
# def RetornaMult(n1,n2):
#     return n1*n2

# print(RetornaMult(float(input("Digite o 1° numero: ")),float(input("Digite o 2° numero: "))))

#ex02
# leo=0
# opcao=0
# def DolarReal():
#     leo = float(input("Digite o valor U$"))
#     print(f"R$ {leo/5.30}")
# def RealDolar():
#     leo = float(input("Digite o valor R$"))
#     print(f"U$ {leo*5.30}")
# def Menu():
#     print("="*8, "CONVERSÃO FODASTICA 3000", "="*8)
#     print("1 - Converter para DOLAR")
#     print("2 - Converter para REAL")
#     print("3 - Sair do programa")
#     print("="*42)

# while opcao!=3:
#     opcao=int(input("\nDigite uma opção: "))
#     if opcao == 1:
#         RealDolar()
#     elif opcao == 2:
#         DolarReal()
#     else:
#         print("OPÇÃO INVÁLIDA")
    

# else: ("\nSAIU DO PROGRAMA")
       
#ex03
saldo=0
valor=0
opcao=0
def Deposito():
    valor=float(input("Valor do deposito R$ "))
    global saldo
    saldo=saldo+valor
def Saque():
    valor=float(input("Valor do saque R$ "))
    global saldo
    saldo=saldo-valor
def Extrato():
    global saldo
    saldo=saldo+valor
    print("-"*10, "EXTRATO", "-"*10)
    print(f"SALDO: R${saldo:.2f}")
    print("-"*29)
def Menu():
    print("="*8, "MATH BANK", "="*  8)
    print("1 - Realizar Deposito")
    print("2 - Realizar Saque")
    print("3 - Emitir Extrato")
    print("4 - Sair")
    print("="*42)

Menu()
while opcao!=4:
    opcao=int(input("\nDigite a opção: "))
    if opcao ==1:
        Deposito()
    elif opcao ==2:
        Saque()
    elif opcao ==3:
        Extrato()
    elif opcao!=4: 
        print("OPÇÃO INVÁLIDA")
else: print("\nSAIU DO PROGRAMA")