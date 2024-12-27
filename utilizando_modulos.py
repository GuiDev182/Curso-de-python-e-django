#bliblioteca math
import math
import random
import pygame


#import math # importa tudo da biblioteca
#from math import ceil # importa apenas uma

# num = int(input("digite um numero: "))

# raiz = math.sqrt(num)
# print(f"a raiz quadrada do numero {num} é {raiz:.2f}")

#Crie um programa que leia um numero real qualquer pelo teclado e mostre na sua tela a sua porcao inteira.
#ex: Digite um numero: 6.127, o numero 6.127 tem a parte inteira 6

# numero_real = float(input("Digite um numero real: "))

# parte_inteira = math.trunc(numero_real)

# print(f"a porção inteira do numero {numero_real} é {parte_inteira}")

#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre
#o comprimento da hipotenusa.

# cateto_oposto = int(input("Digite o comprimento do cateto oposto: "))
# cateto_adjacente = int(input("Digite o comprimento do cateto adjacente: "))

# hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

# print(f"o comprimento da hipotenusa é de {hipotenusa:.2f}")

#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse angulo

# angulo = int(input("Digite um angulo: "))

# seno = math.sin(angulo)
# cosseno = math.cos(angulo)
# tangente = math.tan(angulo)

# print(f"O seno do angulo {angulo} é {seno}, o cosseno é {cosseno} e a tangente é {tangente}")

# um professor quer sortear um dos quatro alunos para apagar o quadro.
#Faça um programa que ajude, lendo o nome deles e escrevendo o nome do escolhido

# lista_alunos = ["joao", "felipe", "jose", "maria"]

# escolhido = random.choice(lista_alunos)

# print(f"o nome escolhido foi {escolhido}")

# o mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# lista_alunos = ["joao", "felipe", "jose", "maria"]
# random.shuffle(lista_alunos)
#
# print(f"a ordem sera de apresentacao sera: {lista_alunos}")

#faça um programa em python que abra e reproduza o audio de um arquivo em mp3

# pygame.mixer.init()
# pygame.mixer.music.load("edm-deep-house-ish-female-vocal-112184.mp3")
# pygame.mixer.music.play()
#
# while pygame.mixer.music.get_busy():
#     continue
# # pygame.quit()








