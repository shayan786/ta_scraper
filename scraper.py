import scraperwiki
import lxml.html
import urllib2
import urllib
import re
from lxml import etree
from pyquery import PyQuery as pq

scrape_url = "http://www.tripadvisor.com/Attraction_Review-g60616-d1015347-Reviews-Kayak_Wailua-Kapaa_Kauai_Hawaii.html"

def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    if value:
        return re.sub(r'<[^>]*?>', '', value)
    return ""
    
email_raw = strip_tags(page(".sprite-grayEmail").next().attr("onclick"))

print email_raw
