pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'portuguesa'
    },
    {
        'nome': 'Marco',
        'sabor': 'presunto'
    }
]

for pedido in pedidos:
    s = 'Nome: {}\nSabor: {}'
    print(s.format(pedido['nome'], pedido['sabor']))
