despesa = int(input('Informe a quantidade de despesas: '))
num_despesa = 0
total_gasto = 0


while despesa > 0:
    num_despesa = num_despesa + 1
    compra = float(input(f'Digite o valor da compra {num_despesa}: '))
    despesa = despesa - 1
    total_gasto = total_gasto + compra
print(f'Você gastou um total de R$ {total_gasto:.2f}'.replace('.' , ',') + '.')