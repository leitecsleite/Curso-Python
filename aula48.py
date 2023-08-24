import copy

from data import products


##new_products = copy.deepcopy(products)

new_products = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

products_order_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['nome']
)

products_order_reverse_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['nome'],
    reverse=True
)

print(*products_order_name, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_order_reverse_name, sep='\n')
