class Articulo:
    def __init__(self, idArt, marca, nombre, precio=None, peso=None, dcto=None, inv=None):
        self.id = idArt
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.dcto = dcto
        self.inv = inv
        pass
    
    def __str__(self):
        return f"Id del producto: |{self.id}| Marca: |{self.marca}| Nombre: |{self.nombre}| Precio (p/pza): |{self.precio}| Peso: |{self.peso}| Descuento: |{self.dcto}| Inventario Disponible: |{self.inv}|"
    
    def setPrecio(self, price):
        self.precio = price
        pass