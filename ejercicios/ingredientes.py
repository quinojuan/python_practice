huevos_1 = 150
harina_1000 = 1300
azucar_1000 = 760
maizena_1000 = 2400
aceite_1000 = 1300
dulce_de_leche_1000 = 3100
coco_1000 = 8310

# bandejitas = 
# papel_film =

cantidad_huevos = input("Ingrese la cantidad de huevos: ")
cantidad_harina = input("Ingrese en gramos la harina que utilizó: ")
cantidad_azucar = input("Ingrese en gramos la azucar que utilizó: ")
cantidad_maizena = input("Ingrese en gramos la maizena que utilizó: ")
cantidad_aceite = input("Ingrese en cm3 el aceite que utilizó: ")
cantidad_dulce = input("Ingrese en gramos el dulce de leche que utilizó: ")
cantidad_coco = input("Ingrese en gramos la cantidad de coco que utilizó: ")
cantidad_alfajores = input("¿Cuántos alfajores le salieron?: ")

costo_total = huevos_1 * int(cantidad_huevos) + (harina_1000 * int(cantidad_harina) / 1000) + (azucar_1000 * int(cantidad_azucar) / 1000) + (maizena_1000 * int(cantidad_maizena) / 1000) + (aceite_1000 * int(cantidad_aceite) / 1000) + (dulce_de_leche_1000 * int(cantidad_dulce) / 1000) + ( coco_1000 * int(cantidad_coco) / 1000)
costo_unitario = int(costo_total) // int(cantidad_alfajores)

precio_venta = 333
gcia = int(precio_venta) - int(costo_unitario)
cantidad_alfajores_vendidos = input("¿Cuantos alfajores vendiste?: ")

gcia_total = int(gcia) * int(cantidad_alfajores_vendidos)

print(f"Cada alfajor salió $ {costo_unitario}!")
print(f"En total ganaste: $ {gcia_total}")
