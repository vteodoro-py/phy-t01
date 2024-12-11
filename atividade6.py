l1 = float(input('Insira o valor do primeiro lado do triângulo: '))
l2 = float(input('Insira o valor do segundo lado do triângulo: '))
l3 = float(input('Insira o valor do terceiro lado do triângulo: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    m1 = 'Os lados formam um triângulo e é um Triângulo '
    if l1 == l2 == l3:
        m2 = 'Equilátero'
    elif l1 == l2 or l2 == l3 or l1 == l3:
        m2 = ' Isóceles'
    elif l1 != l2 and l2 != l3 and l1 != l3:
        m2 = 'Escaleno'
    print(m1 + m2)

else:
    print('Os lados não formam um triângulo')

