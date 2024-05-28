import os, time

os.system("cls")
pacientes = []
banderaMenu =True
banderarut = True
banderaedad = True
while banderaMenu:
    
    banderaMenu = True
    banderarut = True
    banderaedad = True
    banderaPaciente =True
    
    
    print("\tCentro Medico DUOC UC")
    print("1) Registrar paciente")
    print("2) Atencion Paciente")
    print("3) Gestionar Paciente")
    print("Salir")
    
    opc=int(input("Eliga una opcion\n"))
    
    if opc == 1:
        
        print("Menu Registrar Paciente")
        while banderaPaciente:
            while banderarut:
                try:
                    rut=int(input("ingrese Rut del paciente sin digito verificador ni puntos\n"))
                    if rut >5000000 or rut <30000000:
                        print("Rut Ingresado correctamente")
                        banderarut = False
                    else:
                        print("Ingrese un rut valido")
                    
                except:
                    print("Error, ingrese solo numeros enteros en rut del paciente")
            
            name = input("Ingrese el nombre del paciente\n")
            while name == "" or name == " ":
                name = input("El campo Nombre no puede venir vacio\n")
            address = input("Ingrese el Direccion del paciente\n")
            while address == "" or address == " ":
                address = input("El campo Dirección no puede venir vacio\n")
            email = input("Ingrese el correo del paciente\n")
            while "@" not in email or email =="" or email == " ":
                email = input("El campo correo no puede venir vacio y sin @\n")
            
            while banderaedad:
                try:
                    edad=int(input("ingrese Edad del paciente\n"))
                    if edad >= 0 and edad <= 110:
                        print("Edad Ingresado correctamente")
                        banderaedad = False
                    else:
                        print("Ingrese un edad valida")
                    
                except:
                    print("Error, ingrese solo numeros enteros en edad del paciente")
            
            sexo = input("Ingrese el sexo del paciente f o m \n")
            while sexo == "" and name == " " and sexo != "f" and sexo != "m":
                sexo = input("El campo sexo no puede venir vacio\n")
            #Registros se crearar si el paciente asiste a la consulta
            prevision = input ("Ingrese prevision del paciente, Isapre o Fonasa\n")
            while prevision != "Isapre" and prevision != "Fonasa":
                prevision = input ("Error, Ingrese prevision del paciente, Isapre o Fonasa\n")
            
            paciente=[rut,name, address, email, edad, sexo, prevision]
            pacientes.append(paciente) #Para ingresar en la lista "pacientes" los pacientes que se estan registrando
            otroPaciente = int(input("Desea ingresar otro paciente. 1)Si 2) No\n"))
        if otroPaciente ==1:
            continue
        else:
            print(paciente)
            banderaPaciente = False
        
        
        
    elif opc == 2:
        print("Menu Atencion Paciente")
        rutBuscar = int(input("Ingrese rut a atender\n"))
        for paciente in pacientes:
            if pacientes[0] == rutBuscar:
                print(f"Adelante el paciente {pacientes[0]}")
                registro = input("Ingrese sintomas\n")
                while registro == "":
                    registro = input("Ingresar sintomas\n")
                paciente.append(registro)
                print(paciente)
                input("enter para continuar")
        
    elif opc == 3:
        print("Gestionar Paciente ")
        
    elif opc == 4:
        banderaMenu ==False
        

    