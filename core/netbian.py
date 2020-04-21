# @Author  : GentleCP
# @Email   : 574881148@qq.com
# @File    : netbian.py
# @Item    : PyCharm
# @Time    : 2020-04-21 15:33
# @WebSite : https://www.gentlecp.com
import os
import sys
import logging
import requests
from bs4 import BeautifulSoup
from cptools import download_file


def get_html(url):
    return requests.get(url).content

def get_page_num(init_html):
    bs4obj = BeautifulSoup(init_html,'html.parser')
    return int(bs4obj.find('div',{'class':'page'}).find_all('a')[-2].contents[0])

def get_download_url(base_url, content_html):
    bs4obj = BeautifulSoup(content_html,'html.parser')
    src = bs4obj.find('a', {'id': 'img'}).find('img').get('src')
    return base_url + src

def parse_index_html(base_url, index_html):
    bs4obj = BeautifulSoup(index_html, 'html.parser')
    lis = bs4obj.find('ul', {'class': 'clearfix'}).find_all('li')
    for li in lis:
        content_url = base_url + li.find('a').get('href')
        content_html = get_html(content_url)
        yield content_html

def download_img(url, save_pwd):
    if not os.path.exists(save_pwd):
        os.mkdir(save_pwd)
    file_path = save_pwd+'/' + url.split('/')[-1]
    if os.path.exists(file_path):
        return
    download_file(url,file_path = file_path)

def download(base_url, index_html, save_pwd):
    for content_html in parse_index_html(base_url, index_html):
        download_url = get_download_url(base_url, content_html)
        download_img(url = download_url, save_pwd= save_pwd)

def netbian(type=None, base_url = None, save_pwd='../imgs'):
    categories = ['fengjing','meinv','youxi','dongman','yingshi','mingxing','qiche'
            ,'dongwu','renwu','meishi','zongjiao','beijing']
    if type and type in categories:
        init_url = base_url + '/4k'+type
        init_html = get_html(init_url)
        page_num = get_page_num(init_html)
        download(base_url, init_html, save_pwd)

        for index in range(2,page_num+1):
            index_url = init_url + '/index_' + str(index) +'.html'
            index_html = get_html(index_url)
            download(base_url, index_html, save_pwd)

    elif not type in categories:
        logging.error('There is no such category named:{}'.format(type))

    else:
        for type in categories:
            netbian(type, base_url, save_pwd)
