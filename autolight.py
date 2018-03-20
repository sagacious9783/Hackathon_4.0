import RPi.GPIO as GPIO;
import time;
GPIO.cleanup();
GPIO.setmode(GPIO.BOARD);
GPIO.setup(11,GPIO.OUT);
GPIO.setup(40,GPIO.IN);
curr = 0
try:
    while 1:
    		curr=GPIO.input(40)
    		if curr == 1 :
    			GPIO.output(11,True);
    			time.sleep(5);
            else:
            	GPIO.output(11,False);
            
except KeyboardInterrupt:
    GPIO.cleanup();