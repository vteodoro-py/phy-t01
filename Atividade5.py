n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
m = 'Você foi '
if media < 7:
    print(m + 'reprovado.')
elif 7 <= media < 10:
    print(m + 'aprovado!')
elif media == 10:
    print(m + 'aprovado com distinção!')
else:
    print('As notas inseridas não são válidas no sistema.')

