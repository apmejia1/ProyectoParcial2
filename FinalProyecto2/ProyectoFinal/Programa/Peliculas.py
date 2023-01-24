"""
Este programa simula un software para un cine, que tiene la mayoria de funcionalidades que necesita
una entidad de ese tipo como la compra de tickets, la consulta de carteleras, etc.

Autores:
José SanMartín, Alexander Mejía

Versión:
VER 2.7
"""
#importamos la librería os, y la librería random 
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
#Creamos un diccionario necesario para realizar una eleccion randomica
opciones=["0","2","3","4","5","6","7","8","9","0"]
#Lee el texto plano Codigo
codigoR = open("Codigo.txt","r")
#Lee el texto plano Codigo
nombreR = open("Nombre.txt","r")
#Lee el texto plano Codigo
horarioR = open("Horario.txt","r")
#Lee el texto plano Codigo
boletosDisR=open("BoletosDisponibles.txt","r")
#Lee el texto plano Codigo
usuarioR =   open("Usuario.txt","r")
#Lee el texto plano Codigo
nombreEmR =   open("Nombre Empleado.txt","r")
#Lee el texto plano Codigo
userClienteR = open("Cliente.txt","r")
#Lee el texto plano Codigo
nombreClienteR = open("NombreCliente.txt","r")
#Lee el texto plano Codigo
compraR = open("Compra Boletos.txt","r")
#Lee el texto plano Codigo
cedulaR = open("ID.txt","r")
#Lee el texto plano Codigo
codigoCR = open("Codigos Compra.txt","r")
#Lee el texto plano Codigo
nacimientoR = open("Fechas.txt","r")
#Lee el texto plano Codigo
telefonoR=open("Telefono.txt","r")
#Divide el texto ingresado con una coma 
for a in codigoR.readline().split(","):
    if a != " ":
        codigo.append(a)
#Divide el texto ingresado con una coma 
for b in nombreR.readline().split(","):
    if b != " ":
        nombre.append(b)
#Divide el texto ingresado con una coma 
for c in horarioR.readline().split(","):
    if c != " ":
        horario.append(c)
#Divide el texto ingresado con una coma 
for x in boletosDisR.readline().split(","):
    if x != " ":
        boletosDis.append(x)
#Divide el texto ingresado con una coma 
for e in usuarioR.readline().split(","):
    if e != " ":
        usuario.append(e)
#Divide el texto ingresado con una coma 
for f in nombreEmR.readline().split(","):
    if f != " ":
        nombreEmpleado.append(f)
#Divide el texto ingresado con una coma 
for g in codigoCR.readline().split(","):
    if g != " ":
        codigosC.append(g)
#Divide el texto ingresado con una coma 
for h in userClienteR.readline().split(","):
    if h != " ":
            usuariocliente.append(h)
#Divide el texto ingresado con una coma 
for i in nombreClienteR.readline().split(","):
    if i != " ":
        nombrecliente.append(i)
#Divide el texto ingresado con una coma 
for j in compraR.readline().split(","):
    if j != " ":
            boletos.append(j)
#Divide el texto ingresado con una coma 
for k in cedulaR.readline().split(","):
    if k != " ":
        cedula.append(k)
#Divide el texto ingresado con una coma 
for l in nacimientoR.readline().split("."):
    if l != " ":
            nacimiento.append(l)
#Divide el texto ingresado con una coma 
for m in telefonoR.readline().split("."):
    if m != " ":
            telefono.append(m)
#Cierra el texto plano            
userClienteR.close()
#Cierra el texto plano   
nombreClienteR.close()
#Cierra el texto plano   
compraR.close()
#Cierra el texto plano   
cedulaR.close()
#Cierra el texto plano   
codigoCR.close()
#Cierra el texto plano   
nacimientoR.close()
#Cierra el texto plano   
telefonoR.close()
#Cierra el texto plano   
codigoR.close()
#Cierra el texto plano   
nombreR.close()
#Cierra el texto plano   
horarioR.close()
#Cierra el texto plano   
boletosDisR.close()
#Cierra el texto plano   
usuarioR.close()
#Cierra el texto plano   
nombreEmR.close()
#variable que recoge valor de ticket para niño
entradaniños=float(2.50)
#variable que recoge valor de ticket para niño
entradaAdultos=int(5)
def consultarCarteleraEmpleados():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    os.system("cls")
    #Imprime el mensaje de bienvenida
    print("------------------------------------------------------")
    print("----------------------Cartelera-----------------------")
    print("------------------------------------------------------")
    print("La Cartelera Actual es: ")
    #Imprime le model ode la tabala 
    print("|   Codigo    |                   Nombre                       |         Horario       | Boletos")
    # ciclo que recorre codigo según su tamaño
    for x in range(len(codigo)):
        print("    ",codigo[x],"      ",nombre[x],"         ",horario[x],"         ",boletosDis[x])
    # pausa la consola
    os.system("pause")
    # llamado a la función menuEmpleado()
    menuEmpleado()

def consultarCartelera():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # limpieza de la consola
    os.system("cls")
    # impresión de cartelera
    print("------------------------------------------------------")
    print("----------------------Cartelera-----------------------")
    print("------------------------------------------------------")
    print("La Cartelera Actual es: ")
    print("|   Codigo    |                   Nombre                       |         Horario       |")
    # ciclo que recorre la lista según la longitud del código
    for x in range(len(codigo)):
        print("    ",codigo[x],"      ",nombre[x],"         ",horario[x])
    # pausado de consola
    os.system("pause")
    # llamado de la funcion menucliente)
    menucliente()

def agregarPeliculas():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # impresion en pantalla
    print("Ingrese La Pelicula: ")
    print("Llena los siguientes Datos: ")
    # a la variable codigo se añade el input
    codigo.append(input("Codigo de la Pelicula:"))
    # a la variable nombre se añade el input
    nombre.append(input("Nombre de la Pelicula:"))
    # a la variable horario se añade el input
    horario.append(input("Horario en Horas:Segundos")) 
    
    # a la variable boletosDis se añade el input
    boletosDis.append(int(input("Cuantos boletos existen:")))
    # llamado a la función menuEmpleado
    menuEmpleado()

def eliminarPeliculas():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # impresion en pantalla
    print("Eliminando: ")
    # input que recoge codigo
    cod=input("Ingresa el codigo a eliminar: ")
    # ciclo que recorre la longitud de codigo
    for i in range(len(codigo)-1,-1,-1):
        # si los digitos de codigo es igual a cod
        if codigo[i]== cod:
            # codigo elimina el caracter
            codigo.pop(i)
            # nombre elimina el caracter
            nombre.pop(i)
            # horario elimina el caracter
            horario.pop(i)

            print("Eliminado con exito")

def modificarHorario():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # input que recoge codigo
    cod1=input("Ingresa el codigo a modificar: ")
    # ciclo que recorre codigo según su longitud
    for x in range(len(codigo)):
        # si ambos digitos coinciden
         if codigo[x] == cod1:
            # se asigna el nuevo horario
            horario[x] = input("Ingrese el nuevo horario")
            print("Modificado con exito")
    # llama a la función menuEmpleado()
    menuEmpleado()

def buscarPeliculaNombre():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # input que recoge el nombre
    busqueda=input("Ingrese el nombre: ")
    # ciclo que recorre el codigo
    for x in range(len(codigo)):
        # si nombre y busqueda coinciden
        if nombre[x]==busqueda:
            print("El horario es",horario[x])
    os.system("pause")
    # llamado a la función menuEmpleado()
    menuEmpleado()

def menuEmpleado():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    os.system("cls")
    # impresión de menú
    print("-------------------------------------------------------")
    print("--------------Menú Principal de Empleado--------------")
    print("-------------------------------------------------------")
    # input que recoge la opción que decida realizar
    menuprincipal = (input("Menu principal: \n1.- Ver Cartelera \n2.-Insertar Pelicula \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
    # mientras valor sea diferente a 0
    while menuprincipal != "0":
        # if anidado que valida opciones
        if menuprincipal == "1":
            # retorna funcion
            return consultarCarteleraEmpleados()
        elif menuprincipal == "2":
            # retorna funcion
            return agregarPeliculas()                
        elif menuprincipal == "3":
            # retorna funcion
            return eliminarPeliculas()
        elif menuprincipal == "4":
            # retorna funcion
            return  modificarHorario()
        elif menuprincipal== "5":
            # retorna funcion
            return buscarPeliculaNombre()     
        # caso contrario
        else: 
            # vuelve a pedir la opcion
            print("Por favor ingresa una opcion correcta")
        menuprincipal=int(input("Menu principal: \n1.- Ver Cartelera \n2.-Insertar Pelicula \n3.-Eliminar Pelicula \n4.-Modificar Horario \n0.-Salir \nOpcion: "))
        break
    # llama a la función main
    main()
    # apertura de arcivos de texto
    codigoT = open("Codigo.txt","r")
    # apertura de arcivos de texto
    nombreT = open("Nombre.txt","r")
    # apertura de arcivos de texto
    horarioT = open("Horario.txt","r")
    # apertura de arcivos de texto
    boletosDisT=open("BoletosDisponibles.txt","r")
    # ciclo que recorre codigo
    for x in range(len(codigo)):
        # reescribe el valor del caracter 
        codigoT.write(codigo[x]+",")
        # reescribe el valor del caracter
        nombreT.write(nombre[x]+",")
        # reescribe el valor del caracter
        horarioT.write(horario[x]+",")
        # reescribe el valor del caracter
        boletosDisT.write(str(boletosDis[x])+",")
    # cierre de archivo de texto
    codigoT.close()
    # cierre de archivo de texto
    nombreT.close()
    # cierre de archivo de texto
    horarioT.close()
    # cierre de archivo de texto
    boletosDisT.close()

def consultarEmpleados():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    # limpieza de consola
    os.system("cls")
    # impresión de menú
    print("La Cartelera Actual es: ")
    print("|   Usuario    |                   Nombre                       |")
    # ciclo que recorre usuario
    for x in range(len(usuario)):
        # imprime ambos datos
        print("    ",usuario[x],"      ",nombreEmpleado[x])
    # pausado de consola
    os.system("pause")
    # llamado de la función menuGerente()
    menuGerente()        

def agregarEmpleado():
    """
    Esta función agrega empleados a la lista vacia, para obtener un archivo plano
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       No tiene retornos
    """
    # limpieza de consola
    os.system("cls")
    # impresión en pantalla
    print("Llena los siguientes Datos: ")
    # input que recoge el primer nombre
    nombre1=input("Por Favor ingrese el primer nombre: ")
    # input que recoge el segundo nombre
    nombre2=input("Por Favor ingrese el segundo nombre: ")
    # si nombre es vacio
    if nombre2 == "":
        nombre2 = "_"
    # input que recoge el primer apellido
    apellido1=input("Por favor ingrese el Primer apellido: ")
    # input que recoge el segundo apellido
    apellido2=input("Por favor ingrese el segundo apellido: ")
    # almacena variable en minusculas
    resa=nombre1.lower()
    a=resa[0:1]
    # almacena variable en minusculas
    resb=nombre2.lower()
    b=resb[0:1]
    # almacena variable en minusculas
    resc=apellido1.lower()
    c=resc[0:2]
    # almacena variable en minusculas
    resd=apellido2.lower()
    d=resd[0:2]
    # almacena todos las variables en minusculas
    res=(a,b,c,d)
    # nusuario almacena la variable res
    nusuario="".join(res)
    # nusuario almacena la variable res
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    # nusuario almacena la variable res
    res1=(a,b,c,d,random.choice(opciones))
    nusuario1="".join(res1)
    # usuario se agrega a nusuario1
    usuario.append(nusuario1)
    # nombreUsuario une las variables de nombre y apellido
    nombreUsuario=(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    # lista nombreEmpleado agrega el usuario creado a su valor
    nombreEmpleado.append(nombreUsuario)
  
        
    os.system("pause")
    # llamado de función menuGerente
    menuGerente()

def eliminarEmpleado():
    """
    Esta función elimina a un empleado que anteriormente hayamos creado
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       No tiene retornos
    """
    os.system("cls")
    # impresión en pantalla
    print("Eliminando: ")
    # input que pide el código de usuario
    cod=input("Ingresa el codigo usuario eliminar: ")
    # ciclo que recorre usuario
    for i in range(len(usuario)-1,-1,-1):
        # si los valores coinciden
        if usuario[i]== cod:
            # usuario elimina según i
            usuario.pop(i)
            # nombreEmpleado elimina según i
            nombreEmpleado.pop(i)
            print("Eliminado con exito")
    os.system("pause")
    # llamado a menuGerente()
    menuGerente()
    
def buscarEmpleado():
    """
    Esta función tiene como proposito buscar empleados que hayamos creado anteriormente
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       No tiene retornos
    """
    # input que recoge el codigo
    nombre=input("Ingrese el codigo: ")
    # ciclo que recorre nombreEmpleado
    for x in range(len(nombreEmpleado)):
        # si los digitos coinciden 
        if nombreEmpleado[x]==nombre:
            # imprime el valor
            print("El usuario del emepleado es : ",usuario[x])
            
    os.system("pause")  
    # llamado a la función menuGerente()  
    menuGerente()

def menuGerente():
    """
    Esta función almacena las funciones a las que el gerente deberia tener acceso
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       No tiene retornos
    """
    os.system("cls")
    # impresión del menú
    print("------------------------------------------------------")
    print("------------------- Menú de Gerente-------------------")
    print("------------------------------------------------------")
    # input que recoge la opción en la que se desea trabajar
    menuprincipal = input("Menu principal: \n1.- Ver Empleados \n2.-Agregar Empleado \n3.-Eliminar Empleado \n4.-Buscar Empleado \n0.-Salir \nOpcion: ")
    # mientras la opción sea diferente a 0
    while menuprincipal != "0":
        # if anidado que controla las opciones
        if menuprincipal == "1":
            # llamado de la función
            return consultarEmpleados()
        elif menuprincipal == "2":
            # llamado de la función
            return agregarEmpleado()                
        elif menuprincipal == "3":
            # llamado de la función
            return eliminarEmpleado()
        elif menuprincipal== "4":
            # llamado de la función
            return buscarEmpleado()     
        # caso contrario
        else: 
            # pide nuevamente el valor de opción
            print("Por favor ingresa una opcion correcta")
        menuprincipal = input("Menu principal: \n1.- Ver Empleados \n2.-Agregar Empleado \n3.-Eliminar Empleado \n4.-Buscar Empleado \n0.-Salir \nOpcion: ")
        break
    # llamado a la función main()
    main()
    # apertura de archivo plano
    usuarioT =  open("Usuario.txt","w")
    # apertura de archivo plano
    nombreET =  open("Nombre Empleado.txt","w")
 
    # ciclo que recorre el valor de usuario
    for x in range(len(usuario)):
        # reescribe los valores
        usuarioT.write(usuario[x]+",")
        # reescribe los valores
        nombreET.write(str(nombreEmpleado[x])+",")
            
    # cierre de archivo plano
    usuarioT.close()
    # cierre de archivo plano
    nombreET.close()

def comprar():
    """
    Esta función almacena las funciones a las que el cliente deberia tener acceso
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       Retorna laas funciones según el caso
    """
    # impresion del menu
    print("------------------------------------------------------")
    print("--------------------Menú de Compra--------------------")
    print("------------------------------------------------------")
    # input que recoge opcion
    pelicula = (input("Ingrese el titulo de la pelicula que desea ver: "))
    # ciclo que recorre codigo
    for x in range(len(codigo)):
        # si los digitos de las variables coinciden
        if pelicula == nombre[x]:
            # a toma el valor de boletos disponibles
            a = (boletosDis[x])
            # ticket es igual a a
            ticket = int(a)
        else:
            print("La pelicula no coincide con nuestra cartelera")
            return comprar()
    # input que recoge cuantos tickets desea comprar
    adultos=int(input("Ingrese la cantidad de tickets para adultos: "))
    # si no tiene nada valor se pone en 0
    if adultos == None:
        adultos=0
    # input que recoge cuantos tickets desea comprar
    niños=int(input("Ingrese la cantidad de tickets para niños: "))
    # si no tiene nada valor se pone en 0
    if niños ==None:
        niños=0
    # almacena la suma de los boletos de niños y adultos
    boletosacomprar = (adultos+niños)
    # operacion que da el valor de entrada por precio niño
    totalniños=niños*entradaniños
    # operacion que da el valor de entrada por precio adultos
    totaladultos=adultos*entradaAdultos
    # suma de ambos valores 
    preciototal=(totalniños+totaladultos)
    # si boletos superan los tickets disponbibles
    if boletosacomprar>ticket:
        # impresión en pantalla
        print("No existen suficientes boletos ")
        # precio total en 0
        preciototal="0"
        # variable que recoge opción
        continuar=input("Desea seguir comprando? 1(si) y 2(no): ")
        # mientras la opcion sea diferente a 0
        while continuar!="0":
            if continuar=="1":
                return comprar()
            if continuar=="2":
                return main()
            # caso contrario se muestra el precio total de las entradas
            else:
                print("El precios a pagar es: ",preciototal)
        # variable vuelve a pedir opción
        else:
            continuar=input("Desea seguir comprando? 1(si) y 2(no): ")
    # imprimimos en pantalla
    print("Ustede a comprado un total de:",boletosacomprar,"boletos : Para adultos",adultos,"y para niños",niños)
    # imprime boletos restantes
    boletosrestantes=ticket-(boletosacomprar)
    # ciclo que recorre codigo
    for x in range(len(codigo)):
        # si nombre es igual a la pelicula
         if nombre[x] == pelicula:
            # boletos se actualizan al nuevo valor
            boletos[x] = (boletosrestantes)
    # retorna función menuCliente()
    return menucliente()
            

def menucliente():
    """
    Esta función almacena las funciones a las que el cliente deberia tener acceso
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       Retorna laas funciones según el caso
    """
    #impresion del menú
    print("-------------------------------------------------------")
    print("---------------Bienvenido a Menú Cliente---------------")
    print("-------------------------------------------------------")
    # variable que recoge la opcion
    opciones = input("Ingrese una de las opciones: \n1.-Consultar Cartelera \n2.-comprar \n0.-Salir \nOpcion: : ")
    # mientras la opción sea diferente a 0
    while opciones != "0":
        if opciones == "1":
            return consultarCartelera()
        elif opciones == "2":
            return comprar()
    main()

def main():
    """
    Esta función almacena el main de nuestro programa, donde mediante un if anidado controla las opciones a las que nos queremos dirigir
    Parametros:
    ------------
       No tiene parametros de entrada
           
    Retorna:
    ------------
       Retorna las funciones según la opción
    """
    print("------------------------------------------------------")
    print("----------------Bienveido a TicketsPop----------------")
    print("------------------------------------------------------")
    # input que recoge la opcion
    opciones = input("Ingrese una de las opciones: \n1.-Empleado \n2.-Gerente \n3.-Cliente \n0.-Salir\nOpciones: ")
    # mientras la opción sea diferente a 0
    while opciones != "0":
        if opciones == "1":
            return menuEmpleado()
        elif opciones == "2":
            return menuGerente()
        elif opciones == "3":
            return menucliente()
        else:
            print("OPCIÓN NO VALIDA...")

            return main()

if __name__ == "__main__":
    # llamado de la función main
    main()

