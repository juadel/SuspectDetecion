import os
from pickle import load, dump
import datetime
from request_sms import request_sms

def logger(suspect_name):

    try :
        event_logs=load(open("./LogicData/events.dat","rb"))
        #print("face encoding found")
        print("events Files do exist")
    except FileNotFoundError:
        print("no events logs found")
        event_logs={}

    now = datetime.datetime.now
    if event_logs.get(suspect_name) != None:
        print("suspect is in the log")
        if abs(now - event_logs[suspect_name])> datetime.timedelta(minutes=5):
            event_logs[suspect_name] = now
            print("Suspect seen no more than 5  minutes ago")
            #request_sms(suspect_name)
    else:
        event_logs.update(suspect_name = now)
        print (event_logs)
        print("nueva visita de suspect")
        #request_sms(suspect_name)    

    
    dump(event_logs, open("./LogicData/events.dat","wb") )
