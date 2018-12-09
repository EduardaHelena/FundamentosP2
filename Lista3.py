# Questao 1
#idade = input("idade")
#f = 0
#salF = 0
#m = 0
#salM = 0
#salarioMaior = 0


#while(idade > 0):
#    
#    sexo = raw_input("sexo : F ou M")
#    salario = input("Salario")
    
#    if(sexo == "F"):
#        f +=1
#        salF = salF + salario
#       if (idade < 30 and salario > salarioMaior):
#            salarioMaior = salario
#            
#    else:
#        m +=1
#        salM = salM + salario
#        if (idade < 30 and salario > salarioMaior):
#            salarioMaior = salario
#    idade = input("idade")
    
#print "media homens: ", salM/float(m), "media mulheres", salF/float(f),"Maior salario: ", salarioMaior
# ---------------------------------------------------------------------------------------------------------
#Questao 2
#qtd = input("numero de termos: ")
#primeiro = input("o primeiro termo: ")
#razao = input("razao da pa: ")
#print "primeiro: ", primeiro

#for i in range(2, qtd + 1):
#    termo = primeiro + (razao*(i-1))
#    print "termo ", i, ": ", termo
#    
#print "Fim"
#-----------------------------------------------------------------------
#questao 3
#numero = int(input("numero: "))
#qtdPar = 0
#qtdImpar = 0
#somaPar = 0

#while(numero != 0):
#    if(numero%2 == 0):
#        qtdPar +=1
#        somaPar = somaPar + numero
#        media = somaPar/qtdPar
#        print"Numero Par: ", qtdPar
#        print"Numero Impar: ", qtdImpar
#        print"Média Pares: ", media
#        
#    else:
#        qtdImpar +=1
#        print " Numero Impar: ", qtdImpar
#        print " Numero Par: ", qtdPar
#        
#   numero = input("\n numero: ")
    
#-----------------------------------------------------------------------
#questao 4
#print " para fim: digite XXX "
#nomeProduto = raw_input("Nome Produto: ")
#valorCaro = 0
#valorAnterior = 0

#while(nomeProduto != "XXX"):
#    valorProduto = float(input("Valor Produto: "))
#   if(valorProduto == valorAnterior):
#        print "erro: Valor de produto já existente"
#    else:
#        valorAnterior = valorProduto
#        if(valorProduto >= valorCaro):
#            valorCaro = valorProduto
#            nomeCaro = nomeProduto
#    print " para fim: digite XXX "
#    nomeProduto = raw_input("\n Nome do Produto: ")
    

#print "Produto mais caro: ", nomeCaro, valorCaro
#-----------------------------------------------------------------------
#questao 5
#pesoSoma = 0
#for i in range(1, 26):
#    pesoCaixa = input("Peso Numero: ")
#    pesoSoma = pesoSoma + pesoCaixa
    
#print("Peso Total: "), pesoSoma
#-----------------------------------------------------------------------
#questao 6
#somaProduto = 0
#for i in range(1, 51):
#    qtdProduto = input("Quantidade Produto: ")
#    valorProduto = input("Valor Produto: ")
#    somaProduto = somaProduto +(qtdProduto * valorProduto)
#print "Total Gasto: ", somaProduto
#-----------------------------------------------------------------------
#questao 7
#n1 = input("Numero 1 : ")
#n2 = input("Numero 2 : ")
#soma = 0
#if(n1 > n2):
#    print "error : soma não sera realizada"
#else:
#    for i in range(n1 + 1, n2):
#        soma = soma + i
#    print "soma total dos produtos: ", soma
#-----------------------------------------------------------------------
#questao 8
#n1 = input("Diga o primeiro: ")
#n2 = input("Diga o segundo: ")
#soma = 0
#if(n1 > n2):
#     print "error : soma não sera realizada"
#else:
#    for i in range(n1 + 1, n2):
#        if (i%4 == 0):
#           soma = soma + i
#    print "Soma dos Multiplos de 4:  ", soma
#-----------------------------------------------------------------------
#questao 9

#larguraComodo = float(input("Largura"))
#comprimentoComodo = float(input("Comprimento"))
#nomeComodo = raw_input("Nome do Comodo")
#somaArea = 0

#while(larguraComodo > 0 or comprimentoComodo > 0):
    
        #somaArea = somaArea + (larguraComodo * comprimentoComodo)
        
        #larguraComodo = input("Largura")
        #comprimentoComodo = input("Comprimento")
        #nomeComodo = raw_input("Nome do Comodo")
        
        
#print "Area total: ", somaArea
#-----------------------------------------------------------------------
#questao 10

#candidato1_Soma = 0 
#candidato2_Soma = 0
#candidato3_Soma = 0
#candidato4_Soma = 0
#candidato5_Soma = 0

#for i in range(1, 20001):
#    voto = input("input seu voto: 1 - João da Silva, 2- José Ramalho, 3 - Maria Mattos, 4 - Voto em Brando, 5 - Nulo")
#    if(voto == 1):
#        candidato1_Soma = candidato1_Soma + 1
#        
#    elif(voto == 2):
#        candidato2_Soma = candidato2_Soma + 1
#        
#    elif(voto == 3):
#        candidato3_Soma = candidato3_Soma + 1
#        
#    elif(voto == 4):
#        candidato4_Soma = candidato4_Soma + 1
#        
#    elif(voto == 5):
#        candidato5_Soma = candidato5_Soma + 1
#        
#    else:
#        print "error: numero digitado não tem correspondencia com nenhum candidato"
#
#if(candidato1_Soma > candidato2_Soma and candidato1_Soma > candidato3_Soma):
#    print "\n João da Silva, teve mais votos"
#elif(candidato2_Soma > candidato1_Soma and candidato2_Soma > candidato3_Soma):
#    print "\n José Ramalho, teve mais votos"
#elif(candidato3_Soma > candidato1_Soma and candidato3_Soma > candidato2_Soma):
#    print "\n
#    Maria Mattos, teve mais votos"
#else:
#    print "\n Empate"
#    
#
#print "\n Total de votos por candidato:"
#print "Candidato 1: ", candidato1_Soma
#print "Candidato 2: ", candidato2_Soma
#print "Candidato 3: ", candidato3_Soma
#print "Candidato 4: ", candidato4_Soma
#print "Candidato 5: ", candidato5_Soma
#-----------------------------------------------------------------------
#questao 11
# nao tem a formula
#-----------------------------------------------------------------------
#questao 12
#nome_Turma = raw_input("Diga o nome da turma, usando a ordem, ex: Primeira Turma ")
#numero_Turma = 1
#while(numero_Turma <= 8):
#    for i in range(1, 31):
#        nome_Aluno = raw_input("Diga o nome do aluno: ")
#        nota1_Aluno = float(raw_input("Diga a nota 1 do aluno: "))
#        nota2_Aluno = float(raw_input("Diga a nota 2 do aluno: "))
#        
#        media_Aluno = (nota1_Aluno + nota2_Aluno)/2
#        if(media_Aluno >= 5):
#            print"Aluno: ", nome_Aluno, " aprovado, nota: ", media_Aluno
#            print ""
#       else:
#            print"Aluno: ", nome_Aluno, " reprovado, nota: ", media_Aluno
#            print ""
#    print "Final Turma"
#    print ""
#    
#    resposta = raw_input("Deseja começar outra turma: sim ou nao primeira")
#    numero_Turma +=1    
#
#print ""    
#print "Todos os alunos e turmas foram armazenados"
#-----------------------------------------------------------------------
#questao 13 
#respostaS = 0
#respostaN = 0
#total = 0

#resposta = raw_input("Esta satisfeito com o produto: S ou N: ")
#while(resposta != "F"):
#    if(resposta == "S"):
#        respostaS = respostaS + 1
#    elif(resposta == "N"):
#        respostaN = respostaN + 1
#    else:
#        print "error"
#        break
#    resposta = raw_input("Esta satisfeito com o produto: S ou N: ")
#total = respostaS + respostaN
#valorS = float(respostaS * 100)/total
#valorN = float(respostaN * 100)/total
#print "Respostas sim: ", valorS,"%", "Respostas nao: ", valorN,"%"
#print "Total de Respostas: ",total
#-----------------------------------------------------------------------
#questao 14
#somaI = 0
#quantidade = input("quantidade")
#for i in range(1, quantidade + 1, 1):
#    if(i%2 == 1):
#        somaI = somaI + i
#        print "Numero: ", i
#
#print "Soma: ", somaI
#-----------------------------------------------------------------------
#questao 15
 
#for i in range(1,6):
#    par1 = raw_input("Digite o par, separado por espaço: ex 10 12, 1 2: ")
#    Intervalo1 = par1.split()
#    valor1 = int(Intervalo1[0])
#    valor2 = int(Intervalo1[1])
#    for i in range(valor1, valor2 + 1):
#        if(i%2 == 0):
#            print "Numero: ", i
#    print "Fim intervalo"
#    print ""
#-----------------------------------------------------------------------
#questao 16
#cont = 0
#i = 2
#while(cont < 50):
#  print "Numero: ", i
#  cont +=1
#  i = i + 2
#print""
#print cont
#-----------------------------------------------------------------------
#questao 18
#somaIdade = 0
#contJovem = 0
#numeroIdade = 100
#for i in range(1, numeroIdade + 1):
#    idade = input("idade: ")
#    somaIdade = somaIdade + idade
#    if (21 <= idade <= 65):
#        contJovem += 1
#        print contJovem
#        
#print "media grupo: ", (somaIdade)/3
#print "Porcentagem de pessoas com 21 a 65: ", (contJovem*100)/float(numeroIdade)
#-----------------------------------------------------------------------
#questao 19




   

        
 



