precio = float(input("Precio del producto: "))

#Redondear a 2 decimales
precio = round(precio,2)
aux2 = precio

aux1 = int(aux2//100)
aux2 = aux2%100
print( aux1, "billete(s) de $ 100")

aux1 = int(aux2//50)
aux2 %= 50
print( aux1, "billete(s) de $ 50")

aux1 = int(aux2//20)
aux2 %= 20
print( aux1, "billete(s) de $ 20")

aux1 = int(aux2//10)
aux2 %= 10
print( aux1, "billete(s) de $ 10")

aux1 = int(aux2//0.50)
aux2 %= 0.50
print( aux1, "moneda(s) de $ 0.50")

aux1 = int(aux2//0.25)
aux2 %= 0.25
print( aux1, "moneda(s) de $ 0.25")

aux1 = int(aux2//0.10)
aux2 %= 0.10
print( aux1, "moneda(s) de $ 0.10")

aux1 = int(aux2//0.05)
aux2 %= 0.05
print( aux1, "moneda(s) de $ 0.05")

aux1 = int(aux2//0.01)
aux2 %= 0.01
print( aux1, "moneda(s) de $ 0.01")
