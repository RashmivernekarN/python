from turtle import back
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")

    elif hour>=12 and hour<18:
            speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")

    speak("I am jenny sir how may i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

if __name__=="__main__":
    wishMe()
while True:
    query = takecommand().lower()



    if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

    if 'open youTube' in query:
        speak('opening youtube')
        webbrowser.open("youtube.com")

    if 'open google' in query:
        webbrowser.open("google.com")

    if 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

    if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

    if 'play movies' in query:
            codePath = "F:\movies"
            os.startfile('play movies')

    if 'open gmail 1' in query:
            webbrowser.open("jamadaryusuf786@gmail.com")

    if 'open gmail 2' in query:
            webbrowser.open("jamadaryusuf91@gmail.com")

    if 'open whatsapp' in query:  
            speak('opening whatsapp')
            webbrowser.open("web.whatsapp.com")
        
    if 'exit' in query:
            speak('exiting')
            results = exit

    if 'go back' in query:
            speak('going back')
            results = back