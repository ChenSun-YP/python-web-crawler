import sys
from bs4 import BeautifulSoup  #analysize website
import re    #match charachter
import urllib.request,urllib.error  #get web data from url
import xlwt  #save in excel
import sqlite3  #SQLite


class Scraper:
    def __init__(self, site):
        self.site = site


    def scrape(self,url):
        herders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) Chrome/45.0.2454.85 Safari/537.36 115Broswer/6.0.3',
            'Referer': 'https://movie.douban.com/',
            'Connection': 'keep-alive'}

        try:
            req = urllib.request.Request(url, headers=herders)#read
            response = urllib.request.urlopen(req)#solve
            html = response.read().decode('utf8')#decode
            #print(html)
            return html
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)




    def getdata(self, baseurl):
        for i in range (0,3):
            url =baseurl + str(25*i)
            print(url)
            html = Scraper.scrape(self,url) #save

            #solve
            parser = "html.parser"  # analyse

            sp = BeautifulSoup(html, parser)

            print(sp.title.string)#字符串
            #print(sp.a.attrs)#标签的属性值
            #print(sp) #自身类型sp.balbala
            #print(sp.a.string) #注释comment
            print(sp.body.contents[3])
            for tag in sp.find_all("img"):#substitut a
                url = tag.get("src")
                print(url)
                if url is None:
                    continue
                if "html" in url:
                    print("\n" + url)


    def savedata(self,savepath):

        print('save')





if __name__ == '__main__':
    p =6

    news = 'https://movie.douban.com/top250?start='
    Scraper(news).getdata(news)
    #Scraper(news).scrape(news)
