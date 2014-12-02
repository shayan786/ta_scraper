import scraperwiki
import lxml.html
import urllib2
import urllib
import re
from lxml import etree
from pyquery import PyQuery as pq

scrape_url = "http://www.tripadvisor.com/Attraction_Review-g60616-d1015347-Reviews-Kayak_Wailua-Kapaa_Kauai_Hawaii.html"

print scraperwiki.scrape(scrape_url)
