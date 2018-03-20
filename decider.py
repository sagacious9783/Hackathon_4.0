import sys
import subprocess
'''
11 - music auto          Mood_Speech
100 - music manual off   Speech
101  - music manual on	 Speech	 
01  - light auto		 IR
001 - light manual on 	 GPIO
000 - light manual off   GPIO 
subprocess.call("python3 getlink.py",shell=True)
'''



String choice = sys.argv[1]

if(choice[0]=='1'):
	if(choice[1]=="1"):
			
			subprocess.call("python3 automusic.py",shell=True)
if(choice[0]=='1'):
   if(choice[1]=="0"):
		if(choice[2]=="0"):	
			subprocess.call("python3 manualmusicoff.py",shell=True)
if(choice[0]=='1'):
   if(choice[1]=="0"):
		if(choice[2]=="1"):	
			subprocess.call("python3 manualmusicon.py",shell=True)		
if(choice[0]=='0'):
   if(choice[1]=="1"):
			subprocess.call("python3 autolight.py",shell=True)
if(choice[0]=='0'):
   if(choice[1]=="0"):
		if(choice[2]=="1"):	
			subprocess.call("python3 manuallighton.py",shell=True)
if(choice[0]=='0'):
   if(choice[1]=="0"):
		if(choice[2]=="0"):	
			subprocess.call("python3 manuallightoff.py",shell=True)												
