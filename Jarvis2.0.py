from calendar import c
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyautogui
import wolframalpha
from takecommand import *

app=wolframalpha.Client('9YPHVR-5T6GRUVT4U')
#wishMe()
if __name__ == "__main__":
    
    y='yes'
    while y=='yes':
       
        query = takeCommand().lower()
        try:
            z=Translator()
            tr=z.detect(query) 
            if tr.lang=='hi':
                query=z.translate(query).text
            elif 'jarvis what is' in query:
                query = query.replace("jarvis what is", "")
            elif 'what is' in query:
                query = query.replace("what is", "")
            elif "jarvis" in query:
                query=query.replace("jarvis","")
            elif 'is' in query:
                query = query.replace("is", "")
            print(query)
        except Exception as e:
            print("....")

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'news' in query:
            news()
        elif 'translate' in query:
            speak('What should i translate')
            z=takeCommand()
            translate(z)
        elif 'about you' in query:
            speak("I am jarvis, A virtual A I . Created by Abhay Verma .")

        elif 'your name' in query:
            speak("I am jarvis, A virtual A I . Created by Abhay Verma .")


        elif 'who are you' in query:
            speak("I am jarvis, A virtual A I . Created by Abhay Verma .")

        elif 'hello' in query:
            speak("hello sir")

        elif 'hi' in query:
            speak("hi sir")

        elif 'thankyou' in query:
            speak("my pleasuer sir")

        elif 'thanks' in query:
            speak("welcome sir")

        elif 'good' in query:
            speak("thankyou sir")

        elif 'nice' in query:
            speak("Thanks sir")

        elif 'excellent' in query:
            speak("thank you")

        elif 'your name' in query:
            speak('my name is Jarvis')

        elif 'play song' in query:
            webbrowser.open('https://www.google.com/search?q'+query)
            speak("Playing song")

        elif 'play movie' in query:
            query=query.replace("play","")
            webbrowser.open('http://www.google.com/search?q'+query)
            speak("Playing Movie")

        elif 'search ' in query:
            query=query.replace("search","")
            webbrowser.open('http://www.google.com/search?q'+query)
            speak("searching")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'photoshop' in query:
            try:
                os.startfile('C:\\Program Files (x86)\Adobe\\Photoshop 7.0\\Photoshop.exe')
            except:
                speak("Photoshop is not installed")
                
                                
        elif 'open java' in query:
            try:
                os.startfile('C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.3\\bin\\idea64.exe')
            except:
                speak("Sorry sir cant rich java at this movement it is not installed in system")

        elif "open" and "word" in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.exe')

        elif "open" and "power point" in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.exe')

        elif "open" and "exel" in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.exe')

        elif "open" and "one note" in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.exe')

        elif "open code" in query:
            os.startfile("C:\\Users\\Abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        
        elif 'type' in query:
            query=query.replace('type','')
            pyautogui.typewrite(query)
        elif 'close' in query:
            hit("alt")
            hit("f4")
            rel("alt")
            rel("f4")
        elif "sleep" in query:
            speak("Closing System")
            speak("Closing driver")
            speak("clising connection")
            speak("closing connecting to internet")
            speak("getting offline")
            os.system('TASKKILL /F /IM Rainmeter.exe')
        elif 'by' in query:
            os.system('TASKKILL /F /IM Rainmeter.exe')
            break
        elif query == "none":
            print("Say something.......")
        else:
            try:
                z=app.query(query)
                print(next(z.results).text)
                speak(next(z.results).text)
            except:
                speak("Sorry sir cant rich the results")