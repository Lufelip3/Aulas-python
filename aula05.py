import os
os.system("cls")
os.system("color 2")
dd
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
num=int(input("Digite um numero: "))

print(f"\nTABUADA DO {num}\n")
for i in range(1,11):
     print(f"{num} X {i} = {i*num}")