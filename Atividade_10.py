from math import trunc
from operator import truediv

print('********** BANCO SENAI **************')
print()
opcao = input('''Bem vindo ao Menu. Escolha uma das opções:
 [ 1 ] - Depósito
 [ 2 ] - Saque 
 ['s'] - Sair
  ''').lower()
saldo = 0
while True:
    if  opcao != str(1)  and  opcao != str(2) and opcao != 's':
        opcao = input('Insira uma opção válida: ').lower()
        continue

    elif opcao == str(1):
        deposito = float(input('Insira o valor que deseja depositar: '))
        saldo = saldo + deposito
        opcao = input('O que deseja fazer agora? ').lower()
        continue

    elif opcao == str(2):
        if saldo == 0:
            opcao = input('Você não possui saldo suficiente para saque. Tente outra opção: ').lower()
            continue

        else:
            saque = float(input('Insira o valor que deseja sacar: '))
            if saldo - saque < 0:
                        opcao = input('Você não tem saldo suficiente para saque, tente outra opção ou outro valor de saque: ').lower()
            else:
                saldo = saldo - saque
                opcao = input('O que deseja fazer agora? ').lower()
                continue

    elif opcao == 's':
        print(f'Seu saldo final é de R${saldo:.2f}'.replace('.',',') + '. Obrigado por utilizar nossos serviços!')
        break

