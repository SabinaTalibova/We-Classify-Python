import bs4 as bs
import urllib.request
import  csv

source = urllib.request.urlopen('https://oxu.az/politics').read()



#soup = bs.BeautifulSoup(source,'lxml')
soup = bs.BeautifulSoup(source, 'lxml')

data=soup.prettify()

#a way to output formatted source code to file for easy analysing
#with open("Output.html", "w",encoding="utf8") as text_file:
    #text_file.write(data)



with open('onehot.csv','w',encoding="utf8") as testfile:
    csv_writer=csv.writer(testfile)



##now find links in new-i-inner class
    for link in soup.find_all('a', {"class":"news-i-inner"}):
        l=link.get('href')
    #print(l)

        source = urllib.request.urlopen('https://oxu.az'+l).read()
        soup = bs.BeautifulSoup(source,'lxml')
        data=soup.prettify()
        news=soup.find('div', {"class":"news-inner"}).text#.encode('UTF8')

        csv_writer.writerow([news])

        
        #print(news)


  








