# -*- coding: utf-8 -*- 
import requests
import time
from lxml import html

def MakeReq():
    req = 'https://yandex.ru/pogoda/moscow'
    r = requests.get(req)
    page = html.fromstring(r.text)
    return [page, r.content]

def parse(page):
    tree = html.fromstring(page)
    articles = 1
    result = []
    for i in range(articles):
        pathToday = "/html/body/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/div[2]/div[1]/text()"
        pathTemp = "/html/body/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/div[2]/div[2]/text()"
        today = tree.xpath(pathToday)
        a = {'Сегодня будет': '', 'Температура': ''}
        for j in today:
            a['Сегодня будет'] += str(j)
        temp = tree.xpath(pathTemp)
        for j in temp:
            a['Температура'] += str(j)
        result.append(a)
    return result
    print(result)


page = MakeReq()
data = parse(page[1])


s = data[0]['Температура']
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
print(data)
print(integ)