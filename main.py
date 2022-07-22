import requests

url = 'https://api.topvisor.ru/v2/json/get/bank/history'

headers = {
    "Content-type": "application/json",
    "grant_type":"authorization_code",
    "User-Id": "111111",
    "redirect_uri":"https://myintegration.ru/auth/complete",
    "Authorization": "bearer 11111111111111111111"
}

data = {
    "test":"test",
    "demo":"demo"
}

r1 = requests.get(url, headers=headers, data=data)

print(r1)