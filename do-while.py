# codigo para adivinhar um numero

# Inicializa a variável 'palpite' com o valor 0
palpite = 0

# Define o número correto a ser adivinhado como 9
numero = 9

# Inicia um loop infinito
while True:
    # Solicita ao usuário que informe o palpite
    print("qual o numero correto? ")

    # Lê o valor digitado pelo usuário e converte para inteiro
    palpite = int(input())

    # Verifica se o palpite está correto
    if palpite == numero:
        # Informa que o usuário acertou o número
        print("parabens voce acertou")

        # Encerra o loop, pois o número foi acertado
        break

    else:
        # Informa que o usuário errou
        print("voce errou")
