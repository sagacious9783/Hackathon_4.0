import user_speech
import speak
import RPi.GPIO as GPIO;
import time;
GPIO.cleanup();
GPIO.setmode(GPIO.BOARD);

opin=7
GPIO.setup(opin,GPIO.OUT);

text+=user_speech.rec()
GPIO.output(opin,True);
