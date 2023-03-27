import tkinter
from PIL import Image,ImageTk
import os

import yüzalgılama
import egitim
import veriseti
from playsound import playsound

pencere=tkinter.Tk()
pencere.geometry("600x450+50+20")
pencere.configure(background="light blue")
pencere.title("ARAYÜZ")
pencere.resizable(False, False)

# pencere.state("zoomed")
ico = Image.open('indir.jpg')
photo = ImageTk.PhotoImage(ico)
pencere.wm_iconphoto(False, photo)


etiket=tkinter.Label(pencere, text="GİRİŞ",relief="groove",bg="light blue",font=("Arial Black", 12, "bold"),cursor="hand2",bd=10,width=1000, padx=20)
etiket.pack()

resim=ImageTk.PhotoImage(Image.open("indir.jpg"))
buton=tkinter.Button(pencere, image=resim,activebackground="light blue",width=300,height=168)
buton.pack()


etiket1= tkinter.Label(text="  ")
etiket1.pack()

etiket2= tkinter.Label(text="  ")
etiket2.pack()

etiket3= tkinter.Label(text="  ")
etiket3.pack(side="left", fill="x",expand=1,anchor="n")


###################################################     menü giriş fonksiyonları

def data_set():
    print("\n"*3)
    print("veri seti oluşturuluyor .... ")
    print("#" * 100)
    veriseti.start()
    print("veri seti alındı.")
def train_data():
    print("eyitim yapılıyor .... ")
    print("#" * 100)
    egitim.start()
    print("eğitim yapıldı")
def face_dedector():
    print("yüz tespiti yapılıyor  .... ")
    print("#"*100)
    yüzalgılama.start()
    print("yüz tanıma başarılı ")



btn=tkinter.Button(pencere, text="Veriseti",bg="light blue",relief="groove", overrelief="raised",bd=10,height=2, width=8,padx=20,activeforeground="blue",font=("Bahnschrift", 12, "bold"),cursor="hand2",command=data_set,activebackground="white")
btn.pack(side="left", fill="x",expand=1)

btn1=tkinter.Button(pencere, text="Eğitim",bg="light blue",relief="groove",overrelief="raised",bd=10,height=2, width=8,padx=20,activeforeground="blue",font=("Bahnschrift", 12, "bold"),cursor="hand2",command=train_data,activebackground="white")
btn1.pack(side="left", fill="x",expand=1)

btn2=tkinter.Button(pencere, text="Yüz Algılama",bg="light blue",relief="groove",overrelief="raised",bd=10,height=2,width=8, padx=20,activeforeground="blue",font=("Bahnschrift", 12, "bold"),cursor="hand2",command=face_dedector,activebackground="white")
btn2.pack(side="left", fill="x",expand=1)


btn3=tkinter.Button(pencere, text="Çıkış",bg="light blue",relief="groove",overrelief="raised",bd=10,height=2,width=8, padx=20,activeforeground="blue",font=("Bahnschrift", 12, "bold"),activebackground="white",command=pencere.quit,cursor="hand2")
btn3.pack(side="left", fill="x",expand=1)



etiket4 = tkinter.Label(text="    ")
etiket4.pack(side="left",fill="x",expand=1,anchor="n")



pencere.mainloop()
