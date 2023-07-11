import os
import numpy as np
def llenarMatriz(casa):
    p=1
    for i in range(10):
        for j in range(4):
            casa[i,j]=p
            p+=1

def validaOp(op):
    while(True):
        try:
            op=int(input("   Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
    return op


def mostrarDispo(casa):
    os.system("cls")
    print("         A       B               C       D    ")
    for i in range(10):
        print("\n")
        for j in range(4):
            if(j==1):
                print("\t",casa[i,j], end="        ")
            else:
                print("\t",casa[i,j], end="    ")         
    print("\n\n")
    



def validaDepa(depa):
    depa=0
    while True:
        try: 
            depa=int(input("Ingrese número de departamento (1-40): "))
            if (depa>=1 and depa<=40):
                break
            else:
                print(" Por favor ingrese numero de departamento entre  1 y 40")
        except ValueError:
            print(" Por favor ingrese numero de departemento entre 1 y 40")
    return depa



def Disponibles(casa, depa):
    for x in range(10):
        for i in range(4):
            if (depa==casa[x,i]):
                return True
    return False   
  
def comprardep(casa, depa):
 
    for x in range(10):
        for i in range(4):
            if (casa[x,i]==depa):
                casa[x,i]="x"        
                if i==0:
                    pago=3800
                if i==1 :
                    pago=3000
                if i==2 :
                    pago=2800  
                if i==3 :
                    pago=3500
    return pago        


def PagarDepa(casa,depa):
    
    
    for x in range(10):
        for i in range(4):
            if (casa[x,i]==depa):
                casa[x,i]="x"        
                if (i==0):
                    pago=3800
                if (i==1):
                    pago=3000
                if(i==2):
                    pago=2800
                if(i==3):
                    pago=3500

    return pago

def ValidaRut(rut):
    os.system("cls")
    rr=""
    while(len(rr)<=0):
        rr=input("Ingrese rut: ")
        if(len(rr)<8):
            print("Debe tener 8 caracteres minimo")
            rr=""
    rut.append(rr)


def MuestraCompradores(rut):
    MenorDeArreglo=[]

    MenorDeArreglo.sort()
    MenorDeArreglo.reverse()
    print("Rut Compradores",rut)
    



def MenorDeArreglo(rut):
    MenorDeArreglo=[]
    for i in range(30):
        for j in range(7):
            if(rut[i,j]<50000):
                MenorDeArreglo.append(rut[i,j])
                
    MenorDeArreglo.sort()
    MenorDeArreglo.reverse()

def totalventas(casa):
    suma=0
    for x in range(10):
        for i in range(4):
            if(casa[x,i]==0):
                if(i==0):
                    suma+=3800
                if(i==1):
                    suma+=3000
                if(i==2):
                    suma+=2800
                if(i==3):
                    suma+=3500
    return suma





    



        
        


	
