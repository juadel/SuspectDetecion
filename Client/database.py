import os
import face_recognition
from pickle import dump, load

logicDataFolder = "./LogicData"

def dataBaseCreator (image, name):
    # known_face_names = []
    # known_face_encodings=[]
    try :
        known_face_encodings=load(open("./LogicData/logic_faces.dat","rb"))
        print("face encoding found")
    except FileNotFoundError:
        print("no face encoding found")
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




image = "./LogicData/juan.jpg"
name = "Juan"
image2 = "./LogicData/tomas.jpg"
name2 = "Tomas"
image3 = "./LogicData/caro.jpg"
name3 = "Caro"
dataBaseCreator(image, name)
dataBaseCreator(image2,name2)
dataBaseCreator(image3,name3)