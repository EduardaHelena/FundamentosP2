#Faça um programa em pascal para ler as notas de 100 alunos e imprimir quantos alunos
#tiraram nota abaixo da media da turma e quantos tiraram acima ou igual a media.

#soma = 0
#contMaior = 0
#contMenor = 0
#notas = [0.0]*5

#for i in range(0,5):
#  nota = float(input("nota:"))
#  notas[i] = nota
#  soma += notas[i]

#media = soma/5
#print "media:", media

#for j in range(0,5):
# if notas[j] > media:
#    contMaior += 1
#  if notas[j] < media:
#    contMenor += 1
#
#print "quantidadeMaior:", contMaior, "quantidadeMenor:", contMenor
# -------------------------------------------------
#Ler um vetor de 12 posições inteiras e depois ler dois números X e Y de 1 a 12. Imprimir a soma das posições X e Y do vetor.

#vetor = [0.0]*5

#def SomaVetor(x, y, vet):
#  resultado = vet[x] + vet[y]
#  return resultado

#for i in range(0,5):
#  numero = int(input("elemento:"))
#  vetor[i] = numero
#a = input("posicao 1:")
#b = input("posicao 2:")

#print "Soma igual a :", SomaVetor(a, b, notas)
# -------------------------------------------------
#Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas posições.
#Imprima o vetor original e o vetor trocado
#numeros = [0.0]*16

#def troca(vet):
#  for i in range(0, 8):
#    aux=vet[i]
#    vet[i] = vet[i+8]
#    vet[i+8]=aux
#  return vet
  
#for i in range(0,16):
#  numero = int(input("elemento:"))
#  numeros[i] = numero

#print "Original: ", numeros
#print "Trocado: ", troca(numeros)
# -------------------------------------------------

#Preencha um vetor de 10 posições com os primeiros 10 números impares. No final imprima o vetor.
#numero = 1
#vet = [0.0]*10
#achou = False
#for i in range(0,10):
#  achou = False
#  while achou == False:
#    if(numero%2 != 0):
#      vet[i] = numero
#      numero+= 1
#      achou = True
#    else:
#      numero+= 1
#
#print vet
# -------------------------------------------------
#Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X,
#imprimir quantas vezes o número X aparece no vetor.
#numeros = [0.0]*10
#
#for i in range(0,10):
#  numero = int(input("elemento:"))
#  numeros[i] = numero
#
#x = int(input("elemento:"))
#print "aparece:", numeros.count(x)
# -------------------------------------------------
#Leia um vetor de 40 posições contar quantos elementos pares se encontram no vetor.
#numeros = [0.0]*10
#qtdPares = 0
#
#for i in range(0,10):
#  numero = int(input("elemento:"))
#  numeros[i] = numero
#  if (numero % 2 == 0 ):
#    qtdPares += 1

#print "aparece:", qtdPares
#print numeros
# -------------------------------------------------
#Leia dois vetores de 10 posições cada. Armazene em um vetor de 20 posições os elementos
#do vetor 1 depois os elementos do vetor 2. No final imprima os três vetores.
#vet1 = [0.0]*10
#vet2 = [0.0]*10
#vetFinal = []
#
#def Vetor(x,y, vet):
#  for i in range(x,y):
#    numero = int(input("elemento:"))
#    vet[i] = numero
#  return vet

#def vetores(vet, vet2):
#  for i in range (0, len(vet)):
#    numero = vet[i]  
#    vet2.append(numero)
#  return vet2
#print "vetor 1", Vetor(0,10, vet1)
#print "vetor 2", Vetor(0,10, vet2)
#vetores(vet1, vetFinal)
#vetores(vet2, vetFinal)
#print vetFinal
#print len(vetFinal)
# -------------------------------------------------
#Leia dois vetores de 15 posições cada, imprimir a soma dos elementos #dos vetores e a diferença dos elementos dos vetores.
#vet1=[0.0]*15
#vet2=[0.0]*15

#def Vet(vet):
#  for i in range(0,len(vet)):
#    numero = int(input("elemento:"))
#    vet[i] = numero
#  return vet

#def SomaVetor(vet):
#  soma = 0
#  for i in range(0,len(vet)):
#    a = vet[i]
#    soma=soma+a  
#  return soma

#Vet(vet1)
#Vet(vet2)
#print "soma vetor 1 + vetor 2:  ", SomaVetor(vet1) + SomaVetor(vet2)
#print "diferença vetor 1 - vetor 2:  ",  SomaVetor(vet1) - SomaVetor(vet2)  
# -------------------------------------------------
#Leia uma frase e imprima as suas palavras.
#
#frase = raw_input("frase:")
#resultado = frase.split();
#for i in range(0, len(resultado)):
#  print resultado[i]

# -------------------------------------------------
#Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto.
#Branco = 0
#vogal = 0
#resto = 0
#frase = raw_input("frase:")
#print frase
#print len(frase)
#for i in range (0 , len(frase)):
#  if(frase[i].isspace()):
#      Branco +=1
#  elif(frase[i].isalpha()):
#    if(frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
#      vogal +=1
#  else:
#    resto +=1

#print "branco: ", Branco
#print "vogais: ", vogal
#print "resto: ", resto
# -------------------------------------------------

#Fazer um programa para ler dois vetores de 10 posições e colocar em um outro vetor de no máximo 20 posições a união dos elementos. 
#Colocar em um vetor de 10 posições a intercecção dos dois vetores.

#limite = 5
#Vet1 = [0.0]*limite
#Vet2 = [0.0]*limite
#vetFinal = [0.0]*(limite*2)
#vetIntesecao = [0.0]* limite
#indiceFinal = 0

#def Vet(vet):
#  for i in range(0,len(vet)):
#    numero = int(input("elemento:"))
#    vet[i] = numero
#  return vet

#def VetGrande(vet, indice):
#  for i in range(0,len(vet)):
#    vetFinal[indice] = vet[i]
#    indice += 1
#  return indice 

#def Intesecao(vet1, vet2):
#  for i in range(0, len(vet1)):
#    for j in range(0, len(vet2)):
#      if(vet1[i] == vet2[j]):
#        numero = vet1[i] 
#        for i in range (0, len(vetIntesecao)):
#          vetIntesecao[i] = numero
#  return vetIntesecao

#print Vet(Vet1)
#print Vet(Vet2)
#indiceFinal = VetGrande(Vet1, indiceFinal)
#VetGrande(Vet2, indiceFinal)
#print "Uniao: ", vetFinal
#print Intesecao(Vet1, Vet2)
# -------------------------------------------------
#Faça um programa para ler 50 valores de temperaturas em graus Celsius. #Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas em Celsius e Farenheit e 
#quantas temperaturas ficaram acima da media em Farenheit.

#limite = 5
#vetTempCelcius = [0.0]*limite
#vetTempFarenheit = [0.0]*limite 
#mediaC = 0
#mediaF = 0

#def VetTemperatura(vet):
#  somaCelcius = 0
#  for i in range(0,len(vet)):
#    numero = int(input("temperatura em Celcius:"))
#    vet[i] = numero
#  return vet, somaCelcius

#def Transformar(vet1):
#  for i in range(0, len(vet1)):
#    numero = vet1[i]
#    numeroF = ((float(numero*9)/5) + 32)
#    vetTempFarenheit[i] = numeroF
#  return vetTempFarenheit

#def Media(vet1):
#  qtd = len(vet1)
#  soma = 0
#  for i in range(0, len(vet1)):
#    numero = vet1[i]
#    soma += numero
#  return soma/qtd

#def MediaQtd(vet1,media):
#  qtd = 0 
#  for i in range(0, len(vet1)):
#    if(vet1[i] > media):
#      qtd += 1
#  return qtd

  
#VetTemperatura(vetTempCelcius)
#print""
#print "temperaturas em Farenheit: ", Transformar(vetTempCelcius)
#mediaC = Media(vetTempCelcius)
#mediaF = Media(vetTempFarenheit)
#print "media celcius: ", mediaC, "media F: ", mediaF
#print "quantidade de F acima da media: ", MediaQtd(vetTempFarenheit,mediaF)

#--------------------------------------------------------

#14.	Leia uma string e imprima se ela é um palindromo. Um palindromo é uma cadeia que pode ser lida de frente para trás e de trás para frente.  Ex: ‘SOMOS’    ‘1234321’

#string = raw_input('diga a primeira palavra')
#stringInversa = ""
#cont = 1
#for i in range(0, len(string)):
#    stringInversa += string[cont*-1]
#    cont +=1

#if (string == stringInversa):
#  print "É um polindromo", string, " igual a ", #stringInversa
#else:
#  print "Não é um polindromo", string, " diferente de ", stringInversa 

#--------------------------------------------------------
#15.	Leia uma matriz 5x5 e imprima o valor do maior elemento.Imprima também a linha e coluna desse elemento.

#def cMat(x,y):                              
#    print "Digite os valores da matriz ",x,"x",y
#    mat = [0]*x
#    for i in range(0,x):
#        mat[i]= [0]*y
#        for j in range(0,y):
#            mat[i][j]=int(input("Digite aqui: "))
#    return mat
#
#def Maior(mat, x, y):
#    linha = 0 
#    coluna= 0  
#    numeroMaior = 0
#    for i in range(0,x):
#        for j in range(0,y):
#            numero = mat[i][j]
#            if (numero > numeroMaior):
#              numeroMaior = numero
#              linha = i + 1
#              coluna = j + 1
#
#    return numeroMaior, linha, coluna

#Nlinha = 5
#Ncoluna = 5
#Matriz = cMat(Nlinha, Ncoluna)
#print Matriz
#Maior = Maior(Matriz, Nlinha, Ncoluna)
#print "o numero, sua linha e coluna é", Maior

#--------------------------------------------------------
#16.	Leia uma matriz 7x7 e imprima a soma dos elementos da linha 6. Imprima tambem a soma dos elementos da coluna 2. Imprima também a soma dos elementos da diagonal principal. Imprima também o elemento da linha 3 e  coluna 4. Imprima também a soma de todos os elementos pares da matriz. 


#def cMat(x,y):                              
#    print "Digite os valores da matriz ",x,"x",y
#    mat = [0]*x
#    for i in range(0,x):
#        mat[i]= [0]*y
#        for j in range(0,y):
#            mat[i][j]=int(input("Digite aqui: "))
#    return mat

#def SomaLinha(mat, coluna): 
#  linha = int(input('linha: '))
#  linha = linha - 1
#  somaLinha = 0
#  for j in range(0, coluna):
#      somaLinha += mat[linha][j]
#  return somaLinha

#def SomaColuna(mat, linha): 
#  coluna = int(input("Digite a coluna: "))
#  coluna = coluna - 1
#  somaColuna = 0
#  for j in range(0, linha):
#      somaColuna += mat[j][coluna]
#  return somaColuna

#def SomaDiagonalPrincipal(Matriz, coluna):
#  somaDiagonalPrincipal = 0
#  for i in range(0, coluna):
#    somaDiagonalPrincipal += Matriz[i][i]
#  return somaDiagonalPrincipal

#def SomaPares(matriz, linha, coluna):
#  somaPares = 0
#  for i in range(0, linha):
#    for j in range(0, coluna):
#      numero = matriz[i][j]
#      if (numero%2 == 0):
#        somaPares += numero
#  return somaPares

#Linha = 3
#Coluna = 3 
#Matriz = cMat(Linha, Coluna)
#print Matriz

#MatrizLinha = SomaLinha(Matriz, Coluna)
#print "Soma das Linhas: ", MatrizLinha

#MatrizColuna = SomaColuna(Matriz, Linha)
#print "Soma das Colunas: ", MatrizColuna

#MatrizDiagonalPrincipal = SomaDiagonalPrincipal(Matriz, Coluna)
#print "Soma das Diagonal Principal: ", MatrizDiagonalPrincipal

#MatrizPares = SomaPares(Matriz, Linha, Coluna)
#print "Soma elementos pares: ", MatrizPares
#-------------------------------------------------------
#17.	Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a matriz.
                              
#mat = [0]*5
#for i in range(0,5):
#    mat[i]= [0]*5
#    for j in range(0,5):
#      if (i == j):
#        mat[i][j] = 1
#      else: 0
#print mat
#-------------------------------------------------------
#18. Leia uma matriz 6x6 e conte quantos elementos maiores que 10 existem na matriz. Imprima esse valor e a matriz.

#def cMat(x,y):                              
#    print "Digite os valores da matriz ",x,"x",y
#    mat = [0]*x
#    for i in range(0,x):
#        mat[i]= [0]*y
#        for j in range(0,y):
#            mat[i][j]=int(input("Digite aqui: "))
#    return mat

#def MaiorDez(matriz, linha, coluna):
#  cont = 0
#  for i in range(0, linha):
#    for j in range (0, coluna):
#      numero = matriz[i][j]
#      if numero > 10:
#        cont+=1
#  return cont

#linha = 3
#coluna = 3
#Matriz = cMat(linha, coluna)
#MaiorDez = MaiorDez(Matriz, linha, coluna)
#print "Matriz: ", Matriz
#print "Quantidade de elementos maiores que 10: ", #MaiorDez
#-------------------------------------------------------
#19.Leia uma matriz 4x4 e um valor X, procure a primeira vez que esse valor aparece na matriz imprimindo sua linha e coluna. Cason não exista o elemento, imprima uma mensagem de erro.

#def cMat(x,y):                              
#  print "Digite os valores da matriz ",x,"x",y
#  mat = [0]*x
#  for i in range(0,x):
#      mat[i]= [0]*y
#      for j in range(0,y):
#          mat[i][j]=int(input("Digite aqui: "))
#  return mat

#def Localizar(matriz, linha, coluna):
#  procurado = int(input('Diga o numero que voce procura'))
#  achou = False
#  for i in range(0, linha):
#    for j in range(0, coluna):
#      numero = matriz[i][j]
#      if(numero == procurado):
#        achou = True
#        linhaProcurado = i + 1 
#        ColunaProcurado = j + 1
#        return linhaProcurado, ColunaProcurado



#def pMat(mat,x,y):
#    print
#    M = mat
#   for i in range(0,x):
#        for j in range(0,y):
#            print "%10d" % mat[i][j],
#        print

#Linha = 4
#Coluna = 4
#Matriz = cMat(Linha, Coluna)
#print pMat(Matriz, Linha, Coluna)

#Procurado = Localizar(Matriz, Linha, Coluna)
#print "Linha e Coluna ", Procurado
