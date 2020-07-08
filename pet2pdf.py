import os
import glob
from datetime import date
import string

DEBUG_MODE = False
CURRENT_PATH_MODE = True

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
    if DEBUG_MODE: return True

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
        if DEBUG_MODE:
            currentNum = 11
        else:
            lastNum = input('Ultimo numero da ordem: ')
            while (not lastNum.isdigit()):
                print('Entrada nao eh um numero valido')
                lastNum = input('Ultimo numero da ordem: ')
            currentNum = int(lastNum) + 1
        
        # Formação do prefixo do nome dos arquivos
        fileName = str(currentNum) + '. ' + day + '-' + month + ' . '
        print('Arquivos terao nome: ', fileName)
        userOK = userConfirm()
        if not userOK: print()
    return fileName

# Dado o nome de um arquivo com uma extensão qualquer, retira-se a extensão
# Retorna uma nova string com o nome do arquivo sem a extensão
def extArquivo(nome):
    # Assegurar que é uma string
    nome = str(nome)

    # Encontrar o índice do '.' 
    for i in range(len(nome)):
        j = len(nome) - i - 1
        if nome[j] == '.':
            break
    
    # Particiona o nome até antes do '.'
    res = nome[0:j]
    return res

# Dada uma lista com nomes de arquivo
# Retorna uma outra lista apenas com os nomes dos arquivos com extensão '.docx'
def somenteDocx(lista):
    for nomes in lista:
        ext = nomes[-4:]
        print(ext)


def main():
    # DEFINIÇÃO DO PREFIXO
    preffix = defNomeArquivo()
    
    # RENOMEAÇÃO
    # Definir o caminho da pasta-alvo
    if CURRENT_PATH_MODE:
        docsDir = next(os.walk('.'))
    else:
        docsDir = next(os.walk('./docs'))
    docsList = docsDir[2]

    # Renomear de acordo com o prefixo padrão
    for filename in docsList: 
        nomeDOCX = str(filename)
        newnomeDOCX = preffix + nomeDOCX
        if CURRENT_PATH_MODE:
            oldFile = nomeDOCX
            newFile = newnomeDOCX
        else:
            oldFile = os.path.join("docs", nomeDOCX)
            newFile = os.path.join("docs", newnomeDOCX)
        os.rename(oldFile, newFile)
        print('RENOMEAR: ' + newnomeDOCX)
    print()


if (__name__ == '__main__'):
    main()

