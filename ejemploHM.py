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
        self.__tam = 0
        self.__ne = 0
        self.__ub = ""

    def __str__(self):
        return f"Este es un casco de tamaño {self.__tam}"
    

    def setTam(self,t):
        self.__tam = t
    
    def setNe(self,n):
        self.__ne = n
        
    def setUb(self):
        self.__ub = u
        
    def getTam(self,t):
        return self.__tam
    
    def getNe(self):
        return self.__ne
        
    def getUb(self):
        return self.__ub
        
    def registrar(self,u):
        self.ub = u
        print(f"El casco quedó registrado en {self.__ub}")
        
    def 

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
