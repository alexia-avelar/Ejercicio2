from ingresos import Ingresos
from egresos import Egresos

ingresos = Ingresos()
egresos = Egresos()


class Finanzas:
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def registrarIngreso(self, monto):
        ingresos.registrarIngreso(monto)

    def registrarEgreso(self, monto):
        egresos.registrarEgreso(monto)

    def registroIngresos(self):
        ingresos.mostrarIngresos()

    def registroEgresos(self):
        egresos.mostrarEgresos()

    def registrosTransacciones(self):
        ingresos.mostrarIngresos()
        egresos.mostrarEgresos()

    def montoFinalCuenta(self):
        ingresosLista = ingresos.obtenerIngresos()
        egresosLista = egresos.obtenerEgresos()
        totalIngresos = 0.00
        totalEgresos = 0.00

        for ingreso in ingresosLista:
            totalIngresos = totalIngresos + ingreso[1]

        for egreso in egresosLista:
            totalEgresos = totalEgresos + egreso[1]

        montoFinal = self.monto + totalIngresos - totalEgresos
        return montoFinal

    def obtenerNombre(self):
        return self.nombre
