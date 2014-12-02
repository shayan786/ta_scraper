import scraperwiki
import lxml.html
import urllib2
import urllib
import re
from lxml import etree
from pyquery import PyQuery as pq

scrape_url = "http://www.tripadvisor.com/Attractions-g28968-Activities-Washington.html"

header = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11',
           'Cookie': 'PHPSESSID=de45029e5e2fab4f6e5eef56515d6c1c; __utma=123692957.1658163614.1349740913.1349740913.1352756518.2; __utmb=204497347.1.10.1342787814; __utmc=204497347; __utmz=204497347.1341998344.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)' }

email_regex = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')

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

def parse_list(root):
    """ Takes a listing page and indexes all the listings in it """
    for el in root(".listing a.property_title"):
        page_url = "http://www.tripadvisor.com" + el.get("href")
        page = get_url(page_url)
        
        email_raw = strip_tags(page(".sprite-grayEmail").next().attr("onclick"))
        email = email_regex.findall(email_raw)
        
        if email:
          email = email[0]
          print email

def get_sub_loc_urls(url):
    for el in url(".geo_name a"):
        sub_url = "http://www.tripadvisor.com" + el.get("href")
        
        # go to that sub location page
        sub_page = get_url(sub_url)
        
        # go to the activities page
        sub_activities_url = sub_page(".overview .tab1 a").attr("href")
        print sub_activities_url
        
        
        
         
def parse_listing_pages(start_url):
    # not iterate over the pages
    count = 0
    while True:
        url = start_url % (count) # targets each page in the list
        print "On page %s" % url
        root = get_url(url)

        # check if there are items, if not stop since you exceeded the total pages
        if not root(".listing"):
            print "Reached end at page %s" % count
            break

        # this will parse the first listing page
        parse_list(root)
        print "Finished page %s" % count
        count = count + 30

scrape_url_page = get_url(scrape_url)
get_sub_loc_urls(scrape_url_page)


#parse_list(scrape_url_page)
