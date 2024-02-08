#---Inicio HW---
def HW():
    print("Hello World")
#---Fin HW---

def printTicket(carrito):
    print(carrito)
    print(f"Carrito: {carrito.idCart}\nTotal: $ {carrito.getTotal()} mxn")
    print(f"Usted ahorro: $ {carrito.getTotalDcto()} mxn") 