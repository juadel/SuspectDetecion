from tkinter import *


window =Tk()

window.title("Suspect Detector")
## WINDOWS SIZE AND FRAME SETTINGS
window.geometry('{}x{}'.format(400,150))
top_frame = Frame(window,width=250, height=30, pady=6)
btm_frame = Frame(window,width=250, height=30, pady=6,bd=1, relief=SUNKEN) 
window.grid_rowconfigure(1, weight=2)
window.grid_columnconfigure(0,weight=2)
top_frame.grid(row=0, columnspan =1 )
btm_frame.grid(row=1, columnspan =3)
## END


## MENU CONFIGURATION ##
menubar =Menu(window)
## SETTINGS MENU
settings_menu=Menu(menubar, tearoff=0)
settings_menu.add_command(label="Camera")
settings_menu.add_command(label="Notifications")
menubar.add_cascade(label="Settings", menu=settings_menu)
## DATABASE
data_menu=Menu(menubar, tearoff=0)
data_menu.add_command(label="Add a suspect")
data_menu.add_command(label="Delete a suspect")
data_menu.add_command(label="View log")
menubar.add_cascade(label="Database", menu=data_menu)
## QUIT HELP
menubar.add_command(label="Help")
## QUIT MENU
menubar.add_command(label="Quit")

window.config(menu=menubar)
## END

## TEXT ON WINDOW

lbl = Label(top_frame, text="Add a suspect to Database ", font=("Arial", 10))
lbl2 = Label(top_frame, text="Suspect name:  ", font=("Arial", 10))
lbl4= Label(btm_frame, text="  Select picture:  ", font=("Arial", 10))
lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl4.grid(column=0, row=7)

ip_0 = Entry(top_frame,width=20)
ip_0.focus()
ip_1 = Entry(top_frame, width = 20)
pas = Entry(top_frame, show="*", width = 20)
ip_0.grid(column = 2, row = 0)
ip_1.grid(column = 2, row = 1)
pas.grid(column = 2, row =3)

chk_state = BooleanVar() 
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Show Images', var=chk_state)
chk.grid(column=1, row=10)

btn = Button(top_frame, text="Scan LAN")
btn.grid(column = 3 , row = 3 ) 
btn_2 = Button(btm_frame, text = "Browse")
btn_2.grid(column = 2 , row = 7 ) 
btn_3 = Button(btm_frame, text="Scan Folder")
btn_3.grid(column = 3 , row = 7 ) 

window.mainloop()