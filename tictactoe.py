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
def robot(tablero):
    while True:
        r = randint(1,9)
        if validar(r) and validar(tablero[r-1]):
            return r

    
# tablero
tablero = [1,2,3,
           4,5,6,
           7,8,9]


p = 1
system("cls")
color = raw_input("Ingrese codigo de color: ")
system("color "+ color)
system("cls")
system("title _-Seleccion de modo de juego - TTT by Matyaz and Turk-_")
print """
  ______               __                        __  __   
 /      \             /  |                      /  |/  |  
/$$$$$$  |  ______   _$$ |_     ______         _$$ |$$ |_ 
$$ | _$$/  /      \ / $$   |   /      \       / $$  $$   |
$$ |/    | $$$$$$  |$$$$$$/   /$$$$$$  |      $$$$$$$$$$/ 
$$ |$$$$ | /    $$ |  $$ | __ $$ |  $$ |      / $$  $$   |
$$ \__$$ |/$$$$$$$ |  $$ |/  |$$ \__$$ |      $$$$$$$$$$/ 
$$    $$/ $$    $$ |  $$  $$/ $$    $$/         $$ |$$ |  
 $$$$$$/   $$$$$$$/    $$$$/   $$$$$$/          $$/ $$/                                      
        """
print "1. 1 Player (vas a jugar con la consola)"
print "2. 2 Players"
modo = input(">> ")



while True:
    if ganar(tablero) or ganar(tablero) == "empate":
        break
    system("cls")
    system("title _-Juego en progreso...-_")
    print """
       _                                                                                      
      | |                                                                                     
      | |_   _  ___  __ _  ___     ___ _ __    _ __  _ __ ___   __ _ _ __ ___  ___  ___       
  _   | | | | |/ _ \/ _` |/ _ \   / _ \ '_ \  | '_ \| '__/ _ \ / _` | '__/ _ \/ __|/ _ \      
 | |__| | |_| |  __/ (_| | (_) | |  __/ | | | | |_) | | | (_) | (_| | | |  __/\__ \ (_) | _ _ 
  \____/ \__,_|\___|\__, |\___/   \___|_| |_| | .__/|_|  \___/ \__, |_|  \___||___/\___(_|_|_)
                     __/ |                    | |               __/ |                         
                    |___/                     |_|              |___/
         """

    print """
                                  
                                         |      |       
                                      %s  |  %s   |  %s    
                                  -------|------|-------
                                      %s  |  %s   |  %s           
                                  -------|------|-------
                                      %s  |  %s   |  %s          
                                         |      |            
                                  
     """ % (tablero[0],tablero[1],tablero[2], tablero[3],tablero[4],tablero[5], tablero[6],tablero[7],tablero[8])
    # turno de X
    if p == 1:
        pregunta = raw_input("Turno de X. Ingrese su jugada: ")
        if validar(pregunta) and validar(tablero[int(pregunta)-1]):
            tablero[int(pregunta)-1] = "X"
            p = p*-1
        else:
            print "Jugada invalida. Intentelo nuevamente"
            raw_input()
    # turno de O
    elif p == -1 and modo == 2:
        pregunta = raw_input("Turno de O. Ingrese su jugada: ")
        if validar(pregunta) and validar(tablero[int(pregunta)-1]):
            tablero[int(pregunta)-1] = "O"
            p = p*-1
        else:
            print "Jugada invalida. Intentelo nuevamente"
            raw_input()
    # robot pensando
    elif p == -1 and modo == 1:
        r = robot(tablero)
        print "Vamo' a pensar..."
        time.sleep(randint(1,5))
        tablero[r-1] = "O"
        p = p*-1
    # si no, bota al usuario del programa
    else:
        print "Error"
        raw_input()
        exit()



system("cls")
# final del juego
print """
  ______ _             _      _     _                                  __  
 |  ____(_)           | |    | |   (_)                              _  \ \ 
 | |__   _ _ __     __| | ___| |    _ _   _  ___  __ _  ___        (_)  | |
 |  __| | | '_ \   / _` |/ _ \ |   | | | | |/ _ \/ _` |/ _ \            | |
 | |    | | | | | | (_| |  __/ |   | | |_| |  __/ (_| | (_) | _ _   _   | |
 |_|    |_|_| |_|  \__,_|\___|_|   | |\__,_|\___|\__, |\___(_|_|_) (_)  | |
                                  _/ |            __/ |                /_/ 
                                 |__/            |___/

"""


print """
                                  
                                         |      |       
                                      %s  |  %s   |  %s    
                                  -------|------|-------
                                      %s  |  %s   |  %s           
                                  -------|------|-------
                                      %s  |  %s   |  %s          
                                         |      |       
     """ % (tablero[0],tablero[1],tablero[2], tablero[3],tablero[4],tablero[5], tablero[6],tablero[7],tablero[8])
raw_input("Fin del juego, enter para seguir")

if ganar(tablero) == "empate":
    i = 0
else:
    i = 1
while True:
    system("cls")
    if i == 1 and p == -1:
        print """
             _____  __  __          ___       _
          * |  __ \/_ | \ \        / (_)     | | *
            | |__) || |  \ \  /\  / / _ _ __ | | 
          * |  ___/ | |   \ \/  \/ / | | '_ \| | * 
            | |     | |    \  /\  /  | | | | |_|
          * |_|     |_|     \/  \/   |_|_| |_(_) *
             *  *  *  *  *  *  *  *  *  *  *  *  * 

                                             
                                                               
             """
        time.sleep(0.3)
        i = i*-1
    elif i == -1 and p == -1:

        print """
            _____  __  __          ___       _
         * |  __ \/_ | \ \        / (_)     | | *
           | |__) || |  \ \  /\  / / _ _ __ | | 
         * |  ___/ | |   \ \/  \/ / | | '_ \| | * 
           | |     | |    \  /\  /  | | | | |_|
         * |_|     |_|     \/  \/   |_|_| |_(_) *
           *  *  *  *  *  *  *  *  *  *  *  *  *          
                                                               
             """
        time.sleep(0.3)
        i = i*-1
    if i == 1 and p == 1:
        print """
          _____ ___   __          ___       _  
       * |  __ \__ \  \ \        / (_)     | | *
         | |__) | ) |  \ \  /\  / / _ _ __ | | 
       * |  ___/ / /    \ \/  \/ / | | '_ \| | *
         | |    / /_     \  /\  /  | | | | |_| 
       * |_|   |____|     \/  \/   |_|_| |_(_) *
         *  *  *  *  *  *  *  *  *  *  *  *  *       

                                             
                                                               
             """
        time.sleep(0.3)
        i = i*-1
    elif i == -1 and p == 1:

        print """
          _____ ___   __          ___       _  
         |  __ \__ \  \ \        / (_)     | | 
       * | |__) | ) |  \ \  /\  / / _ _ __ | | *
         |  ___/ / /    \ \/  \/ / | | '_ \| | 
       * | |    / /_     \  /\  /  | | | | |_| *
         |_|   |____|     \/  \/   |_|_| |_(_) 
          *  *  *  *  *  *  *  *  *  *  *  *
    
                                                               
             """
        time.sleep(0.3)
        i = i*-1
    elif i == 0:
        system("title _-Empate, nadie gano-_")

        print """
  ______                       _       _            __
 |  ____|                     | |     | |      _   / /
 | |__   _ __ ___  _ __   __ _| |_ ___| |     (_) | | 
 |  __| | '_ ` _ \| '_ \ / _` | __/ _ \ |         | | 
 | |____| | | | | | |_) | (_| | ||  __/_|      _  | | 
 |______|_| |_| |_| .__/ \__,_|\__\___(_)     (_) | | 
                  | |                              \_\
        |_|

                                                
             """
        raw_input()
        system("cls")
        break
    


        
