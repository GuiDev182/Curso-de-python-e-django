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









