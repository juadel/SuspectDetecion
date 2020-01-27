import os
from pickle import load, dump
from datetime import datetime, timedelta
from request_sms import request_sms
wait_time = 5

def logger(suspect_name, phone):
    
    try :
        event_logs=load(open("./LogicData/events.dat","rb"))
        print("events Files do exist")
    except FileNotFoundError:
        print("no events logs found")
        #os.mkdir("./LogicData")
        event_logs={}

    now = datetime.now()
    print(now)
    if event_logs.get(suspect_name) != None:
        print("suspect is in the log")
        if abs(now - event_logs[suspect_name])< timedelta(minutes=wait_time):
            event_logs[suspect_name] = now
            print("Suspect seen no more than 5  minutes ago")
            
        else: 
            event_logs[suspect_name] = now
            request_sms(suspect_name)
            print("Suspected reported")
    else:
        event_logs[suspect_name] = now
        print (event_logs)
        print("nueva visita de suspect")
        request_sms(suspect_name, phone)    

    
    dump(event_logs, open("./LogicData/events.dat","wb") )

