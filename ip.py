from neopixels import *
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
#print(s.getsockname()[0])
s.close()

#ip = "10.110.0.030"  # Test IP address

print ("IP address:",ip)

dot = ip.rindex(".")  # look for last dot
#print (dot)

l = len(ip)-1  # Get the length of the string
#print(l)

lastNum = l-dot  # Find the number of digits in the last part of the address
#print ("Last number = ",lastNum)

if lastNum == 1:
    ip_red = 0
    ip_green = 0
    ip_blue = int(ip[l])
    
elif lastNum == 2:
    ip_red = 0
    ip_green = int(ip[l-1])
    ip_blue = int(ip[l])
    
elif lastNum == 3:
    ip_red = int(ip[l-2])
    ip_green = int(ip[l-1])
    ip_blue = int(ip[l])     
    
    
else:    
    ip_red = 0
    ip_green = 0
    ip_blue = 0
    print ("No IP address found!")
    white(127)  # Neopixel white half brightness
    time.sleep(1)
    clear()  


#print (ip_red, ip_green, ip_blue)
        
#Flash neopixel red
for i in range(0,ip_red):
    red()
    time.sleep(0.3)
    clear() 
    time.sleep(0.3) 

#Flash neopixel green
time.sleep(0.5) 
for i in range(0,ip_green):
    green()
    time.sleep(0.3)
    clear() 
    time.sleep(0.3) 

#Flash neopixel blue
time.sleep(0.5) 
for i in range(0,ip_blue):
    blue()
    time.sleep(0.3)
    clear() 
    time.sleep(0.3) 





