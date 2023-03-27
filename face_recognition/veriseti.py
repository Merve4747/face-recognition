import cv2
import numpy as np
import time
from gtts import gTTS
from playsound import playsound
import os

def start():

    tts = gTTS(text='Hazırsanız başlayalım.Yüzünüzü algılamam için kameraya yaklaşın.Hadi Başlayalım.', lang='tr')
    tts.save("merhaba.mp3")
    os.system("merhaba.mp3")
    time.sleep(10)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    face_id =1
    count = 0

    while True:
        ret, frame = cap.read()
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces = face_cascade.detectMultiScale(grey,1.3,5)
        count += 1


        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", grey[y:y+h,x:x+w])
        cv2.imshow("Kamera",frame)


        if cv2.waitKey(95) & 0xFF==ord("q"):
            break

        elif count >50:
            break


    tts = gTTS(text='Yüzünüz algılandı.', lang='tr')
    tts.save("merhaba.mp3")
    os.system("merhaba.mp3")
    print("Yüzünüz algılandı")



    cap.release()
    cv2.destroyAllWindows()
