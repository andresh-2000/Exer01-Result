def negocio():
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    nombre_cliente = input("nombre del cliente: ")
    terminar = input("Deseas terminar?: ")

    while terminar == "no":
        producto = producto + ", " + input("producto: ")
        costo = costo + float(input("costo ($0.00): "))
        nombre_cliente = nombre_cliente + ", " + input("nombre del cliente: ")
        terminar = input("¿Deseas terminar?: ")
    if terminar == "yes":
        print()
        print("la cuenta del día")
        print()
        print("productos:", producto)
        print("costo total ($0.00): $", costo)
        print("nombre de los clientes:", nombre_cliente)
    else:
        print()
        print("No me has dicho si quieres terminar. Debes poner yes o no")


negocio()
