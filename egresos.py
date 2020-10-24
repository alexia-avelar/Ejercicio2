class Egresos:
    def __init__(self):
        self.egresosList = []

    def registrarEgreso(self, monto):
        egreso = monto
        self.egresosList.append(egreso)

    def mostrarEgresos(self):
        for egreso in self.egresosList:
            print(f"Monto: {str(egreso)}")

    def obtenerEgresos(self):
        return self.egresosList