import re
import os
from stack import Stack


# Cria a pilha
# O topo da pilha serve como identação atual
s = Stack()
s.empilha(0)


#Abre arquivo (Código fonte)
arquivo = open('cod.txt','r')


# Para seguir o padrão é necessário verificar a quantidade de espaços pelo mod do padrão
tab_size = arquivo.readline()
padrao = tab_size.index('{')
tab_size = int(tab_size[padrao+1])


# Serve para saber quantas vezes o while irá ler as linhas do arquivo
arquivo.seek(0)
qtdeLinhas = arquivo.readlines()




# Reseta o ponteiro do arquivo
arquivo.seek(0)

# Precisou andar duas linhas no arquivo porque as duas primeiras linhas é para saber o padrão de tab_size
# definido pelo usuário, a partir da terceira linha é onde de fato começa o código
linha = arquivo.readline()
linha = arquivo.readline()
contadorLinha = 0


#Laço de repetição para ler linha a linha e verificar de fato a identação
# O -2 na linha abaixo, é porque o ponteiro já andou duas linhas
while contadorLinha < len(qtdeLinhas) - 2:
    
    #-------------------------------------------------------------------------------------------------------
    linha = arquivo.readline()
    
    # Encontro a quantidade de espaços
    i = 0
    space = 0
    while linha[i].isspace():
        space += 1
        i += 1
    
    #print(space)
    
    # Encontro a quantidade de \tab até a ocorrência do caractere
    i = 0
    qtdeTab = 0
    while not linha[i].isalpha():
        if linha[i] == "\t":
            qtdeTab += 1
        i += 1


    # Converto a quantidade de tabs e unifico com espaços
    ident = space + ((qtdeTab * tab_size) - qtdeTab)
    #-------------------------------------------------------------------------------------------------------


    # VERIFICAR IDENTAÇÃO DE FATO (O MIOLO)

    if ident > s.topo():
        if ident % tab_size != 0:
            print('Identação errada, linha: ', contadorLinha+3)
            s.empilha(ident)
        else:
            s.empilha(ident)

    elif ident < s.topo():
        verifica = s.topo() - ident
        qtdeDedent = int(verifica / tab_size)

        if qtdeDedent != 0:
            contador = 0

            if ident % tab_size != 0:
                print('Identação errada, linha: ', contadorLinha+3)
            else:
                while contador < qtdeDedent:
                    s.desempilha()
                    contador += 1
                    
    elif space == s.topo():
        pass

    print(s.topo())

    contadorLinha += 1




    