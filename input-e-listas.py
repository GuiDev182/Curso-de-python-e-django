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

valores_numericos = []
valores_digitados = enumerate(valores_numericos[-1])

valores_numericos.append(int(input("Digite um valor: ")))
menu = int(input("Deseja continuar a digitar: \n 1 - Sim \n 2 - Não"))

while menu != 2:
    valores_numericos.append(int(input("Digite um valor: ")))
    menu = int(input("Deseja continuar a digitar: \n 1 - Sim \n 2 - Não"))
    if valores_digitados in valores_numericos:
        print("esse valor já esta na lista")
        valores_numericos.pop()
print(f"os valores em ordem crescente é: {valores_numericos.sort()}")




