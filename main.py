# Developed by Sidharth P.L
# ©Frissco Creative Labs and Cyber Zypher and Sidharth P.L
# This code is fully open-source to be used

from ast import operator
import re
import googlescrap as googleScrap
from winsound import PlaySound
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import pywhatkit
import pyjokes
import pywikihow
from bs4 import BeautifulSoup
import requests
from pygame import mixer
import speedtest
import winsound
import os
import smtplib
import platform

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("How may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output

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


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "proton" in query:
            speak("yeah tell me")
            while True:

                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'internet speed' in query:
                    st = speedtest.Speedtest()
                    dl = st.download()
                    up = st.upload()
                    print('Please wait..')
                    speak(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed.')
                elif 'proton' in query:
                    speak('yes, tell me')
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                elif 'say hello to' in query:
                    wish = query.replace('say hello to', '')
                    speak('hello' + wish)
                elif 'weather' in query:
                    search = 'temprature in chennai'
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "where am i" in query:
                    speak("cheking current location with ip address")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        country = geo_data['country']
                        speak(f"Sir you are in {city} city of {country} country")
                    except Exception as e:
                        speak("Sorry sid, an error occured while processing")
                        pass

                elif 'tell me your internet protocol' in query:
                    try:
                        ipAddr = requests.get('https://api.ipify.org').text
                        speak('my IP address is' + ipAddr)
                    except Exception as e:
                        speak('Sorry sid, I cannot do that now')
                        pass

                elif 'who are you' in query:
                    speak('I am Proton AI, The Voice assistant made from Python and I can do all the basic stuffs that a normal AI can do.')
                elif 'version' in query:
                    speak('1.0')
                elif 'system info' in query:
                    speak('Computer network name' + {platform.mode()})
                elif 'who is' in query or 'what is' in query:
                    person = query.replace('who is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    speak(info)
                elif 'what can you do' in query:
                    speak(
                        'I am a personal AI assistant made for household purposes. I can search anything for you, I can play music and tell jokes and I can do whatever a normal AI can do')
                elif 'who created you' in query:
                    speak('I was created by Sidharth PL')
                elif 'joke' in query:
                    speak((pyjokes.get_joke()))
                elif 'repeat' in query:
                    repeat = query.replace('repeat', '')
                    speak(repeat)
                elif 'activate online search' in query:
                    speak("Taffy search activated")
                    while True:
                        speak("what do you want me to search")
                        how = takeCommand()
                        try:
                            if 'close online search' in how:
                                speak('Taffy search deactivated')
                                break
                            else:
                                max_results = 1
                                how_to = pywikihow.search_wikihow(how, max_results)
                                assert len(how_to) == 1
                                how_to[0].print()
                                speak(how_to[0].summary)
                        except Exception as e:
                            speak("sorry I am unable to server you the results")
                elif 'remember that' in query:
                        rememberMessage = query.replace('remember that', '')
                        rememberMessage = query.replace('louis', '')
                        speak('you told me to remember that' + rememberMessage)
                        remember = open('Remember.txt', 'a')
                        remember.write(rememberMessage)
                        remember.close()
                elif 'what are the pending' in query:
                        remember = open('Remember.txt', 'r')
                        speak('you told me to remember that' + remember.read())
                elif 'i love you' in query:
                    speak('me too! as a friend.')
                elif 'i hate you' in query or 'you suck' in query:
                    speak('I am sorry to disappoint you')
                elif 'hip hip' in query:
                    speak('hooray!')
                elif 'unlock 17a' in query:
                    speak('unlocking 17 A')
                    print('*#!!unlocking 17 A!!#*')
                elif 'Something about you' in query:
                    speak('I am Proton, I am a limited artificial intelligent bot made using Python and Python libraries')
                elif 'thank you' in query:
                    speak("you're welcome")
                    break
                elif 'shutdown' in query:
                    speak("Proton shutting down")
                    exit()
