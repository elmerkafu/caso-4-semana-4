from objetos import alumno, profesor, Archivo

print("BIENVENIDOS - AL - REGISTRO - DE - DOCENTES - Y - ALUMNOS")
numero = int(input(print("DOCENTE --> <1> || ALUMNO --> <0>")))

if numero == 1:

    print(" *************** DOCENTE *******************")

    nombre = input(print("INGRESE SU NOMBRE COMPLETO:::"))
    dni = input(print("INGRESE SU DNI :::"))
    edad = input(print("INGRESE SU EDAD :::"))

    persona = profesor(
        'DOCENTE: <{0}>'.format(nombre), 
        'DNI: <{0}>'.format(dni), 
        'EDAD: <{0}>'.format(edad))

    archivo = Archivo("docente.txt")
    archivo.agregar_profesor(persona)
    archivo.mostrar_archivo()

elif numero == 0:

    print(" *************** ALUMNO *******************")
    nombre = input(print("INGRESE SU NOMBRE COMPLETO:::"))
    dni = input(print("INGRESE SU DNI :::"))
    edad = input(print("INGRESE SU EDAD :::"))
    print(" *************** INGRESO DE NOTAS *******************")
    lista_notas = []
    n=0
    suma = 0
    i = 0
    while n < 4:
        n = n+1
        numero = int(input(print("INGRESE NOTA {0}".format(n))))
        lista_notas.append(numero)

    for elemento in lista_notas:
        suma += elemento
        i += 1

    prom = suma / i
    mayor = max(lista_notas)
    menor = min(lista_notas)
    
    persona = alumno(
        'ALUMNO: <{0}>'.format(nombre), 
        'DNI: <{0}>'.format(dni), 
        'EDAD: <{0}>'.format(edad),
        'MAX NOTA: <{0}>'.format(mayor), 
        'MIN NOTA: <{0}>'.format(menor),
        'PROMEDIO: <{0}>'.format(prom))

    archivo = Archivo("alumno.txt")
    archivo.agregar_alumno(persona)
    archivo.mostrar_archivo()

else:
    print("INGRESO UN NUMERO INCORRECTO")