'''from gtts import gTTS
import os
tts = gTTS('Hello this is google text to speech A P I',lang='en')
tts.save('c:\\Users\\kush\\dataset\\welcome.mp3')
os.system("c:\\Users\\kush\\dataset\\welcome.mp3")'''
import pyttsx3 as p
engine = p.init()
#setting different voice ids
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #voices[0] corresponds to female voice

engine.say("Hello! how are you doing?")
engine.runAndWait()
