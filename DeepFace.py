
import cv2
from keras.models import load_model
import numpy as np
import json 
from fer import FER
from sympy import capture


# model = load_model('/facefeatures_new_model_final.h5')
# model = load_model(r'C:\Users\smriti bansal\Desktop\Code\ML\Open-CV\Face_Recognition\facefeatures_new_model.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
emo_detector = FER(mtcnn=True)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # face =  face_cascade.detectMultiScale(frame)
    # if  len(face) == 0:
    #     cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    # else:
    #     x=face[0][0]
    #     y=face[0][1]
    #     w=face[0][2]
    #     h=face[0][3]
    #     # cropped_face = frame[y:y+h, x:x+w]
    #     frame = cv2.rectangle(frame, (x,y),(x+w,y+h), [0,255,0], 5 )
    # demography = DeepFace.analyze(frame,detection_method='opencv')
    # output = json.dumps(demography,indent=2)
    # print(output)
        # cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    # else:
    #     cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    captured_emotions = emo_detector.detect_emotions(frame)
    if captured_emotions:
        top_emotions = max(captured_emotions[0]["emotions"].items(), key=lambda x:x[1])[0]
        print(top_emotions)
        x = captured_emotions[0]["box"][0]
        y = captured_emotions[0]["box"][1]
        w = captured_emotions[0]["box"][2]
        h = captured_emotions[0]["box"][3]
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h), [19,200,29], 2 )
        frame = cv2.putText(frame,top_emotions+ " " + str(captured_emotions[0]["emotions"][top_emotions]*100) + "%", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (105,182,94), 2)
        # frame = cv2.putText(frame,(x+30,y-30),top_emotions, cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        # Print all captured emotions with the image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()