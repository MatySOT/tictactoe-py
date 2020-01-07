# importar sistema
from os import system
# importar numeros random
from random import randint
# importar tiempo
import time


# validando...
def validar(input1):
    try:
        input1 = int(input1)
        if input1 in [1,2,3,4,5,6,7,8,9]:
            return True
        else:
            return False
    except:
        return False

# revisar ganador
def ganar(tablero):
    if tablero[0] == tablero[1] == tablero[2]:
        return True
    if tablero[3] == tablero[4] == tablero[5]:
        return True
    if tablero[6] == tablero[7] == tablero[8]:
        return True
    if tablero[0] == tablero[4] == tablero[8]:
        return True
    if tablero[2] == tablero[4] == tablero[6]:
        return True
    if tablero[0] == tablero[3] == tablero[6]:
        return True
    if tablero[1] == tablero[4] == tablero[7]:
        return True
    if tablero[2] == tablero[5] == tablero[8]:
        return True
    b = 0
    for a in tablero:
        if a not in [1,2,3,4,5,6,7,8,9]:
            b += 1
    if b == 9:
        return "empate"
            
        
    return False

# jugar con un robot
def robot(tablero, n):
    while True:
        r = randint(1,9)
        if validar(r) and validar(tablero[r-1]):
            return r

    
# tablero
tablero = [1,2,3,
           4,5,6,
           7,8,9]


p = 1
print("1. 1 Player (vas a jugar con la consola)")
print("2. 2 Players")
modo = input(">> ")

n = 0

while True:
    n+=1
    if ganar(tablero) or ganar(tablero) == "empate":
        break

    print ("""
                                  
                                         |      |       
                                      %s  |  %s   |  %s    
                                  -------|------|-------
                                      %s  |  %s   |  %s           
                                  -------|------|-------
                                      %s  |  %s   |  %s          
                                         |      |            
                                  
     """ % (tablero[0],tablero[1],tablero[2], tablero[3],tablero[4],tablero[5], tablero[6],tablero[7],tablero[8]))
    # turno de X
    if p == 1:
        pregunta = input("Turno de X. Ingrese su jugada: ")
        if validar(pregunta) and validar(tablero[int(pregunta)-1]):
            tablero[int(pregunta)-1] = "X"
            p = p*-1
        else:
            print("Jugada invalida. Intentelo nuevamente")
            input()
    # turno de O
    elif p == -1 and int(modo) == 2:
        pregunta = input("Turno de O. Ingrese su jugada: ")
        if validar(pregunta) and validar(tablero[int(pregunta)-1]):
            tablero[int(pregunta)-1] = "O"
            p = p*-1
        else:
            print("Jugada invalida. Intentelo nuevamente")
            input()
    # robot pensando
    elif p == -1 and int(modo) == 1:
        r = robot(tablero,n)
        print("Pensando...")
        time.sleep(randint(1,5))
        tablero[r-1] = "O"
        p = p*-1
    # si no, bota al usuario del programa
    else:
        print("Error")
        input()
        exit()



print("Fin del juego!")


print ("""
                                  
                                         |      |       
                                      %s  |  %s   |  %s    
                                  -------|------|-------
                                      %s  |  %s   |  %s           
                                  -------|------|-------
                                      %s  |  %s   |  %s          
                                         |      |       
     """ % (tablero[0],tablero[1],tablero[2], tablero[3],tablero[4],tablero[5], tablero[6],tablero[7],tablero[8]))
input("Fin del juego, enter para seguir")

if ganar(tablero) == "empate":
    i = 0
else:
    i = 1
while True:
    if i == 1 and p == -1:
        print("ha ganado el jugador uno!")
        time.sleep(0.3)
        i = i*-1
        exit()
    elif i == -1 and p == -1:
        print("ha ganado el jugador uno!")
        time.sleep(0.3)
        i = i*-1
        exit()
    if i == 1 and p == 1:
        print("ha ganado el jugador dos!")
        time.sleep(0.3)
        i = i*-1
        exit()
    elif i == -1 and p == 1:
        print("ha ganado el jugador dos!")
        time.sleep(0.3)
        i = i*-1
        exit()
    elif i == 0:
        print("ha sido un empate! presiona ENTER para continuar")
        input()
        break
    


        
