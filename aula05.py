import os
os.system("cls")
os.system("color 2")
#Estrutura de repetição FOR
#O numero no renge é a quantidade de repetições
#A variavel i é utilizada pr convenção
# FOR COM 1 PARAMETRO
# for i in range(10): #i começa em 0 e vai até range-1
#     print(f"Hello wordl {i}")
#else:
#     print("Acabou o FOR")

# FOR COM 2 PARAMETRO
# for i in range(1,10): #i começa em 1 e vai até range-1 (1 a 9)
#     print(f"Hello wordl {i}")

# FOR COM 3 PARAMETRO
# for i in range(1,10,2): #i começa em 1 e vai até range-1 e incrementa de 2 em 2
#     print(f"Hello wordl {i}")

# ex01
# for i in range(30,48):
#     print(i)

# ex02
# for i in range(0,-51,-1):
#     print(i)

# ex03
# num=int(input("Digite um numero: "))

# print(f"\nTABUADA DO {num}\n")
# for i in range(1,11):
#      print(f"{num} X {i} = {i*num}")

# ex04
print("Digite o valor do pão:")
precoPao = float(input("R$"))

for i in range(1,51):
    print(f"{i} - R$ {precoPao*i:.2f}")

print("-"*30)

quantidade = int(input("\nQuantos pães você deseja levar: "))
print(f"\nTOTAL COMPRA: R${precoPao*quantidade:.2f}")

cupom = input("\nDigite o cupom de desconto: ").lower()
if cupom == "paomurcho":
    print("\nDesconto de 10% aplicado")
    valorFinal = (precoPao*quantidade)*0.9
    print(f"\nValor final R${valorFinal:.2f}\n")
else:
    print("\nCUPOM INVÁLIDO")
    valorFinal = (precoPao*quantidade)
    print(f"Valor final R${valorFinal:.2f}\n")

print("-"*30)
print("\nESCOLHA O SEU MÉTODO DE PAGAMENTO:")
print("NOTA 2 | NOTA 5 | NOTA 10 | NOTA 50 | ")

pagamento=int(input("\nMÉTODO DE PAGAMENTO: NOTA "))
if pagamento>valorFinal:
    print("\n*******************PAGAMENTO REALIZADO*******************")
    print(f"SEU TROCO FOI DE R${pagamento-valorFinal:.2f}")
    print("\nTENHA UM ÓTIMO DIA :)\n")
elif pagamento==valorFinal:
    print("\n*******************PAGAMENTO REALIZADO*******************")
    print("\nTENHA UM ÓTIMO DIA :)\n")
else:
    print("\nERRO NO PAGAMENTO")
    print("\nDINHEIRO INSUFICIENTE")
    print(f"FALTA: R${valorFinal-pagamento:.2f}\n")