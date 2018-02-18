import bs4 as bs
import urllib.request
import  csv
global link
link='https://oxu.az/economy'


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
    with open('data.csv','a',encoding="utf8") as file:
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




global i
i=0
while i<200:
    scrape_news_content()
    link='https://oxu.az'+find_news_links(link)[1]
    i=i+1
print(i)