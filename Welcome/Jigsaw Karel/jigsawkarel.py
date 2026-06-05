from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   

def pick_up_piece():
    move()          
    move()         
    pick_beeper()

def place_piece():
    turn_left()     
    move()          
    turn_right()   
    move()          
    turn_left()
    move()
    put_beeper()

def return_home():
     turn_right()
     turn_right()
     move()
     move()
     turn_right()
     move()  
     move()
     move()
     turn_left()
     turn_left()
     
    
             

def main():
    pick_up_piece()
    place_piece()
    return_home()

if __name__ == '__main__':
    main()
