#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função Depositar(4ª opção)
def Depositar():
    #solicitação para o usuário das variaveis necessárias para depositar(CPF e o valor do deposito) 
    cpf = int(input("Digite o cpf: "))
    valor = float(input("Digite o valor a ser depositado: "))

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
    
    # variavel saldo
    saldo = float(c[3].rstrip(" \n"))
    
    #importar função da data
    from datetime import datetime
    now = datetime.now()
    #armazenar a data numa variavel str
    data = (str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second))
      
    #novo atribuição de valor a saldo
    saldo = saldo + valor
    
    #metodo escrever
    def escrever():
        #após o processo é necessário mudar no arquivo o valor do saldo
        # substituir na linha 2(c[3]), o saldo pelo novo saldo atribuido     
        buffer = StringIO()
    
        #abre o aquivo com o cpf e substitui
        with open(str(cpf) + ".txt", 'r') as stream:
            for index, line in enumerate(stream):
                #buffer é a nova variavel que substituirá a linha 3
                buffer.write(str(saldo) + "\n" if index == 3 else line)

        with open(str(cpf) + ".txt", 'w') as stream:
            #escreve o valor do buffer
            stream.write(buffer.getvalue())
    
    
        #escrever os dados necessários para o extrato: data, saida ou entrada, tarifa, saldo
        arquivo.write("\n")
        arquivo.write("Data: %s " % data)
        arquivo.write(" + ")
        arquivo.write(" %.2f " % valor)
        arquivo.write(" Tarifa: 0.00")
        arquivo.write(" Saldo %.2f " % saldo)
        
        #informa ao usuário o sucesso do debito
        print("Depósito realizado com sucesso")
        print("")
        
    escrever()

    #fecha-se o arquivo e salva
    arquivo.close()        
        