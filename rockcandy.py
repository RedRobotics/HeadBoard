# A simple example program to display the keypresses on a Rockcandy PS3 controller. 
# Author: Neil Lambeth. neil@redrobotics.o.uk @NeilRedRobotics

from evdev import InputDevice, ecodes
import redboard

dev = InputDevice('/dev/input/event0')

L_Fwd = 0
R_Fwd = 0
print 'Start'

print(dev)


for event in dev.read_loop():
    #print(event)  # Uncomment to show all key data
    
    
    if event.type == ecodes.EV_KEY:   
        print(event.code)  # Uncomment to show each keycode
        if event.value == 1:  # Key down
            if event.code == 307:
                print '3'
            elif event.code == 305:
                print '5'
            elif event.code == 304:
                print '4'
            elif event.code == 306:
                print '6'
            elif event.code == 305:
                print '5'
            elif event.code == 309:
                print 'R1'   
            elif event.code == 311:
                print 'R2'     
            elif event.code == 308:
                print 'L1'
            elif event.code == 310:
                print 'L2'
            elif event.code == 312:
                print 'Select'
            elif event.code == 313:
                print 'Start'
            elif event.code == 316:
                print 'Home'


    if event.type == ecodes.EV_ABS:

        if event.code == 1:  # Left analogue Vertical stick

            LY = event.value
            print "Left Y = ",LY


        elif event.code == 0:  # Left analogue Horizontal stick
            
            LX = event.value
            print "Left X = ",LX



        elif event.code == 5:  # Right analogue Vertical stick	
            RY = event.value	
            print "Right Y = ",RY

        elif event.code == 2:  # Right analogue Horizontal stick

            RX = event.value
            print "Right X = ",RX    
          


        if event.code == 16:  # Dpad
            if event.value == -1:
                print 'Dpad LEFT'            
            if event.value == 1: 
                print 'Dpad RIGHT'

        if event.code == 17:
            if event.value == -1:
                print 'Dpad UP'            
            if event.value == 1: 
                print 'Dpad DOWN'






   
