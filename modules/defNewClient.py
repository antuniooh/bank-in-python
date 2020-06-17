#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função NovoCliente(1ª opção)
def NovoCliente():
    #solicitação para o usuário das variaveis necessárias para criação(nome, cpf, tipodeconta, valorInicial, senha) 
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))
    conta = input("Digite o tipo de conta (Salário, Comum ou Plus): ")
    valorInicial = float(input("Digite o valor inicial da conta: "))
    senha = input("Digite a senha do usuário: ")
    
    #criação do arquivo nomeado com o cpf do cliente
    arquivo = open(str(cpf) + ".txt", 'w')
    
    #deve-se conferir a validade do tipo de conta
    if conta == "Salário" or conta =="Comum" or conta =="Plus":
        #as variaveis nome, cpf, senha, valor e tipo de conta são escritas no arquivo do cliente
        arquivo.write("%s \n" % nome)
        arquivo.write("%d \n" % cpf)
        arquivo.write("%s \n" % conta)
        arquivo.write("%d \n" % valorInicial)
        arquivo.write("%s \n " %senha)
        
        #mensagem para avisar ao usuário que o arquivo foi criado
        print("Usuário foi criado com sucesso")
        print("")
        
    else:
        #caso não seja correta volta o menu
        print("O tipo de conta não é válida")
        print("")
    
    #após o uso do arquivo, fecha-se e salva-se
    arquivo.close()  
    