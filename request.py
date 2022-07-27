from typing import Dict
from aiogram.types.base import Integer
from aiohttp.client import request
import requests, os, random, hashlib

class Request:
    def __init__(self):
        self.init_url = 'https://securepay.tinkoff.ru/v2/Init'
        self.charge_method_url_test = 'https://rest-api-test.tinkoff.ru/v2/Charge'
        self.notification_url = 'https://675e-91-185-30-130.ngrok.io/ok',
        self.demo_terminal_key = ''
        self.original_terminal_key = ''
        self.hosting_ip = '172.20.20.210'
        self.tinkoff_token = 't.xsGwdXivDu401boUYhJ8uBn-HT4bitt1Q4FyvWDflH2hZ6QhM38w8BF3dGAV9utOdPC1KPlPBYETQFq7vmrgfw'
        self.telegram_token = '2053903302:AAE219aCcuwIe9_nPAVZjv0krUyRxQ4huDA'
        self.get_state_url_test = "https://rest-api-test.tinkoff.ru/v2/GetState"

    def random_id(self) -> Integer:
        id, total = 0, 6
        l = []
        
        for n in range(total):
            l.append(random.randint(1, 9))
            id = int(''.join(map(str, l)))

        return id    
    
    def hash(self, param: str) -> str:
        hashed_string = hashlib.sha256(param.encode('utf-8')).hexdigest()

        return hashed_string
    
    def AddCustomer(self, url: str, nick: str) -> dict:
        template = {
            "TerminalKey": "",
            "Password": "",
            "CustomerKey": nick
        }
        sorted_dict = dict(sorted(template.items(), key=lambda x: x[0].lower()))

        res = ""
        
        for v in sorted_dict.values():
            res += v
        
        token = self.hash(res)
        data = {
            "TerminalKey": "",
	        "CustomerKey": nick,
            "Token": token
        }

        headers = {"Content-type": "application/json"}

        r = requests.post(url=url, headers=headers, json=data).json()

        return r
    
    def AddCard(self, url: str, nick: str) -> dict:
        template = {
            "TerminalKey": "1637858682527DEMO",
            "Password": "",
            "CheckType": "HOLD",
            "CustomerKey": nick
        }
        sorted_dict = dict(sorted(template.items(), key=lambda x: x[0].lower()))

        res = ""
        
        for v in sorted_dict.values():
            res += v
        
        token = self.hash(res)

        data = {
            "TerminalKey": "",
         	"CustomerKey": nick,
	        "CheckType": "HOLD",
	        "Token": token
        }

        headers = {"Content-type": "application/json"}

        r = requests.post(url=url, headers=headers, json=data).json()
        return r

    def GetCardState(self, url: str, request_key: str) -> dict:
        template = {
            "TerminalKey": "",
            "Password": "",
            "RequestKey": request_key
        }    

        sorted_dict = dict(sorted(template.items(), key=lambda x: x[0].lower()))

        res = ""

        for v in sorted_dict.values():
            res += v
        
        token = self.hash(res)
        data = {
            "TerminalKey": "",
            "RequestKey": request_key,
	        "Token": token
        }    
        headers = {"Content-type": "application/json"}
        r = requests.post(url=url, headers=headers, json=data).json()

        return r

    def Init(self, url: str, customerKey: str, recurrent: bool) -> dict:
        if recurrent == True:
            data = {
             "TerminalKey":"",
             "Amount":"299000",
	         "OrderId": self.random_id(),
             "Recurrent": "Y",
             "CustomerKey": customerKey,
	         "NotificationURL": "https://6c6f-91-185-30-130.ngrok.io/ok"
            }
            headers = {"Content-type": "application/json"}
            r = requests.post(url=url, headers=headers, json=data).json()
            return r

        elif  recurrent == False:
            data = { 
                "TerminalKey":"1637858682527DEMO",
	            "Amount":"299000",
	            "OrderId": self.random_id(),
	            "NotificationURL": "https://6c6f-91-185-30-130.ngrok.io/ok"
            }

            headers = {"Content-type": "application/json"}
            r = requests.post(url=url, headers=headers, json=data).json() 
            return r    
        

    def charge_method(self, payment_id: Integer, rebill_id: Integer):
        template = {
            "TerminalKey": "1637858682527DEMO",
            "Password": "",
            "PaymentId": str(payment_id),
	        "RebillId": str(rebill_id),
        }
        
        sorted_dict = dict(sorted(template.items(), key=lambda x: x[0].lower()))
        res = ""
        for v in sorted_dict.values():
            res += v

        data = {           
	        "TerminalKey": "1637858682527DEMO",
	        "PaymentId": payment_id,
	        "RebillId": rebill_id,
	        "Token": self.hash(res)
        }   

        headers = {"Content-type": "application/json"}

        r = requests.post(url=self.charge_method_url_test, headers=headers, json=data).json()

        return r

    def get_state(self, payment_id: Integer):
        template = {
            "TerminalKey": "1637858682527DEMO",
            "Password": "",
            "PaymentId": str(payment_id)
        }
        sorted_dict = dict(sorted(template.items(), key=lambda x: x[0].lower()))
        res = ""
        for v in sorted_dict.values():
            res += v

        data = {
            "TerminalKey": "1637858682527DEMO",
	        "PaymentId": payment_id,
            "Token": self.hash(res)
        }        

        headers = {"Content-type": "application/json"}

        r = requests.post(
            url=self.get_state_url_test,
            headers=headers,
            json=data
        ).json()

        return r


if __name__ == "__main__":
    '''
    request_class = Request()
    result = request_class.post_request()
    print(result)
    print(result['Success'])
    print(result['PaymentId'])
    print(result['Amount'])
    print(result['PaymentURL'])
    '''

    request_class = Request()
    #print(request_class.AddCustomer("https://rest-api-test.tinkoff.ru/v2/AddCustomer", "12345678910"))
    #res = request_class.AddCard(url="https://rest-api-test.tinkoff.ru/v2/AddCard", nick="12345678910")    
    #print(res['PaymentURL'])
    #print(request_class.GetCardState("https://rest-api-test.tinkoff.ru/v2/GetAddCardState", "eedf8348-0eb9-4bf7-9fdd-80dee2f0971a"))
    #print(request_class.Init(url="https://rest-api-test.tinkoff.ru/v2/Init/", customerKey="800703982", recurrent=False))
    
    #print(request_class.charge_method(payment_id=1191876294, rebill_id=1643217849307))

    
