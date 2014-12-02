import scraperwiki
import lxml.html
import urllib2
import urllib
import re
from lxml import etree
from pyquery import PyQuery as pq

scrape_url = "http://www.tripadvisor.com/Attractions-g60616-Activities-Kapaa_Kauai_Hawaii.html"

scraperwiki.scrape(pageUrl)

root = lxml.html.fromstring(html)

print html
