import re
import os
from stack import Stack

#Cria pilha
s = Stack()

print(os.getcwd())

#Abre arquivo
arquivo = open('cod.txt','r')

# Serve para saber quantas vezes o while irá ler as linhas do arquivo
qtdeLinhas = arquivo.readlines()

# Encontra o padrão de espaços a partir da primeira linha que houver espaços, e utiliza
# a quantidade de espaços como referência
arquivo.seek(0)

#Identificar o padrão 
cont = 0
linha = ''
while cont < len(qtdeLinhas) - 1:
   
   linhaPadrao = arquivo.readline()
   
   if linhaPadrao[0] == ' ':
      linha = linhaPadrao
      break
   cont += 1

arquivo.seek(0)
padrao = 0
for i in range(len(linha)):
      if linha[i].isspace():
         padrao += 1
      else:
         break

# Reseto o ponteiro
#Já ignora a primeira linha, pois a verificação da identação só ocorre a partir da segunda linha
#Lembrar de fazer um tratamento para verificar se a primeira linha tem algum espaço em branco no início
arquivo.seek(0)
linha = arquivo.readline()
s.empilha(0)
contadorLinha = 0
print('INICIO...: P',padrao, ' T', s.topo())

#Laço de repetição para ler linha a linha e verificar de fato a identação
while contadorLinha < len(qtdeLinhas) - 1:
   space = 0
   linha = arquivo.readline()
   contadorLinha += 1
   
   for i in range(len(linha)):
      if linha[i].isspace():
         space += 1
      else:
         break
      
   regex = re.compile(r'\t', re.IGNORECASE)
   resultado = re.findall('\t', linha)
   space += (len(resultado) * padrao) - len(resultado)

   if space > s.topo():

      if space % padrao != 0:
         print ('Identação errada, linha: ', contadorLinha+1)
         s.empilha(space)
         print ('IDENT....: E', space, ' T', s.topo())
      else:
         s.empilha(space)
         print ('IDENT....: E', space, ' T', s.topo())

   elif space < s.topo():
      
      verifica = s.topo() - space
      qtdeDedent = verifica / padrao

      if qtdeDedent != 0:
         contador = 0
         
         if space % padrao != 0:
            print ('Identação errada, linha: ', contadorLinha+1)
         else:
            while contador < qtdeDedent:
               s.desempilha()
               contador +=1

         print ('DEDENT...: E', space, ' T', s.topo())
   elif space == s.topo():
      print('REPEAT...: E', space, ' T', s.topo())
      
arquivo.close()

