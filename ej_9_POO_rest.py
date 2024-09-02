class Restaurante():
    def __init__(self, nombre, comida):
        self.nombre = nombre
        self.comida = comida
    
    def describir_restaurante(self):
        print(f"El nombre del restaurante es {self.nombre}")
        print(f"El tipo de comida que sirve es {self.comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} ha sido abierto.")