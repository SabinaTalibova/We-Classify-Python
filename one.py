import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://oxu.az/politics/242716').read()

soup = bs.BeautifulSoup(source,'lxml')
data=soup.prettify()

#a way to output formatted source code to file for easy analysing
'''with open("Output2.html", "w",encoding="utf8") as text_file:
    text_file.write(data)'''

##now find links in new-i-inner class
print(soup.find('div', {"class":"news-inner"}).text)









