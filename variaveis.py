# numeros inteiros
numeros_inteiros = [1, 2, 3, 4, 5]

# numeros reais
numeros_reais = [1.5, 2.7, 3.2, 4.9, 5.6]

# strings
strings = ['Python', 'is', 'fun']

faturamento =1000
custo = 700
lucro = faturamento - custo

print(f'Lucro: R$ {lucro:.2f}') # Formatação do número com duas casas decimais

email_cliente = 'cliente@example.com'

email_cliente = email_cliente.upper() # Convertendo o email para minúsculas
email_cliente = email_cliente.lower() # Convertendo o email para maiúsculas

# .find() retorna a posição do primeiro caractere da string que corresponde ao padrão
print(email_cliente.find('@'))

#tamanho do texto
tamanho_email = len(email_cliente)
print(f'Tamanho do email: {tamanho_email}')

#pegando um caractere específico
primeiro_caractere = email_cliente[0]
print(f'Primeiro caractere do email: {primeiro_caractere}')

#pegando caracteres de uma posição específica até outra
parte_email = email_cliente[5:12]
print(f'Parte do email: {parte_email}')