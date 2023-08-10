pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Leite'
}

#pessoa.update(nome='novo valor', idade=30)

tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]

pessoa.update(tupla)

print(pessoa)

