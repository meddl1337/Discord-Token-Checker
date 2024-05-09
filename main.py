# Project made for Free2use
# dev: xyzalbaner
# join discord.gg/xyzshop for more :)

# you can skid, but don't sell you indian monkey

import os
import threading
import requests
import ctypes
from datetime import datetime
import time
from lib.styler import Colors, Colorate, Center

class xyzraid:
    def __init__(self):
        self.tokens = self.load_tokens()
        self.nowtimer = datetime.today().strftime('%H:%M:%S')
        os.system("mode 80, 20")
        self.clear()
        self.setTitle("xyzTokenChecker Tool → discord.gg/xyzshop → dev: xyzalbaner")
        self.banner()
        time.sleep(3)

        self.working = 0
        self.invalid = 0

        self.session = requests.Session()

        ts = [threading.Thread(target=self.xyz_main, args=[token]) for token in self.tokens]
        for thread in ts:
            thread.start()
        for thread in ts:
            thread.join()
    
    def load_tokens(self):
        with open("tokens.txt", "r", encoding="utf-8") as file:
            return file.read().splitlines()

    def banner(self):
        banner = f'''
▐▄• ▄  ▄· ▄▌·▄▄▄▄• ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
 █▌█▌▪▐█▪██▌▪▀·.█▌▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
 ·██· ▐█▌▐█▪▄█▀▀▀•██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
▪▐█·█▌ ▐█▀·.█▌▪▄█▀▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
•▀▀ ▀▀  ▀ • ·▀▀▀ •·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀

Token loaded: {len(self.tokens)} | discord.gg/xyzshop | @xyzalbaner

'''
        print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter(banner)))
    
    def clear(self):
        os.system("cls")
    
    def setTitle(self, _str):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
    
    @staticmethod
    def get_headers(token):
        headers = {
            "authorization": token
        }
        return headers
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")

    
    def xyz_main(self, token):
        url = 'https://discord.com/api/v9/users/@me'
        headerz = xyzraid.get_headers(token)
        
        r = self.session.get(url, headers=headerz)

        detail_json = r.json()
        if r.status_code == 200:
            self.working += 1
            self.setTitle(f'xyzTokenChecker by @xyzalbaner | Tokens: {len(self.tokens)} | Valid: {self.working} | Invalid: {self.invalid}')
            details = f'''
┌ {token[:32]} 
├ Status: {self.check_status(r.status_code)} → {r.status_code}
├ Username: {detail_json["username"]}
├ Email: {detail_json["email"]} | Verified: {detail_json["verified"]}
└ Phone: {detail_json["phone"]}
                '''
            print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter(details)))
            open("valid_tokens.txt", "a").write(token + "\n")

        else:
            self.invalid += 1
            self.setTitle(f'xyzTokenChecker by @xyzalbaner | Tokens: {len(self.tokens)} | Valid: {self.working} | Invalid: {self.invalid}')
            details = f'''
┌ {token[:32]} 
└ Status: {self.check_status(r.status_code)} → {r.status_code}
                '''
            print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(details)))
            open("invalid_tokens.txt", "a").write(token + "\n")

xyzraid()
input("")