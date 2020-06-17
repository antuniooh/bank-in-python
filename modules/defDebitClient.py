#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função Debitar(3ª opção)
def Debitar():
    #solicitação para o usuário das variaveis necessárias para debitar(CPF, senha e o valor do debito) 
    cpf = int(input("Digite o cpf: "))
    senha = input("Digite a senha do usuário: ")
    valor = float(input("Digite o valor a ser debitado: "))

    #tenta abrir o arquiv especificado, a partir do cpf do cliente
    try:
        arquivo = open(str(cpf) + ".txt", 'r+') 
    #caso não consiga a partir do cpf especificado
    except OSError:
        #mensagem para avisar ao usuário que o arquivo não foi encontrado evolta se o menu
        print("Arquivo não encontrado")
        print("")
        main()
        
    #ler o arquivo e armazenar numa lista
    c = arquivo.readlines() 

    #variavel saldo, senha, conta e taxa
    saldo = float(c[3].rstrip(" \n"))
    senhaL = c[4].rstrip(" \n")
    conta = c[2].rstrip(" \n")
    taxa = 0.0
    
    #importar função da data
    from datetime import datetime
    now = datetime.now()
    #armazenar a data numa variavel str
    data = (str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-"+ str(now.hour) + "-" + str(now.minute) + "-" + str(now.second))
    
    # metodo escrever, caso seja valido as variaveis digitadas
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
        arquivo.write(" - ")
        arquivo.write(" %.2f " % valor)
        arquivo.write(" Tarifa: %.2f " % taxa)
        arquivo.write(" Saldo %.2f " % saldo)
        
        #informa ao usuário o sucesso do debito
        print("Débito realizado com sucesso")
        print("")
    
    
    #conferir se a senha está correta e o tipo de conta
    if senhaL ==  senha :
        #conferir o tipo de conta para saber até onde é possivel debitar, quando da errado volta-se ao menu
        #caso esteja correto, calcula-se a taxa e abate-se do saldo do cliente
        if conta == "Salário":
            taxa = 0.05 * valor
            if saldo < valor + taxa:
                print("Não é possivel debitar, pois o saldo não pode ser negativo: R$" + str(saldo))
                print("")
            else:
                saldo = saldo - taxa - valor  
                escrever()
        elif conta == "Comum":
            taxa = 0.03 * valor
            if valor + taxa > saldo + 500:
                print("Não é possivel debitar,pois o saldo não pode ficar abaixo de R$ 500: " + "R$" + str(saldo))
                print("")
            else:
                saldo = saldo - taxa - valor 
                escrever()
        elif conta == "Plus":
            taxa = 0.01 * valor
            if valor + taxa > saldo + 5000:
                print("Não é possivel debitar, pois o saldo não pode ficar abaixo de R$ 5000: " + "R$" + str(saldo))
                print("")
            else:
                saldo = saldo - taxa - valor 
                escrever()
    else:
        #caso a senha não esteja correta, exibe a mensagem e volta-se ao menu
        print("Senha incorreta")
        print("")

    #fecha-se o arquivo e salva
    arquivo.close()
