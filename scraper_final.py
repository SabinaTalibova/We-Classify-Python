import bs4 as bs
import urllib.request
import  csv
import time
from multiprocessing import Pool




global link

link='https://oxu.az/ict'
def find_news_links(link):
    links=[]
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    #data=soup.prettify()
    next_page=soup.find('a',{"class":"more"})
    pagination_link=next_page.get('href')
    for link in soup.find_all('a', {"class":"news-i-inner"}):
        l=link.get('href')
        links.append(l)
    return links,pagination_link
def scrape_news_content():
    with open('ikt.csv','a',encoding="utf8") as file:
        writer=csv.writer(file)
        links=find_news_links(link)[0]
        for i in links:
            source=urllib.request.urlopen('https://oxu.az'+i).read()
            soup=bs.BeautifulSoup(source,'lxml')
            #data=soup.prettify()
            news_text=soup.find('div',{"class": "news-inner"}).text
            #label='siyast'
            #writer.writerow(zip([news_text],[label]))
            writer.writerow([news_text])
            time.sleep(2)
global i
i=0
while i<200:
    try:
        link='https://oxu.az'+find_news_links(link)[1]
        scrape_news_content()
        i=i+1
        time.sleep(3)
    except:
        coverage="   "

