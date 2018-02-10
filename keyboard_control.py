import curses
import time
from sideboard import *
stdscr = curses.initscr()
curses.noecho()
#curses.cbreak()
stdscr.keypad(True)


print("\r")
print("W = Forwards\r")
print("S = Backwards\r")
print("A = Left\r")
print("D = Right\r")
print("Spacebar = Stop\r")

time.sleep(3)


def main(stdscr):
    
    keypress = 0
    up = 0
    stop = 0
    while True:
        
        curses.halfdelay(1)
        c = stdscr.getch()
        #print(c)
        #print("\r")
        
        if c == ord('w'):
            keypress = 1
            print("Forward")
            print("\r")
            stop = 0
            M2 (100)
            M1 (100)
            

        elif c == ord('s'):
            keypress = 1
            stop = 0
            print("Backwards")
            print("\r")
            M2 (-100)
            M1 (-100)

        elif c == ord('a'):
            keypress = 1
            stop = 0
            print("Left")
            print("\r")
            M2 (-100)
            M1 (100)

        elif c == ord('d'):
            keypress = 1
            stop = 0
            print("Right")
            print("\r")
            M2 (100)
            M1 (-100)
            
        elif c == 32:  # Spacebar
            keypress = 1
            stop = 0
            print("Stop")
            print("\r")
            M2 (0)
            M1 (0)    
                            

        if c == -1:
            stop += 1
            #print(stop)
            #print("\r")
            #up = 0

        if keypress == 1 and stop > 6:
            keypress = 0
            stop = 0
            print("Stop----------------------------------------")
            print("\r")
            M2 (0)
            M1 (0)
          
curses.wrapper(main)    
            
        
