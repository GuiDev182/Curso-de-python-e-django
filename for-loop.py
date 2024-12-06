#ESTRUTURA DE REPETIÇÃO
from pygame.time import delay

'''for c in range(1,6):
    print('01')
print('fim')'''


'''n = int(input('Digite um numero: '))
for c in range(0,n):
    print(c)
print('Fim')'''

'''i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')'''

'''s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'o somatorio de todos os valores foi {s}')'''

#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
#indp de 10 até 0, com uma pausa de 1 segundo entre eles

'''for c in range(10,0,-1):
    print(c)
    delay(1000)
print("Feliz 2025!!!")'''

#crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50
'''print("numeros pares")
for c in range(0,51,2):
    print(c)'''


#faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres
# e que se encontram no intervalo de 1 ate 500
'''soma = 0
cont = 0
for multiplos in range(1,501,2):
    if multiplos % 3 == 0:
        cont += 1
        soma += multiplos
print(f"a soma de todos os valores é de {soma}")'''

#Faça um programa que leia um numero inteiro qualquer e mostre na sua tela a sua tabuada

numero = int(input("Digite um numero para saber sua tabuada: "))

for indice in range(1, 10):
     print(f"{numero} x {indice} = {numero*indice}")

#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#se o valor digitado for impar, desconsidere
'''soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f"Digite o {c} numero: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"voce informou {cont} numeros pares e a soma foi {soma}")'''

#desenvolva um programa que leia o primeiro termo e a razão de uma pa.
#no final,mostre os 10 primeiros termos dessa progressao.


'''primeiro_termo = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = primeiro_termo + (11 - 1) * razao
for c in range(primeiro_termo,decimo,razao):
        print(c)'''


#Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

'''num = int(input("Digite um numero inteiro: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{c}')
print(f'o numero {num} foi divisivel {tot}')
if tot == 2:
    print('e por isso ele é PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')'''








