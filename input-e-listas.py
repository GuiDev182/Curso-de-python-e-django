email = 'guilherme_email@gmail.com'

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



