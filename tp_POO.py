# """Ejercicio 1: Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo."""
# # class Rectángulo():
# #     def __init__(self, base, altura):
# #         self.base = base
# #         self.altura = altura

# #     def area_rect(self, base, altura):
# #         area = base*altura
# #         return area


# # base = int(input("Ingrese una medida de la base del rectángulo: "))
# # altura = int(input("Ingrese una medida de la altura del rectángulo: "))

# # rectangulito = Rectángulo(base, altura)

# # print(f"El área del rectángulo es de {rectangulito.area_rect(base, altura)} unidades cuadradas.")

# """Ejercicio 2: Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
# como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

# # class Mate():
# #     def __init__(self, cebadas_rest, estado, max_ceb):
# #         self.cebadas_rest = cebadas_rest
# #         self.estado = estado
# #         self.max_ceb = max_ceb

# #     def cebar(self):
# #         try:
# #             if self.estado == 1:
# #                 raise Exception("¡Cuidado! ¡Te quemaste!")
# #             self.estado = 1
# #         except Exception as e:
# #             print(e)
        

# #     def beber(self):
# #         try:
# #             if self.estado == 0:
# #                 raise Exception("¡El mate está vacío!")
# #             self.estado = 0
# #             self.cebadas_rest -= 1
# #             if self.cebadas_rest < 0:
# #                 self.cebadas_rest = 0
# #                 print("Advertencia: el mate está lavado.")
# #         except Exception as e:
# #             print(e)

        
# # leo_matioli = Mate(10, 0, 50)

# # leo_matioli.beber()

# # leo_matioli.cebar()

# # leo_matioli.cebar()

# # leo_matioli.beber()

# # leo_matioli.beber()

# """3) Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
# destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
# un corcho."""

# # class Corcho():
# #     def __init__(self, bodega):
# #         self.bodega = bodega

# # class Botella():
# #     def __init__(self, corcho):
# #         self.corcho = corcho

# # class Sacachorchos():
# #     def __init__(self):
# #         self.corcho = None

# #     def destapar(self, botella):
# #         try:
# #             if botella.corcho == None:
# #                 raise Exception("La botella ya está destapada.")
            
# #             if self.corcho != None:
# #                 raise Exception("El sacacorchos ya tiene un corcho. Se debe limpiar.")
            
# #             self.corcho = botella.corcho
# #             botella.corcho = None
# #         except Exception as e:
# #             print(e)
    
# #     def limpiar(self):
# #         try:
# #             if self.corcho is None:
# #                 raise Exception("No hay un corcho para limpiar.")
# #             self.corcho = None
# #         except Exception as e:
# #             print (e)


# # corcho = Corcho("Bodega Pada Lustro")
# # botella1 = Botella(corcho)
# # sacacorchos = Sacachorchos()

# # sacacorchos.limpiar()
# # sacacorchos.destapar(botella1)
# # sacacorchos.destapar(botella1)
# # sacacorchos.limpiar()
# # sacacorchos.limpiar()


# """Ejercicio 4: Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método. """

# # class Restaurante():
# #     def __init__(self, nombre, comida):
# #         self.nombre = nombre
# #         self.comida = comida
    
# #     def describir_restaurante(self):
# #         print(f"El nombre del restaurante es {self.nombre}")
# #         print(f"El tipo de comida que sirve es {self.comida}")

# #     def abrir_restaurante(self):
# #         print(f"El restaurante {self.nombre} ha sido abierto.")

# # class Heladeria(Restaurante):
# #     def __init__(self, nombre, comida, sabores):
# #         super().__init__(nombre, comida)
# #         self.sabores = sabores

# #     def mostrar_valores(self):
# #         print(f"El nombre del restaurante es {self.nombre}, y su tipo de comida es {self.comida}")
# #         print(self.sabores)

# # heladerilol = Heladeria("Sigmalados", "Helados", ["Chocolate", "Vainilla", "Banana Split", "Mocos"])

# # heladerilol.describir_restaurante()
# # heladerilol.abrir_restaurante()
# # heladerilol.mostrar_valores()


# """Ejercicio 5: Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada"""


# # class Personaje():
# #     def __init__(self, vida, posicion, velocidad):
# #         self.vida = vida
# #         self.posicion = posicion
# #         self.velocidad = velocidad

# #     def recibir_ataques(self, ataque):
# #         try:
# #             self.vida -= ataque
# #             if self.vida < 0:
# #                 self.vida = 0
# #                 raise Exception("El personaje ha muerto.")
# #         except Exception as e:
# #             print(e)
# #         print(f"¡Oh! ¡Eso ha dolido! Ahora la vida del personaje es de {self.vida}")

# #     def mover(self):
# #         direccion = input("Hacía donde se quiere mover (W, A, S, D): ")
# #         if direccion.lower() == "a":
# #             self.posicion[0] -= self.velocidad
# #             print(f"El personaje se ha movido hacia la izquierda a una velocidad de {self.velocidad}.\nAhora su posición es {self.posicion}")
        
# #         elif direccion.lower() == "d":
# #             self.posicion[0] += self.velocidad
# #             print(f"El personaje se ha movido hacia la derecha a una velocidad de {self.velocidad}.\nAhora su posición es {self.posicion}")

# #         elif direccion.lower() == "w":
# #             self.posicion[1] += self.velocidad
# #             print(f"El personaje se ha movido hacia arriba a una velocidad de {self.velocidad}.\nAhora su posición es {self.posicion}")

# #         elif direccion.lower() == "s":
# #             self.posicion[1] -= self.velocidad
# #             print(f"El personaje se ha movido hacia abajo a una velocidad de {self.velocidad}.\nAhora su posición es {self.posicion}")

# #         else:
# #             print("Su elección no ha sido una de las opciones.")


# # class Soldado(Personaje):
# #     def __init__(self, vida, posicion, velocidad, ataque):
# #         super().__init__(vida, posicion, velocidad)
# #         self.ataque = ataque

# #     def atacar(self, objetivo):
# #         objetivo.recibir_ataques(self.ataque)



# # class Campesino(Personaje):
# #     def __init__(self, vida, posicion, velocidad, cosecha):
# #         super().__init__(vida, posicion, velocidad)
# #         self.cosecha = cosecha
    
# #     def cosechar(self):
# #         return self.cosecha
    

# # personaje1 = Personaje(100, [50, 50], 5)

# # soldado1 = Soldado(500, [100, 100], 10, 40)

# # campesino1 = Campesino(50, [0, 0], 70, 69)

# # soldado1.atacar(personaje1)
# # soldado1.atacar(personaje1)
# # soldado1.atacar(personaje1)

# # print(f"La cantidad cosechada del campesino es de {campesino1.cosechar()}")


# # personaje1.mover()
# # soldado1.mover()
# # campesino1.mover()

# """Ejercicio 6: Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

# class Usuario():
#     def __init__(self, nombre, apellido, domicilio, DNI, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.domicilio = domicilio
#         self.DNI = DNI
#         self.edad = edad

#     def describir_usuario(self):
#         print(f"Los datos del usuario son nombre: {self.nombre}, apellido: {self.apellido}, domicilio: {self.domicilio}, DNI: {self.DNI} y edad: {self.edad}")

#     def saludar_usuario(self):
#         print(f"¡Hola! ¡Eres bienvenido/a, {self.nombre}!")

# # usuario1 = Usuario("Enrique", "González", "Los Sauces 160", 47608367, 17)
# # usuario2 = Usuario("Ana", "Giménez", "Los Arces 157", 48901723, 17)
# # usuario3 = Usuario("Kyrene", "Haro", "Los Arces 210", 47608333, 17)
# # usuario4 = Usuario("Agustín", "Romaniello", "General Arias Rengel 555", 48777420, 20)

# # usuario1.describir_usuario()
# # usuario1.saludar_usuario()

# # usuario2.describir_usuario()
# # usuario2.saludar_usuario()

# # usuario3.describir_usuario()
# # usuario3.saludar_usuario()

# # usuario4.describir_usuario()
# # usuario4.saludar_usuario()

# """Ejercicio 7: Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""

# # class Admin(Usuario):
# #     def __init__(self, nombre, apellido, domicilio, DNI, edad):
# #         super().__init__(nombre, apellido, domicilio, DNI, edad)
# #         self.privilegios = ["Puede postear en el foro", "Puede borrar un post", "Puede bannear un usuario", "Puede modificar las reglas", "Puede eliminar el servidor"]

# #     def mostrar_privilegios(self):
# #         print(f"Este administrador tiene los siguientes privilegios: {self.privilegios}")

# # admin1 = Admin("Horacio", "Juárez", "Caseros 234", 34764106, 42)

# # admin1.mostrar_privilegios()

# """Ejercicio 8: Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios."""

# class Privilegios():
#     def __init__(self):
#         self.privilegios = ["Puede postear en el foro", "Puede borrar un post", "Puede bannear un usuario", "Puede modificar las reglas", "Puede eliminar el servidor"]
    
#     def mostrar_privilegios(self):
#         print(f"Este administrador tiene los siguientes privilegios: {self.privilegios}")

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, domicilio, DNI, edad):
#         super().__init__(nombre, apellido, domicilio, DNI, edad)
#         self.privilegios = Privilegios()

# admin1 = Admin("Horacio", "Juárez", "Caseros 234", 34764106, 42)

# admin1.privilegios.mostrar_privilegios()

"""Ejercicio 9: Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante
del ejercicio 4, e impórtela al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus
métodos para asegurarse que la importación funcionó."""
# import ej_9_POO_rest

# ristorante = ej_9_POO_rest.Restaurante("Aquel Novillo", "Patamuslo")

# ristorante.abrir_restaurante()
# ristorante.describir_restaurante()

"""Ejercicio 10: (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
importación?"""
import ejercicio9_restyhel

heladeriaxD = ejercicio9_restyhel.Heladeria("Fineas y Pherb", "Heladitos", ["Frutilla", "Mango", "Cereza", "Pepsi Black"])

heladeriaxD.abrir_restaurante()
heladeriaxD.describir_restaurante()
heladeriaxD.mostrar_valores()