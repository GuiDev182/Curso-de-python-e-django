#condicoes if/else/elif
#if condicao/comparacao:
    # codigo a ser executado caso a condicao seja verdadeira
#else:
    # codigo a ser executado caso a condicao seja falsa

#sinais de comparacao

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

vendas = 1500
meta = 1300
meta2 = 2000
meta_empresa = 20000
vendas_empresa = 10000

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
        bonus = 0.1 * vendas
else:
        bonus = 0
print(f"bonus: {bonus}")

lista_produtos = ["airpod","ipad","iphone","macbook"]
produto_procurado = input("procure um produto: ")
produto_procurado_minuscula = produto_procurado.lower()

if produto_procurado_minuscula in lista_produtos:
    print("produto no estoque")
else:
    print("nao temos esse produto")
