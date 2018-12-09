#-------------------------------------
# Questao1
#n1 = input("Numero 1: ")
#n2 = input("Numero 2: ")
#n3 = input("Numero 3: ")
#if(n1 > n2):
#    if(n1 > n3):
#        print "n1 maior"
#else:
#    if (n2 > n3):
#        print "n2 maior"
#    else:
#        print "n3 maior"

#-------------------------------------
#questao 5

#n1 = input("Nota 1: ")
#n2 = input("Nota 2: ")
#n3 = input("Nota 3: ")

#Media = float(n1+n2+n3)/3
#if(Media <= 2.9):
#    print "Reprovado: ", Media
#else:
#    if(3.0 <= Media and Media <= 6.9):
#        exameNota = 12 - Media
#        print "Exame: ",Media,"Faltam:",exameNota
#
#    else:
#        print "Aprovado", Media

#-------------------------------------
#questao 6

#n1 = input("Numero 1: ")
#n2 = input("Numero 2: ")
#n3 = input("Numero 3: ")

#if(n1 > n2 and n1 > n3):
#    if(n2 > n3):
#        primeiro = n1
#        segundo = n2
#        terceiro = n3
#    else:
#        primeiro = n1
#        segundo = n3
#        terceiro = n2
#   
#else:
#    if(n2 > n3 and n2 > n1):
#        if (n3 > n1):
#            primeiro = n2
#            segundo = n3
#            terceiro = n1
#        else:
#            primeiro = n2
#            segundo = n1
#            terceiro =  n3
#    
#
#print "Ordem: ", primeiro, segundo, terceiro

#-------------------------------------
#questao 7
  
#n1 = input("Numero 1: ")
#operador = raw_input("Diga a operação desejada : soma, subtracao, multiplicacao, divisao: ")
#n2 = input("Numero 2: ")

#if (operador == "soma"):
#    resultado = n1 + n2
#    print"Resultado da Soma: ", resultado
#    
#elif(operador == "subtracao"):
#    resultado = n1-(n2)
#    print "Resultado da Subtração: ", resultado
    
#elif(operador == "multiplicacao"):
#    resultado = n1*n2
#    print "Resultado da Multipicacao: ", resultado
#    
#elif(operador == "divisao"):
#    if (n2 == "0"):
#        print "Divisão por zero, tem resultado indefinido"
#    else:
#        resultado = n1/n2
#        print "Resultado da Divisao: ", resultado

#-------------------------------------
#questao 8

#idade= input("Diga a idade")

#if(idade <= 4):
#    print "Categoria Baby: ", idade, "anos"
#elif(5 <= idade <= 10):
#    print "Categoria Infantil: ", idade, "anos"
            
#elif (11 <= idade <= 17):
#    print "Categoria Juvenil: ", idade, "anos"
            
#else:
#    print "Categoria Master: ", idade, "anos"

#-------------------------------------
#questao 9

#valor = input("Diga o valor: ")

#if(valor <= 50):
#    valorFinal =  valor +(float(valor*5)/100)
    
#elif(50 < valor <= 100):
#    valorFinal = valor +(float(valor*10)/100)
    
#else:
#    valorFinal = valor +(float(valor*15)/100)

#Classificação
#if(valorFinal <= 80):
#    print "Produto Barato: ", valorFinal
#elif(80 < valorFinal <= 120):
#    print "Produto Normal: ", valorFinal
#elif(120 < valorFinal <= 200):
#    print "Produto Caro: ", valorFinal
#else:
#    print "Produto Muito Caro: ", valorFinal

#-------------------------------------
#questao 10

#sexo = raw_input("voce se define como homem ou mulher: ")
#altura = input("Diga sua altura")
#
#if( sexo == "mulher"):
#    peso = ((62.1 * altura) - 44.7)
#    print "o peso ideal: ", peso
#elif( sexo == "homem"):
#    peso = float((72.7 * altura) - 58.0)
#    print "o peso ideal: ", peso
#else:
#    print "erro"


#-------------------------------------
#questao 12

# horas_Professor1 = input("Diga as horas do Professor 1")
# valor_Professor1 = input("Diga valor das horas do Professor 1")
# horas_Professor2 = input("Diga as horas do Professor 2")
# valor_Professor2 = input("Diga valor das horas do Professor 2")

# salario_Professor1 = float(horas_Professor1 * valor_Professor1)
# salario_Professor2 = float(horas_Professor2 * valor_Professor2)

# if(salario_Professor1 > salario_Professor2):
#     print "O salario do professor 1 é maior: ", salario_Professor1
# else:
#     print "O salario do professor 2 é maior: ", salario_Professor2

#-------------------------------------
#questao 15
#numero = input("Digite o numero de 1000 a 9999")
#Parte1 = (numero/100) #Parte1 com 2 digitos
#Parte2 =  numero - (Parte1*100) #com dois ultimo numeros

#soma = Parte1 + Parte2
#resultado = soma**2
#if (resultado == numero):
#    print "o numero ", numero, "tem resultado", resultado, " e obedece a caracteristica do quadrado da soma dos digitos"
#else:
#    print "o numero ", numero, "tem resultado", resultado, " e  nao obedece a caracteristica do quadrado da soma dos digitos"

import math    
x = input("x")
resultado = math.exp(x)
print resultado

    

    
            

    

    
        
