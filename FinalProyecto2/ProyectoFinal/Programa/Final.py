"""
El siguiente programa, pretende simular el sistema de compras de un cine 
con su base de datos

Autores:
Jose Sanmartin, Alexander Mejia 
Verisión:
VER.0.1
"""
#importamos la billioteca necesaria 
import os,random
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
codigo=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
nombre=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
horario=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
boletosDis=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
usuario=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
nombreEmpleado=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
usuariocliente=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
nombrecliente=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
boletos=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
cedula=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
codigosC=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
nacimiento=[]
#Creamos un diccionario necesario para almacenar los datos que necesitemos 
telefono=[]
#Creamos un diccionario necesario para almacenar una serie de numero apra despues aplicar random
opciones=["1","2","3","4","5","6","7","8","9","0"]
#Abris el archivo para su lectura de datos 
codigoR = open("Codigo.txt","r")
#Abris el archivo para su lectura de datos 
nombreR = open("Nombre.txt","r")
#Abris el archivo para su lectura de datos 
horarioR = open("Horario.txt","r")
#Abris el archivo para su lectura de datos 
boletosDisR=open("BoletosDisponibles.txt","r")
#Abris el archivo para su lectura de datos 
usuarioR =   open("Usuario.txt","r")
#Abris el archivo para su lectura de datos 
nombreEmR =   open("Nombre Empleado.txt","r")
#Abris el archivo para su lectura de datos 
userClienteR = open("Cliente.txt","r")
#Abris el archivo para su lectura de datos 
nombreClienteR = open("NombreCliente.txt","r")
#Abris el archivo para su lectura de datos 
compraR = open("Compra Boletos.txt","r")
#Abris el archivo para su lectura de datos 
cedulaR = open("ID.txt","r")
#Abris el archivo para su lectura de datos 
codigoCR = open("Codigos Compra.txt","r")
#Abris el archivo para su lectura de datos 
nacimientoR = open("Fechas.txt","r")
#Abris el archivo para su lectura de datos 
telefonoR=open("Telefono.txt","r")
#Leemos el codigo ingresado 
for a in codigoR.readline().split(","):
    if a != " ":
        codigo.append(a)
for b in nombreR.readline().split(","):
    if b != " ":
        nombre.append(b)
for c in horarioR.readline().split(","):
    if c != " ":
        horario.append(c)
for x in boletosDisR.readline().split(","):
    if x != " ":
        boletosDis.append(x)
for e in usuarioR.readline().split(","):
    if e != " ":
        usuario.append(e)
for f in nombreEmR.readline().split(","):
    if f != " ":
        nombreEmpleado.append(f)
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
telefonoR.close()
codigoR.close()
nombreR.close()
horarioR.close()
boletosDisR.close()
usuarioR.close()
nombreEmR.close()
#Seccion Empleados 
def consultarEmpleados():
    
    os.system("cls")
    print("La Cartelera Actual es: ")
    print("|   Usuario    |                   Nombre                       |")
    for x in range(len(usuario)):
        print("    ",usuario[x],"      ",nombreEmpleado[x])
    os.system("pause")
    
           

def agregarEmpleado():
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
    a=resa[0:1]
    resb=nombre2.lower()
    b=resb[0:1]
    resc=apellido1.lower()
    c=resc[0:2]
    resd=apellido2.lower()
    d=resd[0:2]
    res=(a,b,c,d)
    nusuario="".join(res)
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    res1=(a,b,c,d,random.choice(opciones))
    nusuario1="".join(res1)
    usuario.append(nusuario1)
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    nombreEmpleado.append(nombreUsuario)
  
        
    os.system("pause")
    menuEmpleado()

def eliminarEmpleado():
    os.system("cls")
    print("Eliminando: ")
    cod=input("Ingresa el codigo usuario eliminar: ")
    for i in range(len(usuario)-1,-1,-1):
        if usuario[i]== cod:
            usuario.pop(i)
            nombreEmpleado.pop(i)
            print("Eliminado con exito")
    os.system("pause")
    menuEmpleado()
    
def buscarEmpleado():
    nombre=input("Ingrese el codigo: ")
    for x in range(len(nombreEmpleado)):
        if nombreEmpleado[x]==nombre:
            print("El usuario del emepleado es : ",usuario[x])
            
    os.system("pause")    
    menuEmpleado()

def menuEmpleado():
    os.system("cls")
    menuprincipal=int(input("Menu principal: \n1.- Ver Empleados \n2.-Agregar Empleado \n3.-Eliminar Pelicula \n4.-Buscar Empleado \n5.-Lista Clientes \n0.-Salir \nOpcion: "))
    while menuprincipal!=0:
            if menuprincipal == 1:
                return consultarEmpleados()
            elif menuprincipal == 2:
                return agregarEmpleado()                
            elif menuprincipal == 3:
                return eliminarEmpleado()
            elif menuprincipal== 4:
                return buscarEmpleado()
            elif menuprincipal==5:
                return informacionclientes()     
            else: 
                print("Por favor ingresa una opcion correcta")
            menuprincipal=int(input("Menu principal: \n1.- Ver Cartelera \n2.-Insertar Pelicula \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
            break
    usuarioT =  open("Usuario.txt","w")
    nombreET =  open("Nombre Empleado.txt","w")


    for x in range(len(usuario)):
            usuarioT.write(usuario[x]+",")
            nombreET.write(str(nombreEmpleado[x])+",")
            

    usuarioT.close()
    nombreET.close()

def informacionclientes():
    os.system("cls")
    print("La lista de CLientes: ")
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
    cedula.append(ced)
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
    telefono.append(cell)
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
    nacimiento.append(fn)
    
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    res1=(fn,a,b,c,d,random.choice(opciones))
    nusuario="".join(res1)
    usuariocliente.append(nusuario)
    nombrecliente.append(nombreUsuario)
    print("Hola",nombre1,"tu nombre de usuario es",nusuario)
    os.system("pause")
    menuClientes() 

def consultarCartelera():
    os.system("cls")
    print("La Cartelera Actual es: ")
    print("|   Codigo    |                   Nombre                       |         Horario       |")
    for x in range(len(codigo)):
        print("    ",codigo[x],"      ",nombre[x],"         ",horario[x],"         ")
    os.system("pause")
    menuEmpleado()

def menuClientes():
    os.system("cls")
    menuprincipal=int(input("Menu principal: \n1.- Registrarse \n2.-Ver Cartelera \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
    while menuprincipal!=0:
           
            if menuprincipal == 1:
                return RegistroClientes()               
            elif menuprincipal == 2:
                return consultarCartelera()
            #elif menuprincipal == 4:
                return  modificarHorario()
            #elif menuprincipal== 5:
                return buscarPelicula()     
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

def consultarCarteleraEmpleados():
    os.system("cls")
    print("La Cartelera Actual es: ")
    print("|   Codigo    |                   Nombre                       |         Horario       | Boletos")
    for x in range(len(codigo)):
        print("    ",codigo[x],"      ",nombre[x],"         ",horario[x],"         ",boletosDis[x])
    os.system("pause")
    menuEmpleado()
def agregarPeliculas():
    print("Ingrese La Pelicula: ")
    print("Llena los siguientes Datos: ")
    codigo.append(input("Codigo de la Pelicula:"))
    nombre.append(input("Nombre de la Pelicula:"))
    horario.append(input("Horario: "))
    boletosDis.append(int(input("Cuantos boletos existen:")))
    menuEmpleado()

def eliminarPeliculas():
    print("Eliminando: ")
    cod=input("Ingresa el codigo a eliminar: ")
    for i in range(len(codigo)-1,-1,-1):
        if codigo[i]== cod:
            codigo.pop(i)
            nombre.pop(i)
            horario.pop(i)
            print("Eliminado con exito")
def modificarHorario():
    cod1=input("Ingresa el codigo a modificar: ")
    for x in range(len(codigo)):
         if codigo[x] == cod1:
            horario[x] = input("Ingrese el nuevo horario")
            print("Modificado con exito")
    menuEmpleado()
def buscarPeliculaNombre():
    busqueda=input("Ingrese el nombre: ")
    for x in range(len(codigo)):
        if nombre[x]==busqueda:
            print(horario[x])
    os.system("pause")      
    menuEmpleado()




menuClientes()
