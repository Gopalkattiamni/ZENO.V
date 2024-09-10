import os
import smtplib
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
import time
import pyjokes
import psutil
import speedtest
import bs4
from email.message import EmailMessage
import pyttsx3
import numpy as np
import pyautogui as p

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 175)

# Retrieve email credentials from environment variables
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=7, phrase_time_limit=10)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("please tell me your request")

# To send email
def send_email(to, subject, body):
    msg = EmailMessage()
    msg['From'] = email_address
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def Taskexecution():
    p.press('esc')
    speak("verification successful")
    speak("welcome back thick boy")
    wish()
    while True:
        if 1:
            query = takecommand().lower()

            # Logic building for tasks

            if "yourself" in query or "what can u do" in query:
                speak("i am zeno.v, a personal ai assistant, i am designed to make ur work easy by performing some simple tasks in this device")
            elif "how are you" in query:
                speak("i will always be fine to hear your commands")
            elif "play music" in query:
                music_dir = "C:\songs music"
                songs = os.listdir(music_dir)
                # rd=random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
            elif "wikipedia" in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                print(results)
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "send message" in query:
                speak("to whom you want me to send a message")
                cm1 = takecommand().lower()
                pywhatkit.sendwhatmsg("+1234567890", "Hi", 9, 5)
            elif "play song on youtube" in query:
                cm = takecommand().lower()
                pywhatkit.playonyt(cm)
            elif "email" in query:
                try:
                    speak("what should I say?")
                    content = takecommand().lower()
                    to = "venumadathil72@gmail.com"
                    send_email(to, "Subject", content)
                    speak("email sent")
                except Exception as e:
                    print(e)
                    speak("sorry sir, I'm not able to send this email")
            elif "alarm" in query:
                speak("what time should I set the alarm for, tell like this 'set alarm to' and 'time'")
                tt = takecommand()
                tt = tt.replace("set alarm to ", "")
                tt = tt.replace(".", "")
                import Myalarm

                Myalarm.alarm(tt)
            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif "shut down" in query:
                os.system("shutdown /s /t 5")
            elif "restart" in query:
                os.system("shutdown /r /t 5")
            elif "sleep man" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif "where are we" in query:
                speak("wait sir, let me check")
                try:
                    ipAdd = get('https://api.ipify.org').text
                    print(ipAdd)
                    url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                    geo_request = get(url)
                    geo_data = geo_request.json()
                    city = geo_data['city']
                    speak(f"sir, I'm not sure, but I think we are in {city} city of {geo_data['country_name']}")
                except Exception as e:
                    speak("Sorry, I'm not able to find your location.")
                    pass
            elif "how much power left" in query or "how much power we have" in query or "battery" in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system has {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power to continue work")
                elif percentage >= 40 and percentage < 75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage < 40 and percentage > 15:
                    speak("we don't have much power to work, please connect charger")
                else:
                    speak("we have very low power, please connect charger or connect to a power source")

            elif "introduce yourself" in query:
                speak(
                    "I am zeno.v. Your personal AI Assistant. I am here to assist you with various tasks. How can I help you?")
            elif "goodbye" in query or "bye" in query or "stop" in query:
                speak("Goodbye!")
                sys.exit()

if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach
    
    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type
    
    
    id = 5 #number of persons you want to Recognize
    
    
    names = ['','k']  #names, leave first empty bcz counter starts from 0
    
    
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight
    
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    # flag = True
    
    while True:
    
        ret, img =cam.read() #read the frames using the above created object
    
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another
    
        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
    
        for(x,y,w,h) in faces:
    
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image
    
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
    
            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                Taskexecution()
    
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 
    
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    
    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()