from tkinter import *
from settings import cameraWindow, notificationWindow
from database import addSuspectWin
from face_detector import faceDetectorService
import multiprocessing







window =Tk()

window.title("Suspect Detector")
## WINDOWS SIZE AND FRAME SETTINGS
window.geometry('{}x{}'.format(275,150))
top_frame = Frame(window,width=250, height=30, pady=6)

window.grid_rowconfigure(1, weight=2)
window.grid_columnconfigure(1,weight=2)


## END


## MENU CONFIGURATION ##
menubar =Menu(window)
## SETTINGS MENU
settings_menu=Menu(menubar, tearoff=0)
settings_menu.add_command(label="Camera", command= cameraWindow)
settings_menu.add_command(label="Notifications", command= notificationWindow)
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
chk = Checkbutton(window, text='Show Camera', var=chk_state)
chk.grid(column=1, row=10)


p = multiprocessing.Process(target=faceDetectorService, args=(chk_state.get,))
def startService():
    #faceDetectorService(chk_state.get())
    muProcess.append(p)
    print ('Process before execution:', p, p.is_alive())
    p.start()
    print ('Process running:', p, p.is_alive())
    
   # p.join()
  

def stopService():
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
  

btn = Button(text="START SERVICE", command=startService)
btn.grid(column = 1, row = 1 )
btn = Button(text="STOP SERVICE", command=stopService)
btn.grid(column = 2, row = 1 )  

statusbar = Label(window, text="on the way…")

#statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()

