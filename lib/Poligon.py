# ------ Comienzo
class Poligono:
    def __init__(self, Numlado, Sizelado):
        self.Numlado = Numlado
        self.Sizelado = Sizelado
        pass
    
    def __str__(self):
        return f"Número de Lados: {self.Numlado} y Tamaño del lado: {self.Sizelado} "
    
    def Figure(self):
        match self.Numlado:
            case 3:
                return f"Tu poligono es un triángulo dado a que tiene {self.Numlado} lados"
            case 4:
                return f"Tu poligono es un cuadrado dado a que tiene {self.Numlado} lados"
            case 5:
                return f"Tu poligono es un pentágono dado a que tiene {self.Numlado} lados"
            case 6:
                return f"Tu poligono es un hexágono dado a que tiene {self.Numlado} lados"
            case 7:
                return f"Tu poligono es un heptágono dado a que tiene {self.Numlado} lados"
            case 8:
                return f"Tu poligono es un octágono dado a que tiene {self.Numlado} lados"
            case 9:
                return f"Tu poligono es un eneágono dado a que tiene {self.Numlado} lados"
            case _:
                return "No reconozco tu poligono :("
    
    def Perimeter(self):
        return self.Numlado * self.Sizelado 
            
# ------ Final
    
class PoligonoRegular( Poligono ):
    def __init__(self, Numlado, Sizelado, Apotema):
        super().__init__(Numlado, Sizelado)
        self.Apotema = Apotema
        pass
    
    def __str__(self):
        return f"Número de lados: {self.Numlado}, Tamaño de los lados: {self.Sizelado}, Apotema: {self.Apotema}"
    
    def AreaPoly(self):
        area = ((self.Apotema)*(super().Perimeter()))/2
        return area
    
    def revArea(self):
        if self.AreaPoly() >= 2000:
            return "Si"
        else:
            return "No"
    
    def Color( self,color ):
        self.color = color
        return f"El color es: {self.color}"
        
        