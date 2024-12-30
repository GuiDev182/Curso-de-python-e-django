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
'''print('---'*20)
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
        exit()'''

#faça um programa que leia um numero qualquer e mostre o seu fatorial.
#ex: 5º= 5x4x3x2x1=120

'''numero = int(input("Digite um numero para saber o seu fatorial: "))
fatorando = numero - 1
fatorial = numero * fatorando

while fatorando != 1:
    fatorando -= 1
    fatorial = (fatorial * fatorando)
print(f"o fatorial do numero {numero} é {fatorial}")'''

#desenvolva um programa que leia o primeiro termo e a razão de uma pa.
#no final,mostre os 10 primeiros termos dessa progressao.

'''primeiro_termo = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da PA: "))

termo = 0
while termo != 9:
    primeiro_termo = primeiro_termo + razao
    termo += 1
    print(primeiro_termo)'''

#melhore o desafio anterior perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando
#ele disser que quer mostrar os termos

'''primeiro_termo = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da PA: "))

termo = 0
qtd_termos_a_mais = 0
while termo != 9:
    primeiro_termo = primeiro_termo + razao
    termo += 1
    print(primeiro_termo)

mais_termos = int(input("Gostaria de ver mais termos? \n 1 - Sim \n 2 - Não \n R: "))
if mais_termos == 1:
    qtd_termos = int(input("Quantos termos a mais gostaria de saber? \n R: "))
    while qtd_termos_a_mais != qtd_termos:
        primeiro_termo = primeiro_termo + razao
        termo += 1
        qtd_termos_a_mais += 1
        print(primeiro_termo)
else:
    print("Programa finalizado!")
    exit()'''

#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
#sequencia de fibonnaci
#ex: 0 - 1 - 1 - 2 -3 - 5 - 8

'''lista_fibbo = [1,1,2]
contador = 0
numero = int(input("Digite um numero: "))


while contador != numero:
    contador += 1
    proximo_numero = lista_fibbo[-1] + lista_fibbo[-2]
    lista_fibbo.append(proximo_numero)
print(lista_fibbo[0:contador])'''

#crie um programa que leia varios numeros inteiros pelo teclado.
#o programa só vai parar quando o usuario digitar o valor 999, que é condição de parada.
#no final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)

'''contador_numeros = 0
lista_numeros = []
numeros = int(input("Digite um numero inteiro: "))

while numeros != 999:
    contador_numeros += 1
    lista_numeros.append(numeros)
    numeros = int(input("Digite um numero inteiro: "))
else:
    if numeros == 999:
        soma_lista_numeros = sum(lista_numeros)
        print(f"Você digitou o numero 999, você digitou {contador_numeros} numeros antes da parada e soma deles é {soma_lista_numeros}")
        exit()'''

#crie um programa que leia varios numeros inteiros pelo teclado, no final da execução, mostre a media entre todos os valores
#e qual foi o maior e menor valor lido. o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores

'''lista_numeros = [0]
numeros = int(input("Digite um numero: "))
menu = int(input("Você deseja continuar a digitar? \n 1 - Sim \n 2 - Não \n R: "))
lista_numeros.append(numeros)
while menu != 2:
    if menu > 2 or menu < 1:
        print("valor incorreto, tente novamente")
        menu = int(input("Você deseja continuar a digitar? \n 1 - Sim \n 2 - Não \n R: "))
    else:
        numeros = int(input("Digite um numero: "))
        lista_numeros.append(numeros)
        menu = int(input("Você deseja continuar a digitar? \n 1 - Sim \n 2 - Não \n R: "))
else:
    media = sum(lista_numeros) / 2
    lista_numeros.sort()
    maior = lista_numeros[-1]
    menor = lista_numeros[0 + 1]
    print(f"a média dos numeros digitados foi {media}, o maior numero foi {maior} e o menor foi {menor}")'''



