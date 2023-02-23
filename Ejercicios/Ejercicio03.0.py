precio = float(input("Precio del producto: "))

#Redondear a 2 decimales
precio = round(precio,2)
aux2 = precio

#auxiliar 1 es la parte entera de dividir el precio (aux2) entre 100
aux1 = int(aux2//100)
#auxiliar 2 es el precio (aux2) menos la cantidad de billetes de 100
aux2 -= aux1*100
print( aux1, "billete(s) de $ 100")

#auxiliar 1 es la parte entera de dividir el el restante (aux2) entre 50
aux1 = int(aux2//50)
#auxiliar 2 es el restante (aux2) menos la cantidad de billetes de 50
aux2 -= aux1*50
print( aux1, "billete(s) de $ 50")

aux1 = int(aux2//20)
aux2 -= aux1*20
print( aux1, "billete(s) de $ 20")

aux1 = int(aux2//10)
aux2 -= aux1*10
print( aux1, "billete(s) de $ 10")

aux1 = int(aux2//.50)
aux2 -= aux1*.50
print( aux1, "moneda(s) de $ 0.50")

aux1 = int(aux2//.25)
aux2 -= aux1*.25
print( aux1, "moneda(s) de $ 0.25")

aux1 = int(aux2//.10)
aux2 -= aux1*.10
print( aux1, "moneda(s) de $ 0.10")

aux1 = int(aux2//.05)
aux2 -= aux1*0.05
print( aux1, "moneda(s) de $ 0.05")

aux1 = int(aux2//0.01)
aux2 -= aux1*0.01
print( aux1, "moneda(s) de $ 0.01")
