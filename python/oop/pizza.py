class Pizza:
    pedacos = 8
    
    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Amo atum'
    

    def __init__(self, sabor):
        self.sabor = sabor 

    def pegar_pedaco(self):
        self.pedacos -= 1
    
class Queijo(Pizza):
    pass
class Frango(Pizza):
    pass

