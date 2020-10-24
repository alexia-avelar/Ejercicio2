from finanzas import Finanzas

while True:
    print("")
    print("Menú de programa de finanzas personales:")
    print("1- Iniciar cuenta a $0.00.")
    print("2- Registrar ingresos o egresos.")
    print("3- Registro de ingresos.")
    print("4- Registro de egresos.")
    print("5- Reporte de total de transacciones.")
    print("6- Reporte total de la cuenta.")
    print("0- Salir del programa.")
    option = input("Introduzca el número de la opción que desea realizar: ")
    print("")

    idCounter = 0

    if option == "0":
        break
    elif option == "1":
        idCounter += 1
        idCuenta = idCounter
        nombre = input("Ingrese su nombre: ")
        monto = 0.00
        finanzas = Finanzas(nombre, monto)
        print("Se ha inicializado su cuenta a $0.00")

    elif option == "2":
        option1 = input(
            "1. Registrar Ingreso. 2. Registrar Egreso. Ingrese una opción: "
        )
        if option1 == "1":
            monto = float(input("Ingrese el monto del ingreso: "))
            finanzas.registrarIngreso(monto)
        elif option1 == "2":
            monto = float(input("Ingrese el monto del egreso: "))
            finanzas.registrarEgreso(monto)

    elif option == "3":
        print("Registro de ingresos: ")
        finanzas.registroIngresos()

    elif option == "4":
        print("Registro de Egresos: ")
        finanzas.registroEgresos()

    elif option == "5":
        print("Registro de transacciones: ")
        print("Registro de ingresos: ")
        finanzas.registroIngresos()
        print("Registro de Egresos: ")
        finanzas.registroEgresos()

    elif option == "6":
        nombre = finanzas.obtenerNombre()
        montoFinal = finanzas.montoFinalCuenta()
        print(
            f"El monto actual de la cuenta {str(idCuenta)} ,perteneciente a {nombre} es: ${str(montoFinal)}"
        )
