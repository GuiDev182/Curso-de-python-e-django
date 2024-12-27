# for c in range(0,10):
#     n = int(input("digite um valor: "))
#     if n == 0:
#         print("Voce digitou o valor 0")
#         break

'''par = 0
lista_par = []
lista_impar = []
impar = 0
numero = int(input("digite um valor: "))
while numero != 0:
    numero = int(input("digite um valor: "))
    if numero % 2 == 0:
        par += 1
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
        impar += 1
print(f"você digitou {par} numeros pares e {impar} numeros impares")
print(f"numeros pares digitados: {lista_par}")
print(f"numeros pares digitados: {lista_impar}")'''
#import random

#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' ou 'f'
#caso esteja errado, peça que digite novamente ate ter um valor correto

'''sexo_pessoa = str(input("Digite o sexo: \n M - Masculino \n F - Feminino \n R: ")).lower()

while sexo_pessoa != 'm' and sexo_pessoa != 'f':
    print("valor incorreto! Tente novamente")
    sexo_pessoa = str(input("Digite o sexo: \n M - Masculino \n F - Feminino \n R: ")).lower()
print(f"Sexo: {sexo_pessoa.upper()} ")'''

#melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10.
# so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer

'''lista = range(0,10)
palpites = 0
numeroComputador = random.choice(lista) #ou randint(0,5)
numeroUsuario = int(input("Descubra o numero que o computador pensou de 0 a 5: "))

while numeroUsuario != numeroComputador:
    print(f"Que pena, você errou!!! tente novamente")
    numeroComputador = random.choice(lista)
    palpites += 1
    numeroUsuario = int(input("Descubra o numero que o computador pensou de 0 a 5: "))
print(f"Parabéns! você acertou ! Foram gastos {palpites} palpites para voce acertar")'''

# crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]subtrair
#[3]maior
#[4]novos numeros
#[5]sair do programa
#seu programa deverá realizar a operação solicitada em cada caso
print('---'*20)
valor_um = int(input("Digite o primeiro valor: \n R: "))
valor_dois = int(input("Digite o segundo valor: \n R: "))
print("Menu")

menu = int(input("Escolha uma alternativa: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior valor \n [4] - Novos numeros \n [5] - Sair do programa \n R: "))

while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
    print("valor incorreto! tente novamente")
    menu = int(input("Escolha uma alternativa: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior valor \n [4] - Novos numeros \n [5] - Sair do programa \n R: "))
else:
    if menu == 1:
        soma_total = valor_um + valor_dois
        print(f"a soma total dos numeros {valor_um} e {valor_dois} é {soma_total}")
    elif menu == 2:
        multiplicacao = valor_um * valor_dois
        print(f"a multiplicação dos numeros {valor_um} e {valor_dois} é {multiplicacao}")
    elif menu == 3:
        if valor_um > valor_dois:
            print(f"o numero de maior valor é {valor_um}")
        else:
            print(f" o maior valor é {valor_dois}")
    elif menu == 4:
        while menu == 4:
            valor_um = int(input("Digite o primeiro valor: \n R: "))
            valor_dois = int(input("Digite o segundo valor: \n R: "))
            menu = int(input("Escolha uma alternativa: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior valor \n [4] - Novos numeros \n [5] - Sair do programa \n R: "))
        if menu == 5:
            print("Você saiu do programa")
            exit()
    elif menu == 5:
        print("Você saiu do programa")
        exit()











