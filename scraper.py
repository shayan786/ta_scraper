import scraperwiki
import lxml.html
import urllib2
import urllib
import re
from lxml import etree
from pyquery import PyQuery as pq

scrape_url = "http://www.tripadvisor.com/Attraction_Review-g60616-d1015347-Reviews-Kayak_Wailua-Kapaa_Kauai_Hawaii.html"

def get_url(url):
    req = urllib2.Request(url, None, header)
    response = urllib2.urlopen(req)
    root = pq(response.read().decode('utf-8'))
    return root

def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    if value:
        return re.sub(r'<[^>]*?>', '', value)
    return ""
    
page = get_url(page_url)
    
email_raw = strip_tags(page(".sprite-grayEmail").next().attr("onclick"))

print email_raw
