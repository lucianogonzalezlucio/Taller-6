class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def capacidad(self):
        return f"{self.capacidad} pasajeros"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas, capacidad):
        super(). __init__(marca,modelo,año)
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año}) ({self.num_puertas} puertas)"

    def capacidad(self):
        return f"{self.capacidad_pasajeros} pasajeros"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo, capacidad):
        super(). __init__(marca,modelo,año)
        self.tipo = tipo
        self.capacidad_pasajeros = capacidad

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año}) ({self.tipo})"

    def capacidad(self):
        return f"{self.capacidad_pasajeros} pasajeros"

class Camion(Vehiculo):
    def __init__(self,marca,modelo,año,carga_maxima,capacidad):
        super(). __init__(marca,modelo,año)
        self.carga_maxima = carga_maxima
        self.capacidad_pasajeros = capacidad

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año}) (Carga máxima: {self.carga_maxima} kg)"

    def capacidad(self):
        return f"{self.capacidad_pasajeros} pasajeros"

def imprimir_informe(vehiculos):

    while True:
        
        opcion = input("Ingrese el Vehiculo que desea ingresar (Auto, Moto, Camion) o 'salir' para terminar: ").lower()
        print("----------------")
        if opcion == 'salir':
            break
        elif opcion == 'auto':
            marca = input("Ingrese la marca del auto: ")
            modelo = input("Ingrese el modelo del auto: ")
            año = int(input("Ingrese el año del auto: "))
            num_puertas = int(input("Ingrese el número de puertas del auto: "))
            capacidad = int(input("Ingrese la capacidad del auto: "))
            vehiculo = Auto(marca, modelo, año, num_puertas, capacidad)
            vehiculos.append(vehiculo)
        elif opcion == 'moto':
            marca = input("Ingrese la marca de la moto: ")
            modelo = input("Ingrese el modelo de la moto: ")
            año = int(input("Ingrese el año de la moto: "))
            tipo = input("Ingrese el tipo de la moto: ")
            capacidad = int(input("Ingrese la capacidad de la moto: "))
            vehiculo = Moto(marca, modelo, año, tipo, capacidad)
            vehiculos.append(vehiculo)
        elif opcion == 'camion':
            marca = input("Ingrese la marca del camión: ")
            modelo = input("Ingrese el modelo del camión: ")
            año = int(input("Ingrese el año del camión: "))
            carga_maxima = float(input("Ingrese la carga máxima del camión (kg): "))
            capacidad = int(input("Ingrese la capacidad del camión: "))
            vehiculo = Camion(marca, modelo, año, carga_maxima, capacidad)
            vehiculos.append(vehiculo)
        else:
            print("Opción no válida. Por favor, ingrese 'auto', 'moto', 'camion' o 'salir'.")

    for vehiculo in vehiculos:
        print(vehiculo.descripcion())
        print(vehiculo.capacidad())
        print("--------------------")


if __name__ == "__main__":
    imprimir_informe([])



