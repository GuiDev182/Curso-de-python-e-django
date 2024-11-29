#condicoes if/else/elif
#if condicao/comparacao:
    # codigo a ser executado caso a condicao seja verdadeira
#else:
    # codigo a ser executado caso a condicao seja falsa

#sinais de comparacao

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente


import random
from random import Random

from pygame.time import delay

#escreva um programa que faça o computador "pensar" em un umero inteiro entre 0 e 5.
#e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# o programa devera escrever ma tela se o usuario venceu ou perdeu.

'''lista = [0,1,2,3,4,5]
numeroComputador = random.choice(lista) #ou randint(0,5)
numeroUsuario = int(input("Descubra o numero que o computador pensou de 0 a 5: "))

if numeroUsuario == numeroComputador:
    print(f"Parabéns, você acertou! O numero escolhido foi {numeroComputador}")
else:
    print(f"Que pena, você errou!!! O numero escolhido foi {numeroComputador}")'''

#escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por cada km acima do limite

'''velocidadeCarro = int(input("Digite a velocidade do carro: "))

if velocidadeCarro > 80:
    multa = (velocidadeCarro - 80) * 7
    print(f"Voce ultrapassou a velocidade de 80km, sua multa será de R${multa}")
else:
    print("Você esta dentro do limite permitido!")'''

#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

'''numero_inteiro = int(input("Digite um numero inteiro: "))

par = (numero_inteiro % 2)

if par == 0:
    print(f"o numero {numero_inteiro} é par!")
else:
    print(f" o numero {numero_inteiro} é impar")'''

#desenvolva um programa que pergunte a distancia de uma viagem em km.
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$ 0,45 para viagens mais longas

'''distancia_percorrida = float(input("Digite a distancia da viagem: "))

if distancia_percorrida <= 200:
    valor_total = distancia_percorrida * 0.50
    print(f"O valor total a pagar é de R${valor_total}")
else:
    valor_viagens_longas = distancia_percorrida * 0.45
    print(f"o valor total a pagar para viagens mais longas é de {valor_viagens_longas}")'''

#faça um programa que leia um ano qualquer e mostre se ele é bissexto

'''ano = int(input("Digite um ano para saber se ele é bissexto: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"o ano {ano} é bissexto")
else:
    print(f"o ano {ano} nao e bissexto")

#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.'''

'''primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
terceiro_numero = int(input("Digite o terceiro numero: "))

if (primeiro_numero > segundo_numero) and (primeiro_numero > terceiro_numero):
    print(f"o numero {primeiro_numero} é maior que {segundo_numero} e {terceiro_numero}")
    if segundo_numero > terceiro_numero:
        print(f"e o menor numero é {terceiro_numero}")
    else:
        print(f"e o menor numero é {segundo_numero}")
elif (segundo_numero > primeiro_numero) and (segundo_numero > terceiro_numero):
    print(f"o numero {segundo_numero} é maior que {primeiro_numero} e {terceiro_numero}")
    if primeiro_numero > terceiro_numero:
        print(f"e o menor numero é {terceiro_numero}")
    else:
        print(f"e o menor numero é {primeiro_numero}")
elif (terceiro_numero > primeiro_numero) and (terceiro_numero > segundo_numero):
    print(f"o numero {terceiro_numero} é maior que {primeiro_numero} e {segundo_numero}")
    if segundo_numero > primeiro_numero:
        print(f"e o menor numero é {primeiro_numero}")
    else:
        print(f"e o menor numero é {segundo_numero}")
else:
    print("você digitou os três numeros iguais")'''


#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1.250,00, calcule um aumento de 10%
#para inferiores ou iguais, o aumento e de 15%

'''salario = float(input("Digite o seu salario para verificar o aumento: "))

if salario > 1.250:
    menor_aumento = (salario * 0.10) + salario
    print(f"o valor total do seu salario com aumento é de R${menor_aumento}")
else:
    maior_aumento = (salario * 0.15) + salario
    print(f"o valor total do seu salario com aumento é de R${maior_aumento}")'''

#desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

'''ladoA = int(input("Digite o primeiro comprimento: "))
ladoB = int(input("Digite o segundo comprimento: "))
ladoC = int(input("Digite o terceiro comprimento: "))

if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoB + ladoC) > ladoA:
    print(f"as medidas {ladoA}, {ladoB} e {ladoC} formam um triangulo")
else:
    print(f"as medidas {ladoA}, {ladoB} e {ladoC} não formam um triangulo")'''


#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da csa, o salario do comprador e em quantos anos  ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado

'''valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o seu salario: R$ "))
anos_pagamento = int(input("Digite quantos anos você quer pagar a casa: "))

valor_mensal = valor_casa / anos_pagamento
porcentagem_emprestimo = salario_comprador * 0.30

if valor_mensal < porcentagem_emprestimo:
    print("Seu emprestimo esta aprovado!")
else:
    print("Seu emprestimo foi negado!")'''

#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
#1 para binario
#2 para octal
#3 para hexadecimal

'''numero_inteiro = int(input("Digite um numero inteiro: "))
base_conversao = int(input("Digite qual a base de conversão sera usada: \n 1 - binario\n 2 - octal\n 3 - hexadecimal\n R: "))

if base_conversao == 1:
    binario = bin(numero_inteiro)
    print(f"o numero {numero_inteiro} convertido para binário é {binario}")
elif base_conversao == 2:
    octal = oct(numero_inteiro)
    print(f"o numero {numero_inteiro} convertido para octal é {octal}")
elif base_conversao == 3:
    hexa = hex(numero_inteiro)
    print(f"o numero {numero_inteiro} convertido para hexadeciaml é {hexa}")
else:
    print("Você digitou um numero incorreto, tente novamente!")'''

#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior
#o segundo valor é maior
#nao existe valor maior, os dois sao iguais

'''primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
if primeiro_numero > segundo_numero:
    print(f"o numero {primeiro_numero} é maior que {segundo_numero}")
elif segundo_numero > primeiro_numero:
    print(f"o numero {segundo_numero} é maior que {primeiro_numero}")
else:
    print("os dois numeros são iguais")'''

#faça um programa que leia o ano de um jovem e informe, de acordo com a sua idade:
#se ele ainda vai se alistar ao serviço militar.
#se é a hora de se alistar
#se ja passou do tempo do alistamento
#seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

'''ano = int(input("Digite seu ano de nascimento: "))

idade = 2024 - ano

if idade == 18:
    print(f"você tem {idade} e precisa se alistar ")
elif idade < 18:
    tempo_restante = 18 - idade
    print(f"Você ainda nao possui idade para se alistar, o prazo para o alistamento é de {tempo_restante}")
elif idade > 18:
    prazo_passou = idade - 18
    print(f"Você ja tem mais de {idade} anos e ja se passaram mais {prazo_passou} anos, vai alistar nao vagabundo ?")'''

#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
#media abaixo de 5.0: reprovado
#media entre 5.0 e 6.9: recuperação
#media 7.0 ou superior: aprovado

'''primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media >= 7.0:
    print(f"sua média é de {media}, você esta aprovado!")
elif (media > 5.0) and (media < 6.9):
    print(f"sua média é de {media}, Você esta de recuperação")
else:
    print(f"sua media foi de {media}, você esta reprovado")'''

#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#ate 9 anos: mirin
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 20 anos: senior
# acima: master

'''ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2024 - ano_nascimento

if idade < 9:
    print("Sua categoria: Mirim")
elif (idade >= 9) and (idade < 15):
    print("sua categoria: infantil")
elif (idade >= 15) and (idade < 19):
    print("sua categoria: junior")
elif (idade >= 19) and (idade <= 20):
    print("sua categoria: senior")
else:
    print("sua categoria: master")'''

#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status
#de acordo com a tabela abaixo:

#abaixo de 18.5:abaixo do peso
#entre 18.5 e 25:peso ideal
#25 ate 30:sobrepeso
#30 ate 40:obesidade
#acima de 40:obesidade morbida

'''peso = float(input("Digite o seu peso atual: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura

if peso <= 18.5:
    print("você esta abaixo do peso")
elif peso > 18.5 and peso <= 25:
    print("você esta no peso ideal")
elif peso > 25 and peso <= 30:
    print("Você esta sobrepeso")
elif peso > 30 and peso <= 40:
    print("você esta com obesidade")
else:
    print("Você esta acima do peso")'''

# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#a vista dinheiro/cheque: 10% de desconto
#a vista no cartao: 5% de desconto
#em ate 2x no cartao: preço normal
#3x ou mais:20% de juros

'''valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Digite a forma de pagamento: \n 1 - a vista dnheiro ou cheque \n 2 - a vista no cartao \n 3 - em ate 2x no cartão \n 4 - 3x ou mais \n R:"))

if forma_pagamento == 1:
    desconto_10 =  valor_produto - (valor_produto * 0.10)
    print(f"O valor do produto final com desconto é de R${desconto_10}")
elif forma_pagamento == 2:
    desconto_05 = - valor_produto - (valor_produto * 0.5)
    print(f"O valor do produto final com desconto é de R${desconto_05}")
elif forma_pagamento == 3:
    parcela_duas_vezes = valor_produto / 2
    print(f"O valor do produto final é de R${valor_produto} com parcelas de R${parcela_duas_vezes}")
elif forma_pagamento == 4:
    total_parcelas = int(input("quantas parcelas: "))
    total = valor_produto + (valor_produto * 100 /0.20)
    parcela = total / total_parcelas
    print(f"O valor do produto final é de R${total} com parcelas de R${parcela}")
else:
    print("Você digitou o a forma de pagamento incorreta, tente novamente")'''

# crie um programa que jogue jokenpo

'''print("Vamos jogar jokenpo!!!")
escolha_jogador = int(input("Faça sua escolha: \n  1 - Pedra \n 2 - Papel \n 3 - tesoura \n R: "))
print("Agora o computador vai fazer sua escolha...")
delay(2000)
print("So mais um pouco...")
delay(2000)
print("Todos pronto? ")
delay(2000)
print("Jo...")
delay(1000)
print("ken...")
delay(1000)
print("po...")
delay(2000)
escolha_computador = random.randint(0,3)
#escolha pedra
if escolha_jogador == 1 and escolha_computador == 1:
    print(f"Você escolheu PEDRA e o computador escolheu PEDRA, deu empate!")
elif escolha_jogador == 1 and escolha_computador == 2:
    print(f"Você escolheu PEDRA e o computador escolheu PAPEL, o computador venceu!")
elif escolha_jogador == 1 and escolha_computador == 3:
    print(f"Você escolheu PEDRA e o computador escolheu TESOURA, você venceu!")
#escolha papel
elif escolha_jogador == 2 and escolha_computador == 1:
    print(f"Você escolheu PAPEL e o computador escolheu PEDRA, você venceu!")
elif escolha_jogador == 2 and escolha_computador == 2:
    print(f"Você escolheu PAPEL e o computador escolheu PAPEL, deu empate!")
elif escolha_jogador == 2 and escolha_computador == 3:
    print(f"Você escolheu PAPEL e o computador escolheu TESOURA, o computador venceu!")
#escolha tesoura
elif escolha_jogador == 3 and escolha_computador == 1:
    print(f"Você escolheu TESOURA e o computador escolheu PEDRA, o computador venceu")
elif escolha_jogador == 3 and escolha_computador == 2:
    print(f"Você escolheu TESOURA e o computador escolheu PAPEL, você venceu!")
elif escolha_jogador == 3 and escolha_computador == 3:
    print(f"Você escolheu TESOURA e o computador escolheu TESOURA, Deu empate!")
else:
    print("ops...opção invalida, tente novamente")'''

