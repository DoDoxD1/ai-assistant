import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import datetime
import subprocess
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

gender = 'male'

if gender == 'male':
    addresser = ' Sir '
    ai = ' Friday '
    engine.setProperty('voice',voices[0].id)
else:
    addresser = ' Mam '
    ai = ' Emily '
    engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Error Occured")
        return "none"

    return query

def resolveQuery(query):
    # if query = 'hello':
    #     speak('Hello'+addresser)
    if 'wikipedia' in query:
        print('\nSearching Wikipedia...')
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=2)
        print('According to wikipedia...')
        speak('According to wikipedia...')
        speak(results)
    elif 'youtube' in query:
        print("opening youtube in chrome...")
        speak("opening youtube in chrome...")
        subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','youtube.com'])
    # elif 'bio on bb' in query or 'bio class' in query or 'bio in bb':
    #     print("opening bio class on bb...")
    #     speak("opening bio class on bb...")
    elif 'class' in query:
        print("Joining Class...")
        os.system("C:\\Users\\aunuj\\OneDrive\\Desktop\\class-check.bat")
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%I %M %p")
        if time[0] == '0':
            time = time[1:]
            if time[1] == '0':
                time = time[0]+time[2:]
        if time[2] == '0':
            time = time[:2]+time[3:]
        speak('The Time is'+time)
    else:
        print("I can't get it\n")
        speak("I can't get it")

def wishes(hour):
    greeting = ''
    welcome = 'How May I Help You'
    intro = 'I am'+ai

    if hour>=4 and hour <12:
       greeting = 'Good Morning'+addresser
    elif hour>=12 and hour<16:
        greeting = 'Good Afternoon'+addresser
    elif hour>=16 and hour<24:
        greeting = 'Good evening'+addresser
    else:
        greeting = 'Good Night'+addresser+'you may sleep now!'
    
    print('\n\n'+greeting)
    speak(greeting)
    print(intro+'\n')
    speak(intro)
    print(welcome+'\n')
    speak(welcome)


if __name__ == "__main__":
    hour = int(datetime.datetime.now().hour)
    wishes(hour)
    query = takeInput().lower()
    resolveQuery(query)