from tkinter import *
from settings import Settings
from database import addSuspectWin
from face_detector import FaceDetectorProcess


## Initialize a FaceDetector Process
p = FaceDetectorProcess()
s = Settings()
# Graphics Interface
window =Tk()

window.title("Suspect Detector")
## WINDOWS SIZE AND FRAME SETTINGS
window.geometry('{}x{}'.format(275,100))
top_frame = Frame(window,width=250, height=30, pady=6)
status_frame = Frame(window, width=20, height = 10, pady=6)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)
top_frame.grid(row=0, columnspan =3 )
status_frame.grid(row=3, columnspan=3)

## END


## MENU CONFIGURATION ##
menubar =Menu(window)
## SETTINGS MENU
settings_menu=Menu(menubar, tearoff=0)
settings_menu.add_command(label="Camera", command= s.cameraWindow)
settings_menu.add_command(label="Notifications", command= s.notificationWindow)
menubar.add_cascade(label="Settings", menu=settings_menu)
## DATABASE
data_menu=Menu(menubar, tearoff=0)
data_menu.add_command(label="Add a suspect", command=addSuspectWin)
data_menu.add_command(label="Delete a suspect")
data_menu.add_command(label="View log")
menubar.add_cascade(label="Database", menu=data_menu)
## QUIT HELP
menubar.add_command(label="Help")
## QUIT MENU
menubar.add_command(label="Quit", command=window.destroy)

window.config(menu=menubar)
## END

## TEXT ON WINDOW
chk_state = BooleanVar() 
chk_state.set(False) 
chk = Checkbutton(top_frame, text='Show Camera', var=chk_state)
chk.grid(column=1, row=3)


def startService():
    p.showVideoVariable = chk_state.get()
    print ('Starting Video Capture:')
    p.start()
    print ('Process running:', p.live)
    btnStart.config(state="disabled")
    btnStop.config(state="active")
    if (p.live):
        text.set("Server is Running")
    
  

def stopService():
    p.stop()
    print ('Process terminated:',p.live)
    btnStart.config(state="active")
    btnStop.config(state="disabled")
    text.set("Server Stopped")
    
text= StringVar()
text.set("Press Start to proceed")
status = Label(status_frame,textvariable=text,relief=SUNKEN, anchor=W, bd=2)
status.grid(row = 0)

btnStart = Button(top_frame, text="START SERVER", command=startService)
btnStart.grid(column = 1, row = 2)
btnStop = Button(top_frame, text="STOP SERVER", command=stopService)
btnStop.grid(column = 2, row = 2 )  




window.mainloop()

