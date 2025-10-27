import os
os.system("cls")
os.system("color 2")

#IF encadeado -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA

# x=15

# if x <=20:
#     print("Entrou na linha 11")
# if x <=15:
#     print("Entrou na linha 13")
# if x <=16:
#     print("Entrou na linha 15")

# if x <=20:
#     print("Entrou na linha 18")
# elif x <=15:
#     print("Entrou na linha 20")
# elif x <=16:
#     print("Entrou na linha 22")

# idade=int(input("Digite a sua idade: "))
# if idade<0:
#     print("Idade inválida")
# elif idade<12:
#     print("CRIANÇA")
# elif idade<18:
#     print("ADOLESCENTE")
# elif idade<60:
#     print("ADULTO")
# else:
#     print("IDOSO")    

# nota1=float(input("Digite a 1° nota: "))
# nota2=float(input("Digite a 2° nota: "))
# media = (nota1+nota2)/2
# print(f"\n Sua média foi {media:.1f}")
# if media<5:
#     print("---------REPROVADO---------")
# elif media>=5 and media<=7:
#     print("---------RECUPERAÇÃO---------")
# else:
#     print("---------APROVADO---------") 

peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc=peso/(altura*altura)
print(f"Seu IMC é {imc:.2f}")
if imc<17:
    print("\nMuito abaixo do peso")
elif imc>=17 and imc<18.5:
    print("\nAbaixo do peso")
elif imc>=18.5 and imc<25:
    print("\nPeso normal")
elif imc>=25 and imc<30:
    print("\nAcima do peso")
elif imc>=30 and imc<35:
    print("\nObesidade I")
elif imc>=35 and imc<40:
    print("\nObesidade II (severa)")
else:
    print("\nObesidade III (mórbida)")
