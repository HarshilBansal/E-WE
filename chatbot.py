import pyttsx3
from pyttsx3 import speak
import os
import time
import pyjokes
import datetime
import speech_recognition as sr
import pyautogui
import smtplib

engine = pyttsx3.init()
engine.setProperty('rate', 150)
# Use female voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.setProperty('volume', 3)
engine.runAndWait()
os.system("cls")
print("                                U^.^U - EL                            \n")
# pyttsx3.speak("hello there! ........how are you?")
# pyttsx3.speak("I'm El , I'm a python program that can help you with various things on your system")
# time.sleep(1)
print("May i ask, who are you?? :", end=' ')
pyttsx3.speak(" and May i ask, , , who are you??")
gar = ("hey","hello","my", "name", " Name", "is", "you", "can", "its", "it",
       "call", "me", "i", "am", "this", "should", "would", "side")
nam = list(input().lower().split())
name = [item for item in nam if item not in gar]
print("Hello! " + name[0])
speak("hello " + name[0]+ " ?!." + " its nice to meet you")

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}


import cv2
from fer import FER
from apscheduler.schedulers.background import BackgroundScheduler
# model = load_model('/facefeatures_new_model_final.h5')
# model = load_model(r'C:\Users\smriti bansal\Desktop\Code\ML\Open-CV\Face_Recognition\facefeatures_new_model.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
emo_detector = FER(mtcnn=True)

sched = BackgroundScheduler()

def detect_emotion():
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        captured_emotions = emo_detector.detect_emotions(frame)
        if captured_emotions:
            top_emotions = max(captured_emotions[0]["emotions"].items(), key=lambda x:x[1])[0]
            return top_emotions
        
sched.add_job(detect_emotion, 'interval', seconds=5)
sched.start()      
        # frame = cv2.rectangle(frame, (x,y),(x+w,y+h), [19,200,29], 2 )
        # frame = cv2.putText(frame,top_emotions+ " " + str(captured_emotions[0]["emotions"][top_emotions]*100) + "%", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (105,182,94), 2)
        # frame = cv2.putText(frame,(x+30,y-30),top_emotions, cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        # Print all captured emotions with the image
    
    

import speech_recognition as sr 
import pyttsx3
from pyttsx3 import speak
import wolframalpha
import wikipedia
import webbrowser

import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

def takeinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that agheyain please")
        return "None"
    return query

appid = 'W4AWY2-976YP965PV'
client =  wolframalpha.Client(appid)
print(appid)

# spokenapi = r"http://api.wolframalpha.com/v1/spoken?appid={}&i=How+far+is+Los+Angeles+from+New+York%3f"
spokenapi = r"http://api.wolframalpha.com/v1/spoken?appid={0}&i=".format(appid)
start = time.time()
while True:
    curr = time.time()
    if int(curr - start)%5 == 0:
        detect_emotion()
    query = input("Enter Your Query: ").lower()
    try:
        res = client.query(query)
        ans = next(res.results).text
        print(ans)
        speak(ans)
    #     user_query = query.replace(" ", "+")
    #     URL = spokenapi + user_query
    #     page = requests.get(URL)
    #     print(page.text)
    #     speak(page.text)
    except Exception:
        try:
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        except Exception:
            try: 
                user_query = query.replace(" ", "+")
                print(user_query)
                URL = "https://www.google.co.in/search?q=" + user_query
                # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='Z0LcW XcVN5d').get_text()
                print(result)
                
                # webbrowser.open('https://google.com/search?q=' + query)
            except Exception:
                print("I got nothing! Try rerunning.")

# def query():
    
#     user_query = input('Enter your query: ')

#     URL = "https://www.google.co.in/search?q=" + user_query

#     headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
#     }

#     page = requests.get(URL, headers=headers)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     result = soup.find(class_='Z0LcW XcVN5d').get_text()
#     print(result)

# while True:
#     try:
#         query()
#     except Exception:
#         print('Sorry no result, please be clear')
#     user_input = input('To continue press y: ')
#     if user_input != 'y':
#         break





