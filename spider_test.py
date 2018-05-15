#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import os
import time

url = 'http://w3.nat789.biz/pw/htm_data/16/1803/1077401.html'


def download_jpg(pic_url):
    file_name = time.strftime("%H:%M:%S", time.localtime())
    file_name = file_name.replace(":", "")
    file = file_name + r"/"
    mkdir(file)
    i = 0
    for each in pic_url:
        print(each)
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('error')
            continue
        string = file + str(i) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


def search_baidu(url):
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    download_jpg(pic_url)


def search_jpg(url):

    html = requests.get(url).text
    bf = BeautifulSoup(html, "html.parser")
    texts = bf.find_all('div', class_='tpc_content')
    texts = str(texts)
    pattern = re.compile("http:\S+.jpg")
    result = pattern.findall(texts)
    pic_url = set(result)
    download_jpg(pic_url)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    else:
        print("file exists！")


if __name__ == '__main__':
    search_jpg(url)
