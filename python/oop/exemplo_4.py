class Pizza:
    pedacos = 8

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos
    @abstractmethod
    @staticmethod
    def ingredientes(self):
        return 'Ingredientes'
        

class Calabresa(Pizza):
    @staticmethod
    def ingredientes(self):
        return ['Queijo, Molho']

class Atum(Pizza):
    @staticmethod
    def ingredientes(self):
        return ['Peixe Escorrido', 'Queijo', 'Salsa', 'Coentro'] 

class FrangoComCatupiri(Pizza):
    @staticmethod
    def ingredientes(self):
        return ['']

class Camarao(Pizza):
    pass

class DaCasa(Camarao, Atum):
    pass



    