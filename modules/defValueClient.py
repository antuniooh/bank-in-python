#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função Saldo(5ª opção)
def Saldo():
    #solicitação para o usuário das variaveis necessárias 
    cpf = int(input("Digite o cpf: "))
    senha = input("Digite a senha do usuário: ")
    
    try:
        #tenta abrir o arquiv especificado, a partir do cpf do cliente
        arquivo = open(str(cpf) + ".txt", 'r+') 
    #caso não consiga a partir do cpf especificado
    except OSError:
        #mensagem para avisar ao usuário que o arquivo não foi encontrado e volta ao menu
        print("Arquivo não encontrado")
        print("")
        main()
        
    #ler o arquivo e armazenar numa lista
    c = arquivo.readlines() 
    
    # variavel saldo, senha e cliente
    saldo = float(c[3].rstrip(" \n"))
    senhaL = c[4].rstrip(" \n")
    cliente = c[0].rstrip("\n")

    #conferir se a senha está correta
    if senhaL ==  senha :
        #exibir o saldo e o nome do cliente
        print("")
        print("O saldo atual do cliente ", cliente, "é de: R$ ", saldo)
        print("")
    else:
        #mensagem de erro e volta ao menu
        print("Senha incorreta")
        print("")
        
    #fecha-se o arquivo e salva
    arquivo.close()