def menu():
    print("1.Registrar galleta básica")
    print("2.Registrar galleta con chispas")
    print("3.Registrar galleta rellena")
    print("4.Listar galletas")
    print("5.Buscar por nombre")
    print("6.Eliminar por nombre")
    print("7.Salir ")

class Galletas:
    def __init__(self, nombre, precio, peso):
        self.nombre= nombre
        self.precio= precio
        self.peso=peso

    def mostrar_info(self):
        print("Información de la galleta:")
        print(f"Nombre:{self.nombre} --Precio: {self.precio} --Peso:{self.peso}")

class GalletasChispas(Galletas):
    def __init__(self, nombre,precio,peso,cantidad_chispas):
        super().__init__(self,nombre,precio,peso)
        self.cantidad_chispas= cantidad_chispas
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} --Precio:{self.precio} --Peso:{self.peso} --Cantidad de chispas:{self.cantidad_chispas}")


galletas=[]
while True:
    option=input("Seleccione una opción del menú (1-7):")
    match option:
        case "1":
            nombre = input("Nombre de la galleta básica: ")
            precio = float(input("Precio: "))
            peso = float(input("Peso: "))
            g = Galletas(nombre, precio, peso)
            galletas.append(g)
            print("Galleta básica registrada.")

        case "2":
            print()
        case "3":
            print()
        case "4":
            if galletas:
                for g in galletas:
                    g.mostrar_info()
            else:
                print("No hay galletas registradas.")
        case "5":
            print()
        case "6":
            print()
        case "7":
            print()
        case _:
            print()