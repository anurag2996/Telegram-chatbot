import requests
from bs4 import BeautifulSoup
import json
import os
import datetime


data = requests.get('http://www.mohfw.gov.in/')
soup = BeautifulSoup(data.text,'html.parser')

table = soup.find('table',{'class':'table table-striped'})
tbody = table.find('tbody')

	
Delhi_Rank= tbody.find_all('tr')[7]
Delhi = Delhi_Rank.find_all('td')[1].text.strip()
total_Cases = Delhi_Rank.find_all('td')[2].text.strip()
cured = Delhi_Rank.find_all('td')[3].text.strip()
death = Delhi_Rank.find_all('td')[4].text.strip()
india = tbody.find_all('tr')[33]
total_india = india.find_all('td')[1].text.strip()

current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

information = "Today's Date - {}\n\nInformation about {}\n\n Total cases = {}\n\n cured cases = {}\n\n Total Deaths = {}\n\n Total India = {}\n\n Chatbot by Anurag Gandhi".format(current_time,Delhi,total_Cases,cured,death,total_india)

data = {
	"text" : information
}
# print(data)
webhooks = 'https://hooks.slack.com/services/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'
requests.post(webhooks, json.dumps(data))