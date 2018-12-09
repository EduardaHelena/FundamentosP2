#Faça um programa que leia uma string e crie uma outra string igual,
#mas com  todos os caracteres em maiúsculos.

#primitiva = raw_input('Diga a palavra original')
#derivada = primitiva.upper()
#print derivada
#--------------------------------------------------------
#Faça um programa que leia uma string e crie uma outra string igual,
#mas com  todos os caracteres em minúsculo.

#primitiva = raw_input('Diga a palavra original')
#derivada = primitiva.lower()
#print derivada
#--------------------------------------------------------
#Faça um programa que leia uma string e um caractere e
#diga quantas vezes o caractere aparece na string

#string = raw_input('diga a string:')
#caracter = raw_input('diga o caracter:')
#numero = string.count(caracter)
#print "Caracter: ", caracter , " aparece: ", numero, " vezes"
#--------------------------------------------------------
#Faça um programa que leia uma string e um caractere e
#crie uma outra string sem o caractere lido.
#string = raw_input('diga a string:')
#caracter = raw_input('diga o caracter:')

#for i in range(0, len(string)):
#  novastring=string.replace(caracter, "")

#print "nova string: ", novastring

#--------------------------------------------------------
#Faça um programa que leia uma string e crie uma outra
#string repetindo os caracteres
#Ex:  carro => ccaarrrroo

#string = raw_input('diga a string:')
#novastring = ""
#for i in range(0, len(string)):
#   novastring += string[i]*2
#print "nova string: ", novastring

#--------------------------------------------------------
#Faça um programa que leia uma string e #crie uma outra
#string repetindo apenas as  vogais
#Ex:  carro => caarroo

#string = raw_input('diga a string:')
#string = string.lower()
#novastring = ""
#for i in range(0, len(string)):
#  if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
#    novastring += string[i]*2
#  else:
#    novastring += string[i]
#print "nova string: ", novastring
#--------------------------------------------------------
#Faça um programa que leia uma string e crie uma outra
#string invertendo as posições de dois em dois
#Ex:  mexico => emixoc

#string = raw_input('diga a string:')
#novastring = ""
#for i in range(0, len(string)):
#  if(i%2 != 0):
#    novastring += string[i]+string[i-1]
#print "nova string: ", novastring
#--------------------------------------------------------
#Faça um programa que leia duas strings e imprima a
#interseção entre as strings
#Ex:   cabelo e pelo => e, l, o
#string1 = raw_input('diga a primeira palavra')
#string2 = raw_input('diga a segunda palavra')
#interseccao = ""

#def Busca (string1, letra):
#  achou = False 
#  for i in range(0, len((string1))):
#    if(string1[i] == letra):
#      achou = True
#      return string1
#  if(achou == False):
#    string1 += letra
#    return string1
  

#for i in range(0, len(string1)):
#  for j in range(0, len(string2)):
#    if(string1[i] == string2[j]):
#      letra = string1[i]
#      interseccao = Busca(interseccao, letra)

#print interseccao

