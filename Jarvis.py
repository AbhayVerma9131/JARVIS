import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
from takecommand import *
import pyautogui
import wolframalpha
app=wolframalpha.Client('9YPHVR-5T6GRUVT4U')

wishMe()
if __name__ == "__main__":
    y='yes'

    while y=='yes':
        query = takeCommand().lower()
        if 'jarvis what is' in query:
            query = query.replace("jarvis what is", "")
        elif 'what is' in query:
            query = query.replace("what is", "")
        elif "jarvis" in query:
            query=query.replace("jarvis","")
        elif 'is' in query:
            query = query.replace("is", "")
        print(query)

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
        elif 'activate' in query:
            wishMe()
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

        elif 'play music' in query:
            music_dir = 'E:\\SONG\\New folder (2)'
            songs = os.listdir(music_dir)
            r=len(songs)
            s=random.randrange(1,r)
            os.startfile(os.path.join(music_dir, songs[s]))

        elif 'play movie' in query:
            speak("Which movies should i play Bollywood or Hollywood")
            q2=takeCommand().lower()
            if 'bollywood' in q2:
                movie_dir ='G:\\movies\\bollywood'
                mov=os.listdir(movie_dir)
                r=len(mov)
                m=random.randrange(1,r)
                os.startfile(os.path.join(movie_dir,mov[m]))

            elif 'hollywood' in q2:
                movie_dir= 'G:\\movies\\Hollywood'
                mov=os.listdir(movie_dir)
                r=len(mov)
                m=random.randrange(1,r)
                os.startfile(os.path.join(movie_dir, mov[m]))

            else:
                speak("Sorry sir i cannot find movie")

        elif 'search ' in query:
            webbrowser.open('http://www.google.com/search?q'+query)
            speak("searching")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'photoshop' in query:
            speak("which photoshop should you want")
            speak("Adob photoshop")
            speak("or CS6 photoshop")
            q2=takeCommand().lower()
            if 'adobe photoshop' in q2:
                os.startfile('C:\\Program Files (x86)\Adobe\\Photoshop 7.0\\Photoshop.exe')
                break
            elif 'cs6 photoshop' in q2:
                os.startfile('C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe')
                break
            else:
                speak("sorry sir i can't find photoshop")
                break

        elif 'open java' in query:
            try:
                os.startfile('C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.3\\bin\\idea64.exe')
            except:
                speak("Sorry sir cant rich java at this movement")

        elif "open" and "word" in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\WINWORD.exe')

        elif "open" and "power point" in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\PPTVIEW.exe')

        elif "open" and "exel" in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\EXCEL.exe')

        elif "open" and "one note" in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\ONENOTE.exe')

        elif"open photo brush" in query:
            os.startfile('C:\\Program Files (x86)\\PhotoBrush\\PhotoBrush.exe')

        elif "open adobe" and "reader" in query:
            os.startfile("C:\\Program Files (x86)\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe")

        elif "open fire fox" in query:
            os.startfile("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

        elif "open typing master" in query:
            os.startfile("C:\\Program Files (x86)\\TypingMaster\\tmaster.exe")

        elif "open game" in query:
            speak("which game should i open")
            speak("Vice city")
            print("Vice city")
            speak("mario")
            print("mario")
            speak("Project igi")
            print("Project IGI")
            r=takeCommand().lower()
            if "vice city " in query:
                os.startfile("C:\\Users\\choure computer\\Desktop\\gta-vc.exe")
            elif "mario" in query:
                os.startfile("C:\\Program Files (x86)\\softendo.com\\Super Mario Forever v7.02\\MarioForever 7.02 Beta.exe")
            elif "project igi" in query:
                os.startfile("C:\\Project IGI\\PC\\IGI.exe")

        elif 'open python' in query:
            os.startfile('C:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\bin\\pycharm64.exe')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open sql' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 5.1\\MySQL Command Line Client.ink')
        elif 'open google' in query:
            os.startfile("C:\\Program Files (x86)\Google\\Chrome\\Application\\chrome.exe")

        elif 'email' in query:
            try:
                speak("To whome do i deliver message")
                r=takeCommand().lower()
                speak("What should i say")
                content=takeCommand()
                sendEmail(r,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry message hasn't sended")
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
        else:
            try:
                z=app.query(query)
                print(next(z.results).text)
                speak(next(z.results).text)
            except:
                speak("Sorry sir cant rich the results")