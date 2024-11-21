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
for multiplos in range(0+1,501,3):
    soma += multiplos
    print(multiplos)
print(f"a soma total é de {soma}")'''

#Faça um programa que leia um numero inteiro qualquer e mostre na sua tela a sua tabuada

'''numero = int(input("Digite um numero para saber sua tabuada: "))

for i in range(10):
     print(f"{numero} x {i+1} = {numero*(i+1)}")'''



