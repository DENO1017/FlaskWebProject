import numpy as np
import os
import urllib.request
import requests
from bs4 import BeautifulSoup
from xml.dom.minidom import Document,parse
import xml.sax


class music():
    """description of class"""
    __tablename__ = 'music'
    filename = 'filename'
    filenum = 0
    title = 'title'
    musician = 'musician'
    albumn = 'albumn'
    list = 'list'
    def __init__(self, filename, filenum,title,musician,albumn,list):
        self.filename=filename
        self.filenum=filenum
        self.title=title
        self.musician=musician
        self.albumn=albumn
        self.list = list

class playlist():
    __tablename__='playlist'
    countmusic = 0
    id = 'id'
    title = 'title'
    url = 'url'
    def __init__(self, id, title, url):
        self.id = id
        self.title=title
        self.url=url


def get_filename(path,filetype):
    name = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                print(name)
                name.append(i.replace(filetype,''))
    return name


def get_playlist_ol():
    
    url='https://music.163.com/discover/playlist'
    header = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }
    s=requests.session()
    #print(s.get('https://music.163.com/#/discover/playlist').content)
    bs = BeautifulSoup(s.get(url,headers=header).content,"html.parser")
    #print(bs)
    lst=bs.find_all('div',{'class': 'u-cover u-cover-1'})

    playlists = []

    for play in lst:
        title = play.find('a',{'class': 'msk'})['title']
        #print(title)
        link = play.find('a',{'class': 'msk'})['href']
        #print(link)
        id=link.replace("/playlist?id=", "")
        playlists.append(playlist(id,title,link))


        img = play.find('img',{'class': 'j-flag'})['src']
        path = 'E:\DAM\FlaskWebProject1\FlaskWebProject1\HW2\static\playlists\\'+id
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path+' 创建成功')

            doc = Document()
            root = doc.createElement('playlist')
            doc.appendChild(root)
            head = doc.createElement('head')
            root.appendChild(head)

            t_id=doc.createElement('id')
            t_id_text = doc.createTextNode(id)
            t_id.appendChild(t_id_text)
            head.appendChild(t_id)

            t_title=doc.createElement('title')
            t_title_text = doc.createTextNode(title)
            t_title.appendChild(t_title_text)
            head.appendChild(t_title)
            
            t_url=doc.createElement('url')
            t_url_text = doc.createTextNode(link)
            t_url.appendChild(t_url_text)
            head.appendChild(t_url)

            filename=path+'\info.xml'

            with open(filename,'wb+') as f:
                f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))
            
            filename=path+'\\'+id+'.jpg'
            urllib.request.urlretrieve(img,filename)
        else:
            print(path+' 目录已存在')
        

    #print(lst)
    #respose=requests.get('https://music.163.com/#/discover/playlist')
    #print(respose.status_code)# 响应的状态码 200
    #print(respose.content)  #返回字节信息
    #print(respose.text)  #返回文本内容
    #urls=re.findall(r'class="dec".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
    #print(urls)

    return playlists

def get_music_ol(id):

    filename='E:\DAM\FlaskWebProject1\FlaskWebProject1\HW2\static\playlists\\'+id+'\info.xml'
    dom = parse(filename)
    root = dom.documentElement
    head = root.getElementsByTagName("head")
    for node in head:
        title=node.getElementsByTagName("title")[0].childNodes[0].data
    return title