import speech_recognition as sr
import pyttsx3 as p
from EDITH---Personal-Automation-assistant-.Movie_reviews import *
from EDITH---Personal-Automation-assistant-.Youtube_Music import *
from EDITH---Personal-Automation-assistant-.Wikipedia_Search import *
from EDITH---Personal-Automation-assistant-.Recommendations import *

#enter your name
name = str(input("Enter your name:"))

#initial Conversation
r1 = sr.Recognizer()
engine = p.init()
engine.say('Hello         ' + name + '           I am Edith, your personal assistant')
engine.say('How are you today?')
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print('How are you?')
    audio = r1.listen(source)

    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError:
        print("")

#cue for giving instructions
engine.say('How can I help you ' + name)
engine.say('What would you like me to do?')
engine.runAndWait()
print('what do you want?')

#giving instructions
r2 = sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    audio = r2.listen(source)

    '''use commands as
       #i want information ..provide me informatio
       #can you music ...play music for me
       #recommend me some movies... i want good movie recommendations
       #what is the review for this movie ...moview review please
       etc.'''


    try:
        instruction = r2.recognize_google(audio)
        print(instruction)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError:
        print("")


r3 = sr.Recognizer()
if "information" in instruction:
    engine.say('Information about What?')
    engine.runAndWait()
    print('information about what?')

    with sr.Microphone()  as source:
        r3.adjust_for_ambient_noise(source)
        audio = r3.listen(source)

        try:
            information = r3.recognize_google(audio)
            print(information)
            bot = info()
            bot.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("")

r4 = sr.Recognizer()
if "music" in instruction:
    engine.say('which song do you want me to play?')
    engine.runAndWait()
    print('which song?')

    with sr.Microphone() as source:
        r4.adjust_for_ambient_noise(source)
        audio = r4.listen(source)

        try:
            song = r4.recognize_google(audio)
            print(song)
            bot = youtube_music()
            bot.play_music(song)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("")


r5 = sr.Recognizer()
if "review" in instruction:
    engine.say("which movie's reviews do you want?")
    engine.runAndWait()
    print('which movie?')

    with sr.Microphone() as source:
        r5.adjust_for_ambient_noise(source)
        audio = r5.listen(source)

        try:
            movie = r5.recognize_google(audio)
            print(movie)
            bot = Movie()
            bot.movie_reviews(movie)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("")


if "recommend" in instruction:
    engine.say('here are top 100 movies as per I M D B')
    engine.runAndWait()
    print('here are top 100 movies')
    bot = recom()
    bot.recom_info()










