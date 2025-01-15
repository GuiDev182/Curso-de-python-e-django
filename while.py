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


# faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
#o programa sera interronpido quando o numero solicitado for negativo

'''numero_solicitado = int(input("Digite um numero para saber sua tabuada: "))
while True:
    if numero_solicitado < 0:
        print("Voce digitou um numero negativo")
        break
    else:
        for multiplicador in range(10):
            print(f"{numero_solicitado} x {multiplicador + 1} = {numero_solicitado * (multiplicador + 1)}")
        numero_solicitado = int(input("Digite um numero para saber sua tabuada: "))'''

#faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER,
#mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''import random

print("JOGO DO PAR OU IMPAR")
escolha_jogador = int(input("Faça uma escolha: \n 1 - Par \n 2 - Ímpar \n R: "))
vitorias_jogador = 0
if escolha_jogador == 1:
    lista_impar = [1,3,5,7,9]
    numero_jogador = int(input("Digite um numero Par de 1 a 10: "))
    numero_computador = random.choice(lista_impar)
    delay(1000)
    print(f"o computador escolheu o numero {numero_computador}")
    while numero_jogador > numero_computador:
        print("Você Venceu")
        vitorias_jogador += 1
        print(f"Vitorias: {vitorias_jogador}")
        break
    else:
        print("O computador venceu! tente novamente")
        escolha_jogador = int(input("Faça uma escolha: \n 1 - Par \n 2 - Ímpar \n R: "))
elif escolha_jogador == 2:
    lista_par = [2,4,6,8,10]
    numero_jogador = int(input("Digite um numero Ímpar de 1 a 10: "))
    numero_computador = random.choice(lista_par)
    delay(1000)
    print(f"o computador escolheu o numero {numero_computador}")
    while numero_jogador > numero_computador:
        print("Você Venceu")
        vitorias_jogador += 1
        print(f"Vitorias: {vitorias_jogador}")
        break
    else:
        print("O computador venceu! tente novamente")
        escolha_jogador = int(input("Faça uma escolha: \n 1 - Par \n 2 - Ímpar \n R: "))'''

#crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuario quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20

'''print("CADASTRO DE PESSOAS")
maiores_18 = 0
masculino = 0
feminino = 0
mulheres_menos_20 = 0

idade = int(input("Digite a sua idade: "))
if idade >= 18:
    maiores_18 += 1
sexo = int(input("Digite o seu sexo: \n 1 - Masculino \n 2 - Feminino \n R: "))
if sexo == 1:
    masculino += 1
else:
    feminino += 1
if idade <= 20 and sexo == 2:
    mulheres_menos_20 += 1
menu = int(input("Deseja continuar a cadastrar? \n 1 - Sim \n 2 - Não \n R: "))

while menu != 2:
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        maiores_18 += 1
    sexo = int(input("Digite o seu sexo: \n 1 - Masculino \n 2 - Feminino \n R: "))
    if sexo == 1:
        masculino += 1
    else:
        feminino += 1
    if idade <= 20 and sexo == 2:
        mulheres_menos_20 += 1
    menu = int(input("Deseja continuar a cadastrar? \n 1 - Sim \n 2 - Não \n R: "))
else:
    if idade >= 18 and sexo == 1:
        maiores_18 += 1
        masculino += 1
    elif idade >= 18 and sexo == 2:
        maiores_18 += 1
        feminino += 1
    else:
        feminino += 1
        mulheres_menos_20 += 1

print(f"existem {maiores_18} pessoas maiores que 18 anos, {masculino} pessoas masculinas ,  {feminino} pessoas femininas e {mulheres_menos_20} tem menos que 20 anos")'''


#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print("CADASTRO DE PRODUTOS")

total_gasto = 0
produtos_maior_1000 = 0
produtos = {}

nome_produto = (input("Digite o nome do produto: ")).lower()
produtos = [nome_produto]
preco_produto = {float(input("preco do produto: "))}
produtos = [preco_produto]

print(produtos)








