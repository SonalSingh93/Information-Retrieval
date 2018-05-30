# web crawler - HW1
# Online resources for help
# https://www.coursera.org/learn/python-network-data/lecture/1oHBS/12-5-parsing-web-pages
# used for connection establishment

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import time

#source for SSL certificate clearance
# https://www.coursera.org/learn/python-network-data/lecture/1oHBS/12-5-parsing-web-pages
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

indexLinksCrawled=0
seed = "https://en.wikipedia.org/wiki/Tropical_cyclone"
frontier = list()
visited = list()
depth = 0
frontier = [seed]

def crawl_page(keyword):
    global indexLinksCrawled
    global pages_crawled
    global count_url
    global seed
    global frontier
    global visited
    global depth
    global totalNumOfTags
    #if frontier[indexLinksCrawled] in visited:
    #    break
    #else:
    #    visited.appended(frontier[indexLinksCrawled])
    time.sleep(1)
    html_content = urlopen(frontier[indexLinksCrawled], context=ctx).read()
    #store the contents in a file
    # extract the link which is being crawled
    title = frontier[indexLinksCrawled]
    #append the title to visited list
    visited.append(title)

    # temp for calculating the number of line returned
    temp_count = len(frontier)

    ## Construct the filename with which we are storing the raw html files
    #filename = title[30:]+".txt"
    #fileHandle = open(filename, 'w')
    #fileHandle.write(str(html_content))

    # Extract all the links in the web page that is being parsed using HTML parser
    # and BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    # retireve all tags that start with /wiki/
    #tags = soup.find_all(href=re.compile("/wiki/"))
    tags = soup.find_all(href=re.compile("^/wiki/"))
    # for every href in tag, remove the links that do not start with /wiki
    # remove administrative links that contain ':' in the tags
    # remove duplicate lists by checking if it is already present in the
    # frontier list
    regularExpression = r'.*'+re.escape(keyword)+r'.*'
    for tag in tags:
        hyperlink = tag.get('href')
        hyperlinkText = tag.text
        if re.search(regularExpression,hyperlink,re.IGNORECASE) or re.search(regularExpression,hyperlinkText,re.IGNORECASE):
            #if check_no_prefix(tag,keyword) :
            #if hyperlink.startswith('/wiki'):
                if ':' not in hyperlink:
                    url = "https://en.wikipedia.org"+str(hyperlink)
                    if url not in frontier:
                        frontier.append(url)
    print(frontier[indexLinksCrawled])
    print(indexLinksCrawled)
    indexLinksCrawled = indexLinksCrawled + 1

    #counting how many urls are returned
    final_count=len(frontier)
    totalNumOfTags = final_count - temp_count

    return frontier,totalNumOfTags

# call the crawl_page() function thousand times that crawls the shallow pages first

for i in range(1000):
    if indexLinksCrawled <= 300:
        crawl_page("rain")



# store the links that has been visited
filename = "CRAWLED_LINKS_FOCUSSED.TXT"
fout = open(filename, "w")
count = 1
for link in visited:
    fout.write(link + "\n")
    count += 1
