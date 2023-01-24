op = input("Ingrese su digito: ")


valor = False

while valor == False:
    if op.isdigit() == True:
        valor = True
    else:
        valor = False