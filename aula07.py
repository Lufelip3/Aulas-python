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
def RetornaSoma(n1,n2):
    return n1+n2

print(RetornaSoma(100,200))