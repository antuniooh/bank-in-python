#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função ApagaCliente(2ª opção)
def ApagaCliente():
    #solicitação para o usuário da variavel necessária para apagar(CPF) 
    cpf = int(input("Digite o cpf: "))
    
    #tenta remover o arquivo especificado, a partir do cpf do cliente
    try:
        os.remove(str(cpf) + ".txt")
        #mensagem para avisar ao usuário que o arquivo foi removido
        print("Arquivo removido")
        print("")
    #caso não consiga remover o arquivo a partir do cpf especificado
    except OSError:
        #mensagem para avisar ao usuário que o arquivo não foi encontrado
        print("Arquivo não encontrado")
        print("")

