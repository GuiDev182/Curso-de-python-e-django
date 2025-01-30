'''def lin():
    print('-'*30)

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo(' CURSO EM VIDEO ')
titulo(' APRENDA PYTHON ')
titulo(' GUSTAVO GUANABARA ')

a = 4
b = 5

def soma(numero01, numero02):
    soma = a + b
    print(soma)

soma(4, 5)

#empacotar parametros

def contador(* num):
    print(num)
contador(2,1,7)
contador(8,0)
contador(3)'''
from random import randint
from time import sleep


'''def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [4,6,4,8,9]
dobra(valores)
print(valores)'''

#faça um programa que tenha uma função chamada area, que
# receba as dimensoes de um terreno retangular(largura e comprimento)
# e mostre a area do terreno

'''largura = float(input("Digite a largura: "))
comprimento = float(input("digite o comprimento: "))

def area(largura, comprimento):
    area_retangulo = largura * comprimento
    print(f"a Area do terreno é de {area_retangulo} M²")

print(area(largura, comprimento))'''

# faça um programa quwe tenha uma funcao chamada escreva(),
# que receba um texto qualquer como parametro e mostre uma mensagem com
#tamanho adaptavel
'''texto = input("digite um texto: ")

def escreva(texto):
    print('-'* len(texto))
    print(texto)
    print('-'* len(texto))
    return texto

escreva(texto)'''

#faça um programa que tenha uma função chamada contador(), que receba
# tres parametros: inicio, fim e passo e realiza a contagem
#seu programa tem que realizar tres contagens atraves da funcao criada:

#a)de 1 ate 10, de 1 em 1
#b) de 10 ate 0, de 2 em 2
#uma contagem personalizada

'''def contador01(inicio, fim, passo):
    print("Contagem de 1 ate 10 de 1 em 1")
    sleep(1)
    for contagem in range(inicio,fim,passo):
        print(contagem, end=' ')
        sleep(0.5)
        contagem += 1
    print("FIM!")
contador01(1, 11, 1)'''

'''def contador02(inicio, fim, passo):
    print("Contagem de 10 ate 1 de 2 em 2")
    sleep(1)
    for contagem in range(inicio,fim,passo):
        print(contagem, end=' ')
        sleep(0.5)
        contagem += 1
    print("FIM!")
contador01(10, 0, -2)

print("Agora é sua vez de personalizar a contagem")
sleep(0.5)
inicio = int(input("digite o inicio: "))
fim = int(input("digite o fim: "))
passo = int(input("Digite o passo: "))

def contador03(inicio, fim, passo):
#ordem crescente
    if inicio < fim and passo > 0:
        for contagem in range(inicio,fim,passo):
            print(contagem, end=' ')
            sleep(1)
            contagem += passo
        print("FIM!")
#passo negativo
    elif inicio > fim and passo < 0:
        for contagem in range(inicio,fim,passo):
            print(contagem, end=' ')
            sleep(1)
            contagem += passo
        print("FIM!")
    else:
 #ordem decrescente
        for contagem in range(inicio,fim,-(passo)):
            print(contagem, end=' ')
            sleep(1)
            contagem += passo
        print("FIM!")

contador03(inicio, fim, passo)'''

#faça um programa que tenha uma função chamada maior(), que receba varios
#parametros com valores inteiros.
#seu programa tem que analisar todos os valores e dizer qual deles é maior

'''def maior(* num):
    print('-'*30)
    print("Analisando os valores passados...")
    sleep(0.8)
    if len(num) == 0 or len(num) < 0:
        print("Foram informados 0 valores ao todo")
        print(f"o maior valor informado foi 0")
    else:
        for numero in num:
            sleep(0.8)
            print(numero, end=' ')
        print(f"foram informados {len(num)} valores ao todo")
        print(f"o maior valor informado foi {max(num)}")

maior(4,5,6,9,0,3)
maior(3,1,2)
maior(1,2)
maior(6)
maior()'''

#faça um programa que tenha uma lista chamada numeros e duas funcoes
#chamadas sorteio() e somaPar(). A primeira funcao vai sortear 5 numeros
# e vai colocalos dentro da lista e a segunda funcao vai mostrar a soma
#entre todos os valores pares sorteados pela função anterior

numeros  = []
numeros_pares = []

def sorteio(numeros):
    print(f"Sorteando 5 valores da lista:  ",  end= ' ')
    for indice in range(0, 5):
        sleep(0.8)
        numeros.append(randint(0, 99))
        indice += 1
        print(numeros[-1], end=' ')
    print('PRONTO!')

def somaPar(numeros_pares):

    soma_pares = sum(numeros_pares)
    print(f"Somando os valores pares de {numeros}, temos {soma_pares}")

sorteio(numeros)
somaPar(numeros_pares)








