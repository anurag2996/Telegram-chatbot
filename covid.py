import requests
import json
from bs4 import BeautifulSoup
import json
import os
import datetime
import time


data = requests.get('https://www.worldometers.info/coronavirus/country/india/')
time.sleep(2)
soup = BeautifulSoup(data.text,'html.parser')

totalcase = soup.find('div',{'class':'maincounter-number'}).text.strip()
time.sleep(2)
deaths = soup.find_all('div',{'class':'maincounter-number'})[1].text.strip()
time.sleep(2)
recovered = soup.find_all('div',{'class':'maincounter-number'})[2].text.strip()

information = 'Country: India \n\nTotal Cases: {}\nDeaths: {}\nRecovered: {}'.format(totalcase,deaths,recovered)
# print(information)


class telegram_chatbot():

    def __init__(self):
        # self.token = self.read_token_from_config_file(config)
        self.token = '1196686551:AAHg8FCKNLZKePl7sIk0E2hMdBW1sLp3rcU'
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')


bot = telegram_chatbot()

def make_reply(msg):
    # reply = None
    if msg =="/new":
        reply = information
    else:
        reply = "Check your input"
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)