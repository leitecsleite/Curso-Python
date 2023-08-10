#Métodos úteis dos dicionários em Python
#len -quantas chaves
#keys - iterável com as chaves
#values -iterável com os valores
#items -iterável com chaves e valores
#setdefault - adiciona valor se a chave não existe
#copy - retorna uma cópia rasa (shallow copy)
#get - obtém uma chave
#pop - apaga um item com chave especificada (del)
#popitem - Apaga o último item adicionado
#update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Leite'
}

#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
print()

for chave, valor in pessoa.items():
    print(chave, valor)

