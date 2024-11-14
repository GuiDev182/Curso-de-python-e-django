lista_vendas = [1000,500,800,1500,2000,2300]

meta = 1200
percent_bonus = 0.1

venda = 1000

for venda in lista_vendas:
    if venda >= meta:
        bonus = percent_bonus * venda
    else:
        bonus = 0
    print(bonus)