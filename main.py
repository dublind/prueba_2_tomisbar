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
usuario = []
#-----------------------------
opciones = " "
resp = " "
boleta = " "
clave = ""
clave_confirmar = ""
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
            usuario.append(nombre)
            print("Ingrese segundo nombre: ")
            segundo_nombre = input()
            usuario.append(segundo_nombre)
            print("Ingrese apellido paterno: ")
            apellido_p = input()
            usuario.append(apellido_p)
            print("Ingrese apellido materno: ")
            apellido_m = input()
            usuario.append(apellido_m)
            print("Ingrese rut: ")
            rut = input()
            usuario.append(rut)
            print("Crear clave: ")
            clave = input()
            while clave != clave_confirmar:
                print("confirme su clave: ")
                clave_confirmar = input()
                if clave == clave_confirmar:
                        print("Clave confirmada")
                        usuario.append(clave)
                        haymasopciones = False
                else:
                        print("Las claves no coinciden, intente nuevamente")



    elif opcion == "2":
        haymasopciones = True
        while haymasopciones:
          print("Ingrese nombre de la cuenta: ")
          print("Ingrese clave: ")
          opcion = input()
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
