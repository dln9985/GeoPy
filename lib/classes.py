class Articulo:
    def __init__(self, idArt, marca, nombre, precio=None, peso=None, dcto=None, inv=None):
        self.idArt = idArt
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.dcto = dcto
        self.inv = inv
        pass
    
    def __str__(self):
        return f"Id del producto: |{self.idArt}| Marca: |{self.marca}| Nombre: |{self.nombre}| Precio (p/pza): |{self.precio}| Peso en gr: |{self.peso}| Descuento: |{self.dcto}| Inventario Disponible: |{self.inv}|"
    
    def setPrecio(self, price):
        self.precio = price
        return 0
    
    def setPeso(self, peso):
        self.peso = peso
        return 0
    
    def setDcto(self, dcto):
        self.dcto = dcto
        return 0
    
    def setInv(self, inv):
        self.inv = inv
        return 0
    
    def getPriceDcto(self):
        if self.dcto != None:
            PricewDcto = self.precio - (self.precio * (self.dcto/100))
        else:    
            return PricewDcto
    
class Carrito():
    def __init__(self, idCart):
        self.idCart = idCart
        self.articulos = []
        pass
    
    def __str__(self):
        printCarrito = f"Codigo en serie del carrito: {self.idCart} \n"
        if len(self.articulos) >= 1:
            for i in range(0, len(self.articulos),1 ):
                printCarrito += f"Articulo: {self.articulos[i]} \n"
        else:
                printCarrito += f"Carrito Vacio " 
        return printCarrito
    
    def addArt(self, idArt):
        self.articulos.append( idArt )
        return 0