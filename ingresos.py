class Ingresos:
    def __init__(self):
        self.ingresosList = []

    def registrarIngreso(self, monto):
        ingreso = monto
        self.ingresosList.append(ingreso)

    def mostrarIngresos(self):
        for ingreso in self.ingresosList:
            print(f"Monto: {str(ingreso)}")

    def obtenerIngresos(self):
        return self.ingresosList
