'''email = 'guilherme_email@gmail.com'

novo_email = email.replace('gmail','hotmail')

print(novo_email)


nome = 'guilherme santos'

print(nome.capitalize())
print(nome.title())

print(f'o nome é {nome.title()}')


 #imput de dados
 
input = input('digite seu nome: ')

 #lista

lista = [1,2,3,4]
 
print(lista[0])

lista = sum(lista)

print(lista)

#tmanhoo da lista

lista = [1,2,3,4]

print(len(lista))

#max e min

lista = [1,2,3,4]

print(max(lista))
print(min(lista))

#ver se um elemento esta na lista

lista = ['banana','maca','uva']

print('banana' in lista)

#adicionar um elemento na lista

lista = [1,2,3,4]

lista.append(5)

print(lista)

#remover um elemento da lista

lista = [1,2,3,4]

lista.remove(3) #remove o primeiro elemento encontrado
lista.pop(2) #remove o elemento da posição 2

print(lista)

#editar um elemento da lista

lista = [1,2,3,4]

lista[0] = 10

print(lista)

#contar quantas vezes um elemento aparece na lista

lista = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

print(lista.count(1))

#ordenar uma lista

lista = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

lista.sort() # ordena de forma crescente

lista.sort(reverse=True) # ordena de forma decrescente

print(lista)


#adicionar um elemento em uma posição especifica

lista = [1,2,3,4,5,6,7,8,9,10]
lista.insert(0,0)
print(lista)

#remover um elemento de uma posição especifica

lista = [1,2,3,4,5,6,7,8,9,10]
del lista[0]
lista.pop(0) ou lista.pop() #remove o ultimo elemento da lista ou da posição 0
lista.remove(1)

#criar lista a partit de um range

lista = list(range(0,10))

print(lista)

valores = list()
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')'''
from sqlalchemy.sql.util import expand_column_list_from_order_by

#faça uma programa que leia 5 valores numericos e guarde em uma lista.
#no final mostre qual foi o maior  e o menor valor digitado e as suas
#respectivas posições na lista

'''valores_numericos = []

for valores in range(0,5):
    valores_numericos.append(int(input("Digite um valor: ")))
for posicao, valor in enumerate(valores_numericos):
    print(f"na posição {posicao} encontrei o numero {valor}")

print(f"o menor valor foi {min(valores_numericos)}")
print(f"o maior valor foi {max(valores_numericos)}")'''

#crie um programa onde o usuario possa digitar varios valores numericos
# e cadastre-os e uma lista. Caso o numero já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
#digitados, em ordem crescente.

'''valores = []

while True:
    valor = int(input("Digite um valor: "))
    if valor not in valores:
        valores.append(valor)
    else:
        print("Valor duplicado! Não vou adicionar...")
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
valores.sort()
print(valores)'''

#crie um programa onde o usuario possa digitar 5 valores numericos e
#cadastre-os e uma lista, ja na posição correta de inserção(sem usar o sort())
#no final mostre a lista ordenada na tela

valores = []

for valor in range(0, 5):
    valor = int(input("Digite um numero: "))
    if valor > valores[0]:
        valores.append(valor)
    elif valor
print(valores)







