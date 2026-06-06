from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to
place 20 beepers, then 26 beepers, and end facing East to
the right of the 26 beepers.
"""

def main():
    for i in range(20):
        put_beeper()
    move()  
    
    for i in range(26):
        put_beeper()
    move()  

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()
