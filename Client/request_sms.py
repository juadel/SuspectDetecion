import requests
import json
import datetime

API_endpoint = "https://46p7nhmwib.execute-api.ca-central-1.amazonaws.com/dev/SuspectNotification"

def request_sms(suspect, phone):
    
    body = {'phone_number':phone,'suspect':suspect}
    headers={}
    r = requests.post(url=API_endpoint, data=json.dumps(body), headers=headers)
    print("SMS send:%s"%r.text)

