import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

emailDict = {
  "jishnu": "psjishnu13@gmail.com",
  "irfan": "irfanshereef95@gmail.com",
  "arihant": "arihant10496@gmail.com",
  "hello": "abhirampai1999@gmail.com"
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and  hour < 12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Eveneing!")

speak("I am Jarvis sir. please tell me how may i help you?")

def takeCommand():
    #it takes microphone input from the user and return the string output
   
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 
        #to take gap of one second while speaking otherwise it will consider it is complete speaking
        audio = r.listen(source)
        
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query} \n")


        except Exception:
            print("Say that again please......")
            return("None")
        return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arihant2310@gmail.com', 'your-password-here')
    server.sendmail('arihant2310@gmail.com', to, content)
    server.close()





if __name__ == "__main__":
    WishMe()
if 1:
        query= takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia........')
            query =  query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
       
        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
        
        elif 'open gmail' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("gmail.com")
       
        elif 'open stack overflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= 'E:\\songs'
            songs= os.listdir(music_dir)
            number_files= len(songs)
            rand_no = random.randint(0,number_files-1)
            os.startfile(os.path.join(music_dir, songs[rand_no]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}\n")
        elif 'my birthday' in query:
            speak("Hi Sona, your birthday is on 12th february 2009")
        elif 'open atom' in query:
            codePath = "C:\\Users\\ARIHANT\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)
        elif 'open sublime' in query:
            sublimePath= "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimePath)
        elif 'send email' in query:
            try:
                speak("to whom should i send?")
                toWhom= takeCommand().lower()
                print(toWhom)
                to= emailDict[toWhom]
                print(to)
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to, content);
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my boss, email has not been sent")
        elif 'exit' in query:
            print("Good Bye! Sir")
            speak("Good Bye! sir")
            exit()

        
        
        
        


