import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import os 
import sys
import pyjokes
import pyautogui
import instaloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JA



engine = pyttsx3.init('sapi5')                  ##sapi5 = for taking voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
 

def speak(audio):                               ## pronouncing audio
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int (datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak (f"Good morning! its {tt}")
    elif hour>=12 and hour<18:
        speak (f"Good afternoon ! its {tt}" )
    else:
        speak(f"Good evenning! its {tt} ")


    speak ("I am AR-BoT . please tell me how can i help you? ")    

def takecmd():                                  ## It takes input from phone / desktop mic 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Getting Voice .........")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5 , phrase_time_limit= 15)
    try:
        print("understanding........")
        speak("please wait a minute")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print (e)
        print ("say that again please...")
        return "None"
    return query

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b255af5000174a5b81c6d910329ae3c8'
    mp = requests.get(main_url).json()
    articles = mp["articles"]
    head=[]
    day = ["first ", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len (day)):
        speak(f"today's {day[i]} news is: {head[i]}" )

if __name__ == "__main__":
    speak(" hello sir !")
    wishme()
    while True:
        query = takecmd().lower()
        
        if 'wikipedia' in query.lower():
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences = 2)
            speak(results)

        elif 'open youtube' in query.lower():
            speak("opening youtube")
            webbrowser.open("youtube.com")

    
        elif 'open google'  in query.lower():
            speak("opening google")
            speak("What should i search on google")
            print("what should i Search on google")
            ca = takecmd().lower()
            webbrowser.open(f"{ca}")
        
    
        elif 'play music' in query.lower():
            speak("playing music")
            path="D:\\MUSIC"  
            music_dir = os.listdir(path)
            print (music_dir)
            os.startfile(os.path.join(path,music_dir[0]))
        
        elif 'play movie' in query.lower():
            speak("playing movies")
            path="D:\\movies"  
            movie = os.listdir(path)
            print (movie)
            os.startfile(os.path.join(path,movie[0]))
    
        elif 'geeks for geeks' in query.lower():
            speak("opening geeksforgeeks")
            webbrowser.open("www.geeksforgeeks.com")
    
        elif 'tell me a joke' in query.lower():
            speak("the joke is ")
            joke = pyjokes.get_joke()
            print (joke)
            speak(joke)
           

        elif 'tell me latest news' in query.lower():            ### ONLY BUSINESS NEWS 
            speak ("Please wait a second we are searching latest news for you")
            news()


        elif 'shutdown the laptop' in query.lower():
            speak("shutting down the PC")
            os.system("shutdown /s /t 5")
    
        elif 'restart the laptop' in query.lower():
            speak("restarting the PC")
            os.system("restart /s /t 5")

    
        elif 'take screenshot' in query.lower():
            speak("ok, please tell me the name for this screenshot file")
            name = takecmd().lower()
            speak("Please Hold the screen for few seconds, to take a screenshot")

            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("OK dear we take the snapshot and also save in main folder and now i m ready to another task!!")

        elif 'check instagram profile' in query.lower():
            speak("Please enter the correct username:")
            name = input("Enter the user name :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("Here it's the profile of user you enter")
            speak ("Would you like to download the profile picture of this user account")
            condition = takecmd().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_picture_only=True, )
                speak("OK done sir , profile picture has been saved in the main folder . NOw i am ready to another task")
            else:
                pass
        
        elif 'search temperature' in query.lower():
            speak ("which city you want to search tempearture")
            city = input(f" Name of place :")
            search = (f"Weather in {city}")
            url = (f"https://www.google.com/search?&q={search}")
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {city} is {temp}")
            print(f"{search} now is {temp} :")


        elif 'set alarm' in query.lower():
            speak("Enter the time :")
            time = input ("Enter the time:")
            while True:
                at = datetime.datetime.now()
                now = at.strftime("%I:%M %p")

                if now == time:
                    speak("Time to wakeup sir")
                
                elif now >time:
                    break


        elif 'no thanks' in query.lower() or 'ok thank you' in query.lower():
            speak("Thank you for using me ! have a good day  sir !!")

            sys.exit()

        else :  
            speak ("sorry ! i can't process it...")

