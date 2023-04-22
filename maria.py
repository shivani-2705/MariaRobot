import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Maria Your Robot Sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output.

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold=400
        r.adjust_for_ambient_noise(source, duration=5)
        r.pause_threshold=0.8 # seconds of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)
        print("got it..")
    
        
    try:
        print("Recognising......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"

    return query

def sendEmail(to , content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
   wishMe()
   while True:
        query=takeCommand().lower()
        #logic Task 1
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace("wikipedia", " ")
            results= wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir ='C:\\Users\\Shivani singh\\Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is : {strTime}\n")

        elif 'open code ' in query:
            codepath="C:\\Users\\Shivani singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to ="singhshivani0331@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry Ma'am , I'm not able to sent")
