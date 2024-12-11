#AULA 7:

#Ex 1:
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1 #ou i += 1, é a mesma coisa
#
#Ex 2:
# somador = 0
# while somador < 100:
#     somador += int(input('Digite um número a ser somado: '))
#     print(somador)
#
#Ex 3:
# import time
# tempo = 3600
# while tempo > -1:
#     if tempo == 3600:
#         print('\r', end='1:00:00')
#     else:
#         print('\r', end=f'{tempo//3600}:{tempo//60}:{tempo%60}')
#     time.sleep(1)
#     tempo -=1

#Ex 4:
# while True:
#     email = input('E-mail: ')
#     if email[-4:] != '.com':
#         print('Falta o ".com" ')
#         continue
#     else:
#         print('Bem vindo!')
#         break


# Ex 5:
# acesso = 'vinicius_001'
# controle_acesso = False
# tentativas = 3
# while not controle_acesso:
#     chave_acesso = input('Informe sua credencial: ')
#     if tentativas > 0:
#         if chave_acesso == acesso:
#             controle_acesso = True
#             print('Bem vindo ao sistema.')
#         else:
#             tentativas -= 1
#
#     else:
#         print('Não Deu.')
#         break
#
# Ex 6:
palavra = input("Entre com a palavra: ").lower()
jogo = ["_" for letra in palavra]  # Cria uma lista com "_" para cada letra da palavra

print("Vamos Jogar Forca!")
print("\nPalavra Secreta:", " ".join(jogo))

chances = 6
letras_usadas = set()

while chances > 0:
    letra = input("Fale uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra!")
    else:
        letras_usadas.add(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    jogo[i] = letra
            print("".join(jogo))
        else:
            chances -= 1
            print(f"Essa letra não tem, sobraram {chances} chances.")

    if "_" not in jogo:  # Verifica se todas as letras foram descobertas
        print("Você acertou!")
        break

if "_" in jogo:
    print("Que pena, você perdeu!")
    print("A palavra era:", palavra)