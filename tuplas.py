'''lanche = ('hamburguer', 'suco', 'pizza')
print(sorted(lanche)) #ordena uma tupla/lista/dicionario
#Tuplas são imutaveis

for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}) na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(lanche[1])

#juntar tuplas

a = (2,5,4)
b = (1,3,6)
c = a + b
print(c.count(5)) #mostra qyuantas vezes aparece o valor 5 na tupla
print(c.index(8, 1)) # mostra em qual posição da tupla esta o valor 8, a partir do indice 1
from random import randint, Random'''
from manipulando_textos import lista

#crie um programa que tenha uma tupla totalmente preenchida com uma contagem
#de extensao, de zero ate vinte
#seu programa devera ler um numero pelo teclado(entre 0 e 20)
# e mostralo por extenso

'''contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numero = int(input("Digite um numero entre 0 e 20: \n R: "))

while numero > 0 or numero <= 20:
    if numero == 0:
        print(f' o numero digitado foi {contagem[0]}')
        break
    elif numero == 1:
        print(f' o numero digitado foi {contagem[1]}')
        break
    elif numero == 2:
        print(f' o numero digitado foi {contagem[2]}')
        break
    elif numero == 3:
        print(f' o numero digitado foi {contagem[3]}')
        break
    elif numero == 4:
        print(f' o numero digitado foi {contagem[4]}')
        break
    elif numero == 5:
        print(f' o numero digitado foi {contagem[5]}')
        break
    else:
        print("Numero invalido, tente novamente!")
        numero = int(input("Digite um numero entre 0 e 20: \n R: "))'''


#crie uma tupla preenchida com os 20 primeiros colocados da tebala do campeonato brasileiro
#na ordem de colocação. Depois mostre:
# A) apenas os  5 primeiros colocados.
# B) os ultimos 4 colocados da tabela.
# C) uma lista com os times em ordem alfabetica
# Em que posição na tabela está o time do cruzeiro

'''times = ('Atletico-mg','bahia','botafogo','Ceará','corinthias',
         'cruzeiro','flamengo','fluminense','fortaleza','gremio','internacional'
         ,'juventude','mirassol','palmeiras','red bull bragantino','santos','sao paulo','sport','vasco',
         'vitoria')

print(f"os primeiros colocados são {times[0:5]}")
print(f"os 4 ultimos colocados são {times[-4:]}")
print(f"lista dos times em ordem alfabetica {sorted(times)}")
print(f"o time do cruzeiro esta na {times.index('cruzeiro')} posição")'''

#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
#depois disso,mostre a listagem de numeros gerados e tambem indique o menor
#e o maios valor que estao na tupla
'''from random import Random

tupla = ()

while len(tupla) < 5:
    tupla += (Random().randint(1,10 ),)
    
print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')

#desenvolva um programa que leia  4 valores pelo teclado e guarde em um tupla. No final mostra:
#quantas vezes apareceu o valor 9 
#em que posição foi digitado o primeiro valor 3
# quais foram os numeros pares'''

'''tupla = ()
numeros_pares = ()
tupla = input("Digite um numero: ")

while len(tupla) < 4:
    tupla += (input("digite um numero: "))
if '9' in tupla:
    print(f"o numero 9 aparece {tupla.count('9')} vez na tupla")
if '3' in tupla:
    print(f"o numero 3 aparece na posição {tupla.index('3',0)} pela primeira vez ")

if int(tupla[0]) % 2 == 0:
    numeros_pares = tupla[0]
elif int(tupla[1]) % 2 == 0:
    numeros_pares = tupla[1]
elif int(tupla[2]) % 2 == 0:
    numeros_pares = tupla[2]
elif int(tupla[3]) % 2 == 0:
    numeros_pares = tupla[3]
print(f"os numeros pares são {numeros_pares}")'''


#crie um programa que tenha uma tupla unica com nomes de produtos e seus
#respectivos precos, na sequencia.
#no final, mostre uma listagem de precos, organizando os dados de forma tabular

'''produtos = ('Notebook', 1.000, 'Desktop', 2.500, 'monitor', 200.00, 'teclado', 50.00, 'mouse', 10.00)

print("LISTAGEM DE PREÇOS")
print('-'*35)
for itens in range(0,1):
    print(f"{produtos[0]}........................R${produtos[1]}")
    print(f"{produtos[2]}........................R${produtos[3]}")
    print(f"{produtos[4]}........................R${produtos[5]}")
    print(f"{produtos[6]}........................R${produtos[7]}")
    print(f"{produtos[8]}........................R${produtos[9]}")'''

#crie um programa que tenha uma tupla com varias palavras(nao suar acentos)
#depois disso, voce deve mostrar para cada letra, quais sao suas vogais

lista_palavras = ("me", "ajuda", "pelo", "amor", "de", "deus")
vogais = ('a', 'e', 'i', 'o', 'u')

for iten in range(0,6):
    if 'a' in lista_palavras[0]:
        print(f'a palavra {lista_palavras[0]} tem as vogais {vogais} ')






