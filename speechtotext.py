import speech_recognition as sr
import pyttsx3 as p

r=sr.Recognizer()
engine=p.init()

engine.say("hello! How are you doing?")
engine.runAndWait()
with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError:
        print("")

    engine.say("What do you want me to do?")
    engine.runAndWait()

    text1 = r.listen(source)

    try:
        recognized_text1 = r.recognize_google(text1)
        print(recognized_text1)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError:
        print("")


