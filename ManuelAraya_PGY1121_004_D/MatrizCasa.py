from gettext import npgettext
import os
import numpy as np
import FunCasa as fn
casa=np.empty([10,4], type(int))
casa2=np.empty([10,4], type(int))
fn.llenarMatriz(casa)
os.system("cls")
op=0
depa=0
rut=[]
while(op!=5):
    os.system("cls")
    print("        Inmobiliaria Casa Feliz  ")
    print("1. Comprar departamento ")
    print("2. Mostrar departamentos disponibles ")
    print("3. Ver listado de compradores        ")
    print("4. Mostrar ganancias totales         ")
    print("5. Salir                             ")
    op=fn.validaOp(op)
    if(op==1):
        fn.ValidaRut(rut)
        fn.mostrarDispo(casa)
        depa=fn.validaDepa(depa)
        disponibilidad=fn.Disponibles(casa,depa)
        if disponibilidad:
            print("Departamento Disponible")
            monto=fn.comprardep(casa,depa)
            print("Usted va a cancelar: ", monto,"UF")
        else: 
            print("El departamente que usted ha ingresado no esta disponible")

        os.system("pause")
    if(op==2):
        fn.mostrarDispo(casa)
        os.system("pause")
    if(op==3):
        totalcompradores=fn.MuestraCompradores(rut)
        print(totalcompradores)
        input("<<Enter Para continuar>>")
    if(op==4):
        suma=0
        suma=fn.totalventas(casa)
        if (suma==0):
            print("No hay departamentos vendidos hasta el momento")
        else:

            print("El total de ventas es de ", suma)
            os.system("pause")
        input("<<enter para continuar>>") 
    if(op==5):
        print("\tGracias por usar nuestro servicio") 
        break   
