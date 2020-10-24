class Egresos:
    def __init__(self):
        self.egresosList = []
        self.idCounterEgresos = 0

    def registrarEgreso(self, monto):
        self.idCounterEgresos += 1
        idEgresos = self.idCounterEgresos
        egreso = monto
        self.egresosList.append(egreso)

    def mostrarEgresos(self):
        for egreso in self.egresosList:
            print(f"Id: {}. Monto: {str(egreso)}")

    def obtenerEgresos(self):
        return self.egresosList