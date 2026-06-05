#incomplete and i have to fix errors from  return home
from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_beeper():
    turn_right()    # mira al sur
    move()          # baja 1
    turn_left()     # mira al este
    move()          # derecha 1
    move()          # sale por la puerta
    move()          # llega al beeper

def return_home():
    turn_left()     # mira al norte
    turn_left()     # mira al oeste
    move()          # entra por la puerta
    move() 
    turn_left()
    turn_right() 
    move() 
    turn_right()   # mira al este
   

def main():
    go_to_beeper()
    pick_beeper()
    return_home()

if __name__ == '__main__':
    main()
