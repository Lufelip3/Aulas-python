# Aula 01 - exibindo mensagens no terminal com print("")
#tipos de dados
#strins (texto) -> sempre entre aspas duplas ""
#numerico (int(inteiro) ou ploat (numero quebrado)) -> sem aspas duplas
#print("Olá mundo") #-> text (string)
#print(10) #-> numero inteiro (int)
#print(5.88) #-> numero quebrado (float) 

#operações matemáticas + - * /

#print("20" + "20") #soma de texto (concatenação)
#print(20 + 20) #somando numero

#parametros no print
#print(a,b,c,d,e...) até 128 parametros
#print("escola senai")
#print("escola","senai")

#ex1
#print("Luis Felipe - 18 anos - 463.074.818-03")
#print("Luis Felipe","- 18 anos","- 463.074.818-03")

#ex2
#print("Soma 100 + 50 =",100 + 50)

#ex3
#print("Multiplicando 30*3,33 =", 30*3.33)

#Formatações sep e End-> Final do print()
#sep -> Operador de separação (troca o caractere, por outro caractere)
#end -> Operador final (coloca o caractere no final do print)
#\n -> quebra linha

# print("Hoje é dia 06")
# print("Hoje", "é", "dia", "06",sep="_")

# print("curso de python", end=" no senai")
# print("\naprendendo operadores no print()")

#print("python", "versão", "3", sep="%%", end=" linguagem alto nivel")

# print("Curso", "de", "python", sep="_", end="%%")
# print("\n", "no senai rio claro em parceria com a fatec",sep="*", end="@")
# print("\n", "logica", "de", "programação", sep="_-_-_")

# print("python", "versao3", sep="@@@", end="[]")
# print("\nlogica", "de", "programação", sep="#")
# print("", "uso", "do", "print", sep="&", end="()")

#print("*"*10, "LOJA DO SENAI", "*"*10)

print("#"*15, "PADARIA PÃO DE ONTEM", "#"*15)
print("."*10, "TABELA DE PREÇOS", "."*10)
print("AGUA :      ", "."*10, "R$:10,00")
print("COCA-COLA : ", "."*10, "R$:5,00")
print("PÃO MURCHO :", "."*10, "R$:1,25")