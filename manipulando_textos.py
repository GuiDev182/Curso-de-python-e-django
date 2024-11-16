#fatiamento
#c u r s o e m v i d e o
#1 2 3 4 5 6 7 8 9 10 11 12
from os.path import split

'''frase = 'curso em video'
frase[9:21] #começa do numero 9 ao 21
frase[9:21:2] #começa do numero 9 ao 21, pulando de dois em dois
frase[:5] #começa do inicio e vai ate o 5
frase[6:] # começa do 6 até o final
frase[9::3] # começa no 9 e vai ate o final pulando de 3 em 3
len(frase) #percorre toda a frase mostrando quantos caracteres existe
frase.count('o') #conta quantas vezes aparece a letra 'o'
frase.count('o',0,13) #conta quantas vezes aparece a letra 'o', fatiando do 0 ao 13
frase.find('deo') #mostra posição da palavra buscada começando da primeira letra
frase.rfind('deo') #mostra posição da palavra buscada começando da direita
frase.lfind('deo') #mostra posição da palavra buscada começando da esquerda
'curso' in frase #olha se existe a palavra dentro da frase

#transformação
frase.replace('procurar','susbstituir') #troca uma letra/frase por outra
frase.upper()# colocar a frase em maiusculo
frase.lower()# coloca a frase em minusculo
frase.capitalize()# transforma apenas a primeira letra da frase em maiusculo
frase.title()#
frase.strip()#remove os espaços do final e começo da frase que sao inutilizaveis
frase.rstrip()#remove os espaços do lado direito
frase.lstrip()#remove os espaçoes do lado esquerdo
frase.split()#divide as frases separando em listas
'-'.join(frase)#junta as frases separadas em listas e coloca o '-'nos espaçoes em branco

#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas letras minusculas
#quantas letras ao todo(sem considerar espacos)
#quantas letras tem o primeiro nome

nome_completo = str(input("Digite seu nome completo: "))


maiusculas = nome_completo.upper()
print(f"Seu nome em maiusculo: {maiusculas}")

minusculas = nome_completo.lower()
print(f"Seu nome em minusculo: {minusculas}")

transformar_lista = nome_completo.split()
primeiro_nome = transformar_lista[0].__len__()
print(f"Seu primeiro nome tem {primeiro_nome} letras")

letras_ao_todo = ''.join(transformar_lista).__len__()
print(f"Seu nome todo tem {letras_ao_todo} letras ao todo")'''

#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: digite um numero: 1834
#unidade: 4
#dezenas: 3
#centena:8
#milhar:1

'''numeros = input("Digite um numero de 0 a 9999: ")

primeiro_numero = numeros[0]
segundo_numero = numeros[1]
terceiro_numero = numeros[2]
quarto_numero = numeros[3]

print(f'Unidade: {quarto_numero}\ndezena: {terceiro_numero}\ncentena: {segundo_numero}\nmilhar: {primeiro_numero}')'''

#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo"

'''cidade = input("Digite o nome da sua cidade: ")

lista = cidade.lower().split()

if'santo' in lista[0]:
 print(f"Sua cidade começa com a palavra 'santo'")
else:
    print("Sua cidade nao começa com a palavra santo")'''

#crie um programa que leia o nome de uma pessoa e diga se eka tem "silva" no nome

'''nome_pessoa = input("Digite seu nome completo: ")

lista_nome = nome_pessoa.lower().split()

if 'silva' in lista_nome:
    print("Seu nome tem silva no nome ")
else:
    print("seu nome nao tem silva no nome")'''

#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "a".
#em que posição ela aparece a primeira vez
'''frase = input("Digite uma frase: ").strip()
lista = frase.split()
quantidade_letra = frase.count('a')
primeira_posicao = frase.lower().find('a')
ultima_posicao  = frase.lower().rfind('a')
print(f"a letra 'A' aparece {quantidade_letra}x na frase")
print(f"a primeira letra 'A' apareceu na posicao {primeira_posicao}")
print(f"a ultima letra 'A' apareceu na posicao {ultima_posicao}")'''



#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o ultimo nome separadamente

nome_todo = input("Digite seu nome completo: ").strip()
lista = nome_todo.split()

print(f"Seu primeiro nome é: {lista[0]}")
print(f"Seu ultimo nome é: {lista[-1]}")











