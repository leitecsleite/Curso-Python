a, b = 1 , 2

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6, 
}

pessoas_completa = {**pessoa,**dados_pessoa}


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items(): 
        print(chave, valor)


#mostro_argumentos_nomeados(nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)
#kwargs - keyword arguments(argumentos nomeados)

#(a1, a2), (b1, b2) = pessoa.items() 

#print(b2)

