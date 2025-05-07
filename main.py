#choripan
opcion = ""
noesfindejornada = True
mes = " "
horas = 10
dia  = 0
contador = 0
hora_tomada = 0
producto = ""
#variables ususario
nombre = " "
segundo_nombre = " "
apellido_p = " "
apellido_m = " "
crear_usuario = []
usuario = []
clave = ""
clave_confirmar = ""
usuario_completo = []
#-----------------------------
intentos = 3
opciones = " "
resp = " "
boleta = " "
rut = 0
Num_trans = 0
efectivo = 0
Tarjeta = 0
tipo_pago = " "
num_tarjeta = 0
clave_tarjeta = 0
bar_1 = " "
horario = " "
mod = 0
modificar = ""
contabilidad = " "

print("Bienvenido!")

while noesfindejornada:
    print("1- Crear cuenta")
    print("2- Iniciar sesion")
    print("3- Ingreso de colaboradores")
    print("4- Agenda")
    print("5- Atencion al cliente")
    print("6- salir \n")
    print("Ingrese la opcion deseada: ")
    opcion = input()

    if opcion == "1":
        haymasopciones = True
        while haymasopciones:
            print("Ingrese primer nombre del usuario: ")
            nombre = input()
            crear_usuario.append(nombre)
            print("Ingrese segundo nombre: ")
            segundo_nombre = input()
            crear_usuario.append(segundo_nombre)
            print("Ingrese apellido paterno: ")
            apellido_p = input()
            crear_usuario.append(apellido_p)
            print("Ingrese apellido materno: ")
            apellido_m = input()
            crear_usuario.append(apellido_m)
            print("Ingrese rut: ")
            rut = input()
            crear_usuario.append(rut)
            print("Crear clave: ")
            clave = input()
            while clave != clave_confirmar:
                print("confirme su clave: ")
                clave_confirmar = input()
                if clave == clave_confirmar:
                        print("Clave confirmada")
                        crear_usuario.append(clave)
                        haymasopciones = False
                else:
                        print("Las claves no coinciden, intente nuevamente")
            usuario = crear_usuario[:]
            usuario_completo = usuario
            print(usuario)
    elif opcion == "2":
        haymasopciones = True
        while haymasopciones:
            print("Ingrese nombre de la cuenta: ")
            nombre = input()
            for i in range(intentos):
                print("tienes {} intentos:".format(i))
                print("ingrese nombre: ")
                nombre = input()
                if i == 2:
                  print("debe crear otra cuenta")
                  haymasopciones = False
                elif nombre is usuario:
                    i = 2
            print("Ingrese clave: ")
            clave = input()
            while not clave in usuario:
                print("clave no es valida \n ingrese una clave valida")
                clave = input()

    elif opcion == "3":
        haymasopciones = True
        while haymasopciones:
            print("Ingreso de colaboradores: ")
            print(("Ingrese la clave: "))
            opcion = input()
    elif opcion == "4":
        haymasopciones = True
        while haymasopciones:
            print("Ingrese el mes en el cual desea agendar¨(entre 1 y 12): ")
            mes = int(input())
            if mes < 13 and mes > 0:
                print("Agendado, muchas gracias!")
            else: print ("Invalido")
    elif opcion == "5":
        noesfindejornada = True
        while haymasopciones:
           print ("naxoweko")
    elif opcion == "6":
        noesfindejornada = False
        print ("Hasta pronto!")
    else:
        haymasopciones = True
        while haymasopciones:
            print("\nOpcion invalida intente nuevamente \n")
            haymasopciones = False
