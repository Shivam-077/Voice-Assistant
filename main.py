import subprocess
import pyaudio
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
from urllib.request import urlopen
import speech_recognition as sr
from twilio.rest import Client
from bs4 import BeautifulSoup
from ecapture import ecapture as ec
#from distutils.version import LooseVersion

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am your Assistant, Jarvis")
    speak("How can I help you, Sir")

def takeCommand():
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
        print("Unable to Recognize your voice.")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

def main():
    clear = lambda: os.system('cls')
    clear()
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\shiva\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\\Users\\shiva\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send it to?")
                to = input("Enter the recipient's email: ")
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Jarvis")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shivam.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you're human.")

        elif "why you came to the world" in query:
            speak("Thanks to Shivam. Further, it's a secret")

        elif 'What is love' in query:
            speak("It is the 7th sense that destroys all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Shivam")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=YOUR_API_KEY')
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top news from the Times of India')
                print('=============== TIMES OF INDIA ============' + '\n')
                for item in data['articles']:
                    print(f"{i}. {item['title']}\n{item['description']}\n")
                    speak(f"{i}. {item['title']}\n")
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time you want to stop Jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(f"User asked to locate {location}")
            webbrowser.open(f"https://www.google.com/maps/place/{location}")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the applications are closed before signing out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should I write, sir")
            note = takeCommand()
            with open('jarvis.txt', 'w') as file:
                speak("Sir, should I include date and time?")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(f"{strTime} :- {note}")
                else:
                    file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            with open("jarvis.txt", "r") as file:
                content = file.read()
                print(content)
                speak(content)

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in r.iter_content(chunk_size=2391975):
                    if ch:
                        Pypdf.write(ch)

        elif "jarvis" in query:
            wishMe()

        elif "send message" in query:
            # You need to create an account on Twilio to get these credentials
            account_sid = 'YOUR_ACCOUNT_SID'
            auth_token = 'YOUR_AUTH_TOKEN'
            client = Client(account_sid, auth_token)
            speak("What should I say?")
            message_body = takeCommand()
            message = client.messages.create(
                body=message_body,
                from_='YOUR_TWILIO_NUMBER',
                to='RECEIVER_NUMBER'
            )
            print(message.sid)

        elif "good morning" in query:
            speak("A warm good morning to you. How are you Mister")

        elif "good afternoon" in query:
            speak("A warm good afternoon to you. How are you Mister")

        elif "good evening" in query:
            speak("A warm good evening to you. How are you Mister")

        elif "good night" in query:
            speak("Good night Sir! Have a sweet dreams")

        elif "will you be my girlfriend" in query:
            speak("I'm not sure about that, maybe you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand. I don't have feelings.")

        elif "i am sorry" in query:
            speak("It's okay, I am just a machine.")

        elif "what is the weather" in query:
            api_key = "YOUR_API_KEY"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(f" Temperature (in kelvin unit) = {current_temperature}"
                      f"\n atmospheric pressure (in hPa unit) = {current_pressure}"
                      f"\n humidity (in percentage) = {current_humidity}"
                      f"\n description = {weather_description}")
                speak(f" Temperature (in kelvin unit) = {current_temperature}"
                      f" atmospheric pressure (in hPa unit) = {current_pressure}"
                      f" humidity (in percentage) = {current_humidity}"
                      f" description = {weather_description}")
            else:
                speak(" City Not Found ")

if __name__ == '__main__':
    main()
