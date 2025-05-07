#choripan
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
rut = 0
#-----------------------------
#variables generales
haymasopciones = True
intentos = 3
opciones = " "
resp = " "
boleta = " "
contador = 0
mes = " "
opcion = ""
noesfindejornada = True
#-----------------------------
#variables colaborador
bar = " "
clave_bar = " "
bar_1 = "Tomas"
bar_2 = "Agustin"
clave_bar1 = "1234"
clave_bar2 = "5678"
horario_1 = []
horario_2 = []
ver_horario_1 = " "
mod = ""
mes = 0
hora = 0
nueva_hora = 0
#-----------------------------
 

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
            usuario_completo.append(usuario)
            print("Usuario creado con exito!")
    elif opcion == "2":
        while haymasopciones:
            print("Ingrese su nombre de usuario: ")
            nombre = input()
            print("Ingrese su clave: ")
            clave = input()
            if nombre in usuario and clave in usuario:
                print("Bienvenido de nuevo!")
                haymasopciones = False
            else:
                print("Usuario o clave incorrecta, intente nuevamente")
                intentos -= 1
                if intentos == 0:
                    print("Se han agotado los intentos, vuelva a intentarlo mas tarde")
                    haymasopciones = False
                else:
                    print("Le quedan {} intentos".format(intentos))

    elif opcion == "3":
        while haymasopciones:
            print("Ingreso de colaboradores: ")
            bar = input()
            if bar == bar_1:
                print("Ingrese la clave: ")
                clave_bar = input()
                if clave_bar == clave_bar1:
                    print("Bienvenido Tomas!")
                    print("Tu horario es de 9:00 a 18:00: ")
                    print("Quieres ver tu horas agendadas? (si/no)")
                    ver_horario_1 = input()
                    if ver_horario_1 == "si":
                        print("Estas son tus horas agendadas: ")
                        print(horario_1)
                        print("Quieres modificar tu horario? (si/no)")
                        mod = input()
                        if mod == "si":
                            print("Ingrese el mes de la hora que desea modificar: ")
                            mes = int(input())
                            print("Ingrese la hora que desea modificar: ")
                            hora = int(input())
                            horario_1.remove((mes, hora))
                            print("Ingrese la nueva hora: ")
                            nueva_hora = int(input())
                            horario_1.append((mes, nueva_hora))
                            print("Horario modificado con exito!")
                            print("Estas son tus horas agendadas: ")
                            print(horario_1)
                        elif mod == "no":
                            print("No se ha modificado el horario")
                        else:
                            print("Opcion invalida, no se ha modificado el horario")
                        
                    else:
                        print("Hasta luego!")
                        haymasopciones = False
    
                else:
                    print("Clave incorrecta, intente nuevamente")
            elif bar == bar_2:
                print("Ingrese la clave: ")
                clave_bar = input()
                if clave_bar == clave_bar2:
                    print("Bienvenido Agustin!")
                    haymasopciones = False
                else:
                    print("Clave incorrecta, intente nuevamente")
            else:
                print("Colaborador no registrado, intente nuevamente")
                intentos -= 1
                if intentos == 0:
                    print("Se han agotado los intentos, vuelva a intentarlo mas tarde")
                    haymasopciones = False
                else:
                    print("Le quedan {} intentos".format(intentos))
    elif opcion == "4":
        while haymasopciones:
            print("Ingrese el mes en el cual desea agendar¨(entre 1 y 12): ")
            mes = int(input())
            if mes < 13 and mes > 0:
                print("Agendado, muchas gracias!")
            else: print ("Invalido")
    elif opcion == "5":
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
