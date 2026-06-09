from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def turn_around():
    turn_left()
    turn_left()

def construir_columna():
    turn_left()              
    put_beeper()             
    for i in range(4):
        move()
        put_beeper()
    turn_around()            
    for i in range(4):       
        move()
    turn_left()              

def avanzar_cuatro():
    for i in range(4):
        move()

def main():
    construir_columna()
    avanzar_cuatro()
    construir_columna()
    avanzar_cuatro()
    construir_columna()
    avanzar_cuatro()
    construir_columna()

if __name__ == '__main__':
    main()
