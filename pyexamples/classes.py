
class Pedido(object):
    def __init__(self, nome, endereco, observacoes=None):
        self.nome = nome
        self.endereco = endereco
        self.observacoes = observacoes
