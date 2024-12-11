contatos = {'vinicius': '1111-1111',
            'leonardo':'2222-2222',
            'joao': '3333-3333',
            'joana': '4444-4444'}
contatos.update({'fulano': '5555-5555'})
del contatos['joana']
contatos ['leonardo'] = '1234-5678'
print(contatos)
print(*contatos.keys())

