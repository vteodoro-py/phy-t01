# #  OPERADORES DE COMPARAÇÃO
#
# a = 10 #atribuiçao
# a == 10  #comparaçao
#
#
# #Igualdae:
# print(10==2)
# print(2==2)
# print(2 == 2.0)
# print(2 == '2')
#
# # Diferença:
# print(10 != 2)
# print(2 != 2)
# print(1000 != 100*10)
# print(100 != int('100'))
#
# # Maior que:
# print(10 > 2)
# print(0 > 2)
# # print('100' > 10)  DA ERRO
# print('senha123' > '123')
#
# # Menor que:
# print(10 < 2)
# print(10 < 2 + 9)
# print('palavra pequena' < 'palavra grande')
#
# # Maior ou igual:
# print(10 >= 2)
# print(2 >= 2)
#
# #Menor ou igual
# print(10 <= 12)
# print(100 <= 12)
from operator import truediv

#OPERADORES LÓGICOS

#and:
# condicao_1 = 10 > 0
# condicao_2 = 2 == 2
# print(condicao_1 and condicao_2)
#
# autentic_user = True
# autentic_password = True
# libera_user = autentic_user and autentic_password
# print(libera_user)
#
# #or:
# dinheiro = False
# cartao = True
# pagamento = dinheiro or cartao
# print(pagamento)
#
# print(5 > 2 or 3 <=2)
#
# #not:
# print(not True)
# print(not False)
#
# caixa_cheia = True
# encher_caixa = not caixa_cheia
# print(encher_caixa)

# print(not 10 > 5 and 20 % 2 == 0 or 8 >= 4)

#CONIDICIONAIS

#Ex 1:
# codigo_produto = input('Informe o código do produto: ').upper()
# quantidade_minima = 1000
# quantidade_maxima = 2500
#
# if codigo_produto == 'LED20':
#     quantidade_estoque = (int(input(f'Informe a quantidade do produto {codigo_produto} em estoque: ')))
#     if quantidade_estoque < quantidade_minima:
#         print(f'Compre {quantidade_minima - quantidade_estoque} unidades do produto {codigo_produto}.')
#
#     elif quantidade_estoque > quantidade_maxima:
#         unidades_venda = quantidade_estoque - quantidade_maxima
#         print(f'Venda {unidades_venda} unidades do produto {codigo_produto}.')
#
#     else:
#         print(f'Não há necessidade de compra do produto {codigo_produto}.')
#
# else:
#     print(f'{codigo_produto} não existe em nosso sistema.')


#Ex 2:
# sol = True
# calor = True
#
# if sol and calor:
#     print('Bora para praia!')
# elif sol and not calor:
#     print('Bora para o parque!')
# elif not sol and calor:
#     print('Bora para a piscina!')
# elif not sol and not calor:
#     print('off')


# # Ex 3:
# ano = input('Insira um ano: ')
# if int(ano[-2:]) % 4 == 0:   #'[-2:] pega os dois ultimos caracteres, estudo de INDICES
#     print(f'O ano de {ano} é bissexto.')
# else:
#     print(f'O ano de {ano} não é bissexto.')


# Ex 4:
tempo_prova = float(input('Insira o tempo (em segundos) na prova de 100 metros livres: '))
if tempo_prova < 75:
    print('Classificatória Estaduais.')
elif 75 < tempo_prova <= 85:
    print('Repescagem, prova na próxima semana.')
else:
    print('Obrigado pela participação, infelizmente você não avança com esse tempo. Boa sorte na próxima.')



