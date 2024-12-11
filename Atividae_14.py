produtos = {'celular': [3000,200], 'televisao': [5000, 150]}

while True:
    print()
    acao = (input('''--------------- MENU ---------------
    [ 1 ] Cadastro de novo produto
    [ 2 ] Consulta de informações de produto
    [ 3 ] Alterar preço de produto
    [ 4 ] Remover um produto do cadastro
    [ S ] Sair
        
    Escolha uma opção: '''))


    if acao == '1':
        prod = input('Informe o nome do novo produto: ')
        preco = float(input('Informe o preço do produto: R$ '))
        estoque = int(input('Informe a quantidade em estoque deste produto: '))
        produtos.update({prod:[preco, estoque]})
        continue

    elif acao == '2':
        prod = input('Informe o produto que deseja consultar as informações: ')
        print(produtos[prod])
        continue

    elif acao == '3':
        prod = input('Escolha o produto que deseja alterar o valor: ')
        preco = float(input('Informe o novo preço do produto: '))
        produtos[prod][0] = preco
        continue


    elif acao == '4':
        prod = input('Informe o produto que deseja remover do cadastro: ')
        del produtos[prod]
        continue

    elif acao == 's':
        print(f'Obrigado. Os seus produtos atuais em estoque são: {produtos}')
        break

    else:
        print('Informe uma opção válida.')
        continue

#
# def menu():
#     print("\n--- Menu ---")
#     print("1. Cadastrar produto")
#     print("2. Consultar produto")
#     print("3. Alterar preço")
#     print("4. Remover produto")
#     print("5. Listar produtos")
#     print("6. Sair")
#     return input("Escolha uma opção: ")
#
# def cadastrar(produtos):
#     nome = input("Nome do produto: ").strip()
#     if nome in produtos:
#         print("Produto já cadastrado.")
#         return
#     try:
#         preco = float(input("Preço: R$ "))
#         if preco < 0:
#             print("O preço deve ser positivo.")
#             return
#         quantidade = int(input("Quantidade: "))
#         if quantidade < 0:
#             print("A quantidade deve ser positiva.")
#             return
#         produtos[nome] = {"preço": preco, "quantidade": quantidade}
#         print("Produto cadastrado!")
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")
#
# def consultar(produtos):
#     nome = input("Nome do produto: ").strip()
#     if nome in produtos:
#         print(f"Preço: R${produtos[nome]['preço']:.2f}, Quantidade: {produtos[nome]['quantidade']}")
#     else:
#         print("Produto não encontrado.")
#
# def alterar_preco(produtos):
#     nome = input("Nome do produto: ").strip()
#     if nome in produtos:
#         try:
#             novo_preco = float(input("Novo preço: R$ "))
#             if novo_preco < 0:
#                 print("O preço deve ser positivo.")
#                 return
#             produtos[nome]["preço"] = novo_preco
#             print("Preço alterado!")
#         except ValueError:
#             print("Entrada inválida. Tente novamente.")
#     else:
#         print("Produto não encontrado.")
#
# def remover(produtos):
#     nome = input("Nome do produto: ").strip()
#     if produtos.pop(nome, None):
#         print("Produto removido!")
#     else:
#         print("Produto não encontrado.")
#
# def listar(produtos):
#     if produtos:
#         for nome, dados in produtos.items():
#             print(f"{nome}: R${dados['preço']:.2f}, {dados['quantidade']} unidades")
#     else:
#         print("Nenhum produto cadastrado.")
#
# def main():
#     produtos = {}
#     while True:
#         opcao = menu()
#         if opcao == "1":
#             cadastrar(produtos)
#         elif opcao == "2":
#             consultar(produtos)
#         elif opcao == "3":
#             alterar_preco(produtos)
#         elif opcao == "4":
#             remover(produtos)
#         elif opcao == "5":
#             listar(produtos)
#         elif opcao == "6":
#             print("Saindo do sistema. Até mais!")
#             break
#         else:
#             print("Opção inválida.")
#
# if __name__ == "__main__":
#     main()
#
#



