
# import speech_recognition as sr 
# import pyttsx3
# from pyttsx3 import speak
# import wolframalpha
# import wikipedia
# import webbrowser

# import requests
# from bs4 import BeautifulSoup

# appid = 'W4AWY2-976YP965PV'
# client =  wolframalpha.Client(appid)
# print(appid)

# spokenapi = r"http://api.wolframalpha.com/v1/spoken?appid={0}&i=".format(appid)

# query = input("Enter Your Query: ").lower()
# user_query = query.replace(" ", "+")
# print(user_query)
# URL = spokenapi + user_query
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}
# page = requests.get(URL)
# print(page.text)
# content = page.text
# soup = BeautifulSoup(content, 'html.parser')
# # soup = BeautifulSoup(page.content, 'html.parser')
# result = soup.get_text()
# # print(result)

# from pyttsx3 import speak
# import speech_recognition as sr


# def takeinput():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening")
#         r.pause_threshold=1
#         audio = r.listen(source)
#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio, language='en-in')
#         print(query)
#     except Exception as e:
#         print(e)
#         speak("Say that again please")
#         return "None"
#     return query

# # while 1:
# #     n = takeinput()
# #     print(n)


from logging import info
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import cv2
from fer import FER
from apscheduler.schedulers.background import BackgroundScheduler
# model = load_model('/facefeatures_new_model_final.h5')
# model = load_model(r'C:\Users\smriti bansal\Desktop\Code\ML\Open-CV\Face_Recognition\facefeatures_new_model.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
emo_detector = FER()

sched = BackgroundScheduler()

scheduler = BackgroundScheduler()
scheduler.start()


import logging
# logging.getLogger('apscheduler.scheduler').setLevel('WARNING')
# # You may also have to do:
# logging.getLogger('apscheduler.scheduler').propagate = False
# global Emotion
# Emotion = "Neutral"
def detect_emotion():
    # while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    captured_emotions = emo_detector.detect_emotions(frame)
    if captured_emotions:
        top_emotions = max(captured_emotions[0]["emotions"].items(), key=lambda x:x[1])[0]
        Emotion = top_emotions
        print(Emotion)
            
        
sched.add_job(detect_emotion, 'interval', seconds=10)
logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
sched.start() 
while True:
    # print(Emotion)
    # _, frame = cap.read()
    # frame = cv2.flip(frame, 1)
    # captured_emotions = emo_detector.detect_emotions(frame)
    # if captured_emotions:
    #     top_emotions = max(captured_emotions[0]["emotions"].items(), key=lambda x:x[1])[0]
    #     Emotion = top_emotions
    #     accuracty = str(captured_emotions[0]["emotions"][top_emotions])
    #     print(captured_emotions)
        # print(captured_emotions[0]["emotions"])
        # print(Emotion)
    pass