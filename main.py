import requests
from time import sleep


url = 'http://v4.ipv6-test.com/api/myip.php'
r = requests.get(url).text

TOKEN = 'BOT_TOKEN'
CHAT_ID = 'YOUR_ID'

print("\nThe program was created by printRush\nStarting..\nSuccess!...\n\n")

while True:
    with open('ip.txt', 'r') as f:
        if f.readline() != r:
            rq = requests.get(
                f"https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + CHAT_ID + "&text=" + r)
            with open('ip.txt', 'w') as fw:
                fw.write(r)
                print(rq.json())
    sleep(10)