import os,random
usuariocliente=[]
nombrecliente=[]
boletos=[]
cedula=[]
codigosC=[]
nacimiento=[]
telefono=[]
opciones=["1","2","3","4","5","6","7","8","9","0"]
"""userClienteR = open("Cliente.txt","r")
nombreClienteR = open("NombreCliente.txt","r")
compraR = open("Compra Boletos.txt","r")
cedulaR = open("ID.txt","r")
codigoCR = open("Codigos Compra.txt","r")
nacimientoR = open("Fechas.txt","r")
telefonoR=open("Telefono.txt","r")
for g in codigoCR.readline().split(","):
    if g != " ":
        codigosC.append(g)
for h in userClienteR.readline().split(","):
    if h != " ":
            usuariocliente.append(h)
for i in nombreClienteR.readline().split(","):
    if i != " ":
        nombrecliente.append(i)
for j in compraR.readline().split(","):
    if j != " ":
            boletos.append(j)
for k in cedulaR.readline().split(","):
    if k != " ":
        cedula.append(k)
for l in nacimientoR.readline().split(","):
    if l != " ":
            nacimiento.append(l)
for m in telefonoR.readline().split(","):
    if m != " ":
            telefono.append(m)


userClienteR.close()
nombreClienteR.close()
compraR.close()
cedulaR.close()
codigoCR.close()
nacimientoR.close()
telefonoR.close()"""

def informacionclientes():
    os.system("cls")
    print("La Cartelera Actual es: ")
    print("Usuuario |   Cedula    |                   Nombre                       |        Año de Nacimmiento      | Telefono")
    for x in range(len(cedula)):
        print(usuariocliente[x],"      ",cedula[x],"      ",nombrecliente[x],"         ",nacimiento[x],"         ",telefono[x]   )
    os.system("pause")
    menuClientes()        

def RegistroClientes():
    os.system("cls")
    
    print("Llena los siguientes Datos: ")
    os.system("cls")
    print("Ingrese La Pelicula: ")
    print("Llena los siguientes Datos: ")
    nombre1=input("Por Favor ingrese el primer nombre: ")
    nombre2=input("Por Favor ingrese el segundo nombre: ")
    if nombre2 == "":
        nombre2 = "_"
    apellido1=input("Por favor ingrese el Primer apellido: ")
    apellido2=input("Por favor ingrese el segundo apellido: ")
    resa=nombre1.lower()
    a=resa[0:3]
    resb=nombre2.lower()
    b=resb[0:3]
    resc=apellido1.lower()
    c=resc[0:2]
    resd=apellido2.lower()
    d=resd[0:2]  
    while True:
            #Creamos la condicion para validar datos 
            try:
            #Creamos una funcion que nos permita ingresar la variable dato
                id=int(input("Ingrese su numero de Cedula por favor: "))
                #Revisamos que la condicion se cumpla 
            except ValueError:
                #Enviamos un mensaje de advertencia
                print("Deben ser solo numeros ")
                #Continuamos si las condiciones se cumplen
                continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
            ced=str(id)
            if len(ced)<10:
                #Evaimos un mensaje de advertencia 
                print("Debe tener 10 Caracteres")
                #Se crea la condicion para salir del bucle 
            elif len(ced)>10:
                print("Debe tener solo 10 caracteres")
            else:
                #Salimos del bucle
                break
    cedula.append(id)
    while True:
            #Creamos la condicion para validar datos 
            try:
            #Creamos una funcion que nos permita ingresar la variable dato
                celular=int(input("Ingrese su numero de Celular por favor: "))
                #Revisamos que la condicion se cumpla 
            except ValueError:
                #Enviamos un mensaje de advertencia
                print("Deben ser solo numeros ")
                #Continuamos si las condiciones se cumplen
                continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
            cell=str(celular)
            if len(cell)<9:
                #Evaimos un mensaje de advertencia 
                print("Debe tener 9 Caracteres")
                #Se crea la condicion para salir del bucle 
            elif len(cell)>9:
                print("Debe tener solo 9 caracteres")
            else:
                #Salimos del bucle
                break
    telefono.append(celular)
    while True:
            #Creamos la condicion para validar datos 
            try:
            #Creamos una funcion que nos permita ingresar la variable dato
                fnacimiento=int(input("Ingrese su año de nacimiento: "))
                #Revisamos que la condicion se cumpla 
            except ValueError:
                #Enviamos un mensaje de advertencia
                print("Deben ser solo numeros ")
                #Continuamos si las condiciones se cumplen
                continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
            fn=str(fnacimiento)
            if len(fn)<4:
                #Evaimos un mensaje de advertencia 
                print("Debe tener 10 Caracteres")
                #Se crea la condicion para salir del bucle 
            elif len(fn)>4:
                print("Debe tener solo 10 caracteres")
            elif fnacimiento<1890 or fnacimiento>2007:
                print("No es posible")    
               
            else:
                #Salimos del bucle
                break
    nacimiento.append(fnacimiento)
    boletos.append("0")
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    res1=(fn,a,b,c,d,random.choice(opciones))
    nusuario="".join(res1)
    usuariocliente.append(nusuario)
    nombrecliente.append(nombreUsuario)
    print("Hola",nombre1,"tu nombre de usuario es",nusuario)
    os.system("pause")
    menuClientes() 



def menuClientes():
    os.system("cls")
    menuprincipal=int(input("Menu principal: \n1.- Ver Cartelera \n2.-Insertar Pelicula \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
    while menuprincipal!=0:
            if menuprincipal == 1:
                return informacionclientes()
            elif menuprincipal == 2:
                return RegistroClientes()               
        
            else: 
                print("Por favor ingresa una opcion correcta")
            menuprincipal=int(input("Menu principal: \n1.- Ver Cartelera \n2.-Insertar Pelicula \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
            break
    userClienteT = open("Cliente.txt","w")
    nombreClienteT = open("NombreCliente.txt","w")
    compraT = open("Compra Boletos.txt","w")
    cedulaT = open("ID.txt","w")
    codigoT = open("Codigos Compra.txt","w")
    nacimientoT = open("Fechas.txt","w")
    telefonoT=open("Telefono.txt","w")

    for x in range(len(cedula)):
            nombreClienteT.write(nombrecliente[x]+",")
            userClienteT.write(usuariocliente[x]+",")
            compraT.write(boletos[x]+",")
            cedulaT.write(str(cedula[x])+",")
            codigoT.write(codigosC[x]+",")
            nacimientoT.write(str(nacimiento[x])+",")
            telefonoT.write(str(telefono[x])+",")

    userClienteT.close()
    nombreClienteT.close()
    compraT.close()
    cedulaT.close()
    codigoT.close()
    nacimientoT.close()
    telefonoT.close()

menuClientes()