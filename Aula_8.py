# # minha_lista = []
# # print(minha_lista)
# #
# # lista = [10, 1.4, '01', True]
# # for i in lista:
# #     print(i)
# #
# # numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(numeros)
# # print(numeros[0])
# # print(numeros[::-1])
# #
# # numeros_2 = [10, 11, 12, 13, 14]
# # todos_os_numeros = numeros + numeros_2
# # print(todos_os_numeros)
# #
# # lista = list(range(500))
# # print(lista)
# #
# # palavra = 'paralelepipedo'
# # soletrando = list(palavra)
# # print(soletrando)
#
#  #Métodos para inserçao de elementos:
# frutas = ['laranja', 'uva']
# nova_fruta = 'melancia'
# frutas.append(nova_fruta)
# print(frutas)
# frutas.extend(['banana', 'maçã'])
# print(frutas)
# frutas.insert(0, 'pêra')
# print(frutas)
# frutas[2] = 'abacaxi'
# print(frutas)
#
# #Remover item da lista:
#
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
#
# frutas.remove('melancia')
# print(frutas)
#
# del frutas [2]
# print(frutas)
#
# frutas.sort()
# # print(frutas)
#
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))
#
#
# # Tuplas:
# minha_tupla = (1, 2, 3, 4, 5)
# print(minha_tupla)
# print(type(minha_tupla))
# print(len(minha_tupla))
# for i in minha_tupla:
#     print(i)

lista_alunos = ['joao', "maria", 'ana', 'davi']
notas_alunos =[5, 7, 6, 10]

for item in enumerate(lista_alunos):
    print(item)

for posicao, nome in enumerate(lista_alunos):
    if nome == 'joao':
        notas_alunos[posicao] = 7.5

print(notas_alunos)

# Dicionários
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario['a'])
dicionario ['d'] = 4
print(dicionario)
dicionario ['b'] = 5
print(dicionario)
dicionario.update({'e': 6, 'f': 7, 'g': 8})
print(dicionario)
print(meu_dicionario.items())
print(meu_dicionario.keys())
print(meu_dicionario.values())
for chave, valor in meu_dicionario.items():
    print(chave + ' ---- ' + str(valor))

print(sum(meu_dicionario.values())




