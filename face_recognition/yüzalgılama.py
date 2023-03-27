import time
import cv2
import numpy as np
from gtts import gTTS


import os

def start():
    recognizer =cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("egitim.yml")
    cascadePath = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)


    while True:

        ret, frame =cap.read()
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grey, 1.3,5)
        for(x,y,w,h) in faces:

            cv2.rectangle(frame, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
            Id = recognizer.predict(grey[y:y+h,x:x+w])

            print(Id)
            if(Id[0] == 1):
                Id = "Merve"
                time.sleep(2)

                sayac=0
                tts = gTTS(
                text='Seni tanıdım sen Mervesin',
                lang='tr')

                try :
                    tts.save("Merve.mp3")
                except :
                    print("Dosya zaten kayıtlı...")
                try :
                    os.system("Merve.mp3")
                except :
                    print("Dosya açılırken hata aldı...")

                tts = Id[0] == 1
                print(True,"Merve")
                sayac+=1


            elif (Id[0] == 2) :
                Id = "Zeynep"
                time.sleep(2)
                sayac1 = 0
                tts = gTTS(text='Seni tanıdım sen  Zeynepsin',lang='tr')
                tts.save("Merhaba.mp3")
                os.system("Merhaba.mp3")


                tts = Id[0] == 2
                print(True, "Zeynep")
                sayac1 += 1



            elif (Id[0] == 3) :
                Id = "Hacire"
                tts = gTTS(
                    text='Seni tanıdım sen Haciresin',
                    lang='tr')
                tts.save("Hacire.mp3")
                os.system("Hacire.mp3")


                tts = Id[0] == 1
                print(True, "Hacire")


            elif (Id[0] == 4) :

                Id = "Yahya"
                sayac1 = 0

                tts = gTTS(
                    text='Seni tanıdım sen Yahyasın',
                    lang='tr')

                tts.save("Yahya.mp3")
                os.system("Yahya.mp3")


                tts = Id[0] == 1
                print(True, "Yahya")
                sayac1 += 1



            else :
                Id = "taniyamadim"



                tts = gTTS(
                    text='Sizi Tanıyamadım.',
                    lang='tr')

                tts.save("Hata.mp3")
                os.system("Hata.mp3")
                print("Sizi Tanıyamadım")

            cv2.rectangle(frame, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(frame, str(Id), (x,y-40), font, 2, (255,255,255), 3)


        cv2.imshow("Kamera",frame)


        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
