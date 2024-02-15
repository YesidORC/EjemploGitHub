y={}
c=0


class Persona:
    def __init__(self):
        self.__nombre = "Juan"
        self.__altura = 0.0
        self.__edad = 0

    def getAltura (self):
        return self.__altura
    def getEdad (self):
        return self.__edad
    def SetEdad (self,e):
        self.__edad = e
    def getNombre(self):
        return self.__nombre
    def setNombre(self,n):
        self.__nombre = n
    def comer(self,comida):
        print (f"Esta comiendo {comida}")

    def dormir(self):
        pass


class Casco:
    def __init__(self):
        self.tam = 0
        self.ne = 0
        self.ub = ""

    def __str__(self) -> str:
        return f"Este es un casco de tamaño {self.tam}"
    def registrar(self,u):
        self.ub = u
        print(f"El casco quedó registrado en {self.ub}")

while True:
    x=Casco()
    x1=Casco()
    u = Persona()
    u.setNombre("Juanita")
    print(u.getNombre())
    x.ne=34
    y[c] = x
    c+=1
    print(str(c)+"hola")
    print(x2)
    y[0].registrar("cualquier lugar")
