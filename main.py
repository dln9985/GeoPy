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

print(f"1) Número de lados: {obj_poly_1.Numlado } ")
print(f"2) Tamaño de los lados: {obj_poly_1.Sizelado } ")
print(obj_poly_1.Figure() )

print(obj_poly_1.Perimeter())

print("")

obj_poly_2 = PoligonoRegular(9,15,30)
print(obj_poly_2)
print(obj_poly_2.Figure())
print(f"El perimetro de tu poligono es de {obj_poly_2.Perimeter()} centimetros [cm]")

print(f"El área de tu poligono es de {obj_poly_2.AreaPoly()} centimetros cuadrados [cm^2]")
print(f"¿El área es mayor a 2000? Respuesta: {obj_poly_2.revArea()} ")

obj_poly_2.Color("Rojo Vino")
print(obj_poly_2.color)

num1="10"
num2=0

try:
    div = num1 / num2
#except ZeroDivisionError:
    #print("¿¡¿¡¿Acaso quieres que colapse el universo al dividir entre 0?!?!?")
#except TypeError:
    #print("No puedes dividir Strings entre Números")"""
except Exception as e:
    print(f"Error desconocido: {e} ")
    
print("")