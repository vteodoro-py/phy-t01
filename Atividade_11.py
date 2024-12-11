frutas = ['banana', 'maçã', 'pêra', 'manga', 'uva']
frutas.extend(['melancia', 'melão', 'abacaxi'])
del frutas[1]
frutas.sort()
print(frutas)
print(frutas.count('banana'))