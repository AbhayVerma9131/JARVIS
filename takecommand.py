import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import smtplib
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyautogui
from googletrans import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def news():
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    page = Client.read()
    Client.close()
    soup_page = soup(page, "html.parser")
    news_list = soup_page.findAll("item")
    for news in news_list:
        speak(news.title.text)


def wishMe():
    os.startfile('Rainmeter\\Rainmeter.exe')
    speak("Starting System")
    speak("Installing driver")
    speak("Creating secure connection")
    speak("connecting to internet")
    speak("Going online")
    speak("System startd working")
    speak("Driver has been installed")
    speak("Connection established")
    speak("Internet Acess")
    speak("Now i am online")
    return


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhay45ver@gmail.com', '@bhay9131')
    if to == 'abhilasha mam':
        too = 'marks.kvb@gmail.com'
    elif to == 'papa':
        too = 'prashantver24@gmail.com'
    server.sendmail('abhay45ver@gmail.com', too, content)
    server.close()


def translate(z):
    tr = Translator()
    speak("To which language should i Translate")
    r = takeCommand().lower()
    print(r)
    if 'hindi' in r:
        to_l = 'hi'
    elif 'english' in r:
        to_l = 'en'
    elif 'german' in r:
        to_l = 'de'
    elif 'gujarati' in r:
        to_l = 'gu'
    tra = tr.translate(z, dest=to_l)
    tlt = tra.text
    print(tlt)
    speak(tlt)


def hit(key):
    pyautogui.keyDown(key)
    return


def rel(key):
    pyautogui.keyUp(key)
    return
