import codecs
import urllib.request
import re
import feedparser
from bs4 import BeautifulSoup
import PyPDF2

# assignment 1
from text import textprocess
# assignment 2
from pos import pos

def dataFromUrl(url,path):
    urldata = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(urldata, 'html.parser')
    # remove unnecessary data
    try:
        for x in soup.find_all('table'):
            if x is not None :
                x.decompose()

        for x in soup.find_all('div', id="toc"):
            if x is not None :
                x.decompose()
        for x in soup.find_all('div', role="note"):
            if x is not None :
                x.decompose()
        for x in soup.find_all('div', role="navigation"):
            if x is not None:
                x.decompose()
        for x in soup.find_all('div', {'class': 'reflist'}):
            if x is not None:
                x.decompose()
        for x in soup.find_all('div', {'class': 'navbox'}):
            if x is not None:
                x.decompose()
        soup.find('div', id="catlinks").decompose()
 #       soup.find('div', {'class': 'refbegin refbegin-columns references-column-width'}).decompose()



    except Exception as e: print(e)
    text = soup.get_text()
    text = re.sub(r"\n+", r"\n", text) # remove extra spaces
    text=re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'\[\w+\]', '', text) # remove citation
    file = codecs.open(path, "a", "utf-8")
    file.write(text)
    file.close()




def rssFeed(url,path):
    file = codecs.open(path, "a", "utf-8")
    file.write("RSS FEED")
    NewsFeed = feedparser.parse(url)
    for x in NewsFeed['entries']:
        file.write(x.title + ". " + x.summary + " " + x.published)
    file.close()


def pdfread(pdfName,path,start,end):
    pdfFileObj = open(pdfName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    page_content = ""  # define variable for using in loop.
    for page_number in range(start, end):
        page = pdfReader.getPage(page_number)
        page_content += page.extractText()
    file = codecs.open(path, "a", "utf-8")
    file.write("PDF \n\n")
    file.write(page_content)
    file.close()


file = codecs.open("newinput.txt", "w", "utf-8")
file.write("")
file.close()
# Getting data from 5 Wikipedia article
dataFromUrl("https://en.wikipedia.org/wiki/India","newinput.txt")
dataFromUrl("https://en.wikipedia.org/wiki/Maharashtra","newinput.txt")
dataFromUrl("https://en.wikipedia.org/wiki/Mumbai","newinput.txt")
dataFromUrl("https://en.wikipedia.org/wiki/Nagpur","newinput.txt")
dataFromUrl("https://en.wikipedia.org/wiki/Indian_subcontinent","newinput.txt")

# Getting data from RSS feed
rssFeed("https://timesofindia.indiatimes.com/rssfeedstopstories.cms","newinput.txt")
rssFeed("https://www.thehindu.com/feeder/default.rss","newinput.txt")

# Getting data from PDF
pdfread('crm.pdf','newinput.txt',14,25)

# calling function for 1st assignment
textprocess("newinput.txt")

# calling function for assignment 2
pos("newinput.txt")
