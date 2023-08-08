
def par_impar(numero):
    multiplos_de_dois = numero % 2 == 0

    if multiplos_de_dois:
        return f'{numero} é par'
    else: 
        return f'{numero} é impar'

print(par_impar(2))
print(par_impar(3))