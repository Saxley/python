actual=0 
comparacion= 0
estado = False
textos = [
    "Bienvenido, calculemos las diferencias de años",
    "Introduce el año actual\n",
    "Introduce el año deseado\n"
    ]
print(textos[0])
while estado != True:
    if actual == 0 or comparacion == 0:
        try:
            if actual == 0:
                actual=int(input(textos[1]))
            if comparacion == 0:
                comparacion=int(input(textos[2]))
        except ValueError:
            print("Porfavor introduce el año con numeros")
    else:
        if actual != comparacion:
            estado=True
        else:
            print("Introduciste el mismo año porfavor introduce años diferentes.")
            comparacion = 0
diferencia = actual - comparacion
if diferencia > actual:
    if diferencia == 1:
        print(f"Falta 1 año para llegar al año {comparacion}")
    else:
        print(f"Faltan {diferencia}años para llegar al año que has introducido")
else:
    if diferencia == -1:
        print(f"Ha transcurrido 1 año desde el año {actual}")
    else:
        print(f"Desde el año {comparacion} han pasado {diferencia} año")    
