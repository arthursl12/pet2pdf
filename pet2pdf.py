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

# Apresenta uma seção de confirmação para o usuário, que digita Y ou N
# para confirmar ou negar
def userConfirm():
    validInput = False
    while (not validInput):
        userVal = input('Confirmar? (S/N) ')
        if len(userVal) != 1: continue
        userVal = userVal.upper()
        if userVal != str('S') and userVal != str('N'): continue
        if userVal == 'S':
            validInput = True
            return True
        elif userVal == 'N':
            validInput = True
            return False

def defNomeArquivo():
    userOK = False
    while (not userOK):
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
        userOK = userConfirm()
        if not userOK: print()
    return fileName

def main():
    preffix = defNomeArquivo()


    





if (__name__ == '__main__'):
    main()

