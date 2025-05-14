#13-05-25 10:52
#Choripan 09/05/2025 21:33 (Arreglado el error de agendar otros meses y el de reagendar horas,
# testeado tanto en Agustin cmo en Tomi), falta asignar un texto y un retorno en caso de que elijan una fecha invalida
import random 
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
dia = 0
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
ver_horario = " "
mod = ""
mes = 0
hora = 0
nueva_hora = 0
hora_real = 0
cambio_hora = 0
#-----------------------------
#atencion al cliente
correo = " "
nombre_mail = " "
#-----------------------------
#tipo de pago
rut = " "
tipo_pago = 0
tarjeta = 1
efectovio = 2


print("Bienvenido!")

while noesfindejornada:
    print("Ingrese la opcion deseada: ")
    print("1- Crear cuenta")
    print("2- Iniciar sesion")
    print("3- Ingreso de colaboradores")
    print("4- Agenda")
    print("5- Atencion al cliente")
    print("6- salir \n")
    opcion = input()

    if opcion == "1":
        haymasopciones = True
        while haymasopciones:
            crear_usuario = []
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
                else:
                        print("Las claves no coinciden, intente nuevamente")
            usuario = crear_usuario[:]
            usuario_completo.append(usuario)
            print("Usuario creado con exito!")
            haymasopciones = False

    elif opcion == "2":
        haymasopciones = True
        while haymasopciones:
            print("Ingrese su nombre de usuario: ")
            nombre = input()
            print("Ingrese su clave: ")
            clave = input()
            if nombre in usuario and clave in usuario:
                print("Bienvenido de nuevo!")
                print("{} su numero de usuario ".format(nombre))
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
        haymasopciones = True
        while haymasopciones:
            print("Ingreso de colaboradores (Tomas/Agustin) ")
            bar = input()
            if bar == bar_1:
                print("Ingrese la clave: ")
                clave_bar = input()
                if clave_bar == clave_bar1:
                    print("Bienvenido Tomas!")
                    print("Tu horario es de 9:00 a 18:00: ")
                    print("Quieres ver tu horas agendadas? (si/no)")
                    ver_horario = input()
                    if ver_horario == "si":
                        print("Estas son tus horas agendadas: ")
                        print(horario_1)
                        print("Quieres modificar tu horario? (si/no)")
                        mod = input()
                        if mod == "si":
                            print("Ingrese el mes que desea modificar: ")
                            mes = int(input())
                            print ("ingrese el dia a modificar")
                            dia = int(input())
                            print("Ingrese la hora que desea modificar: ")
                            hora = int(input())
                            for i in range(len(horario_1)):
                                if horario_1[i][1] == mes and horario_1[i][0] == dia and horario_1[i][2] == hora:
                                    horario_1.remove(horario_1[i])
                                    print("Ingrese la nueva hora: ")
                                    cambio_hora = int(input())
                                    horario_1.append([mes, dia, cambio_hora])
                                    print("Horario modificado con exito!")
                                    print("Estas son tus horas agendadas: ")
                                    print(horario_1)
                                else: print ("la hora que quiere modificar no existe en su horario.")
                                haymasopciones = False
                        elif mod == "no":
                            print("No se ha modificado el horario")
                            haymasopciones = False
                        else:
                            print("Opcion invalida, no se ha modificado el horario")
                            haymasopciones = False
                    else:
                        print("Hasta luego!")
                        haymasopciones = False
                else:
                    intentos -= 1
                    if intentos == 0:
                        print("Se han agotado los intentos, vuelva a intentarlo mas tarde")
                        haymasopciones = False
                    print("Le quedan {} intentos".format(intentos))
                    print("Colaborador no registrado, intente nuevamente")
                    print("Clave incorrecta, intente nuevamente")

            elif bar == bar_2:
                print("Ingrese la clave: ")
                clave_bar = input()
                if clave_bar == clave_bar2:
                    print("Bienvenido Agustin!")
                    print("Tu horario es de 9:00 a 18:00: ")
                    print("Quieres ver tu horas agendadas? (si/no)")
                    ver_horario = input()
                    if ver_horario == "si":
                        print("Estas son tus horas agendadas: ")
                        print(horario_2)
                        print("Quieres modificar tu horario? (si/no)")
                        mod = input()
                        if mod == "si":
                            print("Ingrese el mes que desea modificar: ")
                            mes = int(input())
                            print ("ingrese el dia a modificar")
                            dia = int(input())
                            print("Ingrese la hora que desea modificar: ")
                            hora = int(input())
                            for i in range(len(horario_2)):
                                if horario_2[i][1] == mes and horario_2[i][0] == dia and horario_2[i][2] == hora:
                                    horario_2.remove(horario_2[i])
                                    print("Ingrese la nueva hora: ")
                                    cambio_hora = int(input())
                                    horario_2.append([mes, dia, cambio_hora])
                                    print("Horario modificado con exito!")
                                    print("Estas son tus nuevas horas agendadas: ")
                                    print(horario_2)
                                else: print ("la hora que quiere modificar no existe en su horario.")
                                haymasopciones = False
                        elif mod == "no":
                            print("No se ha modificado el horario")
                            haymasopciones = False
                        else:
                            print("Opcion invalida, no se ha modificado el horario")
                            haymasopciones = False
                    else:
                        print("Hasta luego!")
                        haymasopciones = False
                else:
                    intentos -= 1
                    if intentos == 0:
                        print("Se han agotado los intentos, vuelva a intentarlo mas tarde")
                        haymasopciones = False
                    print("Le quedan {} intentos".format(intentos))
                    print("Colaborador no registrado, intente nuevamente")
                    print("Clave incorrecta, intente nuevamente")
    elif opcion == "4":
        haymasopciones = True
        while haymasopciones:
            if nombre in usuario and clave in usuario:
                print("Bienvenido a la agenda de horarios!. \n")
                print("{} desea agendar con Tomas o Agustin? (Tomas/Agustin)".format(nombre))
                bar = input()
                if bar == "Agustin":
                    print("Agustin")
                    print("Ingrese el mes en el cual desea agendar¨(entre 1 y 12): ")
                    mes = int(input())
                    if mes < 13 and mes > 0:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            print("Ingrese el dia (entre 1 y 31): ")
                            dia = int(input())
                            if dia < 32 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_2.append([dia, mes, hora_real])
                                    print("Gracias por su consulta!")
                                    
                                    haymasopciones = False
                                else:
                                    print("Hora invalida, intente nuevamente")

                        elif mes == 2:
                            print("Ingrese el dia (entre 1 y 28): ")
                            dia = int(input())
                            if dia < 29 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_2.append([dia, mes, hora_real, nombre])
                                    print("Gracias por su consulta!")
                                    haymasopciones = False
                        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                            print("Ingrese el dia (entre 1 y 30): ")
                            dia = int(input())
                            if dia < 31 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_2.append([dia, mes, hora_real])
                                    print("Gracias por su consulta!")
                                    haymasopciones = False
                    else:
                        print("mes invalido, intente nuevamente \n")
                elif bar == "Tomas":
                    print("de Tomas")
                    print("Ingrese el mes en el cual desea agendar¨(entre 1 y 12): ")
                    mes = int(input())
                    if mes < 13 and mes > 0:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            print("Ingrese el dia (entre 1 y 31): ")
                            dia = int(input())
                            if dia < 32 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_1.append([dia, mes, hora_real])
                                    print("Gracias por su consulta!")
                                    haymasopciones = False
                                else:
                                    print("Hora invalida, intente nuevamente")
                        elif mes == 2:
                            print("Ingrese el dia (entre 1 y 28): ")
                            dia = int(input())
                            if dia < 29 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_1.append([dia, mes, hora_real])
                                    print("Gracias por su consulta!")
                                    haymasopciones = False
                                else:
                                    print("Hora invalida, intente nuevamente")
                        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                            print("Ingrese el dia (entre 1 y 30): ")
                            dia = int(input())
                            if dia < 31 and dia > 0:
                                print("1- 9:00")
                                print("2- 10:00")
                                print("3- 11:00")
                                print("4- 12:00")
                                print("5- 13:00")
                                print("6- 14:00")
                                print("7- 15:00")
                                print("8- 16:00")
                                print("9- 17:00")
                                print("10- 18:00")
                                print ("Seleccione su hora (entre 9:00 y 18:00 horas)")
                                hora = int(input())
                                if hora < 11 and hora > 0:
                                    hora_real = (hora +8)
                                    print("{} ,su hora agendada es: {}-{}-{} a las {}:00".format(nombre, dia, mes, 2025, hora_real))
                                    horario_1.append([dia, mes, hora_real])
                                    print("Gracias por su consulta!")
                                    print("Ingrese datos de boleta: ")
                                    print("Ingrese rut: ")
                                    rut = input()
                                    print("Ingrese tipo de pago: ")
                                    print("1- Efectivo \n 2- Tarjeta")
                                    tipo_pago = ()
                                    if tipo_pago == 1:
                                            print("perfecto, {}")
                                    haymasopciones = False
                                else:
                                    print("Hora invalida, intente nuevamente")
                        else:
                            print("mes invalido, intente nuevamente")
                haymasopciones = False
            else:
                print("Debe crear un usuario")
                haymasopciones = False

    elif opcion == "5":
        haymasopciones = True
        while haymasopciones:
            print("Ingrese su correo:")
            correo = input()
            print("Ingrese su nombre:")
            nombre_mail = input()
            print("Nos contactaremos muy pronto con usted {}".format(nombre_mail))
            print("Gracias por su consulta!")
            haymasopciones = False
        haymasopciones = False
    elif opcion == "6":
        noesfindejornada = False
        print ("Hasta pronto!")
    else:
        haymasopciones = True
        while haymasopciones:
            print("\nOpcion invalida intente nuevamente \n")
            haymasopciones = False
