import bs4 as bs
import urllib.request
import  csv
import time
from multiprocessing import Pool




global link

link='https://oxu.az/world'
def find_news_links(link):
    links=[]
    req = urllib.request.Request(
    link, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        ,'From': 'sabinatalibova1@gmail.com'
    }

    )
    source = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    #data=soup.prettify()
    next_page=soup.find('a',{"class":"more"})
    pagination_link=next_page.get('href')
    for link in soup.find_all('a', {"class":"news-i-inner"}):
        l=link.get('href')
        links.append(l)
    return links,pagination_link
def scrape_news_content():
    with open('data.csv','a',encoding="utf8") as file:
        writer=csv.writer(file)
        links=find_news_links(link)[0]
        for i in links:
            req = urllib.request.Request(
                link,data=None, 
                headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        ,'From': 'sabinatalibova1@gmail.com'
    }
)            
            source = urllib.request.urlopen(req).read()
            #source=urllib.request.urlopen('https://oxu.az'+i).read()
            soup=bs.BeautifulSoup(source,'lxml')
            #data=soup.prettify()
            news_text=soup.find('div',{"class": "news-inner"}).text
            #label='siyast'
            #writer.writerow(zip([news_text],[label]))
            writer.writerow([news_text])
            time.sleep(2)
global i
i=0
while i<2:
    try:
        link='https://oxu.az'+find_news_links(link)[1]
        scrape_news_content()
        i=i+1
        time.sleep(3)
    except:
        coverage=" stopped scraping "

