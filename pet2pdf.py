import docx2pdf
import os
from datetime import date
import string

# Completa com um zero à esquerda em inteiros de um dígito
# Retorna uma string do inteiro recebido
def completaZero(num):
    if num >= 10:
        return str(num)
    res = '0' + str(num)
    return res


def main():
    ## DEFINIÇAO DO NOME DO ARQUIVO
    # Data
    today = date.today()
    month = completaZero(today.month)
    day = completaZero(today.day)
    
    # Última posição já utilizada
    lastNum = input('Ultimo numero da ordem: ')
    while (not lastNum.isdigit()):
        print('Entrada nao eh um numero valido')
        lastNum = input('Ultimo numero da ordem: ')
    currentNum = int(lastNum) + 1
    
    # Formação do prefixo do nome dos arquivos
    fileName = str(currentNum) + '. ' + day + '-' + month + ' / '
    print('Arquivos terao nome: ', fileName)
    




if (__name__ == '__main__'):
    main()

