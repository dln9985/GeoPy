from lib import *

"""obj_rect = Rectangulo(10,5)
print(obj_rect)

print("Ancho: "+str(obj_rect.ancho))
print("Largo: "+str(obj_rect.largo))

obj_rect_2 = Rectangulo(25,15)
print(obj_rect_2)

print("Ancho: "+str(obj_rect_2.ancho))
print("Largo: "+str(obj_rect_2.largo))

obj_rect_3 = Rectangulo(0,0)
obj_rect_3.ancho = 75
obj_rect_3.largo = 55
print(obj_rect_3)

print("Ancho: "+str(obj_rect_3.ancho)+"[cm]")
print("Largo: "+str(obj_rect_3.largo)+"[cm]")

print("Perimetro: "+str(obj_rect_3.perimetro())+"[cm]")
print("Área: "+str(obj_rect_3.area())+"[cm^2]")"""
print("")

obj_poly_1 = Poligono(5,18)
print(obj_poly_1)

print(f"Número de lados: {obj_poly_1.Numlado } ")
print(f"Tamaño de los lados: {obj_poly_1.Sizelado } ")
print(obj_poly_1.Figure() )

print(obj_poly_1.Perimeter())

print("")

obj_poly_2 = PoligonoRegular(9,15,30)
print(obj_poly_2)
print(obj_poly_2.Figure())
print(obj_poly_2.Perimeter() )
print(obj_poly_2.AreaPoly() )

print("")