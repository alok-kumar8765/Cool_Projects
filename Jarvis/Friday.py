import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    
    elif hour >=12 and hour < 18:
        speak('Good Afternoon')
    
    else:
        speak('Good Evening')
    speak('I am Friday, Updated Version of Jarvis, How may i help you')
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
        
    except Exception as e:
        # print (e)
        print('Say that again please..')
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.google.com',587)
    server.ehlo()
    server.starttls()
    server.login('lex.luther8765@gmail.com','alok.8765')
    server.sendmail('lex.luther8765@gmail.com',to,content)
    server.close()
        
if __name__ == "__main__":
    # speak('This is Lucifer Morning Star Laptop')
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #Logic for wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query:
            music_dir = 'E:\\Mood_Groover\\Hindi_MP3\\New\\Downloaded'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, The Time is {strTime}')
        
        elif 'open vscode' in query:
            code_path = "C:\\Users\\alokk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'email' in query:
            try:
                speak('What should i have to send?')
                content = takeCommand()
                to = 'alok.kumarlove20@gmail.com'
                sendEmail(to,content)
                speak('email  has been sent')
            
            except Exception as e:
                print(e)
                speak('Sorry This Email is not send Right now')
                
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            
        elif 'open browser' in query:
            browser_path = "E:\\Work_Station\\Cool_Python_Project\\My_Browser\\My_Browser.py"
            os.startfile(browser_path)
            
        elif 'quit' in query:
            exit()