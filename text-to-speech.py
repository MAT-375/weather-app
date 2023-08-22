# using gTTS
# from gtts import gTTS

# using pyttsx3

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices[0])
# print(voices[1])
engine.setProperty("voice", voices[0].id)
engine.setProperty("pitch", 0.8)  # Sets the pitch to 0.8
# engine.setProperty('voice', 'en-us')
engine.setProperty("rate", 150)
engine.say("hello there, this is text to speech")
engine.runAndWait()
engine.stop()
