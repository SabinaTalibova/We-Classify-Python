import bs4 as bs
import urllib.request
import  csv




source = urllib.request.urlopen('https://oxu.az/politics').read()
soup = bs.BeautifulSoup(source, 'lxml')
data=soup.prettify()

next_page=soup.find('a',{"class":"more"})
next_link=next_page.get('href')

print(next_link)

