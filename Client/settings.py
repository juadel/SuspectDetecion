from pickle import load, dump
from tkinter import *
import os

def cameraWindow ():
    camerawindow = Toplevel()
    camerawindow.geometry('{}x{}'.format(400, 150))
   
    label= Label(camerawindow,text= "Camera Configuration", font=("Arial", 14))
    label.grid(row=0, column=1)
    user = Label(camerawindow,text= "  Username:  ", font=("Arial", 12))
    user.grid(row=1, column=0)
    password = Label(camerawindow,text= "  Password:  ", font=("Arial", 12))
    password.grid(row=2, column=0)
    ipLabel = Label(camerawindow,text= "  IP Address:  ", font=("Arial", 12))
    ipLabel.grid(row=3, column=0)

    
    userEntry = Entry(camerawindow, width = 20)
    userEntry.grid(row = 1, column = 1)
    pas = Entry(camerawindow, show="*", width = 20)
    pas.grid(row = 2, column = 1)
    ipEntry = Entry(camerawindow, width = 20)
    ipEntry.grid(row = 3, column = 1)

   

    def cameraSettings():
        user = userEntry.get()
        password = pas.get()
        ip = ipEntry.get()
        
        try :
            settings=load(open("./Settings/settings.dat","rb"))
            print("Settings file found")
        except FileNotFoundError:
            print("no settings file")
            os.mkdir("./Settings")
            settings={"user":"admin","password":"12345","ip":"192.168.2.100","phone":"+12345678910"}

        settings["user"]= user
        settings["password"]= password
        settings["ip"]= ip

        dump(settings, open("./Settings/settings.dat","wb") )
        print("Settings saved")
        camerawindow.destroy()
    
    btn = Button(camerawindow, text="SAVE", command=cameraSettings)
    btn.grid(column = 1, row = 4) 

def notificationWindow ():
    notWin = Toplevel()
    notWin.geometry('{}x{}'.format(400, 150))
   
    label= Label(notWin,text= "Notificaction Settings", font=("Arial", 14))
    label.grid(row=0, column=1)
    phone = Label(notWin,text= "  Phone Number:  ", font=("Arial", 12))
    phone.grid(row=1, column=0)
    

    
    phoneEntry = Entry(notWin, width = 20)
    phoneEntry.grid(row = 2, column = 1)
    phoneEntry.insert(0,'+12345678910')
    
    
    def notifications():
        phone = phoneEntry.get()
        try :
            settings=load(open("./Settings/settings.dat","rb"))
            print("Settings file found")
        except FileNotFoundError:
            print("no settings file")
            os.mkdir("./Settings")
            settings={"user":"admin","password":"12345","ip":"192.168.2.100","phone":"+12345678910"}

        settings["phone"]= phone
        dump(settings, open("./Settings/settings.dat","wb") )
        print("Settings saved")
        notWin.destroy()
    
    btn = Button(notWin, text="SAVE", command=notifications)
    btn.grid(column = 1, row = 4) 