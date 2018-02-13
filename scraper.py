import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://oxu.az/politics').read()


soup = bs.BeautifulSoup(source,'lxml')
data=soup.prettify()
#print(data)
#with open("Output.html", "w",encoding="utf8") as text_file:
    #text_file.write(data)


for link in soup.find_all('a',{"class":"news-i-inner"}):
    l=link.get('href')
    source1=urllib.request.urlopen('https://oxu.az'+l).read()
    soup=bs.BeautifulSoup(source1,'lxml')
    data1=soup.prettify()
    with open("Output1.html", "w",encoding="utf8") as text_file:
    	text_file.write(data)



