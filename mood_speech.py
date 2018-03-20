from watson_developer_cloud import ToneAnalyzerV3
import json
tone_analyzer = ToneAnalyzerV3(
  username="7ff3d5a2-1e7c-4ef8-b92a-4efaf93664c9",
  password="hL0DPz7mVZ5q",
  version="2017-09-21"
)

with open(('tone.json')) as tone_json:
  tone = tone_analyzer.tone(tone_json.read())

#print(json.dumps(tone, indent=2))
print((tone["document_tone"]["tones"]))
