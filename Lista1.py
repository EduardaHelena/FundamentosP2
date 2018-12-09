import math
#questao5
#p1 = input("P1: ")
#p2 = input ("P2: ")
#t = input("t: ")
#l1 = input("l1: ")
#l2 = input("l2: ")
#l3 = input("l3: ")
#l4 = input("l4: ")
#l5 = input("l5: ")

#mediaListas = (l1+l2+l3+l4+l5)/5
#media= (0.3*p1)+(0.4*p2)+(0.2*mediaListas)+(0.1*t)

#print "media:", media
# -------------------------------------------

#questao7
#n1 = input("n1: ")
#n2 = input("n2: ")
#n3 = input("n3: ")
#n4 = input("n4: ")

#soma= n1+n2+n3+n4
#print "A soma: ",soma

#-------------------------------------------

#questao8
#n1 = input("n1: ")
#n2 = input("n2: ")
#n3 = input("n3: ")

#media = (n1+n2+n3)/3
#print "A media do Aluno:",media

#-------------------------------------------

#questao9

#salario = input("salario: ")

#novoSalario = (salario*25)/100 + salario
#print "novo salario:", novoSalario

#-------------------------------------------

#questao10

#libra = input("Peso (em libras): ")
#total = libra * 453.6
#print "Resposta: ", total

#-------------------------------------------

#questao11
#polegada = input("Comprimento em Polegada: ")

#centimentros = polegada*2.54
#print polegada, "pol =",centimentros,"cm"

#-------------------------------------------

#questao12
#raio = input("Digite o Raio do circulo")
#area = 3.14159 * (raio**2)
#print "a area: ", area

#-------------------------------------------

#questao13
#m = input(" Diga m ")
#n = input(" Diga n")

#if(m>n):
  #lado1 = (m**2) - (n**2)
  #lado2 =  2*m*n
  #hipotenusa = (m**2) + (n**2)
  #print "lado 1:",lado1,"lado 2:",lado2,"hipotenusa",hipotenusa

#else:
  #print "error"
#-------------------------------------------

#questao14
import math 

#a = float(input(" Diga a "))
#b = float(input(" Diga b "))
#c = float(input(" Diga c "))

#delta = (b**2)- 4*a*c
#if (delta > 0):
    #Raiz_1 = (-b + math.sqrt(delta))/(2*a)
    #Raiz_2 = (-b - math.sqrt(delta))/(2*a)
    #print "raiz 1: ",Raiz_1,"raiz 2: ", Raiz_2
#else:
 #   print "delta negativo"

#-------------------------------------------

#questao15
Real_1  = input("Numero de moedas de 1 Real: ")
Real_50 = input("Numero de moedas de 0,50 centavos: ")
Real_25 = input("Numero de moedas de 0,25 centavos: ")
Real_10 = input("Numero de moedas de 0,10 centavos: ")
Real_5  = input("Numero de moedas de 0,05 centavos: ")
Real_01 = input("Numero de moedas de 0,01 centavos: ")


Total = Real_1 + (Real_50 * 0.5) + (Real_25 * 0.25) + (Real_10 * 0.10) + (Real_5 *0.05) + (Real_01 * 0.01)
print "Quantia total calculada: ", Total

#-------------------------------------------

#questao16

#h = input("Hora: ")
#m = input("Minuto: ")
#s = input("Segundo: ")

#totalSegundo = (h * 3600) + (m * 60) + s
#print totalSegundo, " segundos"

#-------------------------------------------

#questao17

#anos  = input("Diga o ano: ")
#meses = input("Diga os meses: ")
#dias  = input("Diga os dias: ")

#totaldias = (anos*365)+(meses*30)+ dias
#print totaldias," dias"

#-------------------------------------------

#questao18
#dias = input("digas os dias")
#ano = dias/365
#meses = (dias%365)/30
#dias = (dias%365)% 30

#print "anos:", ano," meses:", meses, " dias:", dias


#-------------------------------------------

#questao19 igual a 16

#-------------------------------------------

#questao20

#base = input ("Diga a base")
#altura = input("Diga a altura")

#perimetro = (2*base)+(2*altura)
#area = (base * altura)
#diagonal_elevada = (base**2)+(altura**2)
#diagonal = math.sqrt(diagonal_elevada)

#print "perimetro:",perimetro, " area:",area, " diagonal:",diagonal

#-------------------------------------------

#questao21

#salarioFixo = input("Salario Fixo: ")
#valorVendas = input("Valor Vendas: ")

#salarioFinal = ((valorVendas*4)/100) + salarioFixo
#print "Salario Final: ",salarioFinal
 
#-------------------------------------------

#questao22

#salario = input("Salario: ")
#conta1  = input("Valor conta 1: ")
#conta2  = input("Valor conta 2: ")

#conta1_Final = (conta1 * 2)/100
#conta2_Final = (conta2 * 2)/100
#salario_Final = salario - (conta1_Final + conta2_Final)

#print "Salario Final: ",salario_Final

#-------------------------------------------

#questao23
#n1 = input("n1: ")
#n2 = input("n2: ")
#n3 = input("n3: ")
#p1 = input("p1: ")
#p2 = input("p2: ")
#p3 = input("p3: ")

#media = float((n1*p1) + (n2*p2) + (n3*p3))/(p1 + p2 + p3)
#print "Media Ponderada: ", media

#-------------------------------------------

#questao24

#salario_Funcionario = input("Diga o salario do funcionario: ")
#salario_Minimo      = input("Diga o salario minimo: ")

#quantidade = (salario_Funcionario)/salario_Minimo
#print "o funcionario recebe ", quantidade, "de salarios minimos"






