#fatiamento
#c u r s o e m v i d e o
#1 2 3 4 5 6 7 8 9 10 11 12
from os.path import split

frase = 'curso em video'
frase[9:21] #começa do numero 9 ao 21
frase[9:21:2] #começa do numero 9 ao 21, pulando de dois em dois
frase[:5] #começa do inicio e vai ate o 5
frase[6:] # começa do 6 até o final
frase[9::3] # começa no 9 e vai ate o final pulando de 3 em 3
len(frase) #percorre toda a frase mostrando quantos caracteres existe
frase.count('o') #conta quantas vezes aparece a letra 'o'
frase.count('o',0,13) #conta quantas vezes aparece a letra 'o', fatiando do 0 ao 13
frase.find('deo') #quantas vezes encontrou 'deo' dentro da frase
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