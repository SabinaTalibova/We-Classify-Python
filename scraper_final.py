import bs4 as bs
import urllib.request
import  csv



def find_news_links():
    links=[]
    link='https://oxu.az/politics'
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    data=soup.prettify()
    next_page=soup.find('a',{"class":"more"})
    pagination_link=next_page.get('href')
    for link in soup.find_all('a', {"class":"news-i-inner"}):
        l=link.get('href')
        links.append(l)
    return links,pagination_link

def scrape_news_content():
    with open('data.csv','w',encoding="utf8") as file:
        writer=csv.writer(file)


        links=find_news_links()
        for i in links:
            source=urllib.request.urlopen('https://oxu.az'+i).read()
            soup=bs.BeautifulSoup(source,'lxml')
            data=soup.prettify()
            news_text=soup.find('div',{"class": "news-inner"}).text
            writer.writerow([news_text])





print(find_news_links()[1])
#scrape_news_content()