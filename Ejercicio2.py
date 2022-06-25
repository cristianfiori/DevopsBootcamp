print("Bienvenidos a Restaurant Patagonico!!")

Total = float(input("Ingrese el total de la cuenta:\n $"))
Comensales = float(input("Cuantos son los comensales?\n "))
# Sugerencia de Propina del Restaurant
Propinas = Total * 15 /100
# Impuestos segun regulacion Afip
ImpuestosPais = Total * 21 /100

PrecioFinal = Total + Propinas + ImpuestosPais
DivisionComensales = PrecioFinal / Comensales
print("#########################################\n"
      "La propina sugerida es: $",round(Propinas, 2),"\n",
      "Los impuestos son el 21% : $",round(ImpuestosPais, 2),"\n",
      "Lo consumido en la mesa es: $",round(Total, 2),"\n",
      "El costo total de cada comensal es: $", round(DivisionComensales, 2),"\n",
      "El valor total a pagar es : $", round(PrecioFinal, 2),"\n",
      "#########################################")

print("Gracias por su visita! Los esperamos nuevamente")