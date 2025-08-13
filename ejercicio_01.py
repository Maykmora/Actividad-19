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
        print(f"Nombre {self.nombre} --Precio: {self.precio} --Peso:{self.peso}")


galletas=[]
while True:
    option=input("Seleccione una opción del menú (1-7):")
    match option:
        case "1":
            print()
        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            print()
        case "7":
            print()
        case _:
            print()