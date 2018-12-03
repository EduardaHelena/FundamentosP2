#matrizes - bidimecionais

#indice linha e coluna
# 0 até limite - 1
#Nome da matriz[linha][coluna]
#Primeiro for linha - segundo colunas

#pra pecorrer a matriz
#mat = []
#for i in range(0,2):
 #   mat.append(0)
 #   mat[i] = []
 #   for j in range(0, 3):
 #       mat[i].append(0)
#print mat

#----------------------------------------------------------------
#para somar os elementos
#mat = []
#soma = 0
#numeroAtual = 0

#for i in range(0,3):
 #   mat.append(i)
#    mat[i] = []
#    for j in range(0, 3):
#        mat[i].append(input('digite o elemento da linha:'))
#print mat
#
#for i  in range(0,3):
 #   for j in range(0,3):
 #       numeroAtual = mat[i][j]
 #       if (numeroAtual % 2 == 0):
 #           soma = soma + numeroAtual
#print "a soma é: ", soma
 
#-----------------------------------------------------
#  para somar elementos da diagonal

#mat = []
#soma = 0
#numeroAtual = 0
#for i in range(0,3):
 #   mat.append(i)
 #   mat[i] = []
 #   for j in range(0, 3):
 #       mat[i].append(input('digite o elemento da linha:'))
#print "matriz: ", mat
 
#for i in range(0,3):
 #   for j in range(0,3):
 #       numeroAtual = mat[i][j]
 #       if (i == j):
 #           soma = soma + numeroAtual
#print "a soma é: ", soma

#outra maneira de fazer a soma:
 #for i in range(0,3):
 #    soma += mat[i][i]
#print "a soma é: ", soma

#-----------------------------------------------------
#formatacao de Matriz:
#mat = []
#for i in range(0,3):
 #   mat.append(i)
 #   mat[i] = []
 #   for j in range(0, 3):
 #       mat[i].append(input('digite o elemento da linha:'))

#for i in range(0,3):
 #    for j in range (0,3):
 #        print "%3d" % mat[i][j],
 #    print

 #-----------------------------------------------------
#Para somar as linhas e pares
#mat = []
#somaPar = 0
#somarTotal = 0
#numeroAtual = 0

#for i in range(0,3):
#    mat.append(i)
#   mat[i] = []
#    for j in range(0, 2):
#       mat[i].append(input('digite o elemento da linha:'))

#for i in range(0,3):
#     for j in range (0,2):
#        print "%3d" % mat[i][j],
#     print ""
#    print

#for i  in range(0,3):
 #   somarTotal = 0
 #   for j in range(0,2):
 #       numeroAtual = mat[i][j]
 #       somarTotal = somarTotal + numeroAtual
 #       if (numeroAtual % 2 == 0):
 #           somaPar = somaPar + numeroAtual
 #   print " linha: ", i, " -  soma total da linha", somarTotal
 #   print ""
    
#print "a soma dos pares é: ", somaPar
#-----------------------------------------------------
#para somar as diagonais e criar novo vetor
#-------------------------------------------
 
#aula 2
#matriz 4 x 5 para guardar em um vetor
#mat = []

#desenha a matriz
#for i in range(0,4):
#    mat.append(i)
#    mat[i] = []
#    for j in range(0, 5):
#       mat[i].append(input('digite o elemento da linha:'))

#pra colocar no vetor
#vet=[]*20
#for i in range(0,4):
#    for j in range(0, 5):
#    vet[i*5 + j] = mat[i][j]
#
#print "vet: ", vet

#-------------------------------------------
#Modularização:
#cada modulo faz uma função, trecho com função bem definida
# ex: modulo para ler, escrever e resolver problema
#Programa mais legivel
#Reutifizacao e manutenção mais facil
#Conceito Python: modulo tem rotinas : ex Math

#Para criar uma rotina usamos a palavra DEF:

#def soma(x,y)- x e y são parametros de fora
#s = x + y
#return s - pode retornar direto a soma

#CUIDADO COM A PORRA DA IDENTAÇÃO

#CHAMAR A ROTINA:

#def soma(x,y):#- x e y são parametros de fora
#    s = x + y
#    return s #- pode retornar direto a soma

#A = input("n1")
#B = input("n2")
#print "soma", soma(A,B)

#FUNÇÃO X PROCEDIMENTO
#Função: retorna valor
#Procedimento: Retorna algo como imprimir
# NA PROVA SÓ USAR FUNÇÃO E PROCEDIMENTO EM

#-------------------------------------------
# programa 57 -
# dois valores inteiros,
# e retornar a soma dos multiplos de 7
# MENOS a soma dos multiplos de 13
# entre esses valores

#def somaLimite(x,y):
#    soma = 0
#    for i in range(x+1,y):
#        if(i%7 == 0):
#            soma += i
#        if(i%13 == 0):
#            soma -= i
#    return soma
#
#a = int(input("diga o começo"))
#b = int(input("diga o final"))
#print"resultado: ",somaLimite(a,b)
#-------------------------------------------
# programa 58 -
#fazer um modulo para receber um vetor como parametro e retornar outro sem repeticao
#NAO PODE USAR APPEND na prova!!!!!
#get all - tamanho fixo
#varialvel tamanho
#get all[] = vet[i]
#tamanho +1
#na prova modulo, funcao == só fazer o def
#def vetSemRep(vet):
#    vetAux[]
#    for i in range(0, len(vet)):
#        achou = False
#        for j in range(0, len(vetAux)):
#            if vet[i] == vetAux[j]:
#                achou = True
#            if not achou: (if achou == false)
#                vetAux.append(vet(i))
#
#    return vetAux

#vet[]
#vetNovo[]
#for i in range(0,5):
#    vet.append(int(input("eleme: ")))

#vetNovo = vetSemRep(vet)
#print "vet: ", vet
#print "vet novo", vetNovo
#-------------------------------------------
# PARAMETROS
# valor (copia variavel original, não altera o original) x referencia (passa a propria variavel)
# no python nao tem escolha, passa por REFERENCIA!!!! - IMPORTANTE!
# Exemplo: 
#
#def vetSemRep(vet,x,y):
#   print "vet: ", vet, "x", a, "y", b
#   vet[i] = 99
#   x = 9
#   y = y + 1
#print "vet: ", vet, "x", a, "y", b


#vet[1,2,3]
#a = 0
#b = 0
#vetSemRep(vet,a,b)
#print "vet: ", vet, "x", a, "y", b
#-------------------------------------------
#PROGRAMA 59
vet['a', 'b', 'c']
print vet.count(vet[1])



    

