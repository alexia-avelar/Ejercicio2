class Ingresos:
    def __init__(self):
        self.ingresosList = []
        self.idCounterIngresos = 0

    def registrarIngreso(self, monto):
        self.idCounterIngresos += 1
        idIngresos = self.idCounterIngresos
        ingreso = monto
        self.ingresosList.append(ingreso)

    def mostrarIngresos(self):
        for ingreso in self.ingresosList:
            print(f"Id: {str(idIngresos)}. Monto: {str(ingreso)}")

    def obtenerIngresos(self):
        return self.ingresosList
