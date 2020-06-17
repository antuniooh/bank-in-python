#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

from modules import defNewClient
from modules import defDeleteClient
from modules import defDebitClient        
from modules import defDepositClient
from modules import defValueClient
from modules import defExtractClient
    
#definição da função principal do programa
def main():
    # menu de opções para o usuário
    print("1 - Novo Cliente \n"
         "2 - Apaga Cliente \n"
         "3 - Debita \n"
         "4 - Deposita \n"
         "5 - Saldo \n"
         "6 - Extrato \n \n \n"
         "0 - Sair")
    
    #criação da variavel "menu" que permitirá o funcionamento das opções e solicitação da mesma ao usuário
    menu = int(input("Digite o q deseja fazer: "))
    #enquanto a variavel menu não for "0" ocorrerá a solicitação e a chamada de cada função desejada pelo usuário
    while True:
        if menu == 0:
            break
        elif menu == 1:
            defNewClient.NovoCliente()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 2:
            defDeleteClient.ApagaCliente()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 3:
            defDebitClient.Debitar()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 4:
            defDepositClient.Depositar()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 5:
            defValueClient.Saldo()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 6:
            defExtractClient.Extrato()
            menu = int(input("Digite o q deseja fazer: "))
        else:
            print("O comando digitado não é valido")
            break
#chama-se o metodo main e inicia-se a aplicação       
if __name__ == "__main__":
    main()