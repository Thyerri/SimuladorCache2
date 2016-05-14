## TRABALHO I DE ARQUITETURA DE COMPUTADORES II
## NOMES: CRISTIAN ZATT - 56484
##        THYÉRRI SCHIRMER - 56692

## SIMULADOR DE MEMÓRIA CACHE COM MAPEAMENTO DIRETO

import sys

##variáveis globais de parametros da memória, altere o valor das mesmas para configurar a memória como desejado
setaTamEndereco = 32
setaoffset = 2
setaIndex = 4
setaTag = 24


##função que realiza a leitura do arquivo
def abreArquivo():
    arquivoTexto = open('C:/teste.txt', 'r', encoding="utf8")

    return arquivoTexto

def fechaArquivo(arq):
    arq.close()

#####################################################################################
## FUNÇÃO PRINCIPAL
#####################################################################################
arquivoTxt = abreArquivo()

for linha in arquivoTxt:
    print(linha)
    binLinha = bin(int(linha, 16))
    esquerdaBits = (setaTamEndereco - len(binLinha))


    strBinLinha = str(binLinha)
    strBinLinha = str((binLinha)[2:]).zfill(esquerdaBits)

    print(strBinLinha)
    print (len(strBinLinha))


fechaArquivo(arquivoTxt)

