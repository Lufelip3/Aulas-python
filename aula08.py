import os
os.system("cls")
os.system("color 2")

#ESTRUTURA DE DADOS
#LISTA [] -> REALIZA ARMAZENAMENTO DE MAIS DE UM TIPO DE DADO E MAIS DE UM VALOR
#TUPLA () -> FAZ A MESMA COISA QUE A LISTA, PORÉM É IMUTÁVEL
#DICIONARIO {} -> ESTRUTURA QUE ARMAZENA VARIOS VALORES COM SUAS RESPECTIVAS CHAVES

# lista = []
# #Inserir elementos na lista #append()
# lista.append("senai")#0
# lista.append(0)#1
# lista.append("teste")#2
# lista.append(99.99)#3
# lista.append(True)#4
# print(lista)

#Removendo elementos da lista
#pop(indice) -> remove pelo indice
#remove(value) -> remove pelo valor
#clear() -> limpa toda a lista

# lista.pop(3)
# print(lista)

# lista.remove("senai")
# print(lista)

# lista.clear
# print(lista)

# #Alterando valor da lista
# #lista[indice]=novo_valor
# lista[2]="fatec"
# print(lista)

# #Exibindo os valores da lista
# #Individualmente -> lista[indice]
# print(lista[2])
# #Todos os valores -> Laço de repetição
# #len()-> Retorna o tamanho da lista
# for i in range(len(lista)):
#     print(lista[i])

print("="*17, "SUPERMERCADO 20COMER", "="*17)
print("""
Digite 1: Adicionar um novo nome de Produto na lista 
Digite 2: Remover um produto da lista  
Digite 3: Remover todos os produtos da lista 
Digite 4: Sair do Programa 
Digite 5: Exibir todos os produtos da lista 
""")
print("="*56)
opcao=0
lista = []
while opcao!=4:
    opcao=int(input("\nDigite a opção: "))
    if opcao ==1:
        lista.append(input("Digite o nome do produto: "))
    elif opcao ==2:
        print("Digite o numero correspondente")
        for i in range(len(lista)):
            print(lista[i], "->", i)
        opcaoProduto=int(input("\nDigite a opção: "))
        lista.pop(opcaoProduto)
    elif opcao ==3:
        lista.clear()
    elif opcao ==5:
        for i in range(len(lista)):
            print(lista[i])
    elif opcao!=4: 
        print("OPÇÃO INVÁLIDA")
else: print("\nSAIU DO PROGRAMA")