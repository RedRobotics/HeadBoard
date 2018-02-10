import curses
import time
import redboard
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
print("T = Turbo")

time.sleep(3)


def main(stdscr):
    motor1 = 0
    motor2 = 0
    turbo = False
    
    keypress = 0
    up = 0
    stop = 0
    while True:
        
        curses.halfdelay(1)
        c = stdscr.getch()
        #print(c)  # Uncomment to show keypresses
        #print("\r")
        
        if c == ord('w'):
            keypress = 1
            print("Forward")
            print("\r")
            stop = 0
            #redboard.M2 (100)
            #redboard.M1 (100)
            motor1 = 100
            motor2 = 100

        elif c == ord('s'):
            keypress = 1
            stop = 0
            print("Backwards")
            print("\r")
            #redboard.M2 (-100)
            #redboard.M1 (-100)
            motor1 = -100
            motor2 = -100

        elif c == ord('a'):
            keypress = 1
            stop = 0
            print("Left")
            print("\r")
            #redboard.M2 (-100)
            #redboard.M1 (100)
            motor1 = 100
            motor2 = -100
			
        elif c == ord('d'):
            keypress = 1
            stop = 0
            print("Right")
            print("\r")
            #redboard.M2 (100)
            #redboard.M1 (-100)
            motor1 = -100
            motor2 = 100
            
            
        elif c == 32:  # Spacebar
            keypress = 1
            stop = 0
            print("Stop")
            print("\r")
            #redboard.M2 (0)
            #redboard.M1 (0)    
            motor1 = 0
            motor2 = 0                

        elif c == ord('t') and turbo == False :
            keypress = 1
            stop = 0
            turbo = True
            print ("Turbo on")
            print("\r")

        elif c == ord('t') and turbo == True:
            keypress = 1
            stop = 0
            turbo = False
            print ("Turbo off")
            print("\r")

        if c == -1:
            stop += 1
            #print(stop)
            #print("\r")
          

        if keypress == 1 and stop > 6:
            keypress = 0
            stop = 0
            print("Stop----------------------------------------")
            print("\r")
            #redboard.M2 (0)
            #redboard.M1 (0)
            motor1 = 0
            motor2 = 0


        if turbo == True:
            redboard.M1(motor1)
            redboard.M2(motor2)

        elif turbo == False:
            redboard.M1(motor1 / 2)  # divide motor speed by 2 
            redboard.M2(motor2 / 2)  # divide motor speed by 2
          
curses.wrapper(main)    
            
        
