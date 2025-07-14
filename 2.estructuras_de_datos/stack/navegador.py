from stack import Stack


class Navegador():
    def __init__(self):
        self.historial_atras = Stack()
        self.historial_adelante = Stack()
        self.pagina_actual = None

    def visitar_pagina(self, pagina):
        if self.pagina_actual is not None:
            self.historial_atras.push(self.pagina_actual)
        self.pagina_actual = pagina
        self.historial_adelante.clear()

    def regresar(self):
        if self.historial_atras.is_empty():
            print("No hay historial disponible")
            return
        self.historial_adelante.push(self.pagina_actual)
        self.pagina_actual = self.historial_atras.pop()

    def adelantar(self):
        if self.historial_adelante.is_empty():
            print("No hay historial disponible")
            return
        self.historial_atras.push(self.pagina_actual)
        self.pagina_actual = self.historial_adelante.pop()


if __name__ == "__main__":
    def menu():
        print()
        print("1. Visitar pagina")
        print("2. Regresar")
        print("3. Adelantar")
        print("4. Salir")

    navegador = Navegador()
    while (True):
        if navegador.pagina_actual is not None:
            print(f"\nPagina actual: {navegador.pagina_actual}\n")

        menu()
        opcion = int(input("\n\tOpcion: "))
        if opcion == 1:
            pagina = input("\n: ")
            navegador.visitar_pagina(pagina)
        if opcion == 2:
            navegador.regresar()
        if opcion == 3:
            navegador.adelantar()
        if opcion == 4:
            break
