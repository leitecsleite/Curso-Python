lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir (lista):
    for item in lista: 
        print(item)
    print()

lista1 = sorted(lista, key=lambda item:item['nome'])
lista2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista1)
exibir(lista2)