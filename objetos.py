class alumno():

    def __init__(self, nombre, dni, edad, notaMax, notaMin, prom):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.notaMax = notaMax
        self.notaMin = notaMin
        self.prom = prom

class profesor():

    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def mostrar_archivo(self):
        try:
            file = open(self.nombre_archivo,'r')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print("error:", str(e))
        else:
            file.close()

    def agregar_alumno(self, persona):
        try:
            file = open(self.nombre_archivo, 'a')
            texto_agregar = "{},{},{},{},{},{} \n".format(
                persona.nombre,
                persona.dni,
                persona.edad,
                persona.notaMax,
                persona.notaMin,
                persona.prom
            )
            file.write(texto_agregar)
        except Exception as e:
            print("error:", str(e))
        else:
            file.close()

    def agregar_profesor(self, persona):
        try:
            file = open(self.nombre_archivo, 'a')
            texto_agregar = "{},{},{} \n".format(
                persona.nombre,
                persona.dni,
                persona.edad
            )
            file.write(texto_agregar)
        except Exception as e:
            print("error:", str(e))
        else:
            file.close()

