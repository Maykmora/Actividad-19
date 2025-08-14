def menu():
    print("\n1.Registrar galleta básica")
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
        print("\nInformación de galletas basicas:")
        print(f"Nombre:{self.nombre} --Precio: {self.precio} --Peso:{self.peso}")

class GalletasChispas(Galletas):
    def __init__(self, nombre,precio,peso,cantidad_chispas):
        super().__init__(nombre,precio,peso)
        self.cantidad_chispas= cantidad_chispas
    def mostrar_info(self):
        print("\nInformación Galletas con chispas")
        print(f"Nombre: {self.nombre} --Precio:{self.precio} --Peso:{self.peso} --Cantidad de chispas:{self.cantidad_chispas}")

class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno=sabor_relleno
    def describir_relleno(self):
        print(f"Galleta con relleno sabor:{self.sabor_relleno}")

class GalletasRellena(Galletas,Relleno):
    def __init__(self,nombre, precio, peso, sabor_relleno):
        Galletas.__init__(self,nombre, precio, peso)
        Relleno.__init__(self,sabor_relleno)
    def mostrar_info(self):
        print("\nInformación Galletas Rellenas")
        print(f"Nombre:{self.nombre} -- Precio:{self.precio} --Peso:{self.peso} --Sabor:{self.sabor_relleno}")
galletas=[]
while True:
    menu()
    option=input("Seleccione una opción del menú (1-7):")
    match option:
        case "1":
            while True:
                nombre = input("Nombre de la galleta básica: ")
                if not nombre.strip():
                    print("No ingresaste ningún nombre, inténtelo de nuevo")
                else:
                    try:
                        precio = float(input("Precio: "))
                        if precio <= 0:
                            print("El precio debe ser mayor a 0. Inténtalo de nuevo.")
                            continue
                        peso = float(input("Peso: "))
                        if peso <= 0:
                            print("El peso debe ser mayor a 0. Inténtalo de nuevo.")
                            continue
                        g = Galletas(nombre, precio, peso)
                        galletas.append(g)
                        print("Galleta básica registrada.")
                        break
                    except ValueError:
                        print("Precio y peso deben ser números positivos, inténtelo de nuevo")

        case "2":
            while True:
                nombre = input("Nombre de la galleta con chispas: ")
                if not nombre.strip():
                    print("No ingresaste ningún nombre, inténtelo de nuevo")
                else:
                    try:
                        precio = float(input("Precio: "))
                        if precio <= 0:
                            print("El precio debe ser mayor a 0. Inténtalo de nuevo.")
                            continue
                        peso = float(input("Peso: "))
                        if peso <= 0:
                            print("El peso debe ser mayor a 0. Inténtalo de nuevo.")
                            continue

                        cantidad_chispas=int(input("Cantidad de chispas:"))
                        if cantidad_chispas<=0:
                            print("La cantidad de chispas debe ser mayor a 0. Inténtalo de nuevo")

                        g = GalletasChispas(nombre, precio, peso, cantidad_chispas)
                        galletas.append(g)
                        print("Galleta con chispas registrada.")
                        break
                    except ValueError:
                        print("Precio,peso y cantidad de chispas deben ser números positivos, inténtelo de nuevo")

        case "3":
            while True:
                nombre = input("Nombre de la galleta con relleno: ")
                if not nombre.strip():
                    print("No ingresaste ningún nombre, inténtelo de nuevo")
                else:
                    try:
                        precio = float(input("Precio: "))
                        if precio <= 0:
                            print("El precio debe ser mayor a 0. Inténtalo de nuevo.")
                            continue
                        peso = float(input("Peso: "))
                        if peso <= 0:
                            print("El peso debe ser mayor a 0. Inténtalo de nuevo.")
                            continue
                        sabor_relleno= input("Ingrese el tipo de relleno de la galleta:")
                        if not sabor_relleno.strip():
                            print("No ingresaste ningún relleno, inténtelo de nuevo.")
                            continue

                        g = GalletasRellena(nombre, precio, peso, sabor_relleno)
                        galletas.append(g)
                        print("Galleta rellena registrada.")
                        break
                    except ValueError:
                        print("Precio y peso deben ser números positivos, inténtelo de nuevo")

        case "4":
            if galletas:
                for g in galletas:
                    g.mostrar_info()
            else:
                print("No hay galletas registradas.")
        case "5":
            print("\n--Buscar galleta--")
            nombre_buscado = input("Ingrese el nombre de la galleta que desea buscar: ").strip()
            encontrados = []
            for g in galletas:
                if nombre_buscado.lower() in g.nombre.lower():
                    encontrados.append(g)

            if encontrados:
                for g in encontrados:
                    g.mostrar_info()
            else:
                print("No se encontró ni una galleta con ese nombre")
        case "6":
            print("\n--Eliminar galleta--")
            nombre_eliminar = input("Ingrese el nombre de la galleta que desea eliminar: ").strip()
            encontrados = []
            for galleta in galletas:
                if nombre_eliminar.lower() in galleta.nombre.lower():
                    encontrados.append(galleta)
            if encontrados:
                for galleta in encontrados:
                    galletas.remove(galleta)
                print("Galleta eliminada correctamente")
            else:
                print("No se encontró ninguna galleta con ese nombre.")
        case "7":
            print("Gracias por usar el programa")
            break
        case _:
            print("Opción invalida, inténtelo de nuevo")
