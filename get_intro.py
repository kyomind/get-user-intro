#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import re
import csv

def get_intro_details_from_message(message):
    raw_detail_list = message.split('：')
    detail_list = [i.split('✮')[0] for i in raw_detail_list][1:]
    return detail_list

with open('messages.html','r', encoding='utf8') as messages:
    soup = BeautifulSoup(messages, 'html.parser')

messages = soup.find_all('div', 'text')

insert_list = []
for message in messages:
    if re.search(r'可以這樣稱呼我', message.text):
        detail_list = get_intro_details_from_message(message=message.text)
        insert_list.append(detail_list)   

with open('intro.csv','wt',encoding='utf8',newline='') as intro:
    csv_writer = csv.writer(intro)
    csv_writer.writerows(insert_list)

with open('intro_excel.csv','wt',encoding='cp950',newline='') as intro:
    csv_writer = csv.writer(intro)
    csv_writer.writerows(insert_list)