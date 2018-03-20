import user_speech

import speak

speak.sp('"Which type of music should I play ? motivational , excited or soothing"')
text=""
text+=user_speech.rec()

words = s.split(" ")
for(w in words):
	if(w=="motivational"):
		st="aplay "+ "m" +i + ".mp3"
		subprocess.call(st,shell=True)
	if(w=="soothing"):
		st="aplay "+ "s" +i + ".mp3"
		subprocess.call(st,shell=True)
	if(w=="excited"):
		st="aplay "+ "e" +i + ".mp3"
		subprocess.call(st,shell=True)
