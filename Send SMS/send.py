from tkinter import *
from tkinter.messagebox import *
import requests

def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization' : 'JebRrLQHFYqPz3UMaxAmBTsh6o1kZw4i0yjcfCVO5IDKu9NSlddNygiTer7kORDUx8XfmQIMjp5EbPqB',
        'sender_id' : 'TXTIND',
        'message' : message,
        'route' :  'v3',
        'numbers' : number,
        'language' : 'english'
    }
    response = requests.get(url,params=params)
    dic = response.json()
    print(dic)
    print(type(dic))

    send_sms('7905935478','hello')