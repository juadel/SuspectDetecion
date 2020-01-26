import os
import face_recognition
from pickle import dump, load
from tkinter import *
from tkinter import filedialog

def addSuspectWin():
    addWin = Toplevel()
    addWin.geometry('{}x{}'.format(400, 150))
   
    label= Label(addWin,text= " Suspects Data Base ", font=("Arial", 14))
    label.grid(row=0, column=1)
    nameLbl = Label(addWin,text= "  Suspect Name:  ", font=("Arial", 12))
    nameLbl.grid(row=1, column=0)
    
    pictureLbl = Label(addWin,text= " Select Picture:  ", font=("Arial", 12))
    pictureLbl.grid(row=2, column=0)
    
    
    nameEntry = Entry(addWin, width = 20)
    nameEntry.grid(row = 1, column = 1)
    


    def dataBaseCreator ():
        
        name= nameEntry.get()
        image = filename

        try :
            known_face_encodings=load(open("./LogicData/logic_faces.dat","rb"))
            print("face encoding found")
        except FileNotFoundError:
            print("no face encoding found")
            os.mkdir("./LogicData")
            known_face_encodings= []

        try: 
            known_face_names = load(open("./LogicData/logic_names.dat","rb"))
            print("face names found")
            print(known_face_names)

        except FileNotFoundError:
            print("no names encoding found")
            known_face_names=[]

            
        suspect_face = face_recognition.load_image_file(image)
        known_face_encodings.append(face_recognition.face_encodings(suspect_face)[0])
        known_face_names.append(name)
        #print(len(known_face_names))
        dump(known_face_encodings, open("./LogicData/logic_faces.dat","wb") )
        dump(known_face_names,open("./LogicData/logic_names.dat","wb"))

        print ("suspect file saved succesfully")
        addWin.destroy()
    
    def browse ():
        global filename
        filename=filedialog.askopenfilename(title="Select an Image of the suspect", filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        print(filename)


    btn_2 = Button(addWin, text = "Browse", command= browse)
    btn_2.grid(column = 1 , row = 2 )
     
    btn = Button(addWin, text="ADD", command=dataBaseCreator)
    btn.grid(column = 1, row = 4) 

