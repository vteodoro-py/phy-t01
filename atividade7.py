s = float(input('Insira o salário do funcionário: '))

if s <= 2000:
    sl = s
elif s <= 3500:
    sl = s - (10/100 * s)
elif s <= 5000:
    sl = s - (15/100 * s)
elif s > 5000:
    sl = s - (20/100 * s)

print(f'O salário líquido do funcionário é de R${sl:.2f}'.replace('.' , ',') + '.')
