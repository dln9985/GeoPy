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
            PricewDcto = self.precio   
            return PricewDcto
    
class Carrito():
    def __init__(self, idCart):
        self.idCart = idCart
        self.objarticulos = []
        pass
    
    def __str__(self):
        printCarrito = f"Codigo en serie del carrito: {self.idCart} \n"
        if len(self.objarticulos) >= 1:
            for i in range(0, len(self.objarticulos),1 ):
                printCarrito += f"Articulo: {self.objarticulos[i]} \n"
        else:
                printCarrito += f"Carrito Vacio " 
        return printCarrito
    
    def addArt(self, ObjArt):
        if type(ObjArt.inv) != type(None):    
            if ObjArt.inv >= 1:
                ObjArt.inv -= 1
                self.objarticulos.append( ObjArt )
            else:
                print("No hay inventario disponible")
        else:
            print("Inventario No definido")
        return 0
    
    def getTotal(self):
        Total = 0
        for i in range(0, len(self.objarticulos), 1 ):
            Total += self.objarticulos[i].getPriceDcto()
        
        return Total