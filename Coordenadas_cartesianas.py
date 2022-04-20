


x = float(input("Escriba la posición horizontal de la esquina inferior izquierda del rectángulo: "))
y = float(input("Escriba la posición vertical de la esquina inferior izquierda del rectángulo: "))
w = float(input("Escriba el ancho del rectángulo: "))
h = float(input("Escriba la altura del rectángulo: "))

px = float(input("Escriba  la posición horizontal del punto: "))
py = float(input("Escriba la posición vertical del punto: "))

ver_x= ((x <= px) and (px <=(x+w)))
ver_y= ((y <= py) and (py <=(y+h)))

print(ver_x and ver_y)
print((x <= px) and (px <=(x+w))) and ((y <= py) and (py <=(y+h)))