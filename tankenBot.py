import urllib.request
import re
import time

from Values import DieselPreis
Current_price = 0.0
print("Your TankenBot Is runing !!")

def savePreis(p):
     with open("Values.py","w") as f:
        f.write("DieselPreis = " + str(p))
        
while True:
    request = urllib.request.Request(url = 'https://ich-tanke.de/tankstelle/c7149dcf227a77c9decac3ff4f228cf9/',headers={'User-Agent': 'Mozilla/5.0'})
    f = urllib.request.urlopen(request)
    myfile = str(f.read()).replace('"','')
    x = re.findall(">[0-9]+,[0-9]+<", myfile)
    Current_price = float(x[2].replace('>','').replace('<','').replace(',','.'))
    if Current_price != DieselPreis:
        if Current_price < 1.55 :
            DieselPreis = Current_price
            savePreis(DieselPreis)
            f = urllib.request.urlopen("https://api.telegram.org/bot7763059278:AAGOq5p41F62XU0DTwoeNKa4HBtHEDRr8j4/sendMessage?chat_id=@tanken_channel&parse_mode=Markdown&text=DieselPreis={}%E2%82%AC".format(str(DieselPreis)))
    time.sleep(60)