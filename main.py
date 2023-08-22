import requests
import json
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "en-uk")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("pitch", 0.8)
engine.setProperty("rate", 150)


city = input("Enter the name of the city\n=>")

# register and copy the api key from https://weatherapi.com or use any other api you like
url = f"http://api.weatherapi.com/v1/current.json?key=b566193d76a040c183892910232208&q={city}"


r = requests.get(url)

wdic = json.loads(r.text)
temp_c = wdic["current"]["temp_c"]
w_con = wdic["current"]["condition"]["text"]

weather_report = f"The temprature in {city} is {temp_c} and it is currently {w_con}"

# command = f''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{weather_report}');" '''
# os.system(command)


engine.say(weather_report)
engine.runAndWait()
engine.stop()
