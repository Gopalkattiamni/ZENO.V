import pyttsx3
import speech_recognition as sr
import datetime 
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import time
import pyjokes
import psutil
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[len(voices)-1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=5,phrase_time_limit=10)

    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
       speak("say that again please.....")
       return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am your assistant,please tell me your request")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()

    
if __name__ == "__main__":
    wish()
    while True:
     if 1:

          query=takecommand().lower()

          #logic building for tasks

          if "open notepad" in query:
              npath = "C:\\Windows\\SysWOW64\\notepad.exe"
              os.startfile(npath)

          elif "open command prompt" in query:
              os.system("start cmd")

          elif "open camera" in query:
              cap = cv2.VideoCapture(1)
              while True:
                  ret, img = cap.read()
                  cv2.imshow('webcam',img)
                  k = cv2.waitKey(50)
                  if k==27:
                      break;
              cap.release()
              cv2.destroyAllWindows()

          elif "play music" in query:
              music_dir = "C:\songs music"
              songs = os.listdir(music_dir)
              #rd=random.choice(songs)
              for song in songs:
                  if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

          elif "ip address" in query:
              ip = get('https://api.ipify.org').text
              speak(f"your IP address is {ip}")

          elif "wikipedia" in query:
              speak("searching wikipedia...")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query,sentences=2)
              speak(results)
              print(results)

          elif "open youtube" in query:
              webbrowser.open("www.youtube.com")

          elif "open instagram" in query:
              webbrowser.open("www.instagram.com")

          elif "open stackoverflow" in query:
              webbrowser.open("www.stackoverflow.com")

          elif "open google" in query:
              speak("sir, what should i search on google")
              cm = takecommand().lower()
              webbrowser.open(f"{cm}")
        #   elif "send message"in query:
        #     speak("to whom u want me to send message")
        #     cm1= takecommand().lower()
        #     kit.sendwhatmsg(cm = takecommand().lower(),"hi",09,05)

          elif "play song on youtube" in query:
            cm=takecommand().lower()
            kit.playonyt(cm)

          elif "email " in query:
            try: 
                 speak("what should i say ?")
                 content = takecommand().lower()
                 to = "venumadathil72@gmail.com"
                 sendEmail(to,content)
                 speak("email sent")
            except Exception as e:
              print(e)
            speak("sorry sir,im not able to send this email")
          elif"no thanks" in query:
             speak("thank you sir,have a good day.")
             sys.exit()

#to close any application
          elif"close notepad" in query:
               speak("ok sir closing")
               os.system("taskkill /f /im notepad.exe")

#to set alarm
        #   elif"set alarm" in query:
        #     nn= int(datetime.datetime.now().hour)
        #     if nn==22:
        #          music-dir = 'e:\\music'
        #          songs = os.listdir(music_dir)
        #          os.system(os.path.join(music_dir,songs[0]))
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
              speak("wait sir,let me check")
              try:
                  ipAdd=request.get('https://api.ipify.org').text
                  print(ipAdd)
                  url = 'https://get.geojs.i/v1/ip/geo/'+ipAdd+'.json'
                  geo_request = request.get(url)
                  geo_data = geo_request.json()
                  city = geo_data['country']
                  speak(f"sir im not sure,but i think we are in {city} city of {country}")
              except Exception as e:
                 speak("sorry im not able to find your location")
                 pass
          elif "how much power left" in query or "how much power we have" in query or "battery" in query:
              battery=psutil.sensors_battery()
              percentage = battery.percent
              speak(f"sir our system has {percentage} percent battery")
              if percentage>=75:
                      speak("we have enough power to continue work")
              elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
              elif percentage<=15 and percentage<=30:
                speak("we dont have enough power to work , please connect to charging")
              elif percentage<=15:
                speak("we have very low power , please connect to charging the system willshutdown very soon")
          elif "internet speed" in query:
            st = speedtest.speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")
            
          elif "no thanks" in query or "nothing" in query:
            speak("thanks for using me sir ,  have a good day")
            sys.exit