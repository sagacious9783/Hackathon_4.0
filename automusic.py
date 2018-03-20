import speak
import user_speech



from watson_developer_cloud import ToneAnalyzerV3
import json
tone_analyzer = ToneAnalyzerV3(
  username="7ff3d5a2-1e7c-4ef8-b92a-4efaf93664c9",
  password="hL0DPz7mVZ5q",
  version="2017-09-21"
)

text=""
print("Device asks : How was your day ?")
speak.sp('"How was your day ?"')
text+=user_speech.rec()
print("Device asks : What all did you do?")
speak.sp('"What all did you do?"')
text+=user_speech.rec()
'''
text="the day was  . I am very tired . I am  exhausted."
'''

text=' "text" : '+'"'+text+'"'
f=open("tone.json","w")
f.write('{')
f.write(text)
f.write("}")
f.close()

with open(('tone.json')) as tone_json:
  tone = tone_analyzer.tone(tone_json.read())


#print(json.dumps(tone, indent=2))
maxw=0
temp_tone=""
for tones in (tone["document_tone"]["tones"])):
	if((tones["tone_id"]=="sadness" or tones["tone_id"]=="anger" or tones["tone_id"]=="joy" or tones["tone_id"]=="fear") and tones["score"]>maxw):
		temp_tone=tones["tone_id"]

def play(type_song):
	
	for i in range(1,5):
		st="aplay "+ type_song +i + ".mp3"
		subprocess.call(st,shell=True)

if(temp_tone="sadness" or temp_tone="fear"):
	play("m") #motivational
if(temp_tone="joy"):
	play("e")	 #excited
if(temp_tone="anger"):
	play("s")   #soothing
	
		


