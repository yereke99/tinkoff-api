import hashlib

a_string = '1576146812zch86szfax3s7hml1637858682527DEMO'

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)