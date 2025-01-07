import requests
import time
import os

url = "https://tamelyapi.azurewebsites.net/GetKeyFromLootLabs"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "https://loot-link.com/"
    }

keysamount = int(input("how many keys do you want to generate: "))

if not os.path.exists('keys.txt'):
    open('keys.txt', 'w').close()

for i in range(keysamount):
    try:
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            print(f"Request {i+1} successful: {req.text}")
            with open('keys.txt', 'a') as f:
                for line in req.text.splitlines():
                    f.write(line + '\n')
        else:
            print(f"Request {i+1} failed with status code: {req.status_code}")
        time.sleep(5)
    except Exception as e:
        print(f"Error occurred: {str(e)}")